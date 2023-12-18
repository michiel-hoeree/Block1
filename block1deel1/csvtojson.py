import requests
import json


r = requests.get("https://pokeapi.co/api/v2/pokemon?limit=100&offset=151")
dict = json.loads(r.text)
prettyPrint = json.dumps(dict, indent=2)
pokemonDict = dict["results"]


for pokemon in pokemonDict:
    with open(f"pokemons/{pokemon['name']}.json",'w') as file:
        json_object = json.dumps(pokemon)
        file.write(json_object)