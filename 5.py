import numpy as np

grid = np.zeros((1000,1000))
grid2 = np.zeros((1000,1000))

with open('project_files/5_puzzle1.txt', 'r') as f:
    while True:
        line = f.readline()
        if not line:
            break

        line = line.strip()
        line_split = line.split(' -> ')
        x1,y1 = line_split[0].split(',')
        x2,y2 = line_split[1].split(',')

        if int(x1) == int(x2) or int(y1) == int(y2):
            min_x = min(int(x1), int(x2))
            max_x = max(int(x1), int(x2)) + 1 # inclusive
            min_y = min(int(y1), int(y2))
            max_y = max(int(y1), int(y2)) + 1 # inclusive
            grid[min_x:max_x,min_y:max_y] += 1
            grid2[min_x:max_x,min_y:max_y] += 1
        else:
            skip_x = 1 if int(x1) < int(x2) else -1
            skip_y = 1 if int(y1) < int(y2) else -1
            x1 = int(x1)
            x2 = int(x2) - 1 if int(x2) < int(x1) else int(x2) + 1
            y1 = int(y1)
            y2 = int(y2) - 1 if int(y2) < int(y1) else int(y2) + 1
            grid2[np.arange(x1, x2, skip_x), np.arange(y1, y2, skip_y)] += 1

print("Solution 1: ", np.sum(grid > 1))
print("Solution 2: ", np.sum(grid2 > 1))
