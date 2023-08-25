class Item:
    def __init__(self, name, description):
        self.name = name
        self.description = description

    def use(self, target):
        print(f"Using {self.name} on {target}!")