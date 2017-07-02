import React from 'react';
import ReactDOM from 'react-dom';
import Highcharts from 'highcharts';
import Heatmap from 'highcharts/modules/heatmap.js';




class ChannelChart extends React.Component{

  formatDataChannel(data)
  {
    console.log(" in formatDataChannel");
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


  loadCellChannelsFromServer(){
        $.ajax({
            url: "/pyopenworm/api/getcellionchannels/?cellname="+this.props.currCell,
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


    getInitialState()
    {
      return {
        channelData:[],
        tooltipChannel:{},
        currChannel:""
      };
    }

    componentDidMount() {
      Heatmap(Highcharts);
      this.loadCellChannelsFromServer(this.props.currCell);
    }

    componentWillUnmount() {
        this.chart.destroy();
    }

    render() {
        return (
            <div ref="chchart"/>
        )
    }

}
export default ChannelChart;
