import React from 'react';
import ReactDOM from 'react-dom';
import Highcharts from 'highcharts';
import Heatmap from 'highcharts/modules/heatmap.js';


class IonChannelGrid extends React.Component {

  constructor(props) {
   super(props);
   this.state = {ionchannelsData:[],
   tooltipIonChannel:{}
 };
 }

  formatDataIonChannel(data)
  {
    console.log(" in formatDataIonChannel");
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


  formatToolTipIonChannel(data)
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

  loadIonChannelsFromServer(){
        $.ajax({
            url: "/pyopenworm/api/getchannels",
            datatype: 'json',
            cache: false,
            success: function(data) {
                var ttIChdata = this.formatToolTipIonChannel(data);
                data = this.formatDataIonChannel(data);
                this.setState({ionchannelsData: data,
                  tooltipIonChannel: ttIChdata
                });
                var self = this;
                console.log(this.refs);
                this.IChchart = new Highcharts[this.props.type || "Chart"](
                      this.refs.ionchannelschart,
                      this.props.options
                  );
                this.IChchart.series[0].setData(this.state.ionchannelsData);
                this.IChchart.update({
                  title: {
                      text: 'Ion Channels'
                  },
                    tooltip: {
                      formatter: function() {
                        var x=this.point.x;
                        var y=this.point.y;
                        return ttIChdata[x][y];
                      }
                    },
                    plotOptions: {
                            series: {
                                events: {
                                    click: function (event) {
                                      var channelname = ttIChdata[event.point.x][event.point.y]
                                      self.props.updateCurrCell(channelname);
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
      this.loadIonChannelsFromServer();
    }

    componentWillUnmount() {
        this.IChchart.destroy();

    }

    render() {
        return (
            <div>
            <div ref="ionchannelschart"/>

            </div>
        )
    }
}

export default IonChannelGrid;
