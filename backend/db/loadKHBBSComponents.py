import json
import os

from sqlalchemy import create_engine, text

import credentials

def main():
    db_uri = 'mysql://' + credentials.db['user'] + ":" + credentials.db['password'] + "@" + credentials.db['hostname'] + "/" + credentials.db['name']
    engine = create_engine(db_uri)
    conn = engine.connect()
    
    load_components(conn)

    conn.close()

def load_components(conn):
    directory = os.fsencode('./data/khbbs/components')
    for file in os.listdir(directory):
        filename = os.fsdecode(file)
        if filename.endswith(".json"):
            with open("./data/khbbs/components/" + filename, "r") as f:
                components = json.load(f)
            insert_components(conn, components)
        else:
            continue

def insert_components(conn, components):
    for component in components:
        insert_component(conn, component)

def insert_component(conn, component):
    query = text("INSERT INTO components (name, game_id, type) VALUES (:name, :game_id, :type)")
    result = conn.execute(query, name=component["name"], game_id=component["game_id"], type=component["type"])
    if "T" in component["users"] : insert_terra_link(conn, result.lastrowid)
    if "A" in component["users"] : insert_aqua_link(conn, result.lastrowid)
    if "V" in component["users"] : insert_ventus_link(conn, result.lastrowid)

def insert_terra_link(conn, component_id):
    query = text("INSERT INTO component_compatibilities VALUES (:component_id, 4)")
    conn.execute(query, component_id=component_id)

def insert_aqua_link(conn, component_id):
    query = text("INSERT INTO component_compatibilities VALUES (:component_id, 5)")
    conn.execute(query, component_id=component_id)

def insert_ventus_link(conn, component_id):
    query = text("INSERT INTO component_compatibilities VALUES (:component_id, 6)")
    conn.execute(query, component_id=component_id)


if __name__ == '__main__':
    main()