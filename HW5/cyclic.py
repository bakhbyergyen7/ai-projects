import random

def fitness(state):
    conflicts = 0
    for i in range(len(state)):
        for j in range(i+1, len(state)):
            if state[i] == state[j] or abs(i-j) == abs(state[i]-state[j]):
                conflicts += 1
    return 28 - conflicts

def solve_cyclic():
    state = [random.randint(0, 7) for _ in range(8)]
    evaluations = 1
    while True:
        for col in range(8):
            conflicts = [0] * 8
            for i in range(8):
                conflicts[i] = sum(1 for j in range(8) if state[j] == i or abs(j-col) == abs(i-state[j]))
            min_conflicts = min(conflicts)
            options = [i for i in range(8) if conflicts[i] == min_conflicts]
            row = random.choice(options)
            if conflicts[row] == 0:
                state[col] = row
                evaluations += 1
                f = fitness(state)
                if f == 28:
                    return state, evaluations
                break
        else:
            return None, evaluations

random.seed(42)
solution, evaluations = solve_cyclic()
print(solution, evaluations)
