class Enemy:
    def __init__(self, damage, health):
        self.damage = damage
        self.health = health

    def attack(self):
        pass


class Goblin(Enemy):
    def __init__(self):
        super().__init__(5, 100)
        print("""\nI'm a vengeful goblin.
My poisonous arrows will pierce you!""")


class Orc(Enemy):
    def __init__(self):
        super().__init__(15, 100)
        print("""\nI'm the Dark Lord orc captain.
Your head will be my trophy!""")


class Wrath(Enemy):
    def __init__(self):
        super().__init__(10, 100)
        print("""\nI'm one of the nine dead kings."
You are no match to my powers!""")