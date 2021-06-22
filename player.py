class Player:
    def __init__(self, name, mana, health, damage):
        self.name = name
        self.mana = mana
        self.health = health
        self.damage = damage

    def attack(self):
        print("Attacking")

    def defend(self):
        print("Defending")


class Warrior(Player):
    def __init__(self, name):
        super().__init__(name, 50, 100, 50)
        self.name = name
    mana = 50
    damage = 50
    health = 100
    speed = 1

    def attack(self):
        print("Your warrior is attacking!")

    def defend(self):
        print("Your warrior is defending...")


class Wizard(Player):
    def __init__(self, name):
        super().__init__(name, 100, 75, 25)
        self.name = name
    mana = 100
    damage = 25
    health = 75
    speed = 2

    def attack(self):
        print("Your wizard is attacking...")

    def defend(self):
        print("Your wizard is defending...")
