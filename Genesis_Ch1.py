Universe = None
console.log("Initializing creation...")

# “let there be light”
light = True
console.log("Light created.")

# defined day and night
def separate(light):
    return "Day" if light else "Night"

Day1 = {"light": separate(True)}
console.log("Day 1:", Day1)

# “let there be sky”
sky = True
console.log("Sky created.")

# Created land and ocean
land = "Earth()"
ocean = "Sea()"
console.log("Land and ocean created.")

# Call generateVegetation()
def generateVegetation():
    return ["Grass", "Trees", "Fruit"]

plants = generateVegetation()
console.log("Plants created:", plants)

# Created Sun, Moon, Stars
sun = "Sun()"
moon = "Moon()"
stars = ["Star()" for _ in range(1000)]
console.log("Heavenly lights initialized.")

# “let there be life in the water and sky”
fish = "Fish()"
birds = "Birds()"
console.log("Creatures of water and air created.")

# “let there be animals on land”
animals = ["Lion()", "Elephant()", "Dog()"]
console.log("Land animals created:", animals)

# “let there be Humans in My image”
class Human:
    def __init__(self, name):
        self.name = name
        self.free_will = True

adam = Human("Adam")
eve = Human("Eve")
console.log("Humans created:", adam.name, "and", eve.name)

# Testing:
Universe = [Day1, sky, land, ocean, plants, sun, moon, stars, fish, birds, animals, adam, eve]
if all(Universe):
    console.log("Creation successful. All systems functional.")

# Day 7
rest = True
console.log("System paused. Creator is now resting.")