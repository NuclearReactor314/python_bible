Universe = None

light = True

def separate(light_on: bool) -> str:
    if light_on:
        return "Day"
    else:
        return "Night"

Day1 = {"period": separate(True)}

sky = True

land = "Earth()"  
ocean = "Sea()" 

def generate_vegetation():
    return ["Grass", "Trees", "Fruit"]

plants = generate_vegetation()

sun = "Sun()"
moon = "Moon()"
stars = ["Star()" for _ in range(1000)]

fish = "Fish()"
birds = "Birds()"

animals = ["Lion()", "Elephant()", "Dog()"]

class Human:
    def __init__(self, name: str):
        self.name = name
        self.free_will = True

adam = Human("Adam")
eve = Human("Eve")

Universe = [
    Day1, sky, land, ocean, plants,
    sun, moon, stars,
    fish, birds, animals,
    adam, eve
]

rest = True