class Enemy:
    def __init__(self, damage, health, speed):
        self.damage = damage
        self.health = health
        self.speed = speed

    def attack(self):
        print("The enemy is attacking")


class Goblin(Enemy):
    def __init__(self):
        super().__init__(10, 40, 2)
        print("""\nI'm a vengeful goblin.
My poisonous arrows will pierce you!""")

    def attack(self):
        print("The enemy goblin is attacking!")


class Orc(Enemy):
    def __init__(self):
        super().__init__(30, 100, 1)
        print("""\nI'm the Dark Lord's orc captain.
Your head will be my trophy!""")

    def attack(self):
        print("The enemy orc is attacking!")


class Wraith(Enemy):
    def __init__(self):
        super().__init__(20, 70, 3)
        print("""\nI'm one of the nine dead kings.
You are no match to my powers!""")

    def attack(self):
        print("The enemy wraith is attacking!")
