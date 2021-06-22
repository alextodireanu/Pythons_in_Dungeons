import random
import utils
import enemy
import player


class Battle:
    @staticmethod
    def goblin_fight():
        battle_start = True
        first_round = True
        warrior, wizard = '', ''
        goblin = enemy.Goblin()
        goblin_health, goblin_damage, goblin_speed = goblin.health, goblin.damage, goblin.speed
        warrior_health, warrior_damage, warrior_speed, warrior_mana = 0, 0, 0, 0
        wizard_health, wizard_damage, wizard_speed, wizard_mana = 0, 0, 0, 0
        chosen_fighter, fighter_name = utils.Utils.reader()
        if chosen_fighter == 1:
            warrior = player.Warrior(fighter_name)
            warrior_health, warrior_damage, warrior_speed, warrior_mana = \
                warrior.health, warrior.damage, warrior.speed, warrior.mana
        elif chosen_fighter == 2:
            wizard = player.Wizard(fighter_name)
            wizard_health, wizard_damage, wizard_speed, wizard_mana = \
                wizard.health, wizard.damage, wizard.speed, wizard.mana

        while battle_start:
            if chosen_fighter == 1:
                if first_round:
                    print("\nThe goblin is faster than you and attacks first!")
                    first_round = False
                    goblin.attack()
                    warrior_health -= goblin_damage
                    print(f"\nDirect hit! -{goblin_damage} HP")
                    print(f"\nYou have {warrior_health} HP left!")

                else:
                    next_turn = input("\nYour turn! Type A to attack, D to defend -> ")
                    if next_turn.upper().strip() == "A":
                        if warrior_mana <= 10:
                            print("You don't have enough mana to attack!")
                            goblin.attack()
                            warrior_health -= goblin_damage
                            print(f"\nDirect hit! -{goblin_damage} HP")
                            print(f"\nYou have {warrior_health} HP left!")
                            if warrior_health <= 0:
                                print("Game over!")
                                battle_start = False
                        else:
                            warrior.attack()
                            print(f"\nDirect hit, {warrior_damage} damage dealt!")
                            goblin_health -= warrior_damage
                            warrior_mana -= 10
                            print(f"You have {warrior_mana} mana left!")

                            if goblin_health <= 0:
                                battle_start = False
                                print("\nThe goblin is no match to your power, enemy defeated!")
                                next_scene = input("next scene ->")
                            else:
                                goblin.attack()
                                print(f"\nDirect hit! -{goblin_damage} HP")
                                warrior_health -= goblin_damage
                                if warrior_health <= 0:
                                    print("\nGame over!")
                                    battle_start = False
                                else:
                                    print(f"\nYou have {warrior_health} HP left!")

                    elif next_turn.upper().strip() == "D":
                        if warrior_mana <= 5:
                            print("\nYou don't have enough mana to defend!")
                            goblin.attack()
                            warrior_health -= goblin_damage
                            print(f"\nDirect hit! -{goblin_damage} HP")
                            print(f"\nYou have {warrior_health} HP left!")
                            if warrior_health <= 0:
                                print("Game over!")
                                battle_start = False
                        else:
                            warrior.defend()
                            warrior_mana -= 5
                            print(f"\nYou have {warrior_mana} mana left!")
                            goblin.attack()
                            warrior_health -= int(goblin_damage / 2)
                            print(f"\nYou defended yourself and got less damage! -{goblin_damage / 2} HP")

                            if warrior_health <= 0:
                                battle_start = False
                                print("\nGame over!")
                            else:
                                print(f"\nYou have {warrior_health} HP left!")

            elif chosen_fighter == 2:
                if first_round:
                    random_number = random.randint(0, 1)
                    if random_number == 0:
                        print("\nThe enemy is as faster as you but this time you got lucky!")
                        action = input("\nType A to attack or D to defend -> ")
                        if action.upper().strip() == "A":
                            first_round = False
                            wizard.attack()
                            print(f"\nDirect hit, {wizard_damage} damage dealt!")
                            wizard_mana -= 10
                            print(f"\nYou have {wizard_mana} mana left!")
                            goblin_health -= wizard_damage

                        elif action.upper().strip() == "D":
                            first_round = False
                            wizard.defend()
                            wizard_mana -= 5
                            print(f"\n You have {wizard_mana} mana left!")
                            goblin.attack()
                            wizard_health -= int(goblin_damage / 2)
                            print(f"\nYou defended yourself and got less damage! -{goblin_damage / 2} HP")
                            print(f"You have {wizard_health} HP left!")

                    elif random_number == 1:
                        print("The enemy is as faster as you but this time he got lucky!")
                        first_round = False
                        goblin.attack()
                        print(f"\nDirect hit! -{goblin_damage} HP")
                        wizard_health -= goblin_damage
                        print(f"\nYou have {wizard_health} HP left!")

                else:
                    next_turn = input("\nYour turn! Type A to attack, D to defend -> ")
                    if next_turn.upper().strip() == "A":
                        if wizard_mana <= 10:
                            print("You don't have enough mana to attack!")
                            goblin.attack()
                            wizard_health -= goblin_damage
                            print(f"\nDirect hit! -{goblin_damage} HP")
                            print(f"\nYou have {wizard_health} HP left!")
                            if wizard_health <= 0:
                                print("Game over!")
                                battle_start = False
                        else:
                            wizard.attack()
                            print(f"\nDirect hit, {wizard_damage} damage dealt!")
                            goblin_health -= warrior_damage
                            wizard_mana -= 10
                            print(f"You have {wizard_mana} mana left!")

                            if goblin_health <= 0:
                                battle_start = False
                                print("\nThe goblin is no match to your power, enemy defeated!")
                                next_scene = input("next scene ->")
                            else:
                                goblin.attack()
                                print(f"\nDirect hit! -{goblin_damage} HP")
                                wizard_health -= goblin_damage
                                if wizard_health <= 0:
                                    print("Game over!")
                                    battle_start = False
                                else:
                                    print(f"\nYou have {wizard_health} HP left!")

                    elif next_turn.upper().strip() == "D":
                        if wizard_mana <= 5:
                            print("You don't have enough mana to defend!")
                            goblin.attack()
                            wizard_health -= goblin_damage
                            print(f"\nDirect hit! -{goblin_damage} HP")
                            print(f"\nYou have {wizard_health} HP left!")
                            if wizard_health <= 0:
                                print("Game over!")
                                battle_start = False
                        else:
                            wizard.defend()
                            wizard_mana -= 5
                            print(f"You have {wizard_mana} mana left!")
                            goblin.attack()
                            wizard_health -= int(goblin_damage / 2)
                            print(f"\nYou defended yourself and got less damage! -{goblin_damage / 2} HP")

                            if wizard_health <= 0:
                                print("Game over!")
                                battle_start = False
                            else:
                                print(f"You have {wizard_health} HP left!")

    @staticmethod
    def orc_fight():
        battle_start = True
        first_round = True
        orc = enemy.Orc()
        orc_health, orc_damage, orc_speed = orc.health, orc.damage, orc.speed
        warrior, wizard = '', ''
        warrior_health, warrior_damage, warrior_speed, warrior_mana = 0, 0, 0, 0
        wizard_health, wizard_damage, wizard_speed, wizard_mana = 0, 0, 0, 0
        chosen_fighter, fighter_name = utils.Utils.reader()
        if chosen_fighter == 1:
            warrior = player.Warrior(fighter_name)
            warrior_health, warrior_damage, warrior_speed, warrior_mana = \
                warrior.health, warrior.damage, warrior.speed, warrior.mana
        elif chosen_fighter == 2:
            wizard = player.Wizard(fighter_name)
            wizard_health, wizard_damage, wizard_speed, wizard_mana = \
                wizard.health, wizard.damage, wizard.speed, wizard.mana

        while battle_start:
            if chosen_fighter == 1:
                if first_round:
                    random_number = random.randint(0, 1)
                    if random_number == 0:
                        print("The enemy is as faster as you but this time you got lucky!")
                        action = input("\nType A to attack or D to defend -> ")
                        if action.upper().strip() == "A":
                            first_round = False
                            warrior.attack()
                            print(f"\nDirect hit, {warrior_damage} damage dealt!")
                            warrior_mana -= 10
                            print(f"\nYou have {warrior_mana} mana left!")
                            orc_health -= warrior_damage
                            orc.attack()
                            print(f"\nDirect hit! -{orc_damage} HP")
                            warrior_health -= orc_damage
                            print(f"\nYou have {warrior_health} HP left!")

                        elif action.upper().strip() == "D":
                            first_round = False
                            warrior.defend()
                            warrior_mana -= 5
                            print(f"\n You have {warrior_mana} mana left!")
                            orc.attack()
                            warrior_health -= int(orc_damage / 2)
                            print(f"\nYou defended yourself and got less damage! -{orc_damage / 2} HP")
                            print(f"\nYou have {warrior_health} HP left!")

                    elif random_number == 1:
                        print("\nThe enemy is as faster as you but this time he got lucky!")
                        first_round = False
                        orc.attack()
                        warrior_health -= orc_damage
                        print(f"\nDirect hit! -{orc_damage} HP")
                        print(f"\nYou have {warrior_health} HP left!")

                else:
                    next_turn = input("\nYour turn! Type A to attack, D to defend -> ")
                    if next_turn.upper().strip() == "A":
                        if warrior_mana <= 10:
                            print("You don't have enough mana to attack!")
                            orc.attack()
                            warrior_health -= orc_damage
                            print(f"\nDirect hit! -{orc_damage} HP")
                            print(f"\nYou have {warrior_health} HP left!")
                            if warrior_health <= 0:
                                print("Game over!")
                                battle_start = False
                        else:
                            warrior.attack()
                            orc_health -= warrior_damage
                            print(f"\nDirect hit, {warrior_damage} damage dealt!")
                            warrior_mana -= 10
                            print(f"\nYou have {warrior_mana} mana left!")

                            if orc_health <= 0:
                                battle_start = False
                                print("\nThe orc is no match to your power, enemy defeated!")
                                next_scene = input("next scene ->")
                            else:
                                orc.attack()
                                print(f"\nDirect hit! -{orc_damage} HP")
                                warrior_health -= orc_damage
                                if warrior_health <= 0:
                                    print("Game over!")
                                    battle_start = False
                                else:
                                    print(f"\nYou have {warrior_health} HP left!")

                    elif next_turn.upper().strip() == "D":
                        if warrior_mana <= 5:
                            print("You don't have enough mana to defend!")
                            orc.attack()
                            warrior_health -= orc_damage
                            print(f"\nDirect hit! -{orc_damage} HP")
                            print(f"\nYou have {warrior_health} HP left!")
                            if warrior_health <= 0:
                                print("Game over!")
                                battle_start = False

                        else:
                            warrior.defend()
                            warrior_mana -= 5
                            print(f"You have{warrior_mana} mana left!")
                            orc.attack()
                            warrior_health -= int(orc_damage / 2)
                            print(f"\nYou defended yourself and got less damage! -{orc_damage / 2} HP")

                            if warrior_health <= 0:
                                print("Game over!")
                                battle_start = False
                            else:
                                print(f"You have {warrior_health} HP left!")

            elif chosen_fighter == 2:
                if first_round:
                    print("You are faster than the enemy and have the first move!")
                    action = input("\nType A to attack or D to defend -> ")
                    if action.upper().strip() == "A":
                        first_round = False
                        wizard.attack()
                        print(f"\nDirect hit, {wizard_damage} damage dealt!")
                        wizard_mana -= 10
                        print(f"You have {wizard_mana} mana left!")
                        orc_health -= wizard_damage
                        orc.attack()
                        print(f"\nDirect hit! -{orc_damage} HP")
                        wizard_health -= orc_damage
                        print(f"\nYou have {wizard_health} HP left.")

                    elif action.upper().strip() == "D":
                        first_round = False
                        wizard.defend()
                        wizard_mana -= 5
                        print(f"You have {wizard_mana} mana left!")
                        orc.attack()
                        wizard_health -= orc_damage
                        print(f"\nYou defended yourself and got less damage! -{orc_damage / 2} HP")
                        print(f"\nYou have {wizard_health} HP left.")
                else:
                    next_turn = input("\nYour turn! Type A to attack, D to defend -> ")
                    if next_turn.upper().strip() == "A":
                        if wizard_mana <= 10:
                            print("You don't have enough mana to attack!")
                            orc.attack()
                            wizard_health -= orc_damage
                            print(f"\nDirect hit! -{orc_damage} HP")
                            print(f"\nYou have {wizard_health} HP left!")
                            if wizard_health <= 0:
                                print("Game over!")
                                battle_start = False
                        else:
                            wizard.attack()
                            print(f"\nDirect hit, {wizard_damage} damage dealt!")
                            wizard_mana -= 10
                            print(f"\nYou have {wizard_mana} mana left!")
                            orc_health -= wizard_damage

                            if orc_health <= 0:
                                battle_start = False
                                print("\nThe orc is no match to your power, enemy defeated!")
                                next_scene = input("next scene ->")
                            else:
                                orc.attack()
                                print(f"\nDirect hit! -{orc_damage} HP")
                                wizard_health -= orc_damage
                                if wizard_health <= 0:
                                    print("Game over!")
                                    battle_start = False
                                else:
                                    print(f"\nYou have {wizard_health} HP left.")

                    elif next_turn.upper().strip() == "D":
                        if wizard_mana <= 5:
                            print("You don't have enough mana to defend!")
                            orc.attack()
                            wizard_health -= orc_damage
                            print(f"\nDirect hit! -{orc_damage} HP")
                            print(f"\nYou have {wizard_health} HP left!")
                            if wizard_health <= 0:
                                print("Game over!")
                                battle_start = False
                        else:
                            wizard.defend()
                            wizard_mana -= 5
                            print(f"You have {wizard_mana} mana left!")
                            orc.attack()
                            wizard_health -= int(orc_damage / 2)
                            print(f"\nYou defended yourself and got less damage! -{orc_damage / 2} HP")

                            if wizard_health <= 0:
                                print("Game over!")
                                battle_start = False
                            else:
                                print(f"\nYou have {wizard_health} HP left.")

    @staticmethod
    def wraith_fight():
        battle_start = True
        first_round = True
        wraith = enemy.Wraith()
        wraith_health, wraith_damage, wraith_speed = wraith.health, wraith.damage, wraith.speed
        warrior, wizard = '', ''
        warrior_health, warrior_damage, warrior_speed, warrior_mana = 0, 0, 0, 0
        wizard_health, wizard_damage, wizard_speed, wizard_mana = 0, 0, 0, 0
        chosen_fighter, fighter_name = utils.Utils.reader()
        if chosen_fighter == 1:
            warrior = player.Warrior(fighter_name)
            warrior_health, warrior_damage, warrior_speed, warrior_mana = \
                warrior.health, warrior.damage, warrior.speed, warrior.mana
        elif chosen_fighter == 2:
            wizard = player.Wizard(fighter_name)
            wizard_health, wizard_damage, wizard_speed, wizard_mana = \
                wizard.health, wizard.damage, wizard.speed, wizard.mana

        while battle_start:
            if chosen_fighter == 1:
                if first_round:
                    print("\nThe wraith is faster than you and attacks first!")
                    first_round = False
                    wraith.attack()
                    print(f"\nDirect hit! -{wraith_damage} HP")
                    warrior_health -= wraith_damage
                    print(f"\nYou have {warrior_health} HP left!")
                else:
                    next_turn = input("\nYour turn! Type A to attack, D to defend -> ")
                    if next_turn.upper().strip() == "A":
                        if warrior_mana <= 10:
                            print("You don't have enough mana to attack!")
                            wraith.attack()
                            warrior_health -= wraith_damage
                            print(f"\nDirect hit! -{wraith_damage} HP")
                            print(f"\nYou have {warrior_health} HP left!")
                            if warrior_health <= 0:
                                print("Game over!")
                                battle_start = False
                        else:
                            warrior.attack()
                            print(f"\nDirect hit, {warrior_damage} damage dealt!")
                            warrior_mana -= 10
                            print(f"\nYou have {warrior_mana} mana left!")
                            wraith_health -= warrior_damage

                            if wraith_health <= 0:
                                battle_start = False
                                print("\nThe wraith is no match to your power, enemy defeated!")
                                next_scene = input("next scene ->")
                            else:
                                wraith.attack()
                                print(f"\nDirect hit! -{wraith_damage} HP")
                                warrior_health -= wraith_damage
                                if warrior_health <= 0:
                                    print("Game over!")
                                    battle_start = False
                                else:
                                    print(f"\nYou have {warrior_health} HP left!")

                    elif next_turn.upper().strip() == "D":
                        if warrior_mana <= 5:
                            print("You don't have enough mana to defend!")
                            wraith.attack()
                            warrior_health -= wraith_damage
                            print(f"\nDirect hit! -{wraith_damage} HP")
                            print(f"\nYou have {warrior_health} HP left!")
                            if warrior_health <= 0:
                                print("Game over!")
                                battle_start = False
                        else:
                            warrior.defend()
                            warrior_mana -= 5
                            print(f"You have {warrior_mana} mana left!")
                            wraith.attack()
                            warrior_health -= int(wraith_damage / 2)
                            print(f"\nYou defended yourself and got less damage! -{wraith_damage / 2} HP")

                            if warrior_health <= 0:
                                print("Game over!")
                                battle_start = False
                            else:
                                print(f"\nYou have {warrior_health} HP left!")

            elif chosen_fighter == 2:
                if first_round:
                    print("\nThe wraith is faster than you and attacks first!")
                    first_round = False
                    wraith.attack()
                    print(f"\nDirect hit! -{wraith_damage} HP")
                    wizard_health -= wraith_damage
                    print(f"\nYou have {wizard_health} HP left!")
                else:
                    next_turn = input("\nYour turn! Type A to attack, D to defend -> ")
                    if next_turn.upper().strip() == "A":
                        if wizard_mana <= 10:
                            print("You don't have enough mana to attack!")
                            wraith.attack()
                            wizard_health -= wraith_damage
                            print(f"\nDirect hit! -{wraith_damage} HP")
                            print(f"\nYou have {wizard_health} HP left!")
                            if wizard_health <= 0:
                                print("Game over!")
                                battle_start = False
                        else:
                            wizard.attack()
                            print(f"\nDirect hit, {wizard_damage} damage dealt!")
                            wizard_mana -= 10
                            print(f"You have {wizard_mana} mana left!")
                            wraith_health -= wizard_damage

                            if wraith_health <= 0:
                                battle_start = False
                                print("\nThe orc is no match to your power, enemy defeated!")
                                next_scene = input("next scene ->")
                            else:
                                wraith.attack()
                                print(f"\nDirect hit! -{wraith_damage} HP")
                                wizard_health -= wraith_damage
                                if wizard_health <= 0:
                                    print("Game over!")
                                    battle_start = False
                                else:
                                    print(f"\nYou have {wizard_health} HP left.")

                    elif next_turn.upper().strip() == "D":
                        if wizard_mana <= 5:
                            print("You don't have enough mana to defend!")
                            wraith.attack()
                            wizard_health -= wraith_damage
                            print(f"\nDirect hit! -{wraith_damage} HP")
                            print(f"\nYou have {wizard_health} HP left!")
                            if wizard_health <= 0:
                                print("Game over!")
                                battle_start = False
                        else:
                            wizard.defend()
                            wizard_mana -= 5
                            print(f"You have {wizard_mana} mana left!")
                            wraith.attack()
                            wizard_health -= int(wraith_damage / 2)
                            print(f"\nYou defended yourself and got less damage! -{wraith_damage / 2} HP")

                            if wizard_health <= 0:
                                print("Game over!")
                                next = input("->")
                                battle_start = False
                            else:
                                print(f"\nYou have {wizard_health} HP left.")

    @staticmethod
    def battle_start():
        chosen_enemy = utils.Utils.random_enemy()
        if chosen_enemy == 0:
            Battle.goblin_fight()
        elif chosen_enemy == 1:
            Battle.orc_fight()
        elif chosen_enemy == 2:
            Battle.wraith_fight()
