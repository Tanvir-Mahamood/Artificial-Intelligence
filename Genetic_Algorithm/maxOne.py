import random

# Problem parameters
CHROMOSOME_LENGTH = 10
POPULATION_SIZE = 6
MUTATION_RATE = 0.01 # Probability of Mutation
GENERATIONS = 50

# Fitness function: Count the number of 1s in the chromosome
def fitness(chromosome):
    return sum(chromosome)

# Generate a random chromosome
def generate_chromosome():
    return [random.randint(0, 1) for _ in range(CHROMOSOME_LENGTH)]

# Generate the initial population
def generate_population():
    return [generate_chromosome() for _ in range(POPULATION_SIZE)]

# Select parents using tournament selection
def select_parent(population):
    # sample is used to generate a specified number (k = 3) of unique random items from a sequence
    tournament = random.sample(population, k=3) 
    return max(tournament, key=fitness)

# Perform crossover between two parents
def crossover(parent1, parent2):
    point = random.randint(1, CHROMOSOME_LENGTH - 1)
    child1 = parent1[:point] + parent2[point:]
    child2 = parent2[:point] + parent1[point:]
    return child1, child2

# Mutate a chromosome based on mutation rate
def mutate(chromosome):
    return [bit if random.random() > MUTATION_RATE else 1 - bit for bit in chromosome]

# Genetic Algorithm for MaxOne problem
def genetic_algorithm():
    population = generate_population()

    for generation in range(GENERATIONS):
        # Evaluate fitness and sort population
        population = sorted(population, key=fitness, reverse=True)

        print("Current: ")
        for crom in population:
            print(crom)
            
        best_fitness = fitness(population[0])
        print(f"Generation {generation}: Best Fitness = {best_fitness}, Best Chromosome = {population[0]}")

        # Termination condition: Perfect chromosome found
        if best_fitness == CHROMOSOME_LENGTH:
            break

        # Create the next generation
        next_generation = population[:2]  # Elitism: retain top 2 individuals

        # Fill the rest of the population
        while len(next_generation) < POPULATION_SIZE:
            parent1 = select_parent(population)
            parent2 = select_parent(population)
            child1, child2 = crossover(parent1, parent2)
            next_generation.extend([mutate(child1), mutate(child2)])

        population = next_generation[:POPULATION_SIZE]

    print("Final Solution:")
    print(f"Best Chromosome: {population[0]} with Fitness: {fitness(population[0])}")

if __name__ == "__main__":
    genetic_algorithm()