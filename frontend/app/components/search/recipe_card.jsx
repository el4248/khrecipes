import React from 'react';

class RecipeCards extends React.Component {
  constructor(props) {
    super(props);
  }

  render() {
    let ingredients = [];
    let ingredientCount = this.props.recipe.ingredients.length;
    for(let i = 0; i < ingredientCount; ++i) {
      ingredients.push(<div key={i + Math.random()}>{this.props.recipe.ingredients[i].name}</div>);
    }

    return (
      <section>
        <div>{this.props.recipe.product}</div>
        {ingredients}
      </section>       
    );
  }
}

export default RecipeCards;