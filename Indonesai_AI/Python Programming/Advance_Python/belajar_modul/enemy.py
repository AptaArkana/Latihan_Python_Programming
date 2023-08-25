class Enemy:
    def __init__(self, name, power):
        self.name = name
        self.power = power

    def attack(self, target):
        print(f"{self.name} attacks {target}!")