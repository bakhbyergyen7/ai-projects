from queue import Queue
import numpy as np

def bfs(grid, start, goal):
    n, m = len(grid), len(grid[0])
    q = Queue()
    q.put(start)
    visited = set()
    path = {}
    closed_set = set()
    while not q.empty():
        curr = q.get()
        if curr == goal:
            return construct_path(path, goal, start), len(closed_set), len(q.queue) + len(closed_set),
        i, j = curr
        neighbors = [(i + 1, j), (i - 1, j), (i, j + 1), (i, j - 1)]
        closed_set.add(curr)
        for neighbor in neighbors:
            ni, nj = neighbor
            if 0 <= ni < n and 0 <= nj < m and grid[ni][nj] == 0:
                if neighbor not in visited:
                    visited.add(neighbor)
                    q.put(neighbor)
                    path[neighbor] = curr
    return None

def construct_path(path, goal, start):
    curr = goal
    shortest_path = [goal]
    while curr != start:
        curr = path[curr]
        shortest_path.append(curr)
    shortest_path.reverse()
    return len(shortest_path)

# Testing on the example given in part b
grid = np.zeros((100, 100));
goal = (50, 55)
start = (75, 70)

result = bfs(grid, start, goal)

if result:
    print("Shortest path length:", result[0])
    print("Number of cells in closed set:", result[1])
    print("Number of cells on fringe:", result[2])
else:
    print("No path found")
