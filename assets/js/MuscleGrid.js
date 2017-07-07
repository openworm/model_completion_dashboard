import React from 'react';
import ReactDOM from 'react-dom';
import Highcharts from 'highcharts';
import Heatmap from 'highcharts/modules/heatmap.js';


class MuscleGrid extends React.Component {

  constructor(props) {
   super(props);
   this.state = {
   musclesData:[],
   tooltipMuscle:{}
   };
 }

  formatDataMuscle(data)
  {
    console.log(" in formatDataMuscle");
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


  formatToolTipMuscle(data)
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

    loadMusclesFromServer(){
          $.ajax({
              url: "/pyopenworm/api/getmuscles",
              datatype: 'json',
              cache: false,
              success: function(data) {
                console.log(data);
                  var ttMdata = this.formatToolTipMuscle(data);
                  console.log(ttMdata);
                  data = this.formatDataMuscle(data);
                  console.log(data);
                  this.setState({musclesData: data,
                    tooltipMuscle: ttMdata
                  });
                  var self = this;
                  this.chart = new Highcharts[this.props.type || "Chart"](
                        this.refs.musclechart,
                        this.props.options
                    );
                  this.chart.series[0].setData(this.state.musclesData);
                  this.chart.update({
                    title: {
                        text: 'Muscles'
                    },
                      tooltip: {
                        formatter: function() {
                          var x=this.point.x;
                          var y=this.point.y;
                          return ttMdata[x][y];
                        }
                      },
                      plotOptions: {
                              series: {
                                  events: {
                                      click: function (event) {
                                        var name = ttMdata[event.point.x][event.point.y]
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
      this.loadMusclesFromServer();
    }

    componentWillUnmount() {
        this.chart.destroy();
    }

    render() {

        return (
            <div>
            <div ref="musclechart"/>
            </div>
        )
    }
}

export default MuscleGrid;
