class Human:
    def __init__(self, name: str, age: int = None, children=None):
        self.name = name
        self.age = age
        self.children = children if children else []

adam = Human(name="Adam", age=930)
seth = Human(name="Seth", age=912)
adam.children.append(seth)

enosh = Human(name="Enosh", age=905)
seth.children.append(enosh)

kenan = Human(name="Kenan", age=910)
enosh.children.append(kenan)

mahalalel = Human(name="Mahalalel", age=895)
kenan.children.append(mahalalel)

jared = Human(name="Jared", age=962)
mahalalel.children.append(jared)

enoch = Human(name="Enoch", age=365)
jared.children.append(enoch)

def walk_with_God(human: Human):
    human.age = None
    human.transcended = True

walk_with_God(enoch)

methuselah = Human(name="Methuselah", age=969)
enoch.children.append(methuselah)

lamech = Human(name="Lamech", age=777)
methuselah.children.append(lamech)

noah = Human(name="Noah", age=950)
lamech.children.append(noah)

shem = Human(name="Shem")
ham = Human(name="Ham")
japheth = Human(name="Japheth")
noah.children.extend([shem, ham, japheth])