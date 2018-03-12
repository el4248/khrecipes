import React from 'react';
import RecipeCard from "./recipe_card";

class SearchView extends React.Component {
  constructor(props) {
    super(props);
  }

  componentWillMount() {
    this.props.fetchRecipes("ars solum");
  }

  render() {
    let recipeCards = [];
    for(let recipe in this.props.recipes) {
      let cardInfo = JSON.stringify(this.props.recipes[recipe]);
      recipeCards.push(<RecipeCard key={recipe} recipe={this.props.recipes[recipe]}/>);
    }

    return (
      <div>
        {recipeCards}
      </div>       
    );
  }
}

export default SearchView;