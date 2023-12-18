import requests
import json


r = requests.get(f"https://pokeapi.co/api/v2/pokemon?limit=200&offset=100")
json_object = json.loads(r.text)
prettyPrint = json.dumps(json_object, indent=2)

print(prettyPrint)