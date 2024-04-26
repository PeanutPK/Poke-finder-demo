import requests

# URL of the PokéAPI
url = "https://pokeapi.co/api/v2/pokemon/"


# Function to fetch Pokémon data
def fetch_pokemon():
    pokemon_data = []
    for i in range(1, 151):
        response = requests.get(url + str(i))
        if response.status_code == 200:
            data = response.json()
            pokemon = {
                "name": data["name"],
                "image": data["sprites"]["front_default"],
                "type": ", ".join([t["type"]["name"] for t in data["types"]]),
                "id": data["id"]
            }
            pokemon_data.append(pokemon)
    return pokemon_data


# Function to display Pokémon details
def display_pokemon(pokemon):
    for poke in pokemon:
        print(f'Name: {poke["name"]}')
        print(f'Image: {poke["image"]}')
        print(f'Type: {poke["type"]}')
        print('-' * 30)


# Fetch Pokémon data
pokemon_data = fetch_pokemon()

# Display Pokémon details
display_pokemon(pokemon_data)
