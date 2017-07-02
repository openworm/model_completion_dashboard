import React from 'react';
import ReactDOM from 'react-dom';
import Highcharts from 'highcharts';
import Chart from './chart';

class MatrixApp extends React.Component {
    render() {

    const Channeloptions = {

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
              text: 'Channels'
          },


          colorAxis: {
              min: 0,
              minColor: '#000000',
              maxColor: Highcharts.getOptions().colors[0]
          },

          legend: {
              align: 'right',
              layout: 'vertical',
              margin: 0,
              verticalAlign: 'top',
              y: 25,
              symbolHeight: 280
          },

          series: [{
              name: 'Channel',
              borderWidth: 0,
              data:[],
              dataLabels: {
                  enabled: false,
                  color: '#000000'
              }
          }]

      };



      const Neuronoptions = {

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
              text: 'Neurons'
          },


          colorAxis: {
              min: 0,
              minColor: '#000000',
              maxColor: Highcharts.getOptions().colors[0]
          },

          legend: {
              align: 'right',
              layout: 'vertical',
              margin: 0,
              verticalAlign: 'top',
              y: 25,
              symbolHeight: 280
          },

          series: [{
              name: 'Neurons',
              borderWidth: 0,
              data:[],
              dataLabels: {
                  enabled: false,
                  color: '#000000'
              }
          }]

      };

        return (
              <Chart Neuronoptions={Neuronoptions} Channeloptions={Channeloptions}/>
        );
    }
}

export default MatrixApp;
