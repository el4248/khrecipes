import axios from 'axios';

export const findRecipes = keywords => (
  axios('/search?keywords=' + keywords)
);