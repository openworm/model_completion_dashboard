import React from 'react';
import ReactDOM from 'react-dom';
import { Router, Route, Link, browserHistory } from 'react-router';
import Matrix from './Matrix';
import ChannelMatrix from './ChannelMatrix';

ReactDOM.render((
   <Router history = {browserHistory}>
   <Route path="pyopenworm/" component={Matrix} />
   <Route path="pyopenworm/landing" component={Matrix} />
    <Route path="pyopenworm/channel" component={ChannelMatrix} />
   </Router>

), document.getElementById('app'))
