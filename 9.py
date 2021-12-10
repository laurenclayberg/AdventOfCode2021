import numpy as np

inputs = []

with open('project_files/9_puzzle1.txt', 'r') as f:
    while True:
        line = f.readline()
        if not line:
            break

        line = list(line.strip())
        inputs.append([int(x) for x in line])

numpy_inputs = np.asarray(inputs)
padded_input = np.pad(numpy_inputs, (1,1), 'constant', constant_values=(100,100))

mask = np.zeros(numpy_inputs.shape)

for i in range(1,padded_input.shape[0]-1):
    for j in range(1,padded_input.shape[1]-1):
        cur_val = padded_input[i,j]
        top = padded_input[i-1,j]
        bottom = padded_input[i+1,j]
        left = padded_input[i,j-1]
        right = padded_input[i,j+1]
        if np.min([cur_val, top, bottom, left, right]) == cur_val and cur_val not in [top, bottom, left, right]:
            mask[i-1,j-1] = 1

solution_1 = np.sum((numpy_inputs * mask) + np.ones(numpy_inputs.shape) * mask)
print("Solution 1: ", solution_1)

def get_basin_size(heights, i, j, explored, basin):
    def verify_basin_explore(heights, i, j, explored, basin):
        if i < 0 or j < 0 or i > heights.shape[0] - 1 or j > heights.shape[1] - 1:
            return
        # helper for the below
        if (heights[i,j] < 9 and basin[i,j] == 0):
            basin[i,j] = 1
        if (basin[i,j] == 1 and explored[i,j] == 0):
            explored[i,j] = 1
            get_basin_size(heights, i, j, explored, basin)

    # mark current spot as explored
    explored[i,j] = 1
    # for up down left right if not yet in basin, add and mark,
    # explore all parts of basin that aren't explored
    verify_basin_explore(heights, i-1, j, explored, basin)
    verify_basin_explore(heights, i+1, j, explored, basin)
    verify_basin_explore(heights, i, j-1, explored, basin)
    verify_basin_explore(heights, i, j+1, explored, basin)
    # return basin size when the recursion finishes
    return np.sum(basin) 

basin_sizes = []
for i in range(0,mask.shape[0]):
    for j in range(0,mask.shape[1]):
        if mask[i,j] == 1:
            basin_sizes.append(get_basin_size(numpy_inputs, i, j, np.zeros(numpy_inputs.shape), np.zeros(numpy_inputs.shape)))

top_values = sorted(basin_sizes)
solution_2 = top_values[-1] * top_values[-2] * top_values[-3]
print("Solution 2: ", solution_2)
