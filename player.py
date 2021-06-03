class Player:
    def __init__(self, name, mana, health, damage):
        self.name = name
        self.mana = mana
        self.health = health
        self.damage = damage

    def attack(self):
        pass

class Warrior(Player):
    def __init__(self, name, mana, health, damage):
        super().__init__(name, mana, health, damage)
        self.health += 10
        self.damage += 10

class Wizard(Player):
    def __init__(self, name, mana, health, damage):
        super().__init__(name, mana, health, damage)
        self.mana += 10
        self.health += 10