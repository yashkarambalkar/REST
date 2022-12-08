from geneticAlgorithm import GeneticAlgorithm

numOfGenerations = 15

GA = GeneticAlgorithm()

# Init population at size 10
GA.generatePopulation(10)

# Run algorithm for 15 generations
for generation in range(numOfGenerations):
    GA.fitness()
    GA.sortAndDropPercentange(.50)
    GA.crossOver(2)
    GA.mutate(.25)

print("Population after {} generations: ".format(numOfGenerations))
for item in GA.population:
    print(item.get('value'), " - ", int(item.get('value'), 2))
print("\nThe squared maximum is: ", int(GA.maxVal, 2))
