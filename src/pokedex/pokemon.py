import requests

res = requests.get("https://pokeapi.co/api/v2/pokemon/pikachu")
pokemon = res.json()
print(pokemon["form"])
