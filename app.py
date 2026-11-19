import json

# Open the JSON file and load the Pokedex
with open("./pokedex.json", encoding="utf8") as pokedex:
    data = json.load(pokedex)


def pokemon_names(language="english"):
    """Print every Pokemon name in the selected language."""
    print("\nPokedex names:")

    for pokemon in data:
        name = pokemon.get("name")

        if isinstance(name, dict):
            name = name.get(language, name.get("english", "Unknown"))

        print(name)


def find_pokemon(search_type):
    """Create and print a list of Pokemon matching a type."""
    matches = []
    search_type = search_type.lower()

    for pokemon in data:
        types = pokemon.get("type", pokemon.get("types", []))

        if isinstance(types, str):
            types = [types]

        if any(str(pokemon_type).lower() == search_type for pokemon_type in types):
            name = pokemon.get("name")

            if isinstance(name, dict):
                name = name.get("english", "Unknown")

            matches.append(name)

    if matches:
        print(f"\nPokemon with type '{search_type.title()}':")
        for pokemon_name in matches:
            print(pokemon_name)
    else:
        print(f"No Pokemon found with the type '{search_type.title()}'.")


# Simple menu for testing both functions
choice = input("Enter 'all' to show names or a Pokemon type to search: ").strip()

if choice.lower() == "all":
    pokemon_names()
else:
    find_pokemon(choice)


