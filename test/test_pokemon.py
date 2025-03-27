from src.pokemon import Pokemon, Fire, Water, Grass, Normal, Pokeball, Trainer, Battle
import pytest

def test_class_has_all_attribute_properties():
    test_pokemon = Pokemon('Eevee', 55, 18, 'Headbutt')
    assert hasattr(test_pokemon, 'name')
    assert hasattr(test_pokemon, 'hit_points')
    assert hasattr(test_pokemon, 'attack_damage')
    assert hasattr(test_pokemon, 'move')

def test_class_has_property_values_that_were_passed():
    test_pokemon = Pokemon('Eevee', 55, 18, 'Headbutt')
    assert test_pokemon.name == 'Eevee'
    assert test_pokemon.attack_damage == 18

def test_method_use_move_returns_string_with_name_and_move():
    test_pokemon = Pokemon('Eevee', 55, 18, 'Headbutt') 
    assert test_pokemon.use_move() == 'Eevee used Headbutt'

def test_method_for_health_damage():
    test_pokemon = Pokemon('Eevee', 55, 18, 'Headbutt') 
    assert test_pokemon.take_damage(5) == 50

def test_method_return_true_when_health_is_zero():
    test_pokemon = Pokemon('Eevee', 55, 18, 'Headbutt') 
    test_pokemon.take_damage(56)
    assert test_pokemon.has_fainted() is True

def test_types_are_children_of_pokemon_class():
    assert issubclass(Fire, Pokemon)
    test_pokemon_type_fire = Fire('Charmander', 44, 17, 'Flamethrower','fire', 'grass', 'water')
    test_pokemon_type_water = Water('Vaporeon', 70, 19, 'Hydro pump', 'water', 'fire', 'grass')
    test_pokemon_type_grass = Grass('Leafeon', 65, 17, 'Giga drain', 'grass', 'water', 'fire')
    test_pokemon_type_normal = Normal('Eevee', 55, 18, 'Headbutt', 'normal', None, 'Fighting')
    assert isinstance(test_pokemon_type_fire, Pokemon)
    assert isinstance(test_pokemon_type_water, Pokemon)
    assert isinstance(test_pokemon_type_grass, Pokemon)
    assert isinstance(test_pokemon_type_normal, Pokemon)

def test_parameter_for_subclass_fire():
    test_pokemon_type_fire = Fire('Charmander', 44, 17, 'Flamethrower','fire', 'grass', 'water')
    assert test_pokemon_type_fire.name == 'Charmander'
    assert test_pokemon_type_fire.weak_against == 'water'
    
def test_should_return_the_multiplier_depending_on_the_weak_against():
    test_pokemon_type_fire = Fire('Charmander', 44, 17, 'Flamethrower','fire', 'grass', 'water')
    test_pokemon_type_water = Water('Vaporeon', 70, 19, 'Hydro pump', 'water', 'fire', 'grass')
    test_pokemon_type_grass = Grass('Leafeon', 65, 17, 'Giga drain', 'grass', 'water', 'fire')
    test_pokemon_type_normal = Normal('Eevee', 55, 18, 'Headbutt', 'normal', None, 'Fighting')
    assert test_pokemon_type_fire.get_multiplier(test_pokemon_type_water) == 0.5
    assert test_pokemon_type_grass.get_multiplier(test_pokemon_type_water) == 1.5
    assert test_pokemon_type_normal.get_multiplier(test_pokemon_type_water) == 1

def test_catch_method_pass_pokemon_and_assign_it_to_pokeball_if_empty():
    test_pokemon_type_fire = Fire('Charmander', 44, 17, 'Flamethrower','fire', 'grass', 'water')
    test_pokemon_type_water = Water('Vaporeon', 70, 19, 'Hydro pump', 'water', 'fire', 'grass')
    ball_1 = Pokeball()
    
    ball_1.catch(test_pokemon_type_fire)
    assert ball_1.pokeball is not None
    assert ball_1.pokeball == test_pokemon_type_fire
    
    
    with pytest.raises(Exception, match='pokeball is full'):
        ball_1.catch(test_pokemon_type_water)
    
def test_is_empty_method_when_pokeball_is_empty():
    test_pokemon_type_fire = Fire('Charmander', 44, 17, 'Flamethrower','fire', 'grass', 'water')
    ball_1 = Pokeball()
    assert ball_1.is_empty() == True
    catch_char = ball_1.catch(test_pokemon_type_fire)
    assert ball_1.is_empty() == False

def test_trainer_class_has_a_proberty_belt():
    trainer_1 = Trainer('Ash')
    assert hasattr(trainer_1, 'belt')

def test_pokeballs_are_added_to_belt_if_it_has_less_than_6():
    test_pokemon_type_fire = Fire('Charmander', 44, 17, 'Flamethrower','fire', 'grass', 'water')
    trainer_1 = Trainer('Ash')
    throw_1 = trainer_1.throw_pokeball(test_pokemon_type_fire)
    assert throw_1.pokemon.name == 'Charmander'
    assert trainer_1.belt[0].pokemon.name == 'Charmander'
    throw_2 = trainer_1.throw_pokeball(test_pokemon_type_fire)
    throw_3 = trainer_1.throw_pokeball(test_pokemon_type_fire)
    throw_4 = trainer_1.throw_pokeball(test_pokemon_type_fire)
    throw_5 = trainer_1.throw_pokeball(test_pokemon_type_fire)
    throw_6 = trainer_1.throw_pokeball(test_pokemon_type_fire)
    with pytest.raises(Exception, match='Belt is full'):
        trainer_1.throw_pokeball(test_pokemon_type_fire)

def test_battle_class_properties():
    pok_1 = Water('Vaporeon', 70, 19, 'Hydro pump', 'water', 'fire', 'grass')
    pok_2 = Fire('Charmander', 44, 17, 'Flamethrower','fire', 'grass', 'water')
    battle = Battle(pok_1, pok_2)
    assert battle.pokemon_1 == pok_1
    assert battle.pokemon_2 == pok_2

def test_take_turn_functionality():
    pok_1 = Water('Vaporeon', 70, 19, 'Hydro pump', 'water', 'fire', 'grass')
    pok_2 = Fire('Charmander', 44, 17, 'Flamethrower','fire', 'grass', 'water')
    battle = Battle(pok_1, pok_2)
    for i in range(3):
        battle.take_turn()

def test_take_turn_correctly_calls_attacker_defender_and_substracts_right_hit_points():
    pok_1 = Water('Vaporeon', 70, 19, 'Hydro pump', 'water', 'fire', 'grass')
    pok_2 = Grass('Leafeon', 65, 17, 'Giga drain', 'grass', 'water', 'fire')
    battle = Battle(pok_1, pok_2)
    assert battle.take_turn() == 'Round 1: Leafeon has taken 19.5 damage points, remaining hit points 45.5'
    assert battle.take_turn() == 'Round 2: Vaporeon has taken 18.5 damage points, remaining hit points 51.5'
    assert battle.take_turn() == 'Round 3: Leafeon has taken 19.5 damage points, remaining hit points 26.0'
    assert battle.take_turn() == 'Round 4: Vaporeon has taken 18.5 damage points, remaining hit points 33.0'
    assert battle.take_turn() == 'Round 5: Leafeon has taken 19.5 damage points, remaining hit points 6.5'
    assert battle.take_turn() == 'Round 6: Vaporeon has taken 18.5 damage points, remaining hit points 14.5'

def test_take_turns_flags_when_the_pokemon_has_fainted():
    pok_1 = Water('Vaporeon', 70, 19, 'Hydro pump', 'water', 'fire', 'grass')
    pok_2 = Grass('Leafeon', 65, 17, 'Giga drain', 'grass', 'water', 'fire')
    battle = Battle(pok_1, pok_2)
    battle.take_turn()
    battle.take_turn()
    battle.take_turn()
    battle.take_turn()
    battle.take_turn()
    battle.take_turn()
    assert battle.take_turn() == 'Round 7: Leafeon has taken 19.5 damage points, Leafeon has fainted.'
    
def test_get_winner_returns_None_and_then_correct_winner():
    pok_1 = Water('Vaporeon', 70, 19, 'Hydro pump', 'water', 'fire', 'grass')
    pok_2 = Grass('Leafeon', 65, 17, 'Giga drain', 'grass', 'water', 'fire')
    battle = Battle(pok_1, pok_2)
    assert battle.get_winner() == None
    battle.take_turn()
    assert battle.get_winner() == None
    battle.take_turn()
    assert battle.get_winner() == None
    battle.take_turn()
    assert battle.get_winner() == None
    battle.take_turn()
    assert battle.get_winner() == None
    battle.take_turn()
    assert battle.get_winner() == None
    battle.take_turn()
    assert battle.get_winner() == None
    battle.take_turn()
    assert battle.get_winner() == 'Leafeon has fainted, winner is Vaporeon.'
    



