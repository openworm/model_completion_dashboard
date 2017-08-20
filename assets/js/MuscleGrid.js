import React from 'react';
import ReactDOM from 'react-dom';
import Highcharts from 'highcharts';
import Heatmap from 'highcharts/modules/heatmap.js';
import BodyMusclesGrid from './BodyMusclesGrid';
import PharynxMusclesGrid from './PharynxMusclesGrid';
import * as Rb from 'react-bootstrap';


class MuscleGrid extends React.Component {

    render() {

        return (
            <div>
             <Rb.Col xs={6} md={6}>
             <Rb.Panel>
            <BodyMusclesGrid updateCurrCell={this.props.updateCurrCell} options={this.props.options} />
            </Rb.Panel>
            </Rb.Col>
            <Rb.Col xs={6} md={6}>
            <Rb.Panel>
            <PharynxMusclesGrid updateCurrCell={this.props.updateCurrCell} options={this.props.options} />
            </Rb.Panel>
            </Rb.Col>
            </div>
        )
    }
}

export default MuscleGrid;
