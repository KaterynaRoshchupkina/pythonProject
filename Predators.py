from Mammals import Mammals


class Predators(Mammals):
    def __init__(self, name, species, fur_color, hunting_skill):
        super().__init__(name, species, fur_color)
        self.hunting_skill = hunting_skill

    def hunt(self, target):
        print(f"{self.name} is hunting {target} using {self.hunting_skill}.")

    def make_sound(self):
        print(f"{self.name} roars like a predator.")


lion = Predators(name="Simba", species="Lion", fur_color="Yellow", hunting_skill="sharp claws")

lion.move()
lion.eat("meat")
lion.give_birth()
lion.hunt("gazelle")
lion.make_sound()
