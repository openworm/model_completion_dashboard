import React from 'react';
import ReactDOM from 'react-dom';
import Highcharts from 'highcharts';
import Heatmap from 'highcharts/modules/heatmap.js';


class BodyMusclesGrid extends React.Component {

  constructor(props) {
   super(props);
   this.state = {
   bodymusclesData:[],
   tooltipBodyMuscle:{}
   };
 }

  formatDataBodyMuscle(data)
  {
    console.log(" in formatDataBodyMuscle");
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


  formatToolTipBodyMuscle(data)
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

    loadBodyMusclesFromServer(){
          $.ajax({
              url: "/pyopenworm/api/getbodymuscles",
              datatype: 'json',
              cache: false,
              success: function(data) {
                  var ttBMdata = this.formatToolTipBodyMuscle(data);
                  data = this.formatDataBodyMuscle(data);
                  this.setState({bodymusclesData: data,
                    tooltipBodyMuscle: ttBMdata
                  });
                  var self = this;
                  this.chart = new Highcharts[this.props.type || "Chart"](
                        this.refs.bodymusclechart,
                        this.props.options
                    );
                  this.chart.series[0].setData(this.state.bodymusclesData);
                  this.chart.update({
                    title: {
                        text: 'Body Muscles'
                    },
                      tooltip: {
                        formatter: function() {
                          var x=this.point.x;
                          var y=this.point.y;
                          return ttBMdata[x][y];
                        }
                      },
                      plotOptions: {
                              series: {
                                  events: {
                                      click: function (event) {
                                        var name = ttBMdata[event.point.x][event.point.y]
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
      this.loadBodyMusclesFromServer();
    }

    componentWillUnmount() {
        this.chart.destroy();
    }

    render() {

        return (
          <div>
          <div ref="bodymusclechart"/>
          </div>
        )
    }
}

export default BodyMusclesGrid;
