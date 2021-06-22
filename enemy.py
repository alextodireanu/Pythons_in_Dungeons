class Enemy:
    def __init__(self, damage, health):
        self.damage = damage
        self.health = health

    def attack(self):
        print("The enemy is attacking")


class Goblin(Enemy):
    def __init__(self):
        super().__init__(10, 40)
        print("""\nI'm a vengeful goblin.
My poisonous arrows will pierce you!""")
    damage = 10
    health = 40
    speed = 2

    def attack(self):
        print("The enemy goblin is attacking!")


class Orc(Enemy):
    def __init__(self):
        super().__init__(30, 100)
        print("""\nI'm the Dark Lord's orc captain.
Your head will be my trophy!""")
    damage = 30
    health = 100
    speed = 1

    def attack(self):
        print("The enemy orc is attacking!")


class Wraith(Enemy):
    def __init__(self):
        super().__init__(20, 70)
        print("""\nI'm one of the nine dead kings.
You are no match to my powers!""")
    damage = 20
    health = 70
    speed = 3

    def attack(self):
        print("The enemy wraith is attacking!")
