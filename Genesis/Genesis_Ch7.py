class Person:
    def __init__(self, name):
        self.name = name

noah = Person("Noah")
noah_family = {
    "noah": noah,
    "wife": "Noah's Wife",
    "sons": ["Shem", "Ham", "Japheth"],
    "sons_wives": ["Shem's Wife", "Ham's Wife", "Japheth's Wife"]
}

ark = {
    "inhabitants": noah_family,
    "clean_animals": {"male": 7, "female": 7},
    "unclean_animals": {"male": 1, "female": 1},
    "birds": {"male": 7, "female": 7}
}

god_spoke_to_noah = True
god_command = {
    "enter_ark": True,
    "take_animals": ark,
    "reason": "I will send rain in 7 days",
    "duration": "40 days and 40 nights",
    "judgment": "blot out every living thing"
}

noah_obeyed_all = True
noah_age = 600
flood_start = {
    "year": 600,
    "month": 2,
    "day": 17
}

ark_entered = True

all_entered = {
    "male_female": True,
    "as_commanded_by_God": True
}

god_shut_door = True

flood = {
    "days_of_rain": 40,
    "waters_increased": True,
    "ark_rose": True,
    "waters_prevail": True,
    "mountains_covered": True
}

all_life_outside_ark_died = True

life_destroyed = {
    "man": True,
    "animals": True,
    "creeping_things": True,
    "birds": True
}

noah_preserved = True
ark_inhabitants_preserved = True

waters_prevailed_days = 150