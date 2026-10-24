import random
import requests


pokemon_list = ["Pikachu", "Charizard", "Eevee", "Snorlax", "Bulbasaur"]

pokemon_choice = random.choice(pokemon_list)
url = f"https://pokeapi.co/api/v2/pokemon/{pokemon_choice}"
r = request.get("https://pokeapi.co/api/v2/pokemon/{pokemon_choice}")

if request.status.code == 200:
    info = response.json

    name = info ["name"]
    height = info ["height"]
    weight = info ["weight"]

print(f"Randomly Selecting Pokemon...")
print(f"Selected Pokemon has a height of: {height}")
print(f"Selected Pokemon has a weight of: {weight}")

else:
    print(f"Failed to catch info from the selected pokemon.")

guess = input ("You guess is.....: ")

print(f"Congratulations, You're Correct!!")

print(f"The correct answer is: {pokemon_choice")