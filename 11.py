import numpy as np

with open('project_files/11_puzzle1.txt', 'r') as f:
    energy_levels = np.array([[int(x) for x in line.strip()] for line in f])
    energy_levels_2 = np.copy(energy_levels)

def simulate_step(energy_levels):
    flash_mask = np.ones(energy_levels.shape, np.bool)
    energy_levels = energy_levels + 1

    while np.any(energy_levels > 9 * flash_mask):
        flash_current = energy_levels > 9 * flash_mask # find next to flash
        flash_mask[energy_levels > 9] = 0 # mark all flashed this step
        max_x = energy_levels.shape[0]
        max_y = energy_levels.shape[1]
        for i in range(energy_levels.shape[0]):
            for j in range(energy_levels.shape[1]):
                if flash_current[i,j]: # add 1 all around the one flashing
                    energy_levels[max(0,i-1):min(i+2,max_x),max(j-1,0):min(j+2,max_y)] += 1
        energy_levels[~flash_mask] = 0 # set all the ones that flashed to 0

    unique, counts = np.unique(flash_mask, return_counts=True)
    counts = dict(zip(unique, counts))
    if 0 in counts:
        return (counts[0], energy_levels)
    return (0, energy_levels)

NUM_STEPS = 100
count_flashes = 0
for i in range(NUM_STEPS):
    new_flashes, energy_levels = simulate_step(energy_levels)
    count_flashes += new_flashes

print("Solution 1: ", count_flashes)

count_steps = 0
while True:
    count_steps += 1
    flashes, energy_levels_2 = simulate_step(energy_levels_2)
    if flashes == (energy_levels_2.shape[0] * energy_levels_2.shape[1]):
        break

print("Solution 2: ", count_steps)