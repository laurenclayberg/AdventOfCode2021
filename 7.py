import numpy as np

locations_input = []

with open('project_files/7_puzzle1.txt', 'r') as f:
    while True:
        line = f.readline()
        if not line:
            break

        line = line.strip()
        line_split = line.split(',')
        locations_input = [int(x) for x in line_split]

# set up array of the locations
max_location = np.max(locations_input)
locations = [0 for _ in range(max_location + 1)]
for loc in locations_input:
    locations[loc] += 1

# get the cumulative fuel totals for each location
left_fuel_totals = [0 for _ in range(max_location + 1)]
left_crab_counts = [0 for _ in range(max_location + 1)]
left_crab_counts[0] = locations[0]

for i in range(1, max_location + 1):
    left_fuel_totals[i] = left_fuel_totals[i-1] + left_crab_counts[i-1]
    left_crab_counts[i] = left_crab_counts[i-1] + locations[i]

right_fuel_totals = [0 for _ in range(max_location + 1)]
right_crab_counts = [0 for _ in range(max_location + 1)]
right_crab_counts[max_location] = locations[max_location]

for i in range(max_location - 1, -1, -1):
    right_fuel_totals[i] = right_fuel_totals[i+1] + right_crab_counts[i+1]
    right_crab_counts[i] = right_crab_counts[i+1] + locations[i]

# get the best location with min fuel needed
min_value = left_fuel_totals[0] + right_fuel_totals[0]
for i in range(1, max_location + 1):
    min_value = min(min_value, left_fuel_totals[i] + right_fuel_totals[i])

print("Solution 1: ", min_value)


# get the cumulative fuel totals for each location
left_fuel_totals = [0 for _ in range(max_location + 1)]
left_fuel_add = [0 for _ in range(max_location + 1)]
left_crab_counts = [0 for _ in range(max_location + 1)]
left_crab_counts[0] = locations[0]

for i in range(1, max_location + 1):
    left_fuel_add[i] = left_fuel_add[i-1] + left_crab_counts[i-1]
    left_fuel_totals[i] = left_fuel_totals[i-1] + left_fuel_add[i]
    left_crab_counts[i] = left_crab_counts[i-1] + locations[i]

right_fuel_totals = [0 for _ in range(max_location + 1)]
right_fuel_add = [0 for _ in range(max_location + 1)]
right_crab_counts = [0 for _ in range(max_location + 1)]
right_crab_counts[max_location] = locations[max_location]

for i in range(max_location - 1, -1, -1):
    right_fuel_add[i] = right_fuel_add[i+1] + right_crab_counts[i+1]
    right_fuel_totals[i] = right_fuel_totals[i+1] + right_fuel_add[i]
    right_crab_counts[i] = right_crab_counts[i+1] + locations[i]

# get the best location with min fuel needed
min_value = left_fuel_totals[0] + right_fuel_totals[0]
for i in range(1, max_location + 1):
    min_value = min(min_value, left_fuel_totals[i] + right_fuel_totals[i])

print("Solution 2: ", min_value)