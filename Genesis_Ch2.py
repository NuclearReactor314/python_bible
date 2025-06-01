import logging

logging.basicConfig(level=logging.INFO, format='%(message)s')
log = logging.info

class EdenGarden:
    def __init__(self):
        self.trees = ["Tree of Life", "Tree of Knowledge of Good and Evil"]
        self.river = "Euphrates()"
        self.animals = []
        self.human = None

    def describe(self):
        log("Eden Garden initialized with trees and a river.")
        log("Trees:", ", ".join(self.trees))
        log("River:", self.river)

eden = EdenGarden()
eden.describe()

class Human:
    def __init__(self, name):
        self.name = name
        self.location = None
        self.job = None
        self.partner = None
        self.free_will = True

    def assign_to_garden(self, garden):
        self.location = garden
        self.job = "Care and keep the garden"
        log(f"{self.name} is placed in Eden and assigned to: {self.job}")

adam = Human("Adam")
eden.human = adam
adam.assign_to_garden(eden)

forbidden_tree = "Tree of Knowledge of Good and Evil"
log(f"Command: You may eat from any tree, except the {forbidden_tree}.")

animals_to_create = ["Elephant", "Bird", "Giraffe", "Cat", "Dog"]
for animal in animals_to_create:
    eden.animals.append(animal)
log("Animals created and brought to Adam for naming:", ", ".join(eden.animals))

class Woman(Human):
    def __init__(self, name):
        super().__init__(name)

def create_partner(man):
    log(f"{man.name} is in deep sleep...")
    log("Creating woman from Adam's rib...")
    woman = Woman("Eve")
    man.partner = woman
    woman.partner = man
    log(f"{woman.name} has been created and joined with {man.name}.")

create_partner(adam)

log("Therefore shall a man leave his father and mother, and cleave unto his wife,")
log("and they shall be one flesh.")