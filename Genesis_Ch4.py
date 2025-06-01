class Human:
    def __init__(self, name):
        self.name = name
        self.alive = True

Cain = Human("Cain")
Abel = Human("Abel")

def offering(human, gift):
    return f"{human.name} brought {gift} as an offering."

Cain_offering = offering(Cain, "fruit of the ground")
Abel_offering = offering(Abel, "the firstborn of his flock and their fat portions")

God_accepted_Abel = True
God_accepted_Cain = False

Cain_feelings = "very angry and downcast"

Cain_invited_Abel = "Let us go out to the field"

Cain_killed_Abel = True
if Cain_killed_Abel:
    Abel.alive = False

God_asked = "Where is your brother Abel?"
Cain_answered = "I do not know. Am I my brother's keeper?"

God_cursed_Cain = "Cursed from the ground that opened its mouth to receive Abel's blood"

God_marked_Cain = True

Cain_fear = "Will be killed by others"
God_protection = "Mark of Cain to prevent killing"

descendants_of_Cain = [
    {"name": "Enoch", "city": "named city after him"},
    {"name": "Jabal", "lived in tents and raised livestock"},
    {"name": "Jubal", "father of all who play harp and flute"},
    {"name": "Tubal-cain", "forger of all instruments of bronze and iron"},
]

Cain_family = {
    "wife": "Cain's wife",
    "son": "Enoch"
}