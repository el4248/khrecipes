import React from 'react';
import RecipeCard from "./recipe_card";

class SearchView extends React.Component {
  constructor(props) {
    super(props);
    this._handleKeyPress = this._handleKeyPress.bind(this);
  }

  componentWillMount() {
    
  }

  _handleKeyPress(e) {
    if (e.key === 'Enter') {
      this.props.fetchRecipes(document.querySelector('#recipe-search').value);
    }
  }

  render() {
    let recipeCards = [];
    for(let recipe in this.props.recipes) {
      let cardInfo = JSON.stringify(this.props.recipes[recipe]);
      recipeCards.push(<RecipeCard key={recipe} recipe={this.props.recipes[recipe]}/>);
    }

    return (
      <div>
        <input id="recipe-search" type="text" placeholder="What do you want to make?" onKeyPress={this._handleKeyPress} onFocus={(e) => e.target.placeholder = ""} onBlur={(e) => e.target.placeholder = "What do you want to make?"}/>
        {recipeCards}
      </div>       
    );
  }
}

export default SearchView;