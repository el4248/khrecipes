import React from 'react';
import {Provider} from 'react-redux';
import {BrowserRouter as Router, Route} from 'react-router-dom';

import App from './app';

const Root = ({store}) => (
  <Router>
    <div>
      <Route path="/" component={App}>
      </Route>
    </div>
  </Router>
);

export default Root;