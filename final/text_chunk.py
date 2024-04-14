import re
def split_recipes(file_path):
    # Read the content of the file
    with open(file_path, 'r', encoding='utf-8') as file:
        content = file.read()

    # Split the content into recipes based on the phrase "No. {number}"
    recipes_with_numbers = content.split('No. ')

    # Filter out empty strings and remove leading/trailing whitespaces
    recipes_with_numbers = [recipe.strip() for recipe in recipes_with_numbers if recipe.strip()]

    # Create a dictionary to store recipes
    recipes_dict = {}

    # Add recipes to the dictionary with the sentence starting with "No." as the key
    for recipe in recipes_with_numbers:
        
        # Find the sentence starting with "No."
        no_sentence = "No. " + recipe.split('\n', 1)[0].strip()
        # Add recipe to the dictionary
        # no_sentence = match.group(0)
        recipes_dict[no_sentence] = "No. " + recipe

    return recipes_dict


def recipes_to_return():
    # Path to the text file containing recipes
    file_path = "C:/Users/jdara/Desktop/eestec_2024/CookItalian_obooko.txt"  # Update this with the actual file path

    # Split recipes from the file
    recipes = split_recipes(file_path)
    return recipes


# recipes = recipes_to_return()
# print(recipes.keys())
# print(recipes[recipes.keys(0)])