import React from 'react';
import ReactDOM from 'react-dom';
import {Typeahead} from 'react-bootstrap-typeahead';


class SearchBar extends React.Component {
  constructor(props) {
    super(props);

    this.state = {
      multiple: false,
      allcells: []
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


  componentDidMount() {
    this.loadCellNamesFromServer();
  }

  render() {
    const {multiple} = this.state;

    return (
      <div>
      <Typeahead
        labelKey="name"
        multiple={multiple}
        options={this.state.allcells}
        placeholder="Enter a cell name ..."
      />
      </div>
    );
  }
}

export default SearchBar ;
