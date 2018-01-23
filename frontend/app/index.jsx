import React from 'react';
import ReactDOM from 'react-dom';

import Root from './components/root';

document.addEventListener('DOMContentLoaded', () => {
    const root = document.getElementById('app');

    ReactDOM.render(<Root/>, root);
});