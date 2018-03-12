import merge from 'lodash/merge';

import { RECEIVE_RECIPES } from '../actions/search_actions';

const searchReducer = (state = {}, action) => {
  Object.freeze(state);
  let newState = merge({}, state);

  switch(action.type) {
    case RECEIVE_RECIPES:
      return action.recipes;
    default:
      return state;
  }
};

export default searchReducer;