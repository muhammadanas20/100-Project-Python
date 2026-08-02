recipes = {
    "biryani": {
        "ingrediants" : ["rice","meat","masala","tomato","onion","oil"],
        "steps": ["boil rice in water","make masla with meat,onion,and tomato","mix masala and boil rice and steam it."],
    },
    "salad":
    {
        "ingrediants":["lettuce","tomato","cucumber"],
        "steps": ["chop veges into small piecs","Toss and serve it"],
    }
}

choice = input(f"Choose {list(recipes)} :").lower()

recipe = recipes.get(choice)

if recipe:
    print("Ingrediants:", ", ".join(recipe["ingrediants"]))
    for number,step in enumerate(recipe["steps"],1):
        print(f"{number}. {step}")
else:
    print("Recipe not found")