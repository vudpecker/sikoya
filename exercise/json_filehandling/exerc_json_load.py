import json

with open("exercise\json_filehandling\donut.json", "r") as f:
#with open("donut.json", "r") as f:
    recipes = json.load(f)

#recipe = json.dumps(recipes)

#print("The recipes are " + str(json.dumps(recipes)))


batter_info = recipes.get("batters", {}).get("batter", [])
print(f"The batter info is {batter_info}")
    
print("The first recipe:" + str(recipes["batters"]["batter"]))