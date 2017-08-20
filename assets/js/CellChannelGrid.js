import React from 'react';
import ReactDOM from 'react-dom';
import Highcharts from 'highcharts';
import Heatmap from 'highcharts/modules/heatmap.js';
import * as Rb from 'react-bootstrap';
import ChannelCellChart from './ChannelCellChart';
import IonChannelDetails from './IonChannelDetails.js';




class CellChannelGrid extends React.Component{

  constructor(props) {
     super(props);
     this.state = {
       channelData:[],
       tooltipChannel:{},
       currChannel:"",
       currCell:"",
       currChannel:"",
       cellDetail:{},
       chdetail:false,
       availableChannel:false
     };
   }

   updatecurrChannel(channel)
   {
     this.setState({currChannel:channel,chdetail:true});
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
  const node = ReactDOM.findDOMNode(self.refs.currcellchart);
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

  updateCellDetailsFromServer(){

    $.ajax({
        url: "/pyopenworm/api/findcell?cellname="+this.props.currcell,
        datatype: 'json',
        cache: false,
        success: function(data) {
            console.log("printing");
            console.log(data);
            this.setState({cellDetail:data});
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
                var ttChdata = this.formatToolTipChannel(data);
                data = this.formatDataChannel(data);
                if (data.length == 0)
                {
                  this.setState({availableChannel:false})
                }
                else {
                  this.setState({availableChannel:true})
                }
                console.log(this.state.availableChannel);
                this.setState({channelData: data,
                  tooltipChannel: ttChdata
                });
                // var self = this;
                // this.chart = new Highcharts[this.props.type || "Chart"](
                //       this.refs.chchart,
                //       this.props.Channeloptions
                //   );
                // this.chart.series[0].setData(this.state.channelData);
                // this.chart.update({
                //   title: {
                //       text: 'Channels'
                //   },
                //     tooltip: {
                //       formatter: function() {
                //         var x=this.point.x;
                //         var y=this.point.y;
                //         return ttChdata[x][y];
                //       }
                //     },
                //     plotOptions: {
                //             series: {
                //                 events: {
                //                     click: function (event) {
                //                       var name = ttChdata[event.point.x][event.point.y]
                //                       self.setState({currChannel:name});
                //                       console.log(self.state.currChannel);
                //                     }
                //                 }
                //             }
                //         }
                //   });

                  this.scrollToChannelMatrix();

            }.bind(this)
        });
    }


    updateCellChannelsFromServer(){
          $.ajax({
              url: "/pyopenworm/api/getcellionchannels/?cellname="+this.props.currcell,
              datatype: 'json',
              cache: false,
              success: function(data) {
                console.log("in cell channel get data set");
                  var ttChdata = this.formatToolTipChannel(data);
                  data = this.formatDataChannel(data);

                  console.log("length "+data.length)
                  if (data.length == 0)
                  {
                    this.setState({availableChannel:false})
                  }
                  else {
                    this.setState({availableChannel:true})
                  }
                  console.log(this.state.availableChannel);

                  this.setState({channelData: data,
                    tooltipChannel: ttChdata
                  });
                  // var self = this;
                  // this.chart.series[0].setData(this.state.channelData);
                  // this.chart.update({
                  //   title: {
                  //       text: 'Channels'
                  //   },
                  //     tooltip: {
                  //       formatter: function() {
                  //         var x=this.point.x;
                  //         var y=this.point.y;
                  //         return ttChdata[x][y];
                  //       }
                  //     },
                  //     plotOptions: {
                  //             series: {
                  //                 events: {
                  //                     click: function (event) {
                  //                       var name = ttChdata[event.point.x][event.point.y]
                  //                       self.setState({currChannel:name});
                  //                       console.log(self.state.currChannel);
                  //                     }
                  //                 }
                  //             }
                  //         }
                  //   });

                    this.scrollToChannelMatrix();

              }.bind(this)
          });
      }




    componentDidMount() {
      Heatmap(Highcharts);
      this.loadCellChannelsFromServer();
      this.loadCellDetailsFromServer();
    }

    componentDidUpdate(prevProps, prevState) {
    if (this.state.currCell!=this.props.currcell)
    {
    this.updateCellChannelsFromServer();
    this.updateCellDetailsFromServer();
  //  this.scrollToChannelMatrix();
    this.setState({currCell:this.props.currcell});
    }
  }

    componentWillUnmount() {
        this.chart.destroy();
    }

    render() {

        let celldata;
        if (this.state.cellDetail.celltype=="neuron")
        {
          celldata = <div>
    <Rb.Table striped bordered condensed>
    <tbody>
    <tr>
        <td>
            Type:
        </td>
        <td>
            <ul>
            {(() => {
              if(this.state.cellDetail.type.length>0)
              {
              let store = this.state.cellDetail.type.map(function(type){
            return <li key={type}>{type}</li>;
          });
          return store;
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
            Receptor:
        </td>
        <td>
            <ul>
              {(() => {
              if (this.state.cellDetail.receptors.length>0)
            {
              let store;
              store = this.state.cellDetail.receptors.map(function(receptor){
            return <li key={receptor}>{receptor}</li>;
          });
            return store;
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
            Innexin:
        </td>
        <td>
            <ul>
            {(() => {
              if (this.state.cellDetail.innexin.length>0)
              {
                let store;
              store = this.state.cellDetail.innexin.map(function(innexin){
            return <li key={innexin}>{innexin}</li>;
          });
          return store;
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
            Neurotransmitter:
        </td>
        <td>
            <ul>
            {(() => {
              if (this.state.cellDetail.neurotransmitter.length>0)
              {
                let store;
              store = this.state.cellDetail.neurotransmitter.map(function(neurotransmitter){
            return <li key={neurotransmitter}>{neurotransmitter}</li>;
          });
          return store;
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
            Neuropeptide:
        </td>
        <td>
            <ul>
            {(() => {
              if (this.state.cellDetail.neuropeptide.length>0)
              {
                let store;
              store = this.state.cellDetail.neuropeptide.map(function(neuropeptide){
            return <li key={neuropeptide}>{neuropeptide}</li>;
          });
          return store;
          }
              else {
                return <li>Data not available</li>;
              }
              })()}
            </ul>
        </td>
    </tr>
    </tbody>
    </Rb.Table>
</div>;
        }
        else if (this.state.cellDetail.celltype=="muscle") {

          celldata = <div>
  <Rb.Table striped bordered condensed>
    <tbody>
    <tr>
        <td>
            Neurons:
        </td>
        <td>
            <ul>
            {(() => {
              if (this.state.cellDetail.neurons.length>0)
              {
                let store;
              store=this.state.cellDetail.neurons.map(function(neuron){
            return <li key={neuron}>{neuron}</li>;
          });
        return store;
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
            Receptors:
        </td>
        <td>
            <ul>
            {(() => {
              if (this.state.cellDetail.receptors.length>0)
              {
                let store;
              store = this.state.cellDetail.receptors.map(function(receptor){
            return <li key={receptor}>{receptor}</li>;
          });
          return store;
        }
            else {
              return <li>Data not available</li>;
            }
            })()}
            </ul>
        </td>
    </tr>
    </tbody>
</Rb.Table>
          </div>;
//style={{width: 250, height: 250}}
        }

        let channeldetailsmatrix;
        if (this.state.chdetail)
        {
          channeldetailsmatrix= <IonChannelDetails currchannel={this.state.currChannel} options={this.props.Channeloptions} />;
        }

        return (
            <div>
            <Rb.Panel>
            <Rb.Row>
            <Rb.Col xs={4} md={4} xsOffset={4} mdOffset={4}>
            <div ref="currcellchart"/>
            </Rb.Col>
            </Rb.Row>

            <Rb.Row>
            <Rb.Col xs={5} md={5}>
            {
              this.state.availableChannel
              ? <ChannelCellChart channeldata={this.state.channelData} tooltipdata={this.state.tooltipChannel} chartoptions={this.props.Channeloptions} updatecurrChannel={this.updatecurrChannel.bind(this)}/>
              : <div> No channels available </div>
            }
            </Rb.Col>
            <Rb.Col xs={7} md={7}>
            {celldata}
            </Rb.Col>
            </Rb.Row>
            </Rb.Panel>


            <Rb.Row>
            <Rb.Col xs={10} md={10} xsOffset={1} mdOffset={1}>
            <Rb.Panel>
            {channeldetailsmatrix}
            </Rb.Panel>
            </Rb.Col>
            </Rb.Row>
            </div>
        );
    }

}
export default CellChannelGrid;
