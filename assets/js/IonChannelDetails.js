import React from 'react';
import ReactDOM from 'react-dom';
import Highcharts from 'highcharts';
import Heatmap from 'highcharts/modules/heatmap.js';
import * as Rb from 'react-bootstrap';




class IonChannelDetails extends React.Component{

  constructor(props) {
     super(props);
     this.state = {
       tooltipChannel:{},
       currChannel:"",
       channelDetail:{}
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

  scrollToChannelDetails(){
  const self = this;
  window.requestAnimationFrame(function() {
  const node = ReactDOM.findDOMNode(self.refs.currchannelchart);
  node.scrollIntoView({ behavior: "smooth" });
  });
  }

  loadChannelDetailsFromServer(){

    $.ajax({
        url: "/pyopenworm/api/findchannel?channelname="+this.props.currchannel,
        datatype: 'json',
        cache: false,
        success: function(data) {
            console.log("printing");
            console.log(data);
            this.setState({channelDetail:data});
            this.renderCurrChannelChart();
        }.bind(this)
    });

  }

  renderCurrChannelChart()
  {
    Heatmap(Highcharts);
    this.chart2 = new Highcharts[this.props.type || "Chart"](
          this.refs.currchannelchart,
          this.props.options
      );
    this.chart2.series[0].setData([[0,0,this.state.channelDetail.completeness]]);
    let self=this;
    this.chart2.update({
      title: {
          text: ""+self.state.channelDetail.name
      },
      legend: {
        enabled: false
      },

      });
  }



    componentDidMount() {
      this.loadChannelDetailsFromServer();
      this.scrollToChannelDetails();
      this.setState({currChannel:this.props.currchannel});
    }

    componentDidUpdate(prevProps, prevState) {
    console.log(this.state.currChannel + " " + this.props.currchannel);
    if (this.state.currChannel!=this.props.currchannel)
    {
    this.loadChannelDetailsFromServer();
    this.scrollToChannelDetails();
    this.setState({currChannel:this.props.currchannel});
    }
  }

    componentWillUnmount() {
        this.chart2.destroy();
    }

    render() {

        let channeldata;
        if (this.state.channelDetail.celltype=="ionchannel")
        {
        channeldata= <div>
    <Rb.Table striped bordered condensed>
    <tbody>
    <tr>
        <td>
            Type:
        </td>
        <td>
            <ul>
            {(() => {
              if (this.state.channelDetail.celltype)
              {
             return <li>{this.state.channelDetail.celltype}</li>;
          }
          else {
            return <li>Data not available</li>;
          }
            })()}
            </ul>
        </td>
    </tr>
    <tr>
        <td>
            Description:
        </td>
        <td>
            <ul>
            {(() => {
              if (this.state.channelDetail.description)
              {
                return <li>{this.state.channelDetail.description}</li>;
              }
              else {
                return <li>Data not available </li>;
              }
              })()}
            </ul>
        </td>
    </tr>
    <tr>
        <td>
            Gene Name:
        </td>
        <td>
            <ul>
            {(() => {
              if (this.state.channelDetail.gene_name)
              {
            return <li>{this.state.channelDetail.gene_name}</li>;
          }
          else {
            return <li>Data not available </li>;
          }
          })()}
            </ul>
        </td>
    </tr>
    <tr>
        <td>
            Gene Class:
        </td>
        <td>
            <ul>
            {(() => {
              if (this.state.channelDetail.gene_class)
              {
           return <li>{this.state.channelDetail.gene_class}</li>;
         }
         else {
           return <li>Data not available </li>;
         }
         })()}
            </ul>
        </td>
    </tr>
    <tr>
        <td>
            Expression Pattern:
        </td>
        <td>
            <ul>
            {(() => {
              if (this.state.channelDetail.expression_pattern)
              {
           return <li>{this.state.channelDetail.expression_pattern}</li>;
         }
         else {
           return <li>Data not available </li>;
         }
         })()}
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
            <Rb.Col xs={4} md={4}>
            <div style={{width: 250, height: 250}} ref="currchannelchart"/>
            </Rb.Col>
            <Rb.Col xs={8} md={8}>
            {channeldata}
            </Rb.Col>
            </Rb.Row>
            </Rb.Panel>
            </div>
        );
    }

}
export default IonChannelDetails;
