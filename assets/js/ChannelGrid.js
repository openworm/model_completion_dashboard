import React from 'react';
import ReactDOM from 'react-dom';
import Highcharts from 'highcharts';
import IonChannelGrid from './IonChannelGrid';
import SearchBarChannel from './SearchBarChannel';
import IonChannelDetails from './IonChannelDetails';
import * as Rb from 'react-bootstrap';


class ChannelGrid extends React.Component {

constructor(props) {
   super(props);
   this.state = {
   currChannel:""  };
 }


 updateCurrCell(channel)
 {
   this.setState({currChannel:channel});
 }

render() {

  let channeldetailsmatrix;
  if (this.state.currChannel)
  {
    console.log(this.state.currChannel);
    channeldetailsmatrix= <IonChannelDetails currchannel={this.state.currChannel} options={this.props.HeatMapoptions} />;
  }
    return (
        <div>
        <Rb.Row>
        <Rb.Panel>
        <SearchBarChannel updateCurrCell={this.updateCurrCell.bind(this)} />
        </Rb.Panel>
        </Rb.Row>

        <Rb.Row>
        <Rb.Col xs={10} md={10} xsOffset={1} mdOffset={1}>
        <Rb.Panel>
        <IonChannelGrid updateCurrCell={this.updateCurrCell.bind(this)} options={this.props.HeatMapoptions}/>
        </Rb.Panel>
        </Rb.Col>
        </Rb.Row>

        <Rb.Row>
        <Rb.Col xs={10} md={10} xsOffset={1} mdOffset={1}>
        <Rb.Panel>
        {channeldetailsmatrix}
        </Rb.Panel>
        </Rb.Col>
        </Rb.Row>

        </div>
    );
}

}

export default ChannelGrid;
