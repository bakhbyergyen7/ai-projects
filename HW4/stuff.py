import random
import math

# Define the fitness function to be maximized
def fitness(x):
    return 4 + 2*x + 2*math.sin(20*x) - 4*x*x

# Define the mutation function (x +/- epsilon)
def mutate(x, epsilon):
    r = random.random()
    if r < 0.3:
        return max(0, min(1, x - epsilon))  # x - epsilon
    elif r < 0.7:
        return x  # copy
    else:
        return max(0, min(1, x + epsilon))  # x + epsilon

# Define the crossover function (convex combination of two individuals)
def crossover(x, y, a):
    return a*x + (1-a)*y

# Define the parameters for the experiment
N = 10  # population size
epsilon = 0.01  # mutation step size
num_generations = 1000  # number of generations to run
a_range = (0, 1)  # range of values for a in crossover

# Define the initial population
population = [0.01*k for k in range(101)]
random.shuffle(population)
population = population[:N]

# Run the optimization loop
for generation in range(num_generations):
    # Evaluate the fitness of each individual in the population
    fitnesses = [fitness(x) for x in population]

    # Choose parents for the next generation using roulette selection
    total_fitness = sum(fitnesses)
    parent_probs = [f/total_fitness for f in fitnesses]
    parents = random.choices(population, weights=parent_probs, k=N)

    # Apply crossover and mutation to create the next generation
    next_gen = []
    for i in range(N):
        parent1, parent2 = random.sample(parents, 2)
        a = random.uniform(*a_range)
        child = crossover(parent1, parent2, a)
        child = mutate(child, epsilon)
        next_gen.append(child)

    # Clip individuals to the interval [0, 1]
    next_gen = [max(0, min(1, x)) for x in next_gen]

    # Update the population
    population = next_gen

# Find the best individual and its fitness
best_idx = max(range(N), key=lambda i: fitnesses[i])
best_fitness = fitnesses[best_idx]
best_individual = population[best_idx]

# Print the results
print(f"Best individual: {best_individual}")
print(f"Best fitness: {best_fitness}")
