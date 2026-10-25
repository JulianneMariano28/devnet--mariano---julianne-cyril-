import requests
import random

pokemon_list = ["pikachu","charizard","eevee","snorlax","bulbasaur"]

pokemon_choice = random.choice(pokemon_list)
url = f"https://pokeapi.co/api/v2/pokemon/{pokemon_choice}"

response = requests.get(url)


if response.status_code == 200:
    info = response.json()

    name = info["name"]
    height = info["height"]
    weight = info["weight"]

    ability = random.choice(info["abilities"])["ability"]["name"]

    print("================================")
    print("     WHO'S THAT POKEMON?")
    print("================================")
    print(f"Randomly Selecting a Pokemon...")
    print(f"Height: {height / 10} meters")
    print(f"Weight: {weight / 10} kilograms")
    print(f"Hint: One ability of its is {ability}!")
    print("You have 3 attempts.")

    for attempt in range(1, 4):
        guess = input(
            f"\n        Attempt {attempt}/3\n"
            "================================\n"
            "Enter your guess: "
        ).strip().lower()

        if guess not in pokemon_list:
            print("\nInvalid Pokemon name. Try again!")
            continue

        if guess == name:
            print("Congratulations! You guessed the Pokemon!")
            break
        else:
            print("Wrong guess! Try again.")

    else:
        print(f"Game over! The correct answer is: {name.title()}.")

else:
    print("Failed to retrieve Pokemon information.")
    print("Status Code:", response.status_code)