import React from 'react';
import ReactDOM from 'react-dom';
import Autosuggest from 'react-autosuggest';
import styles from './search.css';

class SearchBar extends React.Component {
  constructor() {
    super();

    this.state = {
      value: '',
      suggestions: [],
      allcells: []
    };
  }

  getSuggestions(value){
    const inputValue = value.trim().toLowerCase();
    const inputLength = inputValue.length;
    return inputLength === 0 ? [] : this.state.allcells.filter(cell =>
      cell.name.toLowerCase().slice(0, inputLength) === inputValue
    );
  }

  getSuggestionValue(suggestion) { return suggestion.name; }
  renderSuggestion(suggestion){

    return (
    <div>
    <strong>{suggestion.name}</strong>
    </div>
  );
}

  onChange (event, { newValue }) {
    this.setState({
      value: newValue
    });
  }

  onSuggestionsFetchRequested({ value }){
    this.setState({
      suggestions: this.getSuggestions(value)
    });
  }

  onSuggestionsClearRequested(){
    this.setState({
      suggestions: []
    });
  }

  loadCellNamesFromServer()
  {

    $.ajax({
        url: "/pyopenworm/api/getallcells/",
        datatype: 'json',
        cache: false,
        success: function(data) {
          this.setState({allcells:data})
        }.bind(this)
    });

  }

  componentDidMount() {
    this.loadCellNamesFromServer();
  }

  render() {
    const { value, suggestions } = this.state;

    const inputProps = {
      placeholder: 'Enter a CellName',
      value,
      onChange: this.onChange.bind(this)
    };

    return (
      <div className={styles.app}>
      <Autosuggest
        suggestions={suggestions}
        onSuggestionsFetchRequested={this.onSuggestionsFetchRequested.bind(this)}
        onSuggestionsClearRequested={this.onSuggestionsClearRequested.bind(this)}
        getSuggestionValue={this.getSuggestionValue.bind(this)}
        renderSuggestion={this.renderSuggestion.bind(this)}
        inputProps={inputProps}
      />
      </div>
    );
  }
}

export default SearchBar;
