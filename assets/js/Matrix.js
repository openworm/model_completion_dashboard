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
