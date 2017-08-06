import React from 'react';
import ReactDOM from 'react-dom';
import Highcharts from 'highcharts';
import Heatmap from 'highcharts/modules/heatmap.js';


class NeuronGrid extends React.Component {

  constructor(props) {
   super(props);
   this.state = {neuronsData:[],
   tooltipNeuron:{}
 };
 }

  formatDataNeuron(data)
  {
    console.log(" in formatDataNeuron");
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

  loadNeuronsFromServer(){
        $.ajax({
            url: "/pyopenworm/api/getneurons",
            datatype: 'json',
            cache: false,
            success: function(data) {
                var ttNdata = this.formatToolTipNeuron(data);
                data = this.formatDataNeuron(data);
                this.setState({neuronsData: data,
                  tooltipNeuron: ttNdata
                });
                var self = this;
                console.log(this.refs);
                this.Nchart = new Highcharts[this.props.type || "Chart"](
                      this.refs.neuronchart,
                      this.props.options
                  );
                this.Nchart.series[0].setData(this.state.neuronsData);
                this.Nchart.update({
                  title: {
                      text: 'Neurons'
                  },
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
      this.loadNeuronsFromServer();
    }

    componentWillUnmount() {
        this.Nchart.destroy();

    }

    render() {
        return (
            <div>
            <div ref="neuronchart"/>
            </div>
        )
    }
}

export default NeuronGrid;
