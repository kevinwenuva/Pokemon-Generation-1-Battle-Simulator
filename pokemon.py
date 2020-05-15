from move import Move
import random

"""
This is the class Pokemon, which generates a pokemon and assigns it to its stats, typing, status, stat boosts, and moves.
"""


class Pokemon:
    pokemon_dictionary = {}
    dv = 15
    ev = 252
    stab = 1.5
    level = 100
    moving = True
    bad_poison_counter = 0
    sleep_counter = random.randint(1, 8)

    def __init__(self, pokemon):
        pokemon_info = []
        if len(Pokemon.pokemon_dictionary) == 0:
            pokedex = open("gen_1_pokemon.csv", "r")
            for x in pokedex:
                pokemon_list = x.strip().split(",")
                Pokemon.pokemon_dictionary[pokemon_list[1].lower()] = pokemon_list
            pokedex.close()
        for key in Pokemon.pokemon_dictionary:
            if key == pokemon.lower():
                pokemon_info = Pokemon.pokemon_dictionary[key]
                break
        self.name = pokemon_info[1].lower()
        self.base_hp = int(pokemon_info[2])
        self.base_attack = int(pokemon_info[3])
        self.base_defense = int(pokemon_info[4])
        self.base_special = int(pokemon_info[5])
        self.base_speed = int(pokemon_info[6])
        self.type1 = pokemon_info[7].lower()
        self.type2 = pokemon_info[8].lower()
        self.actual_hp = int(((self.base_hp+Pokemon.dv)*2+Pokemon.ev/4)*Pokemon.level/100+Pokemon.level+10)
        self.actual_attack = int((((self.base_attack+Pokemon.dv)*2)+Pokemon.ev/4)*(Pokemon.level/100)+5)
        self.actual_defense = int((((self.base_defense+Pokemon.dv)*2)+Pokemon.ev/4)*(Pokemon.level/100)+5)
        self.actual_special = int((((self.base_special+Pokemon.dv)*2)+Pokemon.ev/4)*Pokemon.level/100+5)
        self.actual_speed = int((((self.base_speed+Pokemon.dv)*2)+Pokemon.ev/4)*Pokemon.level/100+5)
        self.battle_hp = int(((self.base_hp+Pokemon.dv)*2+Pokemon.ev/4)*Pokemon.level/100+Pokemon.level+10)
        self.battle_attack = int((((self.base_attack+Pokemon.dv)*2)+Pokemon.ev/4)*(Pokemon.level/100)+5)
        self.battle_defense = int((((self.base_defense+Pokemon.dv)*2)+Pokemon.ev/4)*(Pokemon.level/100)+5)
        self.battle_special = int((((self.base_special+Pokemon.dv)*2)+Pokemon.ev/4)*Pokemon.level/100+5)
        self.battle_speed = int((((self.base_speed+Pokemon.dv)*2)+Pokemon.ev/4)*Pokemon.level/100+5)
        self.attackStage = 1
        self.defenseStage = 1
        self.specialStage = 1
        self.speedStage = 1
        self.move1 = pokemon_info[9].lower()
        self.move2 = pokemon_info[10].lower()
        self.move3 = pokemon_info[11].lower()
        self.move4 = pokemon_info[12].lower()
        self.status = "healthy"

    def get_name(self):
        return self.name

    def get_level(self):
        return self.level

    def get_base_hp(self):
        return self.base_hp

    def get_type1(self):
        return self.type1

    def get_type2(self):
        return self.type2

    def get_status(self):
        return self.status

    def get_base_attack(self):
        return self.base_attack

    def get_base_defense(self):
        return self.base_defense

    def get_base_special(self):
        return self.base_special

    def get_base_speed(self):
        return self.base_speed

    def get_hp(self):
        return self.actual_hp

    def get_attack(self):
        return self.actual_attack

    def get_defense(self):
        return self.actual_defense

    def get_special(self):
        return self.actual_special

    def get_speed(self):
        return self.actual_speed

    def get_battle_hp(self):
        return self.battle_hp

    def get_battle_attack(self):
        return self.battle_attack

    def get_battle_defense(self):
        return self.battle_defense

    def get_battle_special(self):
        return self.battle_special

    def get_battle_speed(self):
        return self.battle_speed

    def getatkstage(self):
        return self.attackStage

    def getdefstage(self):
        return self.defenseStage

    def getspestage(self):
        return self.specialStage

    def getspdstage(self):
        return self.speedStage

    def getmove1(self):
        return self.move1

    def getmove2(self):
        return self.move2

    def getmove3(self):
        return self.move3

    def getmove4(self):
        return self.move4

    def setmove1(self, move):
        self.move1 = move

    def setmove2(self, move):
        self.move2 = move

    def setmove3(self, move):
        self.move3 = move

    def setmove4(self, move):
        self.move4 = move

    def set_status(self, status_condition):
        self.status = status_condition

    def stats_reset(self):
        self.attackStage = 1
        self.defenseStage = 1
        self.specialStage = 1
        self.speedStage = 1

    def setatkstage(self, increase):
        thing = 0
        if increase > 0 and self.attackStage >= 1:
            self.attackStage = (self.attackStage * 2 + increase)/2
        elif increase < 0 and self.attackStage <= 1:
            self.attackStage = 2/(-increase + (2/self.attackStage))
        elif increase > 0 and self.attackStage < 1:
            while 2/(-thing + (2/self.attackStage)) < 1 and increase > thing:
                thing += 1
            self.attackStage = (2 + (increase - thing))/2
        elif increase < 0 and self.attackStage > 1:
            while (self.attackStage * 2 + thing)/2 > 1 and increase < thing:
                thing -= 1
            self.attackStage = 2/(-(increase - thing) + 2)
        if self.attackStage > 4:
            self.attackStage = 4
        if self.attackStage < 0.25:
            self.attackStage = 0.25

    def setdefstage(self, increase):
        thing = 0
        if increase > 0 and self.defenseStage >= 1:
            self.defenseStage = (self.defenseStage * 2 + increase)/2
        elif increase < 0 and self.defenseStage <= 1:
            self.defenseStage = 2/(-increase + (2/self.defenseStage))
        elif increase > 0 and self.defenseStage < 1:
            while 2/(-thing + (2/self.defenseStage)) < 1 and increase > thing:
                thing += 1
            self.defenseStage = (2 + (increase - thing))/2
        elif increase < 0 and self.defenseStage > 1:
            while (self.defenseStage * 2 + thing)/2 > 1 and increase < thing:
                thing -= 1
            self.defenseStage = 2/(-(increase - thing) + 2)
        if self.defenseStage > 4:
            self.defenseStage = 4
        if self.defenseStage < 0.25:
            self.defenseStage = 0.25

    def setspestage(self, increase):
        thing = 0
        if increase > 0 and self.specialStage >= 1:
            self.specialStage = (self.specialStage * 2 + increase)/2
        elif increase < 0 and self.specialStage <= 1:
            self.specialStage = 2/(-increase + (2/self.attackStage))
        elif increase > 0 and self.specialStage < 1:
            while 2/(-thing + (2/self.specialStage)) < 1 and increase > thing:
                thing += 1
            self.specialStage = (2 + (increase - thing))/2
        elif increase < 0 and self.specialStage > 1:
            while (self.specialStage * 2 + thing)/2 > 1 and increase < thing:
                thing -= 1
            self.specialStage = 2/(-(increase - thing) + 2)
        if self.specialStage > 4:
            self.specialStage = 4
        if self.specialStage < 0.25:
            self.specialStage = 0.25

    def setspdstage(self, increase):
        thing = 0
        if increase > 0 and self.speedStage >= 1:
            self.speedStage = (self.speedStage * 2 + increase)/2
        elif increase < 0 and self.speedStage <= 1:
            self.speedStage = 2/(-increase + (2/self.speedStage))
        elif increase > 0 and self.speedStage < 1:
            while 2/(-thing + (2/self.speedStage)) < 1 and increase > thing:
                thing += 1
            self.speedStage = (2 + (increase - thing))/2
        elif increase < 0 and self.speedStage > 1:
            while (self.speedStage * 2 + thing)/2 > 1 and increase < thing:
                thing -= 1
            self.speedStage = 2/(-(increase - thing) + 2)
        if self.speedStage > 4:
            self.speedStage = 4
        if self.speedStage < 0.25:
            self.speedStage = 0.25

    def set_hp(self, damage):
        self.battle_hp -= damage
        if self.battle_hp <= 0:
            self.battle_hp = 0
        if self.battle_hp >= self.get_hp():
            self.battle_hp = self.get_hp()

    def burn(self):
        self.set_status("burned")
        self.battle_attack = self.actual_attack/2
        self.set_hp(int(self.actual_hp/16))

    def paralysis(self):
        self.set_status("paralyzed")
        self.actual_speed = self.actual_speed/4
        moving_factor = random.randint(1, 5)
        if moving_factor == 1:
            self.moving = False
        else:
            self.moving = True

    def poison(self):
        self.set_status("poisoned")
        self.set_hp(int(self.actual_hp/8))

    def bad_poison(self):
        self.set_status("badly poisoned")
        self.bad_poison_counter += 1
        self.set_hp(int(self.actual_hp/16 * self.bad_poison_counter))

    def frozen(self):
        self.set_status("frozen")
        self.moving = False

    def sleep(self):
        self.set_status("asleep")
        self.moving = False
        self.sleep_counter -= 1
        if self.sleep_counter == 0:
            self.moving = True
            self.set_status("healthy")

    def fainted(self):
        if self.get_battle_hp() <= 0:
            return True
        else:
            return False



