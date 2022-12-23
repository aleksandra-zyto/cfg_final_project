

import requests

def recipe_search(ingredient):
    id = ""
    key = ""

    response = requests.get(f"https://api.edamam.com/search?q={ingredient}&app_id={id}&app_key={key}")
    data=response.json()
    return data["hits"]

def get_ingredients(result):
    for ingredient in result["recipe"]['ingredientLines']:
        print(ingredient)

def run():
    ingredient = input("What's on the menu today? ")
    results = recipe_search(ingredient)
    for result in results:
        recipe = result['recipe']
        print(recipe['label'])
        print(recipe['uri'])
        print("\nYou will need: ")
        get_ingredients(result)

        print()

run()
# print(recipe_search("cheese"))
#
# def choose_dish():
