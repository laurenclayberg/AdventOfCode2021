# Parse input

import re
with open('project_files/17_puzzle1.txt', 'r') as f:
    for line in f:
        numbers = re.findall(r"[-]?[\d']+", line)

min_x = int(numbers[0])
max_x = int(numbers[1])
min_y = int(numbers[2])
max_y = int(numbers[3])

# Simulate 1 step

def simulate_step(x_pos, y_pos, x_vel, y_vel):
    x_pos += x_vel
    y_pos += y_vel

    if x_vel > 0:
        x_vel -= 1
    elif x_vel < 0:
        x_vel += 1

    y_vel -= 1

    return x_pos, y_pos, x_vel, y_vel

# Verify starting position

def position_is_valid(x_vel, y_vel, debug=False):
    if debug:
        print("starting veolcity", x_vel, y_vel)
    valid = False 
    max_height = 0
    x_pos = 0
    y_pos = 0
    while x_pos <= max_x and y_pos >= min_y and valid == False:
        x_pos, y_pos, x_vel, y_vel = simulate_step(x_pos, y_pos, x_vel, y_vel)

        if debug:
            print(x_pos, y_pos)

        if x_pos >= min_x and x_pos <= max_x and y_pos >= min_y and y_pos <= max_y:
            valid = True 
        
        max_height = max(max_height, y_pos)
    return valid, max_height

# Check starting velocities

solution_max_height = 0
solution_total_valid_positions = 0
solution_positions = set()
for x in range(max_x+3):
    for y in range(min_y*2, max_x*2):
        valid, max_height = position_is_valid(x, y)

        if valid:
            solution_max_height = max(solution_max_height, max_height)
            solution_total_valid_positions += 1
            solution_positions.add((x,y))

print("Solution 1:", solution_max_height)
print("Solution 2:", solution_total_valid_positions)
