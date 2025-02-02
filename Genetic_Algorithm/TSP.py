import random
import numpy as np

# Problem parameters
NUM_CITIES = 10
POPULATION_SIZE = 20
GENERATIONS = 50
MUTATION_RATE = 0.2

# Generate random coordinates for cities
cities = np.random.rand(NUM_CITIES, 2) * 100
print(cities)

# Calculate Euclidean distance between two cities
def distance(city1, city2):
    return np.linalg.norm(city1 - city2)

# Compute the total distance of the tour
def fitness(chromosome):
    dist = sum(distance(cities[chromosome[i]], cities[chromosome[i + 1]]) for i in range(len(chromosome) - 1))
    dist += distance(cities[chromosome[-1]], cities[chromosome[0]])  # Return to start
    return 1 / dist  # Inverse of distance since GA maximizes fitness

# Generate a random chromosome (random tour)
def generate_chromosome():
    chromosome = list(range(NUM_CITIES))
    random.shuffle(chromosome)
    return chromosome

# Generate the initial population
def generate_population():
    return [generate_chromosome() for _ in range(POPULATION_SIZE)]

# Select parents using tournament selection
def select_parent(population):
    tournament = random.sample(population, k=3)
    return max(tournament, key=fitness)

# Perform Order Crossover (OX)
def crossover(parent1, parent2):
    size = len(parent1)
    start, end = sorted(random.sample(range(size), 2))

    child = [None] * size
    child[start:end] = parent1[start:end]

    pointer = 0
    for city in parent2:
        if city not in child:
            while child[pointer] is not None:
                pointer += 1
            child[pointer] = city

    return child

# Perform swap mutation
def mutate(chromosome):
    if random.random() < MUTATION_RATE:
        i, j = random.sample(range(len(chromosome)), 2)
        chromosome[i], chromosome[j] = chromosome[j], chromosome[i]
    return chromosome

# Genetic Algorithm for TSP
def genetic_algorithm():
    population = generate_population()

    for generation in range(GENERATIONS):
        # Evaluate fitness and sort population
        population = sorted(population, key=fitness, reverse=True)
        best_fitness = fitness(population[0])
        best_distance = 1 / best_fitness
        print(f"Generation {generation}: Best Distance = {best_distance:.2f}, Best Tour = {population[0]}")

        # Create the next generation
        next_generation = population[:2]  # Elitism: retain top 2 individuals

        # Fill the rest of the population
        while len(next_generation) < POPULATION_SIZE:
            parent1 = select_parent(population)
            parent2 = select_parent(population)
            child = crossover(parent1, parent2)
            next_generation.append(mutate(child))

        population = next_generation

    # Final solution
    best_solution = population[0]
    best_distance = 1 / fitness(best_solution)
    print("Final Solution:")
    print(f"Best Tour: {best_solution}, Distance: {best_distance:.2f}")
    

if __name__ == "__main__":
    genetic_algorithm()
