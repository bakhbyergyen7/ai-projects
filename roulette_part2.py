# Part 2: Crossover was added

import random
import math

# Set up the optimization problem
def fitness(x):
    return 4 + 2*x + 2*math.sin(20*x) - 4*x*x

# Set up the optimization algorithm
epsilon = 0.01
pop_size = 10
max_generations = 100

population = [i*epsilon for i in range(pop_size)]
for gen in range(max_generations):
    new_population = []
    total_fitness = sum(fitness(x) for x in population)
    for i in range(pop_size):
        parent1 = random.choices(population, weights=[fitness(x)/total_fitness for x in population], k=1)[0]
        parent2 = random.choices(population, weights=[fitness(x)/total_fitness for x in population], k=1)[0]
        a = random.random()
        x = a*parent1 + (1-a)*parent2
        x_mutated = random.choices([x-epsilon, x, x+epsilon], weights=[0.3, 0.4, 0.3], k=1)[0]
        x_mutated = max(0, min(1, x_mutated))
        if fitness(x_mutated) > fitness(x):
            x = x_mutated
        new_population.append(x)
    population = new_population

# Get the best individual and its fitness
best_ind = max(population, key=fitness)
best_fitness = fitness(best_ind)
print("Best individual:", best_ind)
print("Best fitness:", best_fitness)
