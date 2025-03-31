import random
from src.pokemon import (
    Fire,
    Water,
    Grass,
    Normal,
    Trainer,
    Battle,
)

pokemon_dict = {
    Fire: ["Charmander", 44, 17, "Flamethrower", "fire", "grass", "water"],
    Water: ["Vaporeon", 70, 19, "Hydro pump", "water", "fire", "grass"],
    Grass: ["Leafeon", 65, 17, "Giga drain", "grass", "water", "fire"],
    Normal: ["Eevee", 55, 18, "Headbutt", "normal", None, "Fighting"],
    Fire: ["Flareon", 65, 20, "Fire blast", "fire", "grass", "Water"],
    Water: ["Squirtle", 44, 16, "Surf", "water", "fire", "grass"],
    Grass: ["Bulbasaur", 45, 16, "Razor leaf", "grass", "water", "fire"],
}


# PLAYER 1 - POKEMON 1 #

print("Please enter the name of player_1.")
player_1_name = input()
print(
    f"Hey {player_1_name}! Welcome to the Pokemon game. "
    f"You are now a Pokemon Trainer."
)
print("Would you like to catch some Pokemons?: Y or N")

player_1 = Trainer(player_1_name)
response = input().strip().lower()
pok_1 = None
if response in ["y", "yes"]:
    print("Let's throw a Pokeball to catch your Pokemon! Sound good?")
    input()
    pokemon_1_type, pokemon_1_attributes = random.choice(
        list(pokemon_dict.items())
    )
    pokemon_name, hp, level, move, pokemon_type_str, strength, weakness = (
        pokemon_1_attributes
    )
    pok_1 = pokemon_instance = pokemon_1_type(
        pokemon_name, hp, level, move, pokemon_type_str, strength, weakness
    )
    player_1.throw_pokeball(pokemon_instance)
    print(
        f"You have caught: {pokemon_instance.name} \U0001f49a "
        f"Type: {pokemon_instance.pok_type}, "
        f"Hitpoints: {pokemon_instance.hit_points}, "
        f"Move: {pokemon_instance.move}, "
        f"Damage: {pokemon_instance.attack_damage}, "
        f"Strength: {pokemon_instance.strong_against}, "
        f"Weakness: {pokemon_instance.weak_against}"
    )
else:
    pokemon_1_type, pokemon_1_attributes = random.choice(
        list(pokemon_dict.items())
    )
    pokemon_name, hp, level, move, pokemon_type_str, strength, weakness = (
        pokemon_1_attributes
    )
    pok_1 = pokemon_instance = pokemon_1_type(
        pokemon_name, hp, level, move, pokemon_type_str, strength, weakness
    )
    player_1.throw_pokeball(pokemon_instance)
    print(
        f"No worries! "
        f"For the purpose of this Game your Pokemon is "
        f"{pokemon_instance.name}"
        f" \U0001f49a "
        f"Type: {pokemon_instance.pok_type}, "
        f"Hitpoints: {pokemon_instance.hit_points}, "
        f"Move: {pokemon_instance.move}, "
        f"Damage: {pokemon_instance.attack_damage}, "
        f"Strength: {pokemon_instance.strong_against}, "
        f"Weakness: {pokemon_instance.weak_against}"
    )

# PLAYER 2 - POKEMON 2 #

print("Please enter the name of player_2.")
player_2_name = input()
print(
    f"Hey {player_2_name}! Welcome to the Pokemon game. "
    f"You are now a Pokemon Trainer."
)
print("Would you like to catch some Pokemons?: Y or N")

player_2 = Trainer(player_2_name)
response = input().strip().lower()
pok_2 = None
if response in ["y", "yes"]:
    print("Let's throw a Pokeball to catch your Pokemon! Sound good?")
    input()
    pokemon_2_type, pokemon_2_attributes = random.choice(
        list(pokemon_dict.items())
    )
    pokemon_name, hp, level, move, pokemon_type_str, strength, weakness = (
        pokemon_2_attributes
    )
    pok_2 = pokemon_instance = pokemon_2_type(
        pokemon_name, hp, level, move, pokemon_type_str, strength, weakness
    )
    player_2.throw_pokeball(pokemon_instance)
    if pok_2 == pok_1:
        pokemon_2_type, pokemon_2_attributes = random.choice(
            list(pokemon_dict.items())
        )
        pokemon_name, hp, level, move, pokemon_type_str, strength, weakness = (
            pokemon_2_attributes
        )
        pok_2 = pokemon_instance = pokemon_2_type(
            pokemon_name, hp, level, move, pokemon_type_str, strength, weakness
        )
        player_2.throw_pokeball(pokemon_instance)
    else:
        print(
            f"You have caught: {pokemon_instance.name} \U0001f49a "
            f"Type: {pokemon_instance.pok_type}, "
            f"Hitpoints: {pokemon_instance.hit_points}, "
            f"Move: {pokemon_instance.move}, "
            f"Damage: {pokemon_instance.attack_damage}, "
            f"Strength: {pokemon_instance.strong_against}, "
            f"Weakness: {pokemon_instance.weak_against}"
        )
else:
    pokemon_2_type, pokemon_2_attributes = random.choice(
        list(pokemon_dict.items())
    )
    pokemon_name, hp, level, move, pokemon_type_str, strength, weakness = (
        pokemon_2_attributes
    )
    pok_2 = pokemon_instance = pokemon_2_type(
        pokemon_name, hp, level, move, pokemon_type_str, strength, weakness
    )
    player_2.throw_pokeball(pokemon_instance)
    if pok_2 == pok_1:
        pokemon_2_type, pokemon_2_attributes = random.choice(
            list(pokemon_dict.items())
        )
        pokemon_name, hp, level, move, pokemon_type_str, strength, weakness = (
            pokemon_2_attributes
        )
        pok_2 = pokemon_instance = pokemon_2_type(
            pokemon_name, hp, level, move, pokemon_type_str, strength, weakness
        )
        player_2.throw_pokeball(pokemon_instance)
    else:
        print(
            f"No worries! "
            f"For the purpose of this Game "
            f"your Pokemon is {pokemon_instance.name} \U0001f49a "
            f"Type: {pokemon_instance.pok_type}, "
            f"Hitpoints: {pokemon_instance.hit_points}, "
            f"Move: {pokemon_instance.move}, "
            f"Damage: {pokemon_instance.attack_damage}, "
            f"Strength: {pokemon_instance.strong_against}, "
            f"Weakness: {pokemon_instance.weak_against}"
        )

print("It's time to Battle!")
battle = Battle(pok_1, pok_2)
rounds = 10
for i in range(10):
    battle.take_turn()
battle.get_winner()
