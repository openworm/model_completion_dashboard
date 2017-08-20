import React from 'react';
import ReactDOM from 'react-dom';
import Highcharts from 'highcharts';
import Heatmap from 'highcharts/modules/heatmap.js';
import * as Rb from 'react-bootstrap';
import IonChannelDetails from './IonChannelDetails.js';




class ChannelCellChart extends React.Component{

  constructor(props) {
     super(props);
   }

   createChart()
   {
     this.chart = new Highcharts[this.props.type || "Chart"](
           this.refs.chchart,
           this.props.chartoptions
       );
   }

   updateChart()
   {
     this.chart.series[0].setData(this.props.channeldata);
     var ttChdata= this.props.tooltipdata;
     var self=this;
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
                           self.props.updatecurrChannel(name);
                         }
                     }
                 }
             }
       });
   }

  componentDidMount() {
    this.createChart();
    Heatmap(Highcharts);
  }

  componentDidUpdate(prevProps, prevState) {
  this.updateChart();
  }

  render() {

    return (
      <div style={{height: 250}} ref="chchart"/>
    );

  }
}

export default ChannelCellChart;
