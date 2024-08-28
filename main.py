"""
*
"""
#Dein Code kommt hier hin
import json


def adjust_recipe(r, p):
    """
    *
    Args:
        r:
        p:

    Returns:

    """
    new_rec = load_recipe(r) if isinstance(r, str) else r
    p, new_rec["servings"] = p / new_rec["servings"], p
    new_rec["ingredients"] = dict([(i, int(y*p)) for i, y in new_rec["ingredients"].items()])
    return new_rec


def load_recipe(r):
    """

    Args:
        r:

    Returns:

    """
    return json.loads(r)


if __name__ == '__main__':
    # Beispiel für die Datenstruktur eines Rezepts
    recipe_json = ('{"title": "Spaghetti Bolognese", "ingredients": {"Spaghetti": 400, "Tomato Sauce": 300,'
                   ' "Minced Meat"'
                   ': 500}, "servings": 4}')
    print(adjust_recipe(recipe_json, 2))
    # Dein Code kommt hier hin
