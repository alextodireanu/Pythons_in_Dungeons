import player
import os
import winsound
import enemy
import random


class Utils:
    @staticmethod
    def intro_message():
        sound = 'Main_Menu.wav'
        # the sound will play in a loop and async
        winsound.PlaySound(sound, winsound.SND_ASYNC + winsound.SND_LOOP)
        intro_message = f"""
        \t\t\t {'*' * 84}
        \t\t\t Welcome stranger,
        \t\t\t Here in Hinderlands, you'll get to fight dragons and conquer the deadliest dungeons.
        \t\t\t In a country where magic rules, anything is possible if you wish so.
        \t\t\t It all depends on you, brave hero!
        \t\t\t {'*' * 84}
        """
        return intro_message

    @staticmethod
    def world_intro():
        sound = 'Exploring.wav'
        # the sound will play in a loop and async
        winsound.PlaySound(sound, winsound.SND_ASYNC + winsound.SND_LOOP)
        os.system('cls')
        world_intro_message = "\t\t\tThe Hinderlands are in grave danger and only you can " \
                              "stand a chance against the enemy armies\n"""
        print(world_intro_message)
        crossroad_options = ('village', 'forest', 'desert')
        print("You are at a crossroads with 3 possible paths:")
        index = 1
        for option in crossroad_options:
            print(f'{index}.{option}')
            index += 1
        try:
            chosen_path = int(input("\nChoose your destiny: 1,2 or 3? -> "))
            if chosen_path == 1:
                Utils.village()
            elif chosen_path == 2:
                Utils.forest()
            elif chosen_path == 3:
                Utils.desert()
            else:
                print("Incorrect choice")
        except ValueError:
            print("Only numbers are accepted")
        else:
            return chosen_path

    @staticmethod
    def warrior():
        warrior_name = input("\nYour mighty warrior needs a name -> ")
        warrior = player.Warrior(warrior_name.strip())
        return warrior

    @staticmethod
    def wizard():
        wizard_name = input("\nYour powerful wizard needs a name -> ")
        wizard = player.Wizard(wizard_name.strip())
        return wizard

    @staticmethod
    def random_enemy():
        sound = 'BattleFinal.wav'
        # the sound will play in a loop and async
        winsound.PlaySound(sound, winsound.SND_ASYNC + winsound.SND_LOOP)
        random_number = random.randint(0, 2)
        if random_number == 0:
            print("An enemy appeared:")
            goblin = enemy.Goblin()
            action = input("\nA fight is imminent... Type A to attack or D to defend -> ")
        elif random_number == 1:
            print("An enemy appeared:")
            orc = enemy.Orc()
            action = input("\nA fight is imminent... Type A to attack or D to defend -> ")
        elif random_number == 2:
            print("An enemy appeared:")
            wrath = enemy.Wrath()
            action = input("\nA fight is imminent... Type A to attack or D to defend -> ")
        return

    @staticmethod
    def village():
        os.system('cls')
        village_intro_message = "\t\t\tYour adventure starts in the village of Bannockburn\n"
        print(village_intro_message)
        Utils.random_enemy()
        return

    @staticmethod
    def forest():
        os.system('cls')
        forest_intro_message = "\t\t\tYour adventure starts in the Wolfbel forest\n"
        print(forest_intro_message)
        print(Utils.random_enemy())
        return

    @staticmethod
    def desert():
        os.system('cls')
        desert_intro_message = "\t\t\tYour adventure starts in the Dead Wasteland\n"
        print(desert_intro_message)
        Utils.random_enemy()
        return

    @staticmethod
    def game_start():
        try:
            start = input("Ready to begin your adventure? Y/N -> ")
            game_start = False
            if start.upper().strip() == 'Y':
                game_start = True
            elif start.upper().strip() == 'N':
                game_start = False
            else:
                print("Incorrect choice")
            while game_start:
                if start.strip().upper() == "Y":
                    os.system('cls')
                    print("To start your quest, please select your fighter:")
                    available_fighters = ("Warrior", "Wizard")
                    index = 1
                    for fighter in available_fighters:
                        print(f"{index}.{fighter}")
                        index += 1
                    chosen_fighter = int(input("\nWhat's your choice: 1 or 2? -> "))
                    if chosen_fighter == 1:
                        Utils.warrior()
                        Utils.world_intro()
                    elif chosen_fighter == 2:
                        Utils.wizard()
                        Utils.world_intro()
                    else:
                        print("Incorrect choice")
                elif start.strip().upper() == 'N':
                    game_start = False
                else:
                    print("Incorrect choice")
        except ValueError:
            print("Only numbers are accepted")
        else:
            print()
        return
