class Animal:
    def __init__(self, name, species):
        self.name = name
        self.species = species

    def make_sound(self):
        pass  # Abstract method

    def move(self):
        print(f"{self.name} is moving.")

    def eat(self, food):
        print(f"{self.name} is eating {food}.")
