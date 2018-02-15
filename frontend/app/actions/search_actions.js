import * as SearchUtil from '../util/search_api_util';

export const RECEIVE_RECIPES = "RECEIVE_RECIPES";

export const receiveRecipes = recipes => ({
  type: RECEIVE_RECIPES,
  recipes
});

export const fetchRecipes = keywords => dispatch => (
  SearchUtil.findRecipes(keywords).then(recipes => (
    dispatch(receiveRecipes(recipes))
  ))
)