class Enemy:
    def __init__(self, health, damage):
        self.health = health
        self.damage = damage

    def attack(self):
        pass


class Goblin(Enemy):
    def __init__(self):
        super(Goblin, self).__init__(100, 5)
        print("Glglg!!! I am a Gobil and I will slash you!!!")


class Orc(Enemy):
    def __init__(self):
        super(Orc, self).__init__(100, 15)
        print("Wraar I am a Orc and I will cut you down!!!")


class Rat(Enemy):
    def __init__(self):
        super(Rat, self).__init__(100, 10)
        print("Squil!! I am a Rat and I will eat you alivee!!!")