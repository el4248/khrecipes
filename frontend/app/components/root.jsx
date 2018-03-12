import React from 'react';
import {Provider} from 'react-redux';
import {BrowserRouter as Router, Route, IndexRoute, Switch} from 'react-router-dom';

import App from './app';
import SearchContainer from './search/search_container';
import Test from './test';

const Root = ({store}) => (
  <Provider store={store}>
    <Router>
      <Switch>
        <Route path="/test" component={Test}/>
        <Route path="/" component={App}/>
      </Switch>
    </Router>
  </Provider>
);

export default Root;