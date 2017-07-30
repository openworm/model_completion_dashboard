import React from 'react';
import ReactDOM from 'react-dom';
import {Typeahead} from 'react-bootstrap-typeahead';


class SearchBarChannel extends React.Component {

  constructor(props) {
    super(props);

    this.state = {
      multiple: false,
      allchannels: [],
      inputText: ''
    };
  }

  loadChannelNamesFromServer()
  {

    $.ajax({
        url: "/pyopenworm/api/getchannels",
        datatype: 'json',
        cache: false,
        success: function(data) {
          var channels = [];
          console.log(data);
          for (var key in data)
          {
            channels.push(data[key].name);
          }
          console.log(channels);
          this.setState({allchannels:channels})
        }.bind(this)
    });

  }

  handleKeyPress(target)
  {
    this.setState({inputText:target});
  }

  handleSelect(target)
  {
    this.setState({inputText:target});
    let channelname;
    channelname = String(target).toUpperCase();
    this.props.updateCurrCell(channelname);
  }

  onKeyPressed(event){

    let channelname;
    if (event.key=='Enter')
    {
      channelname = this.state.inputText.toUpperCase();
      this.props.updateCurrCell(channelname);
    }
  }


  componentDidMount() {
    this.loadChannelNamesFromServer();
  }

  render() {
    const {multiple} = this.state;

    return (
      <div onKeyDown={this.onKeyPressed.bind(this)}>
      <Typeahead
        labelKey="name"
        multiple={multiple}
        options={this.state.allchannels}
        placeholder="Enter a ion channel name ..."
        onChange={this.handleSelect.bind(this)}
        onInputChange={this.handleKeyPress.bind(this)}
      />
      </div>
    );
  }
}

export default SearchBarChannel ;
