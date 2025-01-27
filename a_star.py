import numpy as np

def a_star(grid, start, goal):
    rows, cols = grid.shape
    g_values = np.full((rows, cols), np.inf)
    f_values = np.full((rows, cols), np.inf)
    parents = np.full((rows, cols), -1, dtype=np.int32)
    f_values[start[0], start[1]] = 0
    g_values[start[0], start[1]] = 0

    directions = [(0, -1), (0, 1), (-1, 0), (1, 0)]
    open_list = [start]

    closed_set = []
    path_length = 0
    fringe_size = len(open_list)

    while open_list:
        curr_pos = open_list.pop(np.argmin(f_values[tuple(np.array(open_list).T)]))
        closed_set.append(curr_pos)
        fringe_size = len(open_list)

        if tuple(curr_pos) == goal:
            path = [goal]
            while tuple(curr_pos) != start:
                curr_pos = np.array(np.unravel_index(parents[curr_pos[0], curr_pos[1]], (rows, cols)))
                path.append(tuple(curr_pos))
            path_length = len(path)
            return list(reversed(path)), len(closed_set), fringe_size, path_length

        for direction in directions:
            new_pos = [curr_pos[0] + direction[0], curr_pos[1] + direction[1]]
            if (new_pos[0] >= 0 and new_pos[0] < rows and
                new_pos[1] >= 0 and new_pos[1] < cols and
                grid[new_pos[0], new_pos[1]] == 0 and
                g_values[new_pos[0], new_pos[1]] == np.inf):
                g_values[new_pos[0], new_pos[1]] = g_values[curr_pos[0], curr_pos[1]] + 1
                f_values[new_pos[0], new_pos[1]] = g_values[new_pos[0], new_pos[1]] + abs(new_pos[0] - goal[0]) + abs(new_pos[1] - goal[1])
                open_list.append(new_pos)
                parents[new_pos[0], new_pos[1]] = np.ravel_multi_index(curr_pos, (rows, cols))

    return [], len(closed_set), fringe_size, path_length

grid = np.zeros((100, 100));
goal = (50, 55)
start = (75, 70)

shortest_path = a_star(grid, start, goal)

if shortest_path:
    print("Shortest path:", shortest_path)
else:
    print("No path found")