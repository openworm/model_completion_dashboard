import React from 'react';
import ReactDOM from 'react-dom';
import Highcharts from 'highcharts';
import Heatmap from 'highcharts/modules/heatmap.js';
import ChannelChart from './ChannelChart';

class Chart extends React.Component {

  constructor(props) {
   super(props);
   this.state = {neuronsData:[],
   tooltipNeuron:{},
   currCell:""  };
 }

  // getInitialState()
  // {
  //   return {
  //     neuronsData:[],
  //     tooltipNeuron:{},
  //     currCell:""
  //   };
  // }

  formatDataNeuron(data)
  {
    console.log(" in formatDataNeuron");
    var converteddata = [];
    var ROWS = 20;
    var r=0;var c=0;
    for(var key in data)
    {
      r+=1;
      if (r!=0 && r%ROWS==0)
      {
        r=0;
        c+=1;
      }
      console.log(data[key]);
      converteddata.push([parseInt(r),parseInt(c),parseInt(data[key].completeness)]);
    }
    return converteddata;
  }

  formatToolTipNeuron(data)
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
      r+=1;
      if (r!=0 && r%ROWS==0)
      {
        r=0;
        c+=1;
      }
      console.log(data[key]);
      names[r][c]=data[key].name;
    }
    return names;
  }

  loadNeuronsFromServer(){
        $.ajax({
            url: "/pyopenworm/api/getneurons",
            datatype: 'json',
            cache: false,
            success: function(data) {
              console.log(data);
                var ttNdata = this.formatToolTipNeuron(data);
                console.log(ttNdata);
                data = this.formatDataNeuron(data);
                console.log(data);
                this.setState({neuronsData: data,
                  tooltipNeuron: ttNdata
                });
                var self = this;
                this.chart = new Highcharts[this.props.type || "Chart"](
                      this.refs.chart,
                      this.props.Neuronoptions
                  );
                this.chart.series[0].setData(this.state.neuronsData);
                this.chart.update({
                    tooltip: {
                      formatter: function() {
                        var x=this.point.x;
                        var y=this.point.y;
                        return ttNdata[x][y];
                      }
                    },
                    plotOptions: {
                            series: {
                                events: {
                                    click: function (event) {
                                      var name = ttNdata[event.point.x][event.point.y]
                                      self.setState({currCell:name});
                                      console.log(self.state.currCell);
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
      this.loadNeuronsFromServer();
    }

    componentWillUnmount() {
        this.chart.destroy();
    }

    render() {

      let channelmatrix;
      if (this.state.currCell)
      {
        channelmatrix= <ChannelChart currcell={this.state.currCell} Channeloptions={this.props.Channeloptions} />;
      }
        return (
            <div>
            <div ref="chart"/>
            {channelmatrix}
            </div>
        )
    }
}

export default Chart;
