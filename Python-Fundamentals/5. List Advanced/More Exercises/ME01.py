population = list(map(int, input().split(", ")))
minimum_wealth = int(input())

for index, person_wealth in enumerate(population):
    wealthiest_value = max(population)
    wealthiest_person = population.index(wealthiest_value)
    if person_wealth == population[wealthiest_person]:
        continue
    while population[index] < minimum_wealth < population[wealthiest_person]:
        population[index] += 1
        population[wealthiest_person] -= 1

if min(population) < minimum_wealth:
    print("No equal distribution possible")
else:
    print(population)