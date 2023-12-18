# heb een een folder gemaakt waarin ik alle pokemons zet genaamd "pokemons". deze kan geleegd worden met clearPokemons.py

import requests
import json

pokemonName = input("Welke pokemon wilt u opzoeken? ")
r = requests.get(f"https://pokeapi.co/api/v2/pokemon/{pokemonName}")
json_object = json.loads(r.text)
prettyPrint = json.dumps(json_object, indent=2)

print(prettyPrint)