import {connect} from 'react-redux';
import {fetchRecipes} from '../../actions/search_actions';
import SearchView from './search';

const mapStateToProps = state => ({
  recipes: state.recipes
});

const mapDispatchToProps = dispatch => ({
  fetchRecipes: keywords => dispatch(fetchRecipes(keywords))
});

export default connect(mapStateToProps, mapDispatchToProps)(SearchView);