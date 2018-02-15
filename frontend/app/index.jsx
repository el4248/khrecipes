import React from 'react';
import ReactDOM from 'react-dom';
import axios from 'axios';

import Root from './components/root';

document.addEventListener('DOMContentLoaded', () => {
  const root = document.getElementById('app');
  window.axios = axios;
  ReactDOM.render(<Root/>, root);
});