import json

from util import get_soup, clean_contents

BASE_URL = "http://www.finalfantasykingdom.net/"
RECIPE_SUFFIX = "bbsmelding.php"

def main():
    get_recipes();
    return

def get_recipes():
    soup = get_soup(BASE_URL + RECIPE_SUFFIX)
    tables = soup.find_all("table")    #16 tables
    attack = tables[11]
    parse_table(attack, "attack")
    magic = tables[12]
    parse_table(magic, "magic")
    action = tables[13]
    parse_table(action, "action")
    shotlock = tables[14]
    parse_table(shotlock, "shotlock")

def parse_table(table, productType):
    recipes = []
    recipe_rows = table.find_all("tr")
    row_iter = iter(recipe_rows)
    next(row_iter)       #ignore header row
    for tr in row_iter:
        recipes.append(parse_recipe_row(tr, productType))
    print("found " + str(len(recipes)) + " " + productType + "...")
    with open("../data/recipes/KHBBS" + productType + ".json", "w") as file_pointer:
        json.dump(recipes, file_pointer)

def parse_recipe_row(tr, productType):
    recipe = {}
    td = tr.find_all("td")
    recipe["game_id"] = 4
    recipe["type"] = productType
    recipe["product"] = clean_contents(td[0].renderContents())
    recipe["recipe_type"] = clean_contents(td[3].renderContents())
    recipe["success"] = clean_contents(td[5].renderContents())
    recipe["components"] = []
    recipe["components"].append(clean_contents(td[1].renderContents()))
    recipe["components"].append(clean_contents(td[2].renderContents()))
    
    #site uses "blank.png" in place of image if not useable by a certain character
    users = ""
    character_images = td[4].find_all("img")
        
    if character_images[0].get("src") == "bbs/dlterra1.png" : users += "T"
    if character_images[1].get("src") == "bbs/dlventus1.png" : users += "V"
    if character_images[2].get("src") == "bbs/dlaqua1.png" : users += "A"
    recipe["users"] = users
    return recipe

if __name__ == '__main__':
    main()