import os
import winsound
import random
import battle

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
                print("\nIncorrect choice")
        except ValueError:
            print("\nOnly numbers are accepted")
        else:
            return chosen_path

    @ staticmethod
    def choose_fighter():
        print("To start your quest, please select your fighter:")
        available_fighters = ("Warrior", "Wizard")
        index = 1
        for fighter in available_fighters:
            print(f"{index}.{fighter}")
            index += 1
        try:
            chosen_fighter = int(input("\nWhat's your choice: 1 or 2? -> "))
            if chosen_fighter == 1:
                Utils.warrior()
            elif chosen_fighter == 2:
                Utils.wizard()
            else:
                print("Incorrect choice")
        except ValueError:
            print("Only numbers are accepted")
        else:
            return chosen_fighter

    @staticmethod
    def warrior():
        chosen_fighter = 1
        warrior_name = input("\nYour mighty warrior needs a name -> ")
        try:
            with open('save_file.txt', mode='w') as writeFile:
                writeFile.write(f'chosen_fighter = {chosen_fighter}')
                writeFile.write(f'\nwarrior_name = {warrior_name}')
        except IOError:
            print("Error writing file")
        else:
            writeFile.close()

    @staticmethod
    def wizard():
        chosen_fighter = 2
        wizard_name = input("\nYour powerful wizard needs a name -> ")
        try:
            with open('save_file.txt', mode='w') as writeFile:
                writeFile.write(f'chosen_fighter = {chosen_fighter}')
                writeFile.write(f'\nwizard_name = {wizard_name}')
        except IOError:
            print("Error writing file")
        else:
            writeFile.close()

    @staticmethod
    def goblin():
        print("An enemy goblin appeared, a fight is imminent:")
        chosen_enemy = 0
        try:
            with open('save_file.txt', mode='a') as writeFile:
                writeFile.write(f'\nchosen_enemy = {chosen_enemy}')
        except IOError:
            print("Error writing file")
        else:
            writeFile.close()

    @staticmethod
    def orc():
        print("An enemy orc appeared, a fight is imminent:")
        chosen_enemy = 1
        try:
            with open('save_file.txt', mode='a') as writeFile:
                writeFile.write(f'\nchosen_enemy = {chosen_enemy}')
        except IOError:
            print("Error writing file")
        else:
            writeFile.close()

    @staticmethod
    def wraith():
        print("An enemy wraith appeared, a fight is imminent:")
        chosen_enemy = 2
        try:
            with open('save_file.txt', mode='a') as writeFile:
                writeFile.write(f'\nchosen_enemy = {chosen_enemy}')
        except IOError:
            print("Error writing file")
        else:
            writeFile.close()

    @staticmethod
    def random_enemy():
        sound = 'BattleFinal.wav'
        # the sound will play in a loop and async
        winsound.PlaySound(sound, winsound.SND_ASYNC + winsound.SND_LOOP)
        random_number = random.randint(0, 2)
        if random_number == 0:
            Utils.goblin()
        elif random_number == 1:
            Utils.orc()
        elif random_number == 2:
            Utils.wraith()
        return random_number

    @staticmethod
    def village():
        os.system('cls')
        village_intro_message = "\t\t\tYour adventure starts in the village of Bannockburn\n"
        print(village_intro_message)
        battle.Battle.battle_start()
        return

    @staticmethod
    def forest():
        os.system('cls')
        forest_intro_message = "\t\t\tYour adventure starts in the Wolfbel forest\n"
        print(forest_intro_message)
        battle.Battle.battle_start()
        return

    @staticmethod
    def desert():
        os.system('cls')
        desert_intro_message = "\t\t\tYour adventure starts in the Dead Wasteland\n"
        print(desert_intro_message)
        battle.Battle.battle_start()
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
                    Utils.choose_fighter()
                    Utils.world_intro()
                elif start.strip().upper() == 'N':
                    game_start = False
                else:
                    print("Incorrect choice")
        except ValueError:
            print("Only numbers are accepted")
        else:
            print()
        return

    @staticmethod
    def reader():
        try:
            with open('save_file.txt', mode='r') as readFile:
                chosen_fighter = int(readFile.readline().split()[-1])
                fighter_name = readFile.readline().split()[-1]
        except IOError:
            print("Error reading file")
        else:
            readFile.close()
        return chosen_fighter, fighter_name