import React from 'react';
import ReactDOM from 'react-dom';
import Highcharts from 'highcharts';
import Heatmap from 'highcharts/modules/heatmap.js';
import * as Rb from 'react-bootstrap';




class CellChannelGrid extends React.Component{

  constructor(props) {
     super(props);
     this.state = {
       channelData:[],
       tooltipChannel:{},
       currChannel:"",
       currCell:"",
       cellDetail:{}
     };
   }

  formatDataChannel(data)
  {
    console.log(" in formatCellChannel");
    var converteddata = [];
    var ROWS = 20;
    var r=0;var c=0;
    for(var key in data)
    {
      if (r!=0 && r%ROWS==0)
      {
        r=0;
        c+=1;
      }
      console.log(data[key]);
      converteddata.push([parseInt(r),parseInt(c),parseInt(data[key].completeness)]);
      r+=1;
    }
    return converteddata;
  }

  formatToolTipChannel(data)
  {
    var names = {};
    var ROWS = 20;
    var r=0;var c=0;
    for (var k=0;k<ROWS;k++)
    {
      names[k]={};
    }
    for(var key in data)
    {
      if (r!=0 && r%ROWS==0)
      {
        r=0;
        c+=1;
      }
      console.log(data[key]);
      names[r][c]=data[key].name;
      r+=1;
    }
    return names;
  }

  scrollToChannelMatrix(){
  const self = this;
  window.requestAnimationFrame(function() {
  const node = ReactDOM.findDOMNode(self.refs.chchart);
  node.scrollIntoView({ behavior: "smooth" });
  });
  }

  loadCellDetailsFromServer(){

    $.ajax({
        url: "/pyopenworm/api/findcell?cellname="+this.props.currcell,
        datatype: 'json',
        cache: false,
        success: function(data) {
            console.log("printing");
            console.log(data);
            this.setState({cellDetail:data});
            this.renderCurrCellChart();
        }.bind(this)
    });

  }

  renderCurrCellChart()
  {
    this.chart1 = new Highcharts[this.props.type || "Chart"](
          this.refs.currcellchart,
          this.props.Channeloptions
      );
    console.log("in render cell chart");
    console.log(this.state.cellDetail.name);
    console.log(this.state.cellDetail.completeness);
    this.chart1.series[0].setData([[0,0,this.state.cellDetail.completeness]]);
    let self=this;
    this.chart1.update({
      title: {
          text: ""+self.state.cellDetail.name
      },
      legend: {
        enabled: false
      },

      });
  }



  loadCellChannelsFromServer(){
        $.ajax({
            url: "/pyopenworm/api/getcellionchannels/?cellname="+this.props.currcell,
            datatype: 'json',
            cache: false,
            success: function(data) {
              console.log(data);
                var ttChdata = this.formatToolTipChannel(data);
                console.log(ttChdata);
                data = this.formatDataChannel(data);
                console.log(data);
                this.setState({channelData: data,
                  tooltipChannel: ttChdata
                });
                var self = this;
                this.chart = new Highcharts[this.props.type || "Chart"](
                      this.refs.chchart,
                      this.props.Channeloptions
                  );
                this.chart.series[0].setData(this.state.channelData);
                this.chart.update({
                  title: {
                      text: 'Channels'
                  },
                    tooltip: {
                      formatter: function() {
                        var x=this.point.x;
                        var y=this.point.y;
                        return ttChdata[x][y];
                      }
                    },
                    plotOptions: {
                            series: {
                                events: {
                                    click: function (event) {
                                      var name = ttChdata[event.point.x][event.point.y]
                                      self.setState({currChannel:name});
                                      console.log(self.state.currChannel);
                                    }
                                }
                            }
                        }
                  });

            }.bind(this)
        });
    }



    componentDidMount() {
      Heatmap(Highcharts);
      this.loadCellChannelsFromServer();
    }

    componentDidUpdate(prevProps, prevState) {
    if (this.state.currCell!=this.props.currcell)
    {
    this.loadCellDetailsFromServer();
    this.scrollToChannelMatrix();
    this.setState({currCell:this.props.currcell});
    }
  }

    componentWillUnmount() {
        this.chart.destroy();
    }

    render() {

        let celldata
        if (this.state.cellDetail.celltype=="neuron")
        {
          celldata= <div>
    <Rb.Table striped bordered condensed>
    <tbody>
    <tr>
        <td>
            Type:
        </td>
        <td>
            <ul>
            {
              this.state.cellDetail.type.map(function(type){
            return <li key={type}>{type}</li>;
          })}
            </ul>
        </td>
    </tr>
    <tr>
        <td>
            Receptor:
        </td>
        <td>
            <ul>
            {
              this.state.cellDetail.receptors.map(function(receptor){
            return <li key={receptor}>{receptor}</li>;
            })}
            </ul>
        </td>
    </tr>
    <tr>
        <td>
            Innexin:
        </td>
        <td>
            <ul>
            {
              this.state.cellDetail.innexin.map(function(innexin){
            return <li key={innexin}>{innexin}</li>;
            })}
            </ul>
        </td>
    </tr>
    <tr>
        <td>
            Neurotransmitter:
        </td>
        <td>
            <ul>
            {
              this.state.cellDetail.neurotransmitter.map(function(neurotransmitter){
            return <li key={neurotransmitter}>{neurotransmitter}</li>;
            })}
            </ul>
        </td>
    </tr>
    <tr>
        <td>
            Neuropeptide:
        </td>
        <td>
            <ul>
            {
              this.state.cellDetail.neuropeptide.map(function(neuropeptide){
            return <li key={neuropeptide}>{neuropeptide}</li>;
            })}
            </ul>
        </td>
    </tr>
    </tbody>
    </Rb.Table>
</div>;
        }

        return (
            <div>
            <Rb.Panel>
            <Rb.Row>
            <Rb.Col xs={8} md={8} xsOffset={2} mdOffset={2}>
            <div ref="chchart"/>
            </Rb.Col>
            </Rb.Row>


            <Rb.Row>
            <Rb.Col xs={4} md={4}>
            <div style={{width: 250, height: 250}} ref="currcellchart"/>
            </Rb.Col>
            <Rb.Col xs={8} md={8}>
            {celldata}
            </Rb.Col>
            </Rb.Row>
            </Rb.Panel>
            </div>
        );
    }

}
export default CellChannelGrid;
