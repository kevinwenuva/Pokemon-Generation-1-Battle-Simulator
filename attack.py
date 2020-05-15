from pokemon import Pokemon
from move import Move
import random

"""
The function attack does an attack on a pokemon from another pokemon. Using the damage formula for pokemon, the damage 
is calculated by using the attacker pokemon's attack stats and the defender pokemon's defense stats. Then, special side 
effects are programmed by using data from moves.csv.
"""
def attack(attacker_pokemon, defender_pokemon, move):
    move = Move(move)
    random_modifier = random.randint(85, 101) / 100
    type_advantage_list = []
    if move.get_type() == attacker_pokemon.get_type1() or move.get_type() == attacker_pokemon.get_type1():
        stab = 1.5  # STAB stands for same type attack bonus
    else:
        stab = 1
    critical_factor = int(attacker_pokemon.get_base_speed() / 2)
    critical_hit = random.randint(0, 256)
    if critical_factor in range(critical_hit, 256):
        critical_modifier = 2
    else:
        critical_modifier = 1
    type_advantage = open("type_advantages.csv", "r")
    for line in type_advantage:
        type_advantage_thing = line.strip().lower().split(",")
        type_advantage_list.append(type_advantage_thing)
    for line in range(len(type_advantage_list)):
        if move.get_type().lower() == type_advantage_list[line][1] and defender_pokemon.get_type1().lower() == type_advantage_list[line][2]:
            type_advantage_modifier_1 = float(type_advantage_list[line][3])
            break
        else:
            type_advantage_modifier_1 = 1
    for line in range(len(type_advantage_list)):
        if move.get_type().lower() == type_advantage_list[line][1] and defender_pokemon.get_type2().lower() == type_advantage_list[line][2]:
            type_advantage_modifier_2 = float(type_advantage_list[line][3])
            break
        else:
            type_advantage_modifier_2 = 1
    type_advantage_modifier = type_advantage_modifier_1 * type_advantage_modifier_2
    attacker_special = attacker_pokemon.get_battle_special()
    defender_special = defender_pokemon.get_battle_special()
    attacker_attack = attacker_pokemon.get_battle_attack()
    defender_defense = defender_pokemon.get_battle_defense()
    if critical_modifier == 1:
        attacker_special_stage = attacker_pokemon.getspestage()
        attacker_attack_stage = attacker_pokemon.getatkstage()
        defender_defense_stage = defender_pokemon.getdefstage()
        defender_special_stage = defender_pokemon.getspestage()
    else:
        attacker_special_stage = 1
        attacker_attack_stage = 1
        defender_defense_stage = 1
        defender_special_stage = 1
    accuracy_factor = random.randint(1, 101)
    move_accuracy = move.get_accuracy()
    if move_accuracy != "*":
        if accuracy_factor in range(1, int(move_accuracy)+1):
            accuracy_modifier = 1
        else:
            accuracy_modifier = 0
    else:
        accuracy_modifier = 1
    power = move.get_power()
    if attacker_pokemon.get_status() != "healthy":
        if attacker_pokemon.get_status() == "burned":
            attacker_pokemon.burn()
        if attacker_pokemon.get_status() == "paralyzed":
            attacker_pokemon.paralysis()
        if attacker_pokemon.get_status() == "poisoned":
            attacker_pokemon.poison()
        if attacker_pokemon.get_status() == "frozen":
            attacker_pokemon.frozen()
        if attacker_pokemon.get_status() == "badly poisoned":
            attacker_pokemon.bad_poison()
        if attacker_pokemon.get_status() == "asleep":
            attacker_pokemon.sleep()
    if move.get_category().lower() == "special":
        special_effect = move.get_effect()
        if special_effect[0] == "user":
            if special_effect[1] == "critical":
                critical_factor = int(attacker_pokemon.get_base_speed() * 4)
                if critical_factor > 255:
                    critical_factor = 255
                critical_hit = random.randint(0, 256)
                if critical_factor > critical_hit:
                    critical_modifier = 2
                else:
                    critical_modifier = 1
                if critical_modifier == 1:
                    attacker_special_stage = attacker_pokemon.getspestage()
                    defender_special_stage = defender_pokemon.getspestage()
                else:
                    attacker_special_stage = 1
                    defender_special_stage = 1
                if attacker_pokemon.moving:
                    defender_pokemon.set_hp(int((42 * power * ((attacker_special * attacker_special_stage) /
                                                           (defender_special * defender_special_stage)) / 50 + 2)
                                            * stab * random_modifier * critical_modifier * type_advantage_modifier) *
                                            accuracy_modifier)
            elif special_effect[1] == "drain":
                if attacker_pokemon.moving:
                    defender_pokemon.set_hp(int((42 * power * ((attacker_special * attacker_special_stage) /
                                                           (defender_special * defender_special_stage)) / 50 + 2)
                                            * stab * random_modifier * critical_modifier * type_advantage_modifier) *
                                            accuracy_modifier)
                    print(int((42 * power * ((attacker_special * attacker_special_stage) /
                                                           (defender_special * defender_special_stage)) / 50 + 2)
                                            * stab * random_modifier * critical_modifier * type_advantage_modifier) *
                                            accuracy_modifier)
                    attacker_pokemon.set_hp(int(-(int((42 * power * ((attacker_special * attacker_special_stage) /
                                                           (defender_special * defender_special_stage)) / 50 + 2)
                                            * stab * random_modifier * critical_modifier * type_advantage_modifier) *
                                            accuracy_modifier*float(special_effect[2]))))
        elif special_effect[0] == "target":
            if special_effect[1] == "speed":
                speed_factor = int(float(special_effect[3]) * 100)
                speed_chance = random.randint(1, 101)
                if speed_chance <= speed_factor:
                    defender_pokemon.setspdstage(2/(defender_pokemon.getspdstage() + int(special_effect[2])))
                if attacker_pokemon.moving:
                    defender_pokemon.set_hp(int((42 * power * ((attacker_special * attacker_special_stage) /
                                                               (defender_special * defender_special_stage)) / 50 + 2)
                                            * stab * random_modifier * critical_modifier * type_advantage_modifier) *
                                            accuracy_modifier)
            elif special_effect[1] == "special":
                special_factor = int(float(special_effect[3]) * 100)
                special_chance = random.randint(1, 101)
                if special_chance <= special_factor:
                    defender_pokemon.setspestage((defender_pokemon.getspestage() + int(special_effect[2])))
                if attacker_pokemon.moving:
                    defender_pokemon.set_hp(int((42 * power * ((attacker_special * attacker_special_stage) /
                                                               (defender_special * defender_special_stage)) / 50 + 2)
                                            * stab * random_modifier * critical_modifier * type_advantage_modifier) *
                                            accuracy_modifier)
            elif special_effect[1] == "trap":
                defender_pokemon.moving = False
                if attacker_pokemon.moving:
                    defender_pokemon.set_hp(int((42 * power * ((attacker_special * attacker_special_stage) /
                                                           (defender_special * defender_special_stage)) / 50 + 2)
                                            * stab * random_modifier * critical_modifier * type_advantage_modifier) *
                                            accuracy_modifier)
            elif defender_pokemon.get_status() == "healthy":
                if special_effect[1] == "frozen":
                    frozen_factor = int(float(special_effect[2]) * 100)
                    frozen_chance = random.randint(1, 101)
                    if frozen_chance < frozen_factor:
                        defender_pokemon.frozen()
                    if attacker_pokemon.moving:
                        defender_pokemon.set_hp(int((42 * power * ((attacker_special * attacker_special_stage) /
                                                                   (defender_special * defender_special_stage)) / 50 + 2)
                                                * stab * random_modifier * critical_modifier * type_advantage_modifier) *
                                                accuracy_modifier)
                elif special_effect[1] == "paralysis":
                    paralyze_factor = int(float(special_effect[2]) * 100)
                    paralyze_chance = random.randint(1, 101)
                    if paralyze_chance <= paralyze_factor:
                        defender_pokemon.paralysis()
                    if attacker_pokemon.moving:
                        defender_pokemon.set_hp(int((42 * power * ((attacker_special * attacker_special_stage) /
                                                                   (defender_special * defender_special_stage)) / 50 + 2)
                                                * stab * random_modifier * critical_modifier * type_advantage_modifier) *
                                                accuracy_modifier)
                elif special_effect[1] == "burn":
                    burn_factor = int(float(special_effect[2]) * 100)
                    burn_chance = random.randint(1, 101)
                    if burn_chance <= burn_factor:
                        defender_pokemon.burn()
                    if attacker_pokemon.moving:
                        defender_pokemon.set_hp(int((42 * power * ((attacker_special * attacker_special_stage) /
                                                                   (defender_special * defender_special_stage)) / 50 + 2)
                                                * stab * random_modifier * critical_modifier * type_advantage_modifier) *
                                                accuracy_modifier)
            else:
                if attacker_pokemon.moving:
                    defender_pokemon.set_hp(int((42 * power * ((attacker_special * attacker_special_stage) /
                                                               (defender_special * defender_special_stage)) / 50 + 2)
                                                * stab * random_modifier * critical_modifier * type_advantage_modifier) *
                                            accuracy_modifier)
        else:
            defender_pokemon.set_hp(int((42 * power * ((attacker_special * attacker_special_stage) /
                                                   (defender_special * defender_special_stage)) / 50 + 2)
                                        * stab * random_modifier * critical_modifier * type_advantage_modifier) *
                                    accuracy_modifier)
    elif move.get_category().lower() == "physical":
        physical_effect = move.get_effect()
        if physical_effect[0] == "user":
            if physical_effect[1] == "multiple":
                if attacker_pokemon.moving:
                    if "-" in physical_effect[2]:
                        times = random.randint(2, 6)
                    for x in range(times):
                        defender_pokemon.set_hp(int((42 * power * ((attacker_attack * attacker_attack_stage) /
                                                                   (defender_defense * defender_defense_stage)) / 50 + 2)
                                                    * stab * random_modifier * critical_modifier * type_advantage_modifier) *
                                                accuracy_modifier)
                    else:
                        for x in range(int(physical_effect[2])):
                            defender_pokemon.set_hp(int((42 * power * ((attacker_attack * attacker_attack_stage) /
                                                                    (defender_defense * defender_defense_stage)) / 50 + 2)
                                                    * stab * random_modifier * critical_modifier * type_advantage_modifier) *
                                                accuracy_modifier)
            elif physical_effect[1] == "recoil":
                if attacker_pokemon.moving:
                    defender_pokemon.set_hp(int((42 * power * ((attacker_attack * attacker_attack_stage) /
                                                               (defender_defense * defender_defense_stage)) / 50 + 2)
                                                * stab * random_modifier * critical_modifier * type_advantage_modifier) *
                                            accuracy_modifier)
                attacker_pokemon.set_hp((int((42 * power * ((attacker_attack * attacker_attack_stage) /
                                                               (defender_defense * defender_defense_stage)) / 50 + 2)
                                                * stab * random_modifier * critical_modifier * type_advantage_modifier) *
                                            accuracy_modifier * (float(physical_effect[2]))))
            elif physical_effect[1] == "faint":
                if attacker_pokemon.moving:
                    defender_pokemon.set_hp(int((42 * power * ((attacker_attack * attacker_attack_stage) /
                                                               (defender_defense * defender_defense_stage)) / 50 + 2)
                                                * stab * random_modifier * critical_modifier * type_advantage_modifier) *
                                            accuracy_modifier)
                    attacker_pokemon.set_hp(attacker_pokemon.get_battle_hp())
            elif physical_effect[1] == "recharge":
                if attacker_pokemon.moving:
                    print(int((42 * power * ((attacker_attack * attacker_attack_stage) /
                                             (defender_defense * defender_defense_stage)) / 50 + 2)
                              * stab * random_modifier * critical_modifier * type_advantage_modifier) *
                          accuracy_modifier)
                    defender_pokemon.set_hp(int((42 * power * ((attacker_attack * attacker_attack_stage) /
                                                               (defender_defense * defender_defense_stage)) / 50 + 2)
                                                * stab * random_modifier * critical_modifier * type_advantage_modifier) *
                                            accuracy_modifier)
                    if defender_pokemon.get_battle_hp() > 0:
                        attacker_pokemon.moving = False
            elif physical_effect[1] == "critical":
                critical_factor = int(attacker_pokemon.get_base_speed() * 4)
                critical_hit = random.randint(0, 256)
                if critical_factor in range(critical_hit, 256):
                    critical_modifier = 2
                else:
                    critical_modifier = 1
                if critical_modifier == 1:
                    attacker_special_stage = attacker_pokemon.getspestage()
                    defender_special_stage = defender_pokemon.getspestage()
                else:
                    attacker_special_stage = 1
                    defender_special_stage = 1
                if attacker_pokemon.moving:
                    defender_pokemon.set_hp(int((42 * power * ((attacker_attack * attacker_attack_stage) /
                                                               (defender_defense * defender_defense_stage)) / 50 + 2)
                                                * stab * random_modifier * critical_modifier * type_advantage_modifier) *
                                            accuracy_modifier)
            elif physical_effect[1] == "fixed":
                if attacker_pokemon.moving:
                    if float(physical_effect[2]) > 1:
                        defender_pokemon.set_hp(int(physical_effect[2]))
                    else:
                        defender_pokemon.set_hp(int(float(physical_effect[2]) * defender_pokemon.get_battle_hp()))
        elif physical_effect[0] == "target":
            if physical_effect[1] == "trap":
                defender_pokemon.moving = False
                if attacker_pokemon.moving:
                    defender_pokemon.set_hp(int((42 * power * ((attacker_attack * attacker_attack_stage) /
                                                           (defender_defense * defender_defense_stage)) / 50 + 2)
                                            * stab * random_modifier * critical_modifier * type_advantage_modifier) *
                                            accuracy_modifier)
            if defender_pokemon.get_status() == "healthy":
                if physical_effect[1] == "paralysis":
                    paralyze_factor = int(float(physical_effect[2]) * 100)
                    paralyze_chance = random.randint(1, 101)
                    if paralyze_chance <= paralyze_factor:
                        defender_pokemon.paralysis()
                    if attacker_pokemon.moving:
                        defender_pokemon.set_hp(int((42 * power * ((attacker_attack * attacker_attack_stage) /
                                                                   (defender_defense * defender_defense_stage)) / 50 + 2)
                                                    * stab * random_modifier * critical_modifier * type_advantage_modifier) *
                                                accuracy_modifier)
                elif physical_effect[1] == "poison":
                    poison_factor = int(float(physical_effect[2]) * 100)
                    poison_chance = random.randint(1, 101)
                    if poison_chance <= poison_factor:
                        defender_pokemon.poison()
                    if attacker_pokemon.moving:
                        print(int((42 * power * ((attacker_attack * attacker_attack_stage) /
                                                 (defender_defense * defender_defense_stage)) / 50 + 2)
                                  * stab * random_modifier * critical_modifier * type_advantage_modifier) *
                              accuracy_modifier)
                        defender_pokemon.set_hp(int((42 * power * ((attacker_attack * attacker_attack_stage) /
                                                                   (defender_defense * defender_defense_stage)) / 50 + 2)
                                                    * stab * random_modifier * critical_modifier * type_advantage_modifier) *
                                                accuracy_modifier)
            else:
                if attacker_pokemon.moving:
                    print(int((42 * power * ((attacker_attack * attacker_attack_stage) /
                                             (defender_defense * defender_defense_stage)) / 50 + 2)
                              * stab * random_modifier * critical_modifier * type_advantage_modifier) *
                          accuracy_modifier)
                    defender_pokemon.set_hp(int((42 * power * ((attacker_attack * attacker_attack_stage) /
                                                               (defender_defense * defender_defense_stage)) / 50 + 2)
                                                * stab * random_modifier * critical_modifier * type_advantage_modifier) *
                                            accuracy_modifier)
        else:
            if attacker_pokemon.moving:
                print(int((42 * power * ((attacker_attack * attacker_attack_stage) /
                                                           (defender_defense * defender_defense_stage)) / 50 + 2)
                                            * stab * random_modifier * critical_modifier * type_advantage_modifier) *
                                        accuracy_modifier)
                defender_pokemon.set_hp(int((42 * power * ((attacker_attack * attacker_attack_stage) /
                                                           (defender_defense * defender_defense_stage)) / 50 + 2)
                                            * stab * random_modifier * critical_modifier * type_advantage_modifier) *
                                        accuracy_modifier)
    elif move.get_category().lower() == "status":
        status_effect = move.get_effect()
        if accuracy_modifier == 1:
            if attacker_pokemon.moving:
                if status_effect[0] == "user":
                    if status_effect[1] == "speed":
                        attacker_pokemon.setspdstage(int(status_effect[2]))
                    elif status_effect[1] == "special":
                        attacker_pokemon.setspestage(int(status_effect[2]))
                    elif status_effect[1] == "attack":
                        attacker_pokemon.setatkstage(int(status_effect[2]))
                    elif status_effect[1] == "recover":
                        attacker_pokemon.set_hp(int(-(float(status_effect[2]) * attacker_pokemon.get_hp())))
                    elif status_effect[1] == "defense":
                        attacker_pokemon.setdefstage(int(status_effect[2]))
                    elif status_effect[1] == "sleep":
                        attacker_pokemon.set_hp(-attacker_pokemon.get_hp())
                        attacker_pokemon.set_status("asleep")
                elif status_effect[0] == "target":
                    if defender_pokemon.get_status() == "healthy":
                        if status_effect[1] == "paralysis":
                            defender_pokemon.set_status("paralyzed")
                        elif status_effect[1] == "sleep":
                            defender_pokemon.set_status("asleep")
                        elif status_effect[1] == "badlypoisoned":
                            defender_pokemon.set_status("badly poisoned")
                    if status_effect[1] == "defense":
                        defender_pokemon.setdefstage(-2)
                elif status_effect[0] == "?":
                    attacker_pokemon.setmove4(defender_pokemon.getmove1())
    return defender_pokemon.get_battle_hp()