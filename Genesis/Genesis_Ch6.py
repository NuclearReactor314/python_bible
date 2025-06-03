class Person:
    def __init__(self, name=None, lifespan=None):
        self.name = name
        self.lifespan = lifespan
        self.children = []

god = "YHWH"
humans_multiplied = True

sons_of_god = ["sons_of_God_{}".format(i) for i in range(1, 100)]
daughters_of_men = ["daughter_{}".format(i) for i in range(1, 100)]

marriages = list(zip(sons_of_god, daughters_of_men))

god_declared = {
    "spirit_will_not_strive_forever": True,
    "human_is_flesh": True,
    "lifespan_limit": 120
}

nephilim = ["Nephilim_{}".format(i) for i in range(1, 10)]
mighty_men = nephilim
men_of_renown = nephilim

god_saw = {
    "human_wickedness": "great",
    "heart_inclination": "only_evil"
}

god_regretted_creation = True
god_grieved = True

judgment = {
    "destroy_man": True,
    "destroy_beast": True,
    "destroy_creeping_thing": True,
    "destroy_birds": True
}

noah = Person(name="Noah")
noah_favored_by = god

noah_desc = {
    "righteous": True,
    "blameless": True,
    "walked_with_God": True
}

shem = Person(name="Shem")
ham = Person(name="Ham")
japheth = Person(name="Japheth")

noah.children = [shem, ham, japheth]

earth_state = {
    "corrupt": True,
    "filled_with_violence": True
}

god_announced = {
    "end_of_all_flesh": True,
    "earth_filled_with_violence": True,
    "destruction_imminent": True
}

ark = {
    "material": "gopher_wood",
    "rooms": True,
    "sealed_inside_and_out": True,
    "dimensions": {
        "length_cubits": 300,
        "width_cubits": 50,
        "height_cubits": 30
    },
    "window": {
        "size": "1_cubit",
        "location": "top"
    },
    "door": {
        "location": "side"
    },
    "decks": 3
}

flood = {
    "coming": True,
    "waters_to_destroy_all_flesh": True
}

covenant = {
    "with": noah
}

ark_inhabitants = {
    "noah": noah,
    "sons": noah.children,
    "wife": "Noah's Wife",
    "sons_wives": ["Wife_of_Shem", "Wife_of_Ham", "Wife_of_Japheth"]
}

living_things_to_save = {
    "kinds": "all",
    "quantity": "two_of_each_gender"
}

food_gathered = "enough_for_all"

noah_obeyed = True