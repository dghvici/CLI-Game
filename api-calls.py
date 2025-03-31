import requests
import random
from pprint import pprint


base_url = "https://pokeapi.co/api/v2/pokemon/"
def get_pokemon():
    id = random.randint(0, 999)
    url = f"{base_url}/{id}/"
    response = requests.get(url)
    data = response.json()
    pprint(data)

get_pokemon()