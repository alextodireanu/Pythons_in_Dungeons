class Player:
    def __init__(self, name, mana, health, damage, speed):
        self.name = name
        self.mana = mana
        self.health = health
        self.damage = damage
        self.speed = speed

    def attack(self):
        print("Attacking")

    def defend(self):
        print("Defending")


class Warrior(Player):
    def __init__(self, name):
        super().__init__(name, 50, 100, 50, 1)
        self.name = name


    def attack(self):
        print("Your warrior is attacking!")

    def defend(self):
        print("Your warrior is defending...")


class Wizard(Player):
    def __init__(self, name):
        super().__init__(name, 100, 75, 25, 2)
        self.name = name


    def attack(self):
        print("Your wizard is attacking...")

    def defend(self):
        print("Your wizard is defending...")
