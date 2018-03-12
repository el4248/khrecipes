import { combineReducers } from 'redux';

import recipes from '../reducers/search_reducer';

const rootReducer = combineReducers({
  recipes
});

export default rootReducer;