import React from 'react';
import ReactDOM from 'react-dom';
import Highcharts from 'highcharts';
import CellChannelGrid from './CellChannelGrid';
import NeuronGrid from './NeuronGrid';
import MuscleGrid from './MuscleGrid';
import SearchBar from './SearchBar';
import * as Rb from 'react-bootstrap';


class Grid extends React.Component {

constructor(props) {
   super(props);
   this.state = {
   currCell:""  };
 }


 updateCurrCell( cell)
 {
   this.setState({currCell:cell});
 }

render() {

  let channelmatrix;
  if (this.state.currCell)
  {
    console.log(this.state.currCell);
    channelmatrix= <CellChannelGrid currcell={this.state.currCell} Channeloptions={this.props.HeatMapoptions} />;
  }
    return (
        <div>
        <Rb.Row>
        <Rb.Panel>
        <SearchBar />
        </Rb.Panel>
        </Rb.Row>

        <Rb.Row>
        <Rb.Col xs={10} md={10} xsOffset={1} mdOffset={1}>
        <Rb.Panel>
        <NeuronGrid updateCurrCell={this.updateCurrCell.bind(this)} options={this.props.HeatMapoptions}/>
        </Rb.Panel>
        </Rb.Col>
        </Rb.Row>

        <Rb.Row>
        <MuscleGrid updateCurrCell={this.updateCurrCell.bind(this)} options={this.props.HeatMapoptions}/>
        </Rb.Row>

        {channelmatrix}
        </div>
    );
}

}

export default Grid;
