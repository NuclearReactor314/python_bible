class Person:
    def __init__(self, name: str, descendants=None):
        self.name = name
        self.descendants = descendants if descendants else []

jacob = Person("Jacob")

reuben = Person("Reuben")
simeon = Person("Simeon")
levi = Person("Levi")
judah = Person("Judah")
issachar = Person("Issachar")
zebulun = Person("Zebulun")
benjamin = Person("Benjamin")
dan = Person("Dan")
naphtali = Person("Naphtali")
gad = Person("Gad")
asher = Person("Asher")

jacob.descendants.extend([
    reuben, simeon, levi, judah,
    issachar, zebulun, benjamin,
    dan, naphtali, gad, asher
])

joseph = Person("Joseph")
jacob.descendants.append(joseph)

jacob_family = jacob.descendants
total_people = 70  # excluding Joseph, who was already in Egypt

joseph_in_egypt = True
joseph_died = True
all_brothers_died = True

israelites_increased = True

new_pharaoh = "Pharaoh_Unknown_Joseph"

if new_pharaoh == "Pharaoh_Unknown_Joseph":
    israelites_population = "very_large"
    pharaoh_feared = True
    pharaoh_said = "Let us deal shrewdly with them"

taskmasters_assigned = True
forced_labor = ["Pithom", "Rameses"]

oppression = True

if oppression:
    israelites_population = "even_larger"

egyptians_feared = True

hebrew_midwives = ["Shiphrah", "Puah"]
pharaoh_order = "Kill all Hebrew boys at birth"

midwives_feared_God = True
midwives_disobeyed = True

god_rewarded_midwives = True

pharaoh_commanded = "Throw every Hebrew boy into the Nile"