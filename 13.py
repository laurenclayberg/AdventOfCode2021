import numpy as np

x_coords = []
y_coords = []

fold_axis = []
fold_line = []

with open('project_files/13_puzzle1.txt', 'r') as f:
    for line in f:
        line = line.strip()
        if len(line) == 0:
            continue
        elif ',' in line:
            line_split = line.split(',')
            x_coords.append(int(line_split[0]))
            y_coords.append(int(line_split[1]))
        else:
            fold = line.split()[2]
            fold_split = fold.split('=')
            fold_axis.append(fold_split[0])
            fold_line.append(int(fold_split[1]))

x_size = max(x_coords)
y_size = max(y_coords)

# create and mark the grid
grid = np.zeros((y_size+1,x_size+1), np.bool)
for i in range(len(x_coords)):
    grid[y_coords[i],x_coords[i]] = 1

# perform the folds
def flip_horizontal(grid, fold):
    grid_left = grid[:,:fold]
    grid_right = grid[:,fold+1:]
    width_left = grid_left.shape[1]
    width_right = grid_right.shape[1]

    grid_right_flip = np.fliplr(grid_right)

    if width_left == width_right:
        base = grid_left
        top = grid_right_flip
    elif width_left > width_right:
        np_pad = ((0, 0),(width_left - width_right,0))
        base = grid_left
        top = np.pad(grid_right_flip, pad_width=np_pad, mode='constant', constant_values=0)
    else:
        np_pad = ((0, 0),(width_right - width_left,0))
        base = grid_right_flip
        top = np.pad(grid_left, pad_width=(width_right - width_left,0), mode='constant', constant_values=0)

    return base + top

def flip_vertical(grid, fold):
    grid_top = grid[:fold,:]
    grid_bottom = grid[fold+1:,:]
    width_top = grid_top.shape[0]
    width_bottom = grid_bottom.shape[0]

    grid_bottom_flip = np.flipud(grid_bottom)

    if width_top == width_bottom:
        base = grid_top
        top = grid_bottom_flip
    elif width_top > width_bottom:
        np_pad = ((width_top - width_bottom,0),(0, 0))
        base = grid_top
        top = np.pad(grid_bottom_flip, pad_width=np_pad, mode='constant', constant_values=0)
    else:
        np_pad = ((width_bottom - width_top,0),(0, 0))
        base = grid_bottom_flip
        top = np.pad(grid_top, pad_width=np_pad, mode='constant', constant_values=0)

    return base + top

# part 1
grid_1 = np.copy(grid)
if fold_axis[0] == 'y':
    grid_1 = flip_vertical(grid_1, fold_line[0])
else:
    grid_1 = flip_horizontal(grid_1, fold_line[0])

print("Solution 1: ", np.sum(grid_1))

# part 2
grid_2 = np.copy(grid)
for i in range(len(fold_axis)):
    if fold_axis[i] == 'y':
        grid_2 = flip_vertical(grid_2, fold_line[i])
    else:
        grid_2 = flip_horizontal(grid_2, fold_line[i])

print("Solution 2: ")
for row in grid_2:
    row_str = ""
    for i in row:
        if i == 0:
            row_str = row_str + '.'
        else:
            row_str = row_str + '#'
    print(row_str)
