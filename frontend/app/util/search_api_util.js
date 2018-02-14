import axios from 'axios';

export const findRecipe = keywords => (
    axios('/search?keywords=' + keywords)
);