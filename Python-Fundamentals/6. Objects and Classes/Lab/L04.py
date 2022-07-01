class Zoo:
    __animals = 0  # class attribute

    def __init__(self, name):
        self.name = name
        self.mammals = []
        self.fishes = []
        self.birds = []

    def add_animal(self, species, name):
        if species == "mammal":
            self.mammals.append(name)
        elif species == "fish":
            self.fishes.append(name)
        else:
            self.birds.append(name)
        Zoo.__animals += 1

    def get_info(self, species):
        if species == "mammal":
            result = f"Mammals in {self.name}: {', '.join(self.mammals)}\nTotal animals: {Zoo.__animals}"
        elif species == "fish":
            result = f"Fishes in {self.name}: {', '.join(self.fishes)}\nTotal animals: {Zoo.__animals}"
        else:
            result = f"Birds in {self.name}: {', '.join(self.birds)}\nTotal animals: {Zoo.__animals}"

        return result


zoo_name = input()
count = int(input())

zoo = Zoo(zoo_name)
for line in range(count):
    animal = input().split()
    animal_species = animal[0]
    animal_name = animal[1]
    zoo.add_animal(animal_species, animal_name)

interested_species = input()
print(zoo.get_info(interested_species))
