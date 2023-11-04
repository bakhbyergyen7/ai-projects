import random

# Function to check if two queens are attacking each other
def is_attacking(x1, y1, x2, y2):
    return x1 == x2 or y1 == y2 or abs(x1 - x2) == abs(y1 - y2)

# Function to count the number of non-attacking pairs of queens
def count_non_attacking_pairs(board):
    count = 0
    n = len(board)
    for i in range(n):
        for j in range(i+1, n):
            if not is_attacking(i, board[i], j, board[j]):
                count += 1
    return count

# Function to choose the variable based on the algorithm type
def choose_variable(board, algorithm_type):
    if algorithm_type == "random":
        return random.randint(0, len(board)-1)
    elif algorithm_type == "cyclic":
        # Choose the next variable based on the variable with the most conflicts
        n = len(board)
        conflicts = [0] * n
        for i in range(n):
            for j in range(n):
                if i != j and is_attacking(i, board[i], j, board[j]):
                    conflicts[i] += 1
        current_variable = board.index(max(board)) % n
        for i in range(1, n):
            next_variable = (current_variable + i) % n
            if conflicts[next_variable] > conflicts[current_variable]:
                return next_variable
        return current_variable


# Function to find the value that minimizes the conflicts
def min_conflicts_value(variable, board):
    n = len(board)
    min_conflicts = n
    min_values = []
    for value in range(n):
        conflicts = 0
        for j in range(n):
            if j != variable and is_attacking(variable, value, j, board[j]):
                conflicts += 1
        if conflicts < min_conflicts:
            min_conflicts = conflicts
            min_values = [value]
        elif conflicts == min_conflicts:
            min_values.append(value)
    return random.choice(min_values)

# Function to apply the min-conflicts algorithm
def min_conflicts(board, algorithm_type, max_steps):
    for i in range(max_steps):
        fitness = count_non_attacking_pairs(board)
        if fitness == 28:
            return board, i
        variable = choose_variable(board, algorithm_type)
        value = min_conflicts_value(variable, board)
        board[variable] = value
    return None, max_steps

# Function to print the board as a string of digits
def print_board(board):
    print("".join(str(i) for i in board))

# Main function
if __name__ == "__main__":
    n = 8  # Board size
    max_steps = 10000  # Maximum number of steps
    algorithm_type = input("Enter algorithm type (random or cyclic): ")
    evaluations = []
    for i in range(100):
        board = [i for i in range(n)]
        random.shuffle(board)  # Random initial assignment
        solution, steps = min_conflicts(board, algorithm_type, max_steps)
        if solution is None:
            print("Failed to find a solution after", steps, "steps.")
        else:
            print_board(solution)
            print("Found a solution after", steps, "steps.")
            evaluations.append(steps)

    print("Average number of evaluations:", sum(evaluations) / len(evaluations))
    print("Successful (out of 100): ",len(evaluations))