import random
import operator
import math

class GeneticAlgorithm:
    def __init__(self):
        self.population = []
        self.maxVal = bin(0)


    def generatePopulation(self, size):
        for i in range(size):
            # selects random number between 0 - 10 and converts to binary
            self.population.append({'value': bin(random.randrange(0, 10)), 'rank': 0})

    def fitness(self):
        # checks against best value yet
        for item in self.population:
            if (int(item.get('value'), 2) * int(item.get('value'), 2)) > int(self.maxVal, 2):
                self.maxVal = bin(int(item.get('value'), 2) * int(item.get('value'), 2))

        # applies fitness value
        for item in self.population:
            item['rank'] = int(item.get('value'), 2) / math.sqrt(int(self.maxVal, 2))

    def sortAndDropPercentange(self, percentToKeep):
        self.population.sort(key=operator.itemgetter('rank'))

        num = int(len(self.population) * percentToKeep)
        self.population[0:num] = []

    def crossOver(self, index):
        for i in range(0, len(self.population) - 1, 2):
            p1 = self.population[i].get('value')
            p2 = self.population[i + 1].get('value')
            child = '0b' + p2[index] + p1[index:]
            self.population.append({'value': child, 'rank': 0})
            self.keepThreshold(len(self.population)-1)


    def mutate(self, percentage):
        # mutates a percentage of the population by flipping 1 random bit in string
        mutations = []
        selectedMutations = [random.randrange(0, len(self.population) - 2) for i in range(math.floor(len(self.population) * percentage))]
        for index in selectedMutations:
            mutationIndex = random.randrange(2, len(self.population[index].get('value')) - 1)
            value = self.population[index].get('value')
            if self.population[index].get('value')[index] == '1':
                mutations.append({'value': value[:mutationIndex] + '0' + value[mutationIndex+1:], 'rank':0})
            else:
                mutations.append({'value': value[:mutationIndex] + '1' + value[mutationIndex+1:], 'rank':0})
        self.population.extend(mutations)



    # prevents string from getting above value 31
    def keepThreshold(self, index):
        if len(self.population[index].get('value')) > 7:
            rmIndex = random.randrange(2, len(self.population[index].get('value')))
            value = self.population[index].get('value')
            self.population[index]['value'] = value[:rmIndex] + value[rmIndex+1:]



