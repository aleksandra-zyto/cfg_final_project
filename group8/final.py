
import requests
from termcolor import colored


def recipe_search(ingredient):
    """makes requests to the API with a given ingredient"""
    key = ""
    response = requests.get(f"https://api.spoonacular.com/recipes/complexSearch?query={ingredient}&apiKey={key}")
    data = response.json()
    recipes = []
    for recipe in data["results"]:
        id = recipe["id"]
        recipe_info = requests.get(f"https://api.spoonacular.com/recipes/{id}/information?includeNutrition=false&apiKey={key}").json()
        recipes.append(recipe_info)
        # stores the recipe info in a list

    return recipes


def compare_lists(user_list, result):
    """compares the requirements of the user and what is in the recipe"""
    recipe_list = []
    if result["vegetarian"] == True:
        recipe_list.append("vegetarian")
    elif result["vegan"] == True:
        recipe_list.append("vegan")
    elif result["dairyFree"] == True:
        recipe_list.append("df")
    elif result["glutenFree"] == True:
        recipe_list.append("gf")

    for element in user_list:
        if element in recipe_list:
            print(colored(element, "green"))
        else:
            print(colored(element, "red"))


def run():
    ingredient = input("What's on the menu today? ")
    diet = input("Do you have any dietary requirements? (vegetarian, vegan, gluten free or dairy free)\nEnter vegetarian, vegan, gf or df.\nValues should be separated by a space: ")
    time = int(float(input("How much time do you have for the recipe?\nEnter minutes\nIf it doesn't matter just continue: ")))
    print()
    user_list = diet.lower().split()
    results = recipe_search(ingredient)
    for result in results:
        if time >= result["readyInMinutes"]:
            print(result["title"])
            print(result["sourceUrl"])
            print("Recipe ready in {a} minutes or less".format(a=result["readyInMinutes"]))
            if user_list:
                print("Green dietary requirements are satisfied in the recipe: ")
                compare_lists(user_list, result)

            with open("recipe.txt", "a") as text_file:
                text_file.write("\n" + result["title"])
                text_file.write("\n" + result["sourceUrl"])
                text_file.write("\n" + "Recipe ready in " + str(result["readyInMinutes"]) + " minutes or less")
                text_file.write("\n" + " ")
            print()


run()
