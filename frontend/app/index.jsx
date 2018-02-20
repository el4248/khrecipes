import React from 'react';
import ReactDOM from 'react-dom';
import axios from 'axios';

import Root from './components/root';
import configureStore from './store/store';

document.addEventListener('DOMContentLoaded', () => {
  let store = configureStore();
  window.store = store;
  const root = document.getElementById('app');
  ReactDOM.render(<Root store={store}/>, root);
});