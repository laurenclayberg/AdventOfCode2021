import numpy as np

grid_list = []

with open('project_files/15_puzzle1.txt', 'r') as f:
    for line in f:
        line = line.strip()
        grid_list.append([int(x) for x in line])

grid = np.asarray(grid_list)
grid_sums = np.zeros(grid.shape, np.int32)

for i in range(grid.shape[0]): # vertical
    for j in range(grid.shape[0]): # horizontal
        if i == 0 and j == 0:
            grid_sums[i,j] = 0
        elif i == 0:
            grid_sums[i,j] = grid_sums[i,j-1] + grid[i,j]
        elif j == 0:
            grid_sums[i,j] = grid_sums[i-1,j] + grid[i,j]
        else:
            grid_sums[i,j] = min(grid_sums[i,j-1], grid_sums[i-1,j]) + grid[i,j]

print("Solution 1:", grid_sums[i,j])

# Part 2

grid_template = np.copy(grid)
grid_extend = np.copy(grid)

for i in range(1,5):
    grid_template = grid_template + 1
    grid_template = np.mod(grid_template, np.zeros(grid_template.shape, np.int32) + 10)
    grid_mask = grid_template == 0
    grid_template = grid_template + grid_mask
    grid_extend = np.concatenate((grid_extend, grid_template), axis=0)

grid_template = np.copy(grid_extend)

for i in range(1,5):
    grid_template = grid_template + 1
    grid_template = np.mod(grid_template, np.zeros(grid_template.shape, np.int32) + 10)
    grid_mask = grid_template == 0
    grid_template = grid_template + grid_mask
    grid_extend = np.concatenate((grid_extend, grid_template), axis=1)

grid_extend = np.mod(grid_extend, np.zeros(grid_extend.shape, np.int32) + 10)
grid_mask = grid_extend == 0

grid_extend = grid_extend + grid_mask

import networkx as nx

graph = nx.DiGraph()

for i in range(grid_extend.shape[0]):
    for j in range(grid_extend.shape[1]):
        graph.add_node((i,j))

for i in range(grid_extend.shape[0]):
    for j in range(grid_extend.shape[1]):
        w = grid_extend[i,j]

        if i - 1 >= 0:
            graph.add_edge((i-1,j), (i,j), weight=w)
        if i + 1 < grid_extend.shape[0]:
            graph.add_edge((i+1,j), (i,j), weight=w)
        if j - 1 >= 0:
            graph.add_edge((i,j-1), (i,j), weight=w)
        if j + 1 < grid_extend.shape[1]:
            graph.add_edge((i,j+1), (i,j), weight=w)

sol_2 = nx.shortest_path_length(graph, source=(0,0), target=(grid_extend.shape[0]-1,grid_extend.shape[1]-1), weight='weight')

print("Solution 2:", sol_2)
