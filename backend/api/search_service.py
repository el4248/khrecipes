from sqlalchemy import text
class SearchService():
    def __init__(self, db_conn):
        self.db = db_conn

    def find_recipe(self, keywords, game_id):
        query_results = self.__get_recipes(keywords, game_id)    #TODO: implement using ORM notions
        return self.__consolidate_recipes(query_results)

    def __consolidate_recipes(self, query_results):
        recipes = {}
        for entry in query_results:
            if entry.id in recipes:
                recipes[entry.id]["ingredients"].append({"name": entry.ingredient_name, "type": entry.ingredient_type, "qty": entry.qty})
            else:
                recipes[entry.id] = {
                    "product": entry.prod_name,
                    "product_type": entry.prod_type,
                    "recipe_type": entry.recipe_type,
                    "success": entry.success,
                    "ingredients": [{"name": entry.ingredient_name, "type": entry.ingredient_type, "qty": entry.qty}]
                }
        return recipes

    def find_recipe_by_ingredient(self, keywords, game_id):
        query_results = self.__get_recipes_by_ingredient(keywords, game_id)#TODO: implement using ORM notions
        return self.__consolidate_recipes(query_results)

    def __get_recipes(self, keywords, game_id):
        query = text("""SELECT
                    recipes.id,
                    products.name as prod_name,
                    products.type as prod_type,
                    ingredients.name as ingredient_name,
                    ingredients.type as ingredient_type,
                    recipe_type, 
                    qty, 
                    success
                FROM
                    recipes
                JOIN
                    components ingredients
                ON
                    recipes.ingredient_id = ingredients.id
                JOIN 
                    components products
                ON
                    recipes.product_id = products.id
                WHERE
                    products.game_id = :game_id AND products.name like :keywords""")
        return self.db.engine.execute(query, keywords=keywords, game_id=game_id).fetchall()

    def __get_recipes_by_ingredient(self, keywords, game_id):
        query = text ("""SELECT
                    recipes.id,
                    products.name as prod_name,
                    products.type as prod_type,
                    ingredients.name as ingredient_name,
                    ingredients.type as ingredient_type,
                    recipe_type, 
                    qty, 
                    success
                FROM
                    recipes
                JOIN
                    components ingredients
                ON
                    recipes.ingredient_id = ingredients.id
                JOIN 
                    components products
                ON
                    recipes.product_id = products.id
                WHERE
                    ingredients.game_id = :game_id AND ingredients.name like :keywords""")
        return self.db.engine.execute(query, keywords=keywords, game_id=game_id).fetchall()
