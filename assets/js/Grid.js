import React from 'react';
import ReactDOM from 'react-dom';
import Highcharts from 'highcharts';
import CellChannelGrid from './CellChannelGrid';
import NeuronGrid from './NeuronGrid';
import MuscleGrid from './MuscleGrid';
import SearchBar from './SearchBar';

class Grid extends React.Component {

constructor(props) {
   super(props);
   this.state = {
   currCell:""  };
 }

//   <NeuronGrid updateCurrCell={this.updateCurrCell.bind(this)} options={this.props.HeatMapoptions}/>

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
        <SearchBar />
        <NeuronGrid updateCurrCell={this.updateCurrCell.bind(this)} options={this.props.HeatMapoptions}/>
        <MuscleGrid updateCurrCell={this.updateCurrCell.bind(this)} options={this.props.HeatMapoptions}/>
        {channelmatrix}
        </div>
    );
}

}

export default Grid;
