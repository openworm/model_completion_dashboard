import React from 'react';
import ReactDOM from 'react-dom';
import {Typeahead} from 'react-bootstrap-typeahead';


class SearchBar extends React.Component {

  constructor(props) {
    super(props);

    this.state = {
      multiple: false,
      allcells: [],
      inputText: ''
    };
  }

  loadCellNamesFromServer()
  {

    $.ajax({
        url: "/pyopenworm/api/getallcells/",
        datatype: 'json',
        cache: false,
        success: function(data) {
          var cells = [];
          console.log(data);
          for (var key in data)
          {
            cells.push(data[key].name);
          }
          console.log(cells);
          this.setState({allcells:cells})
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
    let cellname;
    cellname = String(target).toUpperCase();
    this.props.updateCurrCell(cellname);
  }

  onKeyPressed(event){

    let cellname;
    if (event.key=='Enter')
    {
      cellname = this.state.inputText.toUpperCase();
      this.props.updateCurrCell(cellname);
    }
  }


  componentDidMount() {
    this.loadCellNamesFromServer();
  }

  render() {
    const {multiple} = this.state;

    return (
      <div onKeyDown={this.onKeyPressed.bind(this)}>
      <Typeahead
        labelKey="name"
        multiple={multiple}
        options={this.state.allcells}
        placeholder="Enter a cell name ..."
        onChange={this.handleSelect.bind(this)}
        onInputChange={this.handleKeyPress.bind(this)}
      />
      </div>
    );
  }
}

export default SearchBar ;
