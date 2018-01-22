import json
import os

from sqlalchemy import create_engine, text

import credentials

def main():
    db_uri = 'mysql://' + credentials.db['user'] + ":" + credentials.db['password'] + "@" + credentials.db['hostname'] + "/" + credentials.db['name']
    engine = create_engine(db_uri)
    conn = engine.connect()
    
    load_recipes(conn)

    conn.close()

def load_recipes(conn):
    cur_id = get_max_recipe_id(conn)
    cur_id = cur_id + 1 if cur_id else 1
        
    directory = os.fsencode('./data/khbbs/recipes')
    for file in os.listdir(directory):
        filename = os.fsdecode(file)
        if filename.endswith(".json"):
            with open("./data/khbbs/recipes/" + filename, "r") as f:
                recipes = json.load(f)
            cur_id = insert_recipes(conn, recipes, cur_id)
        else:
            continue

def insert_recipes(conn, recipes, id):
    for recipe in recipes:
        insert_recipe(conn, recipe, id)
        id += 1
    return id

def insert_recipe(conn, recipe, id):
    product_id = get_component_id(conn, recipe["product"])
    for component in recipe["components"]:
        ingredient_id = get_component_id(conn, component)
        insert_recipe_row(conn, id, ingredient_id, product_id, recipe["recipe_type"], 1, int(recipe["success"])/100, 4)
    if "T" in recipe["users"] : insert_terra_link(conn, id)
    if "A" in recipe["users"] : insert_aqua_link(conn, id)
    if "V" in recipe["users"] : insert_ventus_link(conn, id)

def get_component_id(conn, name):
    query = text("SELECT id FROM components WHERE name like :name")
    result = conn.execute(query, name=name).fetchone()
    return result[0]

def insert_recipe_row(conn, id, ingredient_id, product_id, recipe_type, count, success, game_id):
    query = text("INSERT INTO recipes VALUES (:id, :ingredient_id, :product_id, :recipe_type, :count, :success, 4)")
    conn.execute(query, id=id, ingredient_id=ingredient_id, product_id=product_id, recipe_type=recipe_type, count=count, success=success)

def insert_terra_link(conn, recipe_id):
    query = text("INSERT INTO recipe_compatibilities VALUES (:recipe_id, 4)")
    conn.execute(query, recipe_id=recipe_id)

def insert_aqua_link(conn, recipe_id):
    query = text("INSERT INTO recipe_compatibilities VALUES (:recipe_id, 5)")
    conn.execute(query, recipe_id=recipe_id)

def insert_ventus_link(conn, recipe_id):
    query = text("INSERT INTO recipe_compatibilities VALUES (:recipe_id, 6)")
    conn.execute(query, recipe_id=recipe_id)

def get_max_recipe_id(conn):
    query = text("SELECT MAX(id) FROM recipes")
    result = conn.execute(query).fetchone()
    return result[0]

if __name__ == '__main__':
    main()