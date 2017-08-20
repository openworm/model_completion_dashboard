import React from 'react';
import ReactDOM from 'react-dom';
import Highcharts from 'highcharts';
import Heatmap from 'highcharts/modules/heatmap.js';


class PharynxMusclesGrid extends React.Component {

  constructor(props) {
   super(props);
   this.state = {
   pharynxmusclesData:[],
   tooltipPharynxMuscle:{}
   };
 }

  formatDataPharynxMuscle(data)
  {
    console.log(" in formatPharynxBodyMuscle");
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
      converteddata.push([parseInt(r),parseInt(c),parseInt(data[key].completeness)]);
      r+=1;
    }
    return converteddata;
  }


  formatToolTipPharynxMuscle(data)
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

    loadPharynxMusclesFromServer(){
          $.ajax({
              url: "/pyopenworm/api/getpharynxmuscles",
              datatype: 'json',
              cache: false,
              success: function(data) {
                  var ttPMdata = this.formatToolTipPharynxMuscle(data);
                  data = this.formatDataPharynxMuscle(data);
                  this.setState({pharynxmusclesData: data,
                    tooltipPharynxMuscle: ttPMdata
                  });
                  var self = this;
                  this.chart = new Highcharts[this.props.type || "Chart"](
                        this.refs.pharynxmusclechart,
                        this.props.options
                    );
                  this.chart.series[0].setData(this.state.pharynxmusclesData);
                  this.chart.update({
                    title: {
                        text: 'Pharynx Muscles'
                    },
                      tooltip: {
                        formatter: function() {
                          var x=this.point.x;
                          var y=this.point.y;
                          return ttPMdata[x][y];
                        }
                      },
                      plotOptions: {
                              series: {
                                  events: {
                                      click: function (event) {
                                        var name = ttPMdata[event.point.x][event.point.y]
                                       self.props.updateCurrCell(name);
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
      this.loadPharynxMusclesFromServer();
    }

    componentWillUnmount() {
        this.chart.destroy();
    }

    render() {

        return (
          <div>
          <div ref="pharynxmusclechart"/>
          </div>
        )
    }
}

export default PharynxMusclesGrid;
