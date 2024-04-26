from bs4 import BeautifulSoup

# Assuming pokedex is a string containing HTML
# You can load it from a file or a web page using requests library
pokedex = '''
<div id="pokedex">
    <input id="searchbar" type="text" oninput="search_pokemon()">
    <ul>
        <li class="card">
            <img class="card-image" src="...">
            <h2 class="card-title">Bulbasaur</h2>
            <p class="card-subtitle">Type: Grass, Poison</p>
        </li>
        <li class="card">
            <img class="card-image" src="...">
            <h2 class="card-title">Charmander</h2>
            <p class="card-subtitle">Type: Fire</p>
        </li>
        <li class="card">
            <img class="card-image" src="...">
            <h2 class="card-title">Squirtle</h2>
            <p class="card-subtitle">Type: Water</p>
        </li>
    </ul>
</div>
'''


# Function to search for a Pokemon
def search_pokemon():
    # Get the input value and convert it to lowercase
    input_text = input().lower()

    # Parse the HTML
    soup = BeautifulSoup(pokedex, 'html.parser')

    # Get all the cards
    cards = soup.find_all(class_='card')

    # Loop through each card
    for card in cards:
        # Get the name of the Pokemon from the card title
        pokemon_name = card.find(class_='card-title').text.lower()

        # If the input text is not found in the Pokemon name
        # Hide the card, else show it
        if input_text not in pokemon_name:
            card['style'] = 'display: none;'
        else:
            card['style'] = 'display: list-item;'


# Call the search function
search_pokemon()
