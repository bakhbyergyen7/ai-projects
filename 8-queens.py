import random

# Returns the fitness score of the state
def fitness(state):
    attacks = 0
    for i in range(8):
        for j in range(i+1, 8):
            if state[i] == state[j]:
                attacks += 1
            offset = j - i
            if state[i] == state[j] - offset or state[i] == state[j] + offset:
                attacks += 1
    return 28 - attacks

# Returns a random initial state
def random_state():
    return [random.randint(0, 7) for _ in range(8)]

# Returns a random neighbor of the given state
def random_neighbor(state):
    neighbor = list(state)
    i = random.randint(0, 7)
    j = random.randint(0, 7)
    while j == state[i]:
        j = random.randint(0, 7)
    neighbor[i] = j
    return neighbor

# Solves the 8-Queens problem using Random-restart Hill Climbing
def solve():
    evaluations = 0
    while True:
        state = random_state()
        while True:
            neighbor = random_neighbor(state)
            if fitness(neighbor) > fitness(state):
                state = neighbor
            else:
                break
            evaluations += 1
            if fitness(state) == 28:
                print("Solution found: " + "".join(str(q) for q in state))
                print("Number of fitness evaluations: " + str(evaluations))
                return
# Runs the solve() function 100 times and records the number of evaluations required to find a solution
num_evaluations = []
for i in range(100):
    evaluations = 0
    while True:
        state = random_state()
        for j in range(10000):
            neighbor = random_neighbor(state)
            if fitness(neighbor) > fitness(state):
                state = neighbor
            evaluations += 1
            if fitness(state) == 28:
                num_evaluations.append(evaluations)
                break
        if len(num_evaluations) == i+1:
            break

# Computes the average number of evaluations required to find a solution
average_evaluations = sum(num_evaluations) / len(num_evaluations)
print("Average number of evaluations: " + str(average_evaluations))
print("State: ", state)