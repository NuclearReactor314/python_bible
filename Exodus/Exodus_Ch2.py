class Person:
    def __init__(self, name: str = None, tribe: str = None, gender: str = None):
        self.name = name
        self.tribe = tribe
        self.gender = gender
        self.children = []

levite_man = Person(tribe="Levi", gender="male")
levite_woman = Person(tribe="Levi", gender="female")

moses = Person(name="Moses", gender="male")
levite_woman.children.append(moses)
levite_man.children.append(moses)

moses_hidden = True
hidden_duration = 3  

basket = {
    "material": ["papyrus", "tar", "pitch"],
    "contents": [moses],
    "location": "Nile"
}

sister = Person(gender="female")
sister_position = "watching_from_distance"

pharaoh_daughter = Person(gender="female")

if pharaoh_daughter:
    basket_found = True
    baby_cried = True
    pharaoh_daughter_felt_pity = True

hebrew_nurse_offered = True
mother_hired_as_nurse = True

moses_returned_to_pharaoh_daughter = True
moses_named = "Moses"


moses_adult = True
hebrew_beaten = True
egyptian_killed = True
egyptian_hidden = "sand"

next_day = True
two_hebrews_fighting = True
moses_confronts = True
truth_exposed = True

pharaoh_heard = True
pharaoh_tried_to_kill = True
moses_fled = True
moses_fled_to = "Midian"


priest_of_midian = Person()
priest_daughters = [Person(gender="female") for _ in range(7)]

shepherds_drove_them_away = True
moses_rescued = True
watered_flock = True

father = priest_of_midian
father_replied = "Invite him to eat"

zipporah = priest_daughters[0]
moses_married = zipporah

gershom = Person(name="Gershom", gender="male")
moses.children.append(gershom)


egypt_king_died = True
israelites_groaned = True
god_heard = True
god_remembered_covenant = True
god_looked_on = True