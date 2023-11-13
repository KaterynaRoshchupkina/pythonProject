from Animals import Animal


class Mammals(Animal):
    def __init__(self, name, species, fur_color):
        super().__init__(name, species)
        self.fur_color = fur_color

    def give_birth(self):
        print(f"{self.name} is giving birth to live young.")

    def make_sound(self):
        print(f"{self.name} makes a mammal sound.")
