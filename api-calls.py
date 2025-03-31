import requests
import random
from pprint import pprint


base_url = "https://pokeapi.co/api/v2/pokemon/"
def get_pokemon():
    id = random.randint(0, 999)
    if id:
        pokemon_url = f"{base_url}/{id}/"
        response = requests.get(pokemon_url)
        data = response.json()
        poke_name = data["name"]
        poke_type = [type_info['type']['name'] for type_info in data['types']][0]
        moves = [move_info['move']['name'] for move_info in data['moves']][0]
        print(poke_name, poke_type, moves)

get_pokemon()
