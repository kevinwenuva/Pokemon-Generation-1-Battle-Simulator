import pygame
import gamebox
from pokemon import Pokemon
import attack
from move import Move


"""
You need to wait five seconds before switching out a fainted pokemon, and don't hold down any button for too long, as 
you might accidentally press the button again for the next turn. Also, when a pokemon faints, the other side should not 
press any buttons.
"""
# Need the pokemon people want, direct them to overview if they need it.
pokemon1_1 = Pokemon(input("Player 1, what is your first Pokemon (This will be the first pokemon sent "
                           "out during the battle)? "))
pokemon1_2 = Pokemon(input("What is your second Pokemon? "))
pokemon1_3 = Pokemon(input("What is your third Pokemon? "))
pokemon1_4 = Pokemon(input("What is your fourth Pokemon? "))
pokemon1_5 = Pokemon(input("What is your fifth Pokemon? "))
pokemon1_6 = Pokemon(input("What is your sixth Pokemon? "))
print("\n" * 10)  # This is so that player 2 doesn't see what player 1 chose.
pokemon2_1 = Pokemon(input("Player 2, what is your first Pokemon "
                           "(This will be the first pokemon sent out during the battle)? "))
pokemon2_2 = Pokemon(input("What is your second Pokemon? "))
pokemon2_3 = Pokemon(input("What is your third Pokemon? "))
pokemon2_4 = Pokemon(input("What is your fourth Pokemon? "))
pokemon2_5 = Pokemon(input("What is your fifth Pokemon? "))
pokemon2_6 = Pokemon(input("What is your sixth Pokemon? "))

pokemon1_active = pokemon1_1
pokemon2_active = pokemon2_1

# ------ DISPLAY --------
#displays the initial pokemon sprites and health bars that are updated when changed
# ------ SMALL CAMERA ------
camera = gamebox.Camera(600, 450)
pokemon1_out = gamebox.from_image(150, 250, "Sprites/" + str(pokemon1_active.get_name()) + ".png")
pokemon2_out = gamebox.from_image(450, 50, "Sprites/" + str(pokemon2_active.get_name()) + ".png")
pokemon1_health = gamebox.from_color(150, 210,"green",pokemon2_active.get_battle_hp()/pokemon2_active.get_hp()*100, 5)
pokemon2_health = gamebox.from_color(450,15,"green",pokemon2_active.get_battle_hp()/pokemon2_active.get_hp()*100, 5)
walls = [
    gamebox.from_color(298,375,"black",4,150),
    gamebox.from_color(400,300,"black",800,4)
    ]
player1_done = False
player2_done = False
player1_move = "none"
player2_move = "none"
player1_switch = False
player2_switch = False
switch_target1 = "none"
switch_target2 = "none"
timer = 300
letter = 0
player1_score = 0
player2_score = 0
score1 = 0
score2 = 0
game_on = True

"""
Player inputs cause attacks and switching. Display pokemon sprites, health bars, status conditions, instructions.
Pokemon faints when it reaches 0 health and needs to be switched. Keeps the score in a best of 3 and resets the game after
a player wins a round and declares a winner after a player wins two rounds.
"""

def tick(keys):
    global pokemon1_active
    global pokemon2_active
    global pokemon1_out
    global pokemon2_out
    global pokemon1_health
    global pokemon2_health
    global player1_done
    global player2_done
    global player1_move
    global player2_move
    global player1_switch
    global player2_switch
    global switch_target1
    global switch_target2
    global timer
    global letter
    global player1_score
    global player2_score
    global score1
    global score2
    global game_on
    # ------ START SCREEN -------
    if game_on:
        camera.clear("white")
        instructions1 = gamebox.from_text(300, 100, "Pokemon", 20, 'black')
        instructions2 = gamebox.from_text(300, 150, "kqw6cf and rbp9k", 20, 'black')
        instructions3 = gamebox.from_text(300, 200, "Press Space to Start, Pressing the corresponding button next to an action will do that action.", 20, 'black')
        instructions4 = gamebox.from_text(300, 250, "If you need help with how to play pokemon, go to this link: ", 20, 'black')
        instructions5 = gamebox.from_text(300, 300, "https://www.dragonflycave.com/mechanics/battling-basics", 20, "black")
        instructions6 = gamebox.from_text(300, 350, "Do not hold down any button, press lightly. Also wait 5 seconds before pressing", 20, "black")
        camera.draw(instructions1)
        camera.draw(instructions2)
        camera.draw(instructions3)
        camera.draw(instructions4)
        camera.draw(instructions5)
        camera.draw(instructions6)
        if pygame.K_SPACE in keys:
            game_on = False
    # ------- USER INPUT ---------
    # ------- MULTIPLAYER ---------

    if player1_done is False:
        if pygame.K_1 in keys:
            player1_move = pokemon1_active.getmove1()
            player1_done = True
        if pygame.K_2 in keys:
            player1_move = pokemon1_active.getmove2()
            player1_done = True
        if pygame.K_3 in keys:
            player1_move = pokemon1_active.getmove3()
            player1_done = True
        if pygame.K_4 in keys:
            player1_move = pokemon1_active.getmove4()
            player1_done = True
        if pygame.K_q in keys:
            if not pokemon1_1.fainted() and pokemon1_1 != pokemon1_active:
                switch_target1 = pokemon1_1
                player1_switch = True
        if pygame.K_w in keys:
            if not pokemon1_2.fainted() and pokemon1_2 != pokemon1_active:
                switch_target1 = pokemon1_2
                player1_switch = True
        if pygame.K_e in keys:
            if not pokemon1_3.fainted() and pokemon1_3 != pokemon1_active:
                switch_target1 = pokemon1_3
                player1_switch = True
        if pygame.K_r in keys:
            if not pokemon1_4.fainted() and pokemon1_4 != pokemon1_active:
                switch_target1 = pokemon1_4
                player1_switch = True
        if pygame.K_t in keys:
            if not pokemon1_5.fainted() and pokemon1_5 != pokemon1_active:
                switch_target1 = pokemon1_5
                player1_switch = True
        if pygame.K_y in keys:
            if not pokemon1_6.fainted() and pokemon1_6 != pokemon1_active:
                switch_target1 = pokemon1_6
                player1_switch = True
    if player2_done is False:
        if pygame.K_7 in keys:
            player2_move = pokemon2_active.getmove1()
            player2_done = True
        if pygame.K_8 in keys:
            player2_move = pokemon2_active.getmove2()
            player2_done = True
        if pygame.K_9 in keys:
            player2_move = pokemon2_active.getmove3()
            player2_done = True
        if pygame.K_0 in keys:
            player2_move = pokemon2_active.getmove4()
            player2_done = True
        if pygame.K_f in keys:
            if not pokemon2_1.fainted()and pokemon2_1 != pokemon2_active:
                switch_target2 = pokemon2_1
                player2_switch = True
        if pygame.K_g in keys:
            if not pokemon2_2.fainted()and pokemon2_2 != pokemon2_active:
                switch_target2 = pokemon2_2
                player2_switch = True
        if pygame.K_h in keys:
            if not pokemon2_3.fainted()and pokemon2_3 != pokemon2_active:
                switch_target2 = pokemon2_3
                player2_switch = True
        if pygame.K_j in keys:
            if not pokemon2_4.fainted()and pokemon2_4 != pokemon2_active:
                switch_target2 = pokemon2_4
                player2_switch = True
        if pygame.K_k in keys:
            if not pokemon2_5.fainted()and pokemon2_5 != pokemon2_active:
                switch_target2 = pokemon2_5
                player2_switch = True
        if pygame.K_l in keys:
            if not pokemon2_6.fainted()and pokemon2_6 != pokemon2_active:
                switch_target2 = pokemon2_6
                player2_switch = True

    # -------Fainting-------
    if pokemon1_active.fainted() is True:
        timer = 300-letter
        if letter < 50:
            letter += 1
            message = str(pokemon1_active.get_name()) + ' fainted!'
            faint_message = gamebox.from_text(300,130, message[:letter//2], 30, "red")
            pokemon1_out = gamebox.from_image(150, 250, "Sprites/" + 'pokeball' + ".png")
        if letter >= 50:
            letter += 1
            message = 'Switch?'
            faint_message = gamebox.from_text(300, 120, message[:(letter-25)//2], 30, "red")
            if player1_switch is True:
                pokemon1_active = switch_target1
                pokemon1_out = gamebox.from_image(150, 250, "Sprites/" + str(pokemon1_active.get_name()) + ".png")
                pokemon1_health = gamebox.from_color(150, 210, "green",
                                                     pokemon1_active.get_battle_hp() / pokemon1_active.get_hp() * 100, 5)
                pokemon2_health = gamebox.from_color(450, 15, "green",
                                                     pokemon2_active.get_battle_hp() / pokemon2_active.get_hp() * 100, 5)
                player1_switch = False
                player2_switch = False
                player1_done = False
                player2_done = False
                timer = 300
                letter = 0
    elif pokemon2_active.fainted() is True:
        timer = 300-letter
        if letter < 50:
            letter += 1
            message = str(pokemon2_active.get_name()) + ' fainted!'
            faint_message = gamebox.from_text(300,120, message[:letter//2], 30, "red")
            pokemon2_out = gamebox.from_image(450, 50, "Sprites/" + 'pokeball' + ".png")
        if letter >= 50:
            letter += 1
            message = 'Switch?'
            faint_message = gamebox.from_text(300, 130, message[:(letter-25)//2], 30, "red")
            if player2_switch is True:
                pokemon2_active = switch_target2
                pokemon2_out = gamebox.from_image(450, 50, "Sprites/" + str(pokemon2_active.get_name()) + ".png")
                pokemon1_health = gamebox.from_color(150, 210, "green",
                                                     pokemon1_active.get_battle_hp() / pokemon1_active.get_hp() * 100, 5)
                pokemon2_health = gamebox.from_color(450, 15, "green",
                                                     pokemon2_active.get_battle_hp() / pokemon2_active.get_hp() * 100, 5)
                player1_switch = False
                player2_switch = False
                player1_done = False
                player2_done = False
                timer = 300
                letter = 0
    else:
        faint_message = gamebox.from_text(300,1000, 'none', 20, "red")

    # -------Moves-------
    if player1_done is True and player2_done is True:
        if pokemon1_active.get_battle_speed() > pokemon2_active.get_battle_speed():
            first = pokemon1_active
            second = pokemon2_active
            first_move = player1_move
            second_move = player2_move
        else:
            first = pokemon2_active
            second = pokemon1_active
            first_move = player2_move
            second_move = player1_move
        if first_move is not 'none':
            attack.attack(first, second, first_move)
            pokemon1_health = gamebox.from_color(150, 210, "green",
                                             pokemon1_active.get_battle_hp() / pokemon1_active.get_hp() * 100, 5)
            pokemon2_health = gamebox.from_color(450, 15, "green",
                                             pokemon2_active.get_battle_hp() / pokemon2_active.get_hp() * 100, 5)
        if second.fainted() is not True:
            if second_move is not 'none':
                attack.attack(second, first, second_move)
            pokemon1_health = gamebox.from_color(150, 210, "green",
                                                 pokemon1_active.get_battle_hp() / pokemon1_active.get_hp() * 100, 5)
            pokemon2_health = gamebox.from_color(450, 15, "green",
                                                 pokemon2_active.get_battle_hp() / pokemon2_active.get_hp() * 100, 5)
        player1_switch = False
        player2_switch = False
        player1_done = False
        player2_done = False
        timer = 300

    if player1_switch is True and player2_switch is True:
        pokemon1_active = switch_target1
        pokemon1_out = gamebox.from_image(150, 250, "Sprites/" + str(pokemon1_active.get_name()) + ".png")
        pokemon2_active = switch_target2
        pokemon2_out = gamebox.from_image(450, 50, "Sprites/" + str(pokemon2_active.get_name()) + ".png")
        pokemon1_health = gamebox.from_color(150, 210, "green",
                                             pokemon1_active.get_battle_hp() / pokemon1_active.get_hp() * 100, 5)
        pokemon2_health = gamebox.from_color(450, 15, "green",
                                             pokemon2_active.get_battle_hp() / pokemon2_active.get_hp() * 100, 5)
        player1_switch = False
        player2_switch = False
        player1_done = False
        player2_done = False
        timer = 300

    if player1_switch is True and player2_done is True:
        pokemon1_active = switch_target1
        pokemon1_out = gamebox.from_image(150, 250, "Sprites/" + str(pokemon1_active.get_name()) + ".png")
        if player2_move is not 'none':
            attack.attack(pokemon2_active, pokemon1_active, player2_move)
        pokemon1_health = gamebox.from_color(150, 210, "green",
                                             pokemon1_active.get_battle_hp() / pokemon1_active.get_hp() * 100, 5)
        pokemon2_health = gamebox.from_color(450, 15, "green",
                                             pokemon2_active.get_battle_hp() / pokemon2_active.get_hp() * 100, 5)
        player1_switch = False
        player2_switch = False
        player1_done = False
        player2_done = False
        timer = 300


    if player1_done is True and player2_switch is True:
        pokemon2_active = switch_target2
        pokemon2_out = gamebox.from_image(450, 50, "Sprites/" + str(pokemon2_active.get_name()) + ".png")
        if player1_move is not 'none':
            attack.attack(pokemon1_active, pokemon2_active, player1_move)
        pokemon1_health = gamebox.from_color(150, 210, "green",
                                             pokemon1_active.get_battle_hp() / pokemon1_active.get_hp() * 100, 5)
        pokemon2_health = gamebox.from_color(450, 15, "green",
                                             pokemon2_active.get_battle_hp() / pokemon2_active.get_hp() * 100, 5)
        player1_switch = False
        player2_switch = False
        player1_done = False
        player2_done = False
        timer = 300
    # --------TURN TIMER -------
    timer -= 1
    time_left = gamebox.from_text(300,150, str(timer//10), 40, 'red')
    if timer <= 0:
        if player1_done is False and player1_switch is False:
            player1_done = True
            player1_move = 'none'
        if player2_done is False and player2_switch is False:
            player2_done = True
            player2_move = 'none'

    # --------Status-------
    if pokemon1_active.get_status() is 'burned':
        status1 = gamebox.from_text(100, 200, 'BRN', 15, 'red')
    elif pokemon1_active.get_status() is 'poisoned' or pokemon1_active.get_status() is 'badly poisoned':
        status1 = gamebox.from_text(100, 200, 'PSN', 15, 'purple')
    elif pokemon1_active.get_status() is 'paralyzed':
        status1 = gamebox.from_text(100, 200, 'PAR', 15, 'orange')
    elif pokemon1_active.get_status() is 'frozen':
        status1 = gamebox.from_text(100, 200, 'FRZ', 15, 'blue')
    elif pokemon1_active.get_status() is 'asleep':
        status1 = gamebox.from_text(100, 200, 'SLP', 15, 'black')
    else:
        status1 = gamebox.from_text(120, 1000, 'none', 15, 'black')

    if pokemon2_active.get_status() is 'burned':
        status2 = gamebox.from_text(420, 5, 'BRN', 15, 'red')
    elif pokemon2_active.get_status() is 'poisoned' or pokemon1_active.get_status() is 'badly poisoned':
        status2 = gamebox.from_text(420, 5, 'PSN', 15, 'purple')
    elif pokemon2_active.get_status() is 'paralyzed':
        status2 = gamebox.from_text(420, 5, 'PAR', 15, 'orange')
    elif pokemon2_active.get_status() is 'frozen':
        status2 = gamebox.from_text(420, 5, 'FRZ', 15, 'blue')
    elif pokemon2_active.get_status() is 'asleep':
        status2 = gamebox.from_text(420,5, 'SLP', 15, 'black')
    else:
        status2 = gamebox.from_text(450, 1000, 'none', 15, 'black')

    modifier1 = [
        gamebox.from_text(130, 200, 'ATK: ' + str(pokemon1_active.getatkstage()), 15, 'black'),
        gamebox.from_text(160, 200, 'DEF: ' + str(pokemon1_active.getdefstage()), 15, 'black'),
        gamebox.from_text(190, 200, 'SPC: ' + str(pokemon1_active.getspestage()), 15, 'black'),
        gamebox.from_text(220, 200, 'SPE: ' + str(pokemon1_active.getspdstage()), 15, 'black')
        ]
    modifier2 = [
        gamebox.from_text(450, 5,'ATK: ' + str(pokemon2_active.getatkstage()), 15, 'black'),
        gamebox.from_text(480, 5,'DEF: ' + str(pokemon2_active.getdefstage()), 15, 'black'),
        gamebox.from_text(510, 5, 'SPC: ' + str(pokemon2_active.getspestage()), 15, 'black'),
        gamebox.from_text(540, 5, 'SPE: ' + str(pokemon2_active.getspdstage()), 15, 'black')
        ]
    # -----HEALTH METER-----
    health1 = gamebox.from_text(155+pokemon1_active.get_battle_hp() / pokemon1_active.get_hp() * 100,210, str(int(pokemon1_active.get_battle_hp() / pokemon1_active.get_hp() * 100))+ '%', 20,'green')
    health2 = gamebox.from_text(455+pokemon2_active.get_battle_hp() / pokemon2_active.get_hp() * 100, 15, str(int(pokemon2_active.get_battle_hp() / pokemon2_active.get_hp() * 100))+ '%', 20,'green')
    # --------Info--------
    moves = [
        gamebox.from_text(75, 315, "1. " + pokemon1_active.getmove1(), 20, "black"),
        gamebox.from_text(225, 315, "2. " + pokemon1_active.getmove2(), 20, "black"),
        gamebox.from_text(75, 350, "3. " + pokemon1_active.getmove3(), 20, "black"),
        gamebox.from_text(225, 350, "4. " + pokemon1_active.getmove4(), 20, "black"),
        gamebox.from_text(375, 315, "7. " + pokemon2_active.getmove1(), 20, "black"),
        gamebox.from_text(525, 315, "8. " + pokemon2_active.getmove2(), 20, "black"),
        gamebox.from_text(375, 350, "9. " + pokemon2_active.getmove3(), 20, "black"),
        gamebox.from_text(525, 350, "0. " + pokemon2_active.getmove4(), 20, "black")
    ]

    switches = [
        gamebox.from_text(50, 385, "Q." + pokemon1_1.get_name(), 20, "black"),
        gamebox.from_text(150, 385, "W." + pokemon1_2.get_name(), 20, "black"),
        gamebox.from_text(250, 385, "E." + pokemon1_3.get_name(), 20, "black"),
        gamebox.from_text(50, 420, "R." + pokemon1_4.get_name(), 20, "black"),
        gamebox.from_text(150, 420, "T." + pokemon1_5.get_name(), 20, "black"),
        gamebox.from_text(250, 420, "Y." + pokemon1_6.get_name(), 20, "black"),
        gamebox.from_text(350, 385, "F." + pokemon2_1.get_name(), 20, "black"),
        gamebox.from_text(450, 385, "G." + pokemon2_2.get_name(), 20, "black"),
        gamebox.from_text(550, 385, "H." + pokemon2_3.get_name(), 20, "black"),
        gamebox.from_text(350, 420, "J." + pokemon2_4.get_name(), 20, "black"),
        gamebox.from_text(450, 420, "K." + pokemon2_5.get_name(), 20, "black"),
        gamebox.from_text(550, 420, "L." + pokemon2_6.get_name(), 20, "black")
    ]
    if pokemon1_1.fainted():
        switches[0] = gamebox.from_text(50, 385, "Q." + pokemon1_1.get_name(), 20, "red")
    if pokemon1_2.fainted():
        switches[1] = gamebox.from_text(150, 385, "W." + pokemon1_2.get_name(), 20, "red")
    if pokemon1_3.fainted():
        switches[2] = gamebox.from_text(250, 385, "E." + pokemon1_3.get_name(), 20, "red")
    if pokemon1_4.fainted():
        switches[3] = gamebox.from_text(50, 420, "R." + pokemon1_4.get_name(), 20, "red")
    if pokemon1_5.fainted():
        switches[4] = gamebox.from_text(150, 420, "T." + pokemon1_5.get_name(), 20, "red")
    if pokemon1_6.fainted():
        switches[5] = gamebox.from_text(250, 420, "Y." + pokemon1_6.get_name(), 20, "red")
    if pokemon2_1.fainted():
        switches[6] = gamebox.from_text(350, 385, "F." + pokemon2_1.get_name(), 20, "red")
    if pokemon2_2.fainted():
        switches[7] = gamebox.from_text(450, 385, "G." + pokemon2_2.get_name(), 20, "red")
    if pokemon2_3.fainted():
        switches[8] = gamebox.from_text(550, 385, "H." + pokemon2_3.get_name(), 20, "red")
    if pokemon2_4.fainted():
        switches[9] = gamebox.from_text(350, 420, "J." + pokemon2_4.get_name(), 20, "red")
    if pokemon2_5.fainted():
        switches[10] = gamebox.from_text(450, 420, "K." + pokemon2_5.get_name(), 20, "red")
    if pokemon2_6.fainted():
        switches[11] = gamebox.from_text(550, 420, "L." + pokemon2_6.get_name(), 20, "red")

    done1 = gamebox.from_text(150, 290, "not done", 20, "red")
    done2 = gamebox.from_text(450, 90, "not done", 20, "red")
    if player1_done is True:
        done1 = gamebox.from_text(150,290,"done", 20,"red")
    if player2_done is True:
        done2 = gamebox.from_text(450, 90, "done", 20, "red")
    if player1_switch is True:
        done1 = gamebox.from_text(150, 290, "done", 20, "red")
    if player2_switch is True:
        done2 = gamebox.from_text(450, 90, "done", 20, "red")

    #--------Winning--------
    # "multiple levels" implemented as a best of 3 game approved by Caroline
    if pokemon1_1.fainted() and pokemon1_2.fainted() and pokemon1_3.fainted() and pokemon1_4.fainted() and pokemon1_5.fainted() and pokemon1_6.fainted():
        time_left = gamebox.from_text(300, 1500, str(timer // 10), 40, 'red')
        if score2 == 0:
            player2_score += 1
            score2 += 10
        letter += 1
        message = 'player 1 blacked out!'
        faint_message = gamebox.from_text(300, 130, message[:letter // 2], 30, "red")
        if letter > 50:
            message = 'score is: '+ str(player1_score) + "-" + str(player2_score) + " press space to continue"
            faint_message = gamebox.from_text(300, 130, message[:(letter-100) // 2], 30, "red")
        if pygame.K_SPACE in keys:
            score2 = 0
            letter = 0
            pokemon1_1.set_hp(-pokemon1_1.get_hp())
            pokemon1_2.set_hp(-pokemon1_2.get_hp())
            pokemon1_3.set_hp(-pokemon1_3.get_hp())
            pokemon1_4.set_hp(-pokemon1_4.get_hp())
            pokemon1_5.set_hp(-pokemon1_5.get_hp())
            pokemon1_6.set_hp(-pokemon1_6.get_hp())
            pokemon1_active = pokemon1_1
            pokemon1_1.set_status("healthy")
            pokemon1_2.set_status("healthy")
            pokemon1_3.set_status("healthy")
            pokemon1_4.set_status("healthy")
            pokemon1_5.set_status("healthy")
            pokemon1_6.set_status("healthy")
            pokemon1_1.stats_reset()
            pokemon1_2.stats_reset()
            pokemon1_3.stats_reset()
            pokemon1_4.stats_reset()
            pokemon1_5.stats_reset()
            pokemon1_6.stats_reset()
            pokemon2_1.set_hp(-pokemon2_1.get_hp())
            pokemon2_2.set_hp(-pokemon2_2.get_hp())
            pokemon2_3.set_hp(-pokemon2_3.get_hp())
            pokemon2_4.set_hp(-pokemon2_4.get_hp())
            pokemon2_5.set_hp(-pokemon2_5.get_hp())
            pokemon2_6.set_hp(-pokemon2_6.get_hp())
            pokemon2_active = pokemon2_1
            pokemon2_1.set_status("healthy")
            pokemon2_2.set_status("healthy")
            pokemon2_3.set_status("healthy")
            pokemon2_4.set_status("healthy")
            pokemon2_5.set_status("healthy")
            pokemon2_6.set_status("healthy")
            pokemon2_1.stats_reset()
            pokemon2_2.stats_reset()
            pokemon2_3.stats_reset()
            pokemon2_4.stats_reset()
            pokemon2_5.stats_reset()
            pokemon2_6.stats_reset()
            pokemon1_out = gamebox.from_image(150, 250, "Sprites/" + str(pokemon1_active.get_name()) + ".png")
            pokemon2_out = gamebox.from_image(450, 50, "Sprites/" + str(pokemon2_active.get_name()) + ".png")
            pokemon1_health = gamebox.from_color(150, 210, "green",
                                                 pokemon1_active.get_battle_hp() / pokemon1_active.get_hp() * 100, 5)
            pokemon2_health = gamebox.from_color(450, 15, "green",
                                                 pokemon2_active.get_battle_hp() / pokemon2_active.get_hp() * 100, 5)
    if pokemon2_1.fainted() and pokemon2_2.fainted() and pokemon2_3.fainted() and pokemon2_4.fainted() and pokemon2_5.fainted() and pokemon2_6.fainted():
        time_left = gamebox.from_text(300, 1500, str(timer // 10), 40, 'red')
        letter += 1
        if score1 == 0:
            player1_score += 1
            score1 += 10
        message = "player 2 blacked out!"
        faint_message = gamebox.from_text(300, 130, message[:letter // 2], 30, "red")
        if letter > 50:
            message = 'score is: '+ str(player1_score) + "-" + str(player2_score) + " press space to continue"
            faint_message = gamebox.from_text(300, 130, message[:(letter-100) // 2], 30, "red")
        if pygame.K_SPACE in keys:
            letter = 0
            score1 = 0
            pokemon1_1.set_hp(-pokemon1_1.get_hp())
            pokemon1_2.set_hp(-pokemon1_2.get_hp())
            pokemon1_3.set_hp(-pokemon1_3.get_hp())
            pokemon1_4.set_hp(-pokemon1_4.get_hp())
            pokemon1_5.set_hp(-pokemon1_5.get_hp())
            pokemon1_6.set_hp(-pokemon1_6.get_hp())
            pokemon1_active = pokemon1_1
            pokemon1_1.set_status("healthy")
            pokemon1_2.set_status("healthy")
            pokemon1_3.set_status("healthy")
            pokemon1_4.set_status("healthy")
            pokemon1_5.set_status("healthy")
            pokemon1_6.set_status("healthy")
            pokemon1_1.stats_reset()
            pokemon1_2.stats_reset()
            pokemon1_3.stats_reset()
            pokemon1_4.stats_reset()
            pokemon1_5.stats_reset()
            pokemon1_6.stats_reset()
            pokemon2_1.set_hp(-pokemon2_1.get_hp())
            pokemon2_2.set_hp(-pokemon2_2.get_hp())
            pokemon2_3.set_hp(-pokemon2_3.get_hp())
            pokemon2_4.set_hp(-pokemon2_4.get_hp())
            pokemon2_5.set_hp(-pokemon2_5.get_hp())
            pokemon2_6.set_hp(-pokemon2_6.get_hp())
            pokemon2_active = pokemon2_1
            pokemon2_1.set_status("healthy")
            pokemon2_2.set_status("healthy")
            pokemon2_3.set_status("healthy")
            pokemon2_4.set_status("healthy")
            pokemon2_5.set_status("healthy")
            pokemon2_6.set_status("healthy")
            pokemon2_1.stats_reset()
            pokemon2_2.stats_reset()
            pokemon2_3.stats_reset()
            pokemon2_4.stats_reset()
            pokemon2_5.stats_reset()
            pokemon2_6.stats_reset()
            pokemon1_out = gamebox.from_image(150, 250, "Sprites/" + str(pokemon1_active.get_name()) + ".png")
            pokemon2_out = gamebox.from_image(450, 50, "Sprites/" + str(pokemon2_active.get_name()) + ".png")
            pokemon1_health = gamebox.from_color(150, 210, "green",
                                                 pokemon1_active.get_battle_hp() / pokemon1_active.get_hp() * 100, 5)
            pokemon2_health = gamebox.from_color(450, 15, "green",
                                                 pokemon2_active.get_battle_hp() / pokemon2_active.get_hp() * 100, 5)
    if player1_score is 2:
        letter += 1
        message = 'player 1 wins! Exit the game'
        faint_message = gamebox.from_text(300, 130, message[:letter // 2], 30, "red")
        game_on = False
        #end game
    if player2_score is 2:
        letter += 1
        message = 'player 2 wins! Exit the game'
        faint_message = gamebox.from_text(300, 130, message[:letter // 2], 30, "red")
        game_on = False
        #end game


    #---------APPROPRIATE IMAGE/SPRITES---------
    if not game_on:
        camera.clear("white")
        camera.draw(pokemon1_out)
        camera.draw(pokemon2_out)
        camera.draw(pokemon1_health)
        camera.draw(pokemon2_health)
        camera.draw(done1)
        camera.draw(done2)
        camera.draw(time_left)
        camera.draw(faint_message)
        camera.draw(status1)
        camera.draw(status2)
        camera.draw(health1)
        camera.draw(health2)
        for m1 in modifier1:
            camera.draw(m1)
        for m2 in modifier2:
            camera.draw(m2)
        for wall in walls:
            camera.draw(wall)
        for move in moves:
            camera.draw(move)
        for switch in switches:
            camera.draw(switch)
    camera.display()


gamebox.timer_loop(10, tick)