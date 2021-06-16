class Enemy:
    def __init__(self, damage, health):
        self.damage = damage
        self.health = health

    def attack(self):
        pass


class Goblin(Enemy):
    def __init__(self):
        super().__init__(5, 100)
        print("My poisonous arrows will kill you!")


class Orc(Enemy):
    def __init__(self):
        super().__init__(15, 100)
        print("I will cut you down!")


class Wrath(Enemy):
    def __init__(self):
        super().__init__(10, 100)
        print("You are no match to my powers!")