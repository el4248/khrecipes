import React from 'react';
import SearchContainer from './search/search_container';
const App = ({children}) => (
  <div>
    <SearchContainer/>
    {children}
  </div>
);

export default App;