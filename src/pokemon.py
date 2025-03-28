class Pokemon:

    def __init__(self, name, hit_points, attack_damage, move):
        self.name = name
        self.hit_points = hit_points
        self.attack_damage = attack_damage
        self.move = move

    def use_move(self):
        return f"{self.name} used {self.move}"

    def take_damage(self, damage_points):
        self.hit_points = self.hit_points - damage_points
        return self.hit_points

    def has_fainted(self):
        if self.hit_points <= 0:
            return True
        else:
            return False


class Fire(Pokemon):
    def __init__(
        self,
        name,
        hit_points,
        attack_damage,
        move,
        pok_type,
        strong_against,
        weak_against,
    ):
        super().__init__(name, hit_points, attack_damage, move)
        self.pok_type = pok_type
        self.strong_against = strong_against
        self.weak_against = weak_against

    def get_multiplier(self, pokemon):
        self.pokemon = pokemon
        if self.strong_against == pokemon.pok_type:
            return 1.5
        if self.weak_against == pokemon.pok_type:
            return 0.5
        else:
            return 1


class Water(Pokemon):
    def __init__(
        self,
        name,
        hit_points,
        attack_damage,
        move,
        pok_type,
        strong_against,
        weak_against,
    ):
        super().__init__(name, hit_points, attack_damage, move)
        self.pok_type = pok_type
        self.strong_against = strong_against
        self.weak_against = weak_against

    def get_multiplier(self, pokemon):
        self.pokemon = pokemon
        if self.strong_against == pokemon.pok_type:
            return 1.5
        if self.weak_against == pokemon.pok_type:
            return 0.5
        else:
            return 1


class Grass(Pokemon):
    def __init__(
        self,
        name,
        hit_points,
        attack_damage,
        move,
        pok_type,
        strong_against,
        weak_against,
    ):
        super().__init__(name, hit_points, attack_damage, move)
        self.pok_type = pok_type
        self.strong_against = strong_against
        self.weak_against = weak_against

    def get_multiplier(self, pokemon):
        self.pokemon = pokemon
        if self.strong_against == pokemon.pok_type:
            return 1.5
        if self.weak_against == pokemon.pok_type:
            return 0.5
        else:
            return 1


class Normal(Pokemon):
    def __init__(
        self,
        name,
        hit_points,
        attack_damage,
        move,
        pok_type,
        strong_against,
        weak_against,
    ):
        super().__init__(name, hit_points, attack_damage, move)
        self.pok_type = pok_type
        self.strong_against = strong_against
        self.weak_against = weak_against

    def get_multiplier(self, pokemon):
        self.pokemon = pokemon
        if self.strong_against == pokemon.pok_type:
            return 1.5
        if self.weak_against == pokemon.pok_type:
            return 0.5
        else:
            return 1


class Pokeball:
    def __init__(self):
        self.pokeball = None

    def catch(self, pokemon):
        self.pokemon = pokemon
        if self.is_empty():
            self.pokeball = pokemon
        else:
            raise Exception("pokeball is full")

    def is_empty(self):
        return not self.pokeball


class Trainer:
    def __init__(self, name):
        self.name = name
        self.belt = [Pokeball() for i in range(6)]

    def throw_pokeball(self, pokemon):
        for indx, pok in enumerate(self.belt):
            if pok.is_empty():
                pok.catch(pokemon)
                return pok
        raise Exception("Belt is full")


class Battle:
    def __init__(self, pokemon_1, pokemon_2):
        self.pokemon_1 = pokemon_1
        self.pokemon_2 = pokemon_2
        self.whos_turn = 0

    def take_turn(self):
        while self.pokemon_1.hit_points > 0 and self.pokemon_2.hit_points > 0:
            attacker = (
                self.pokemon_1 if self.whos_turn % 2 == 0 else self.pokemon_2
            )
            defender = (
                self.pokemon_1 if self.whos_turn % 2 != 0 else self.pokemon_2
            )
            damage = attacker.get_multiplier(defender) + attacker.attack_damage
            defender.take_damage(damage)
            self.whos_turn += 1
            if self.pokemon_1.hit_points > 0 and self.pokemon_2.hit_points > 0:
                print(
                    f"Round {self.whos_turn}: {defender.name} "
                    f"has taken {damage} damage points, "
                    f"remaining hit points {defender.hit_points}"
                )
                return (
                    f"Round {self.whos_turn}: {defender.name} "
                    f"has taken {damage} damage points, "
                    f"remaining hit points {defender.hit_points}"
                )
            else:
                print(
                    f"Round {self.whos_turn}: {defender.name} "
                    f"has taken {damage} damage points, "
                    f"{defender.name} has fainted."
                )
                return (
                    f"Round {self.whos_turn}: {defender.name} "
                    f"has taken {damage} damage points, {defender.name} "
                    f"has fainted."
                )

    def get_winner(self):
        if self.pokemon_1.hit_points < 0:
            print(
                f"{self.pokemon_1.name} has fainted, "
                f"winner is {self.pokemon_2.name}."
            )
            return (
                f"{self.pokemon_1.name} has fainted, "
                f"winner is {self.pokemon_2.name}."
            )
        elif self.pokemon_2.hit_points < 0:
            print(
                f"{self.pokemon_2.name} has fainted, "
                f"winner is {self.pokemon_1.name}."
            )
            return (
                f"{self.pokemon_2.name} has fainted, "
                f"winner is {self.pokemon_1.name}."
            )
        else:
            print("Winner:", None)
            return None
