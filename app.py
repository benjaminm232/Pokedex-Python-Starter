import json

# Open the JSON file and load the Pok edex
with open("./pokedex.json", encoding="utf8") as pokedex:
    data = json.load(pokedex)


# Create a function that will take the data from the JSON file and you will iterate through the list of pokemon and print each pokemons name.

# Add a language choice feature and print the pokemons name based on the user input

# Develop a function that creates a new list of pokemon based on the type the user searched for. If no pokemon was found of that type inform the user

#Develop a function to find all pokemon matching the name the user searched for. Ex. if "Char" return Charmander, Charmeleon and Charizard. Make the user aware if no pokemon was found. 


#Based on user input, show all moves that a pokemon could learn based on their type. For example, if Charizard is fire/fyling, show all fire and flying moves. HINT import the moves.json file too!

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

choice = input("Enter 'all' to show names or a Pokemon type to search: ").strip()

if choice.lower() == "all":
    pokemon_names()
else:
    find_pokemon(choice)


