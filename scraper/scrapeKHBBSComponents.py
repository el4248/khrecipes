import json

from util import get_soup

BASE_URL = "http://www.finalfantasykingdom.net/"
ATTACKS_SUFFIX = "bbsatkcommand.php"
MAGIC_SUFFIX = "bbsmagcommand.php"
MOVEMENT_SUFFIX = "bbsmovecommand.php"

def main():
	get_components(BASE_URL + ATTACKS_SUFFIX, "attack")
	get_components(BASE_URL + MAGIC_SUFFIX, "magic")
	get_components(BASE_URL + MOVEMENT_SUFFIX, "movement")
	return

def get_components(url, componentType):
	components = []
	soup = get_soup(url)
	attack_table_rows = soup.find_all("table")[10].find_all("tr")
	row_iter = iter(attack_table_rows)
	next(row_iter)		#ignore header row
	for tr in row_iter:
		items_in_tr = len(tr.findChildren())
		if items_in_tr > 13 or items_in_tr < 4:	#ignore odd rows that get detected but aren't part of the chart
			continue
		components.append(parse_component_row(tr, componentType))
	print("found " + str(len(components)) + " " + componentType + "...")
	with open("../data/components/KHBBS" + componentType + ".json", "w") as file_pointer:
	    json.dump(components, file_pointer)


def parse_component_row(tr, componentType):
	attack = {}
	td = tr.find_all("td")
	attack["name"] = str(td[0].renderContents()).lstrip("b'").rstrip("\\n'")
	attack["game_id"] = 4
	attack["type"] = componentType

	#site uses "blank.png" in place of image if not useable by a certain character
	users = ""
	if componentType == "movement":
		character_images = td[3].find_all("img")		#on the movement page, rows are 4 <td> long
	else:
		character_images = td[6].find_all("img")
		
	if character_images[0].get("src") == "bbs/dlterra1.png" : users += "T"
	if character_images[1].get("src") == "bbs/dlventus1.png" : users += "V"
	if character_images[2].get("src") == "bbs/dlaqua1.png" : users += "A"
	attack["users"] = users

	return attack

if __name__ == '__main__':
    main()