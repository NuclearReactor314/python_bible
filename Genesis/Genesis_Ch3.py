class Human:
    def __init__(self, name):
        self.name = name
        self.has_eaten_forbidden = False
        self.is_naked = True
        self.in_garden = True

    def eat(self, fruit):
        if fruit == "forbidden fruit":
            self.has_eaten_forbidden = True
            return f"{self.name} ate the {fruit}."
        return f"{self.name} ate the {fruit}."

    def realize_nakedness(self):
        if self.has_eaten_forbidden:
            self.is_naked = True
            return f"{self.name} realized they were naked."

    def cover(self):
        if self.is_naked:
            self.is_naked = False
            return f"{self.name} sewed fig leaves together and covered themselves."

    def leave_garden(self):
        if self.has_eaten_forbidden:
            self.in_garden = False
            return f"{self.name} was banished from the Garden of Eden."

class Serpent:
    def tempt(self, human):
        return f"The serpent said to {human.name}, 'You will not surely die.'"

adam = Human("Adam")
eve = Human("Eve")
serpent = Serpent()

temptation = serpent.tempt(eve)
eve_eats = eve.eat("forbidden fruit")
adam_eats = adam.eat("forbidden fruit")

realize_adam = adam.realize_nakedness()
realize_eve = eve.realize_nakedness()

cover_adam = adam.cover()
cover_eve = eve.cover()

god_curses = [
    "Cursed is the serpent above all livestock and wild animals.",
    "To the woman, increased pain in childbirth and desire for her husband.",
    "To the man, cursed ground and painful toil."
]

banish_adam = adam.leave_garden()
banish_eve = eve.leave_garden()