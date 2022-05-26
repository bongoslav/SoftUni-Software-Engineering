animals = input()

animals_list = animals.split(", ")
animals_list.reverse()

for index, animal in enumerate(animals_list):
    if animals_list[0] == "wolf":
        print("Please go away and stop eating my sheep")
        break
    elif animal == "wolf":
        print(f"Oi! Sheep number {index}! You are about to be eaten by a wolf!")