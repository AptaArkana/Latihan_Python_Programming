class Hero:
    def __init__(self, name, health):
        self.name = name
        self.health = health

    def attack(self, enemy):
        print(f"{self.name} attacks {enemy}!")

    def use_item(self, item):
        print(f"{self.name} uses {item}!")