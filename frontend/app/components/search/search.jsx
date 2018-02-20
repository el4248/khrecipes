import React from 'react';

class SearchView extends React.Component {
  constructor(props) {
    super(props);
  }

  componentDidMount() {
    this.props.fetchRecipes("ars solum");
    // console.log(this.props.recipes);
  }

  render() {
    return (
    <div>
      {JSON.stringify(this.props.recipes)}
    </div>       
    );
  }
}

export default SearchView;