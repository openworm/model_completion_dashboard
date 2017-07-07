import React from 'react';
import ReactDOM from 'react-dom';
import Matrix from './Matrix';

class App extends React.Component {
  render() {
    return (
        <div>
        <Matrix />
        </div>
    );
  }
}
ReactDOM.render(<App />, document.getElementById("app"));
