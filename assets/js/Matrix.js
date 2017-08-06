import React from 'react';
import ReactDOM from 'react-dom';
import Highcharts from 'highcharts';
import Grid from './Grid';

class Matrix extends React.Component {
    render() {


      const HeatMapoptions = {

            chart: {
                type: 'heatmap',
                marginTop: 40,
                marginBottom: 80,
                plotBorderWidth: 1
            },

            xAxis: {
          visible: false
            },

            yAxis: {
          visible: false
      },


            title: {
                text: 'title'
            },

            colorAxis : {
              dataClasses: [{
                from: 0,
                to: 1,
                color: '#FF0000'
            },{
                from:1,
                to:2,
                color:'#FF8000'
            },{
                from:2,
                to:3,
                color:'#FFD700'
            },{
                from:3,
                to: 4,
                color:'#00CED1'
            },{
              from: 4,
              color: '#00FF00'
            }]

            },

            legend: {
              enabled : false
            },
            
         //
        //     legend: {
        //      title: {
        //          text: 'Degree of completion'
        //      },
        //      align: 'center',
        //      verticalAlign: 'bottom',
        //      floating: false,
        //      itemDistance: 0,
        //      layout: 'horizontal',
        //      valueDecimals: 0,
        //      backgroundColor: 'rgba(255,255,255,0.3)',
        //      symbolRadius: 0,
        //  },

            // legend: {
            //     align: 'right',
            //     layout: 'vertical',
            //     margin: 0,
            //     verticalAlign: 'top',
            //     y: 25,
            //     symbolHeight: 280
            // },

            // legend:{
            //   enabled: false
            // },

            series: [{
                name: 'name',
                borderWidth: 0,
                data:[],
                dataLabels: {
                    enabled: false,
                    color: '#000000'
                }
            }]

        };

        return (
          <div>
              <Grid HeatMapoptions={HeatMapoptions} />
              </div>
        );
    }
}

export default Matrix;
