import random

CHROMOSOME_LENGTH = 10
POPULATION_SIZE = 12
NO_MEMBER = 3
NO_GROUP = int(POPULATION_SIZE / NO_MEMBER)
MUTATION_RATE = 0.01

def fitness(chromosome):
    return sum(chromosome)

def generate_chromosome():
    return [random.randint(0, 1) for _ in range(CHROMOSOME_LENGTH)]

def generate_population():
    return [generate_chromosome() for _ in range(POPULATION_SIZE)]

def selection(population):
    tournament = random.sample(population, k=NO_MEMBER) 
    return max(tournament, key=fitness)

def crossover(parent1, parent2):
    point = random.randint(1, CHROMOSOME_LENGTH - 1)
    child1 = parent1[:point] + parent2[point:]
    child2 = parent2[:point] + parent1[point:]
    return child1, child2

def mutation(chromosome):
    return [bit if random.random() > MUTATION_RATE else 1 - bit for bit in chromosome]


def genetic_algorithm():
    population = generate_population()
    selected_population = []
    crossed_population = []

    print("------------------------------")
    print("Step-1 and Step-2: Population Generation and Fitness")
    for i in population:
        print(f"{i} Fitness = {fitness(i)}")

    print("------------------------------")
    print("Step-3: Selection")
    for _ in range(NO_GROUP):
        selected_population.append(selection(population))
    
    for i in selected_population:
        print(i)
    

    print("------------------------------")
    print("Step-4: Crossover")
    idx = random.sample(range(0, NO_GROUP), 2)
    idx1, idx2 = idx[0], idx[1]
    # print(idx1)
    # print(idx2)
    child1, child2 = crossover(selected_population[idx1], selected_population[idx2])
    # print(child1)
    # print(child2)
    for i in range(len(selected_population)):
        if i == idx1:
            crossed_population.append(child1)
        elif i == idx2:
            crossed_population.append(child2)
        else:
            crossed_population.append(selected_population[i])
    
    
    for i in crossed_population:
        print(i)

    print("------------------------------")
    print("Step-5: Mutation")
    idx = random.sample(range(1, NO_GROUP+1), 1)
    idx1 = idx[0] - 1
    for i in range(len(crossed_population)):
        if i == idx1:
            crossed_population[i] = mutation(crossed_population[i])

    print(len(selected_population))
    for i in crossed_population:
        print(i)

if __name__ == "__main__":
    genetic_algorithm()