import React from 'react';
import ReactDOM from 'react-dom';
import Highcharts from 'highcharts';
import Heatmap from 'highcharts/modules/heatmap.js';
import BodyMusclesGrid from './BodyMusclesGrid';
import PharynxMusclesGrid from './PharynxMusclesGrid';


class MuscleGrid extends React.Component {

    render() {

        return (
            <div>
            <BodyMusclesGrid updateCurrCell={this.props.updateCurrCell} options={this.props.options} />
            <PharynxMusclesGrid updateCurrCell={this.props.updateCurrCell} options={this.props.options} />
            </div>
        )
    }
}

export default MuscleGrid;
