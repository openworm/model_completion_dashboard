import React from 'react';
import ReactDOM from 'react-dom';
import MatrixApp from './MatrixApp';

class App extends React.Component {
  render() {
    return (
        <h1>
        <MatrixApp />
        </h1>
    );
  }
}
ReactDOM.render(<App />, document.getElementById("app"));
