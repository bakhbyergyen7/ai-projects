import numpy as np

def gbfs(grid, start, goal):
    m, n = len(grid), len(grid[0])
    queue = [start]
    visited = set()
    parent = dict()
    closed_set_count = 0
    fringe_count = 1
    while queue:
        current = queue.pop(0)
        if current in visited:
            continue
        visited.add(current)
        closed_set_count += 1
        if current == goal:
            return construct_path(parent, current), closed_set_count, fringe_count
        for move in moves:
            x, y = current
            x2, y2 = x + move[0], y + move[1]
            if x2 >= 0 and x2 < m and y2 >= 0 and y2 < n and grid[x2][y2] == 0 and (x2, y2) not in visited:
                parent[(x2, y2)] = current
                h = manhattan_distance(goal, (x2, y2))
                queue = insert_in_order(queue, (x2, y2), h)
                fringe_count += 1
    return None, closed_set_count, fringe_count

def manhattan_distance(goal, current):
    return abs(goal[0] - current[0]) + abs(goal[1] - current[1])

def insert_in_order(queue, node, heuristic_value):
    for i, n in enumerate(queue):
        if manhattan_distance(goal, n) > heuristic_value:
            queue.insert(i, node)
            return queue
    queue.append(node)
    return queue

def construct_path(parent, current):
    path = [current]
    while current in parent:
        current = parent[current]
        path.append(current)
    path.reverse()
    return path

moves = [(0, 1), (0, -1), (1, 0), (-1, 0)]

# Testing on the example given in part b
grid = np.zeros((100, 100));
goal = (50, 55)
start = (75, 70)
shortest_path, closed_set_count, fringe_count = gbfs(grid, start, goal)

if shortest_path:
    print("Shortest path:", len(shortest_path))
    print("Number of cells in closed set:", closed_set_count)
    print("Number of cells in fringe:", fringe_count)
else:
    print("No path found")
