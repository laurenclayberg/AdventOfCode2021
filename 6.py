import numpy as np

input_fish = []

with open('project_files/6_puzzle1.txt', 'r') as f:
    while True:
        line = f.readline()
        if not line:
            break

        line = line.strip()
        line_split = line.split(',')
        input_fish = [int(x) for x in line_split]

# Part 1

fish = np.asarray(input_fish)

num_rounds = 80
for i in range(num_rounds - 1):
    fish = fish - 1
    new_fish = np.sum(fish == 0)
    # list adjustments are 1 higher because the first step of the loop
    # is to subtract 1
    fish[fish == 0] = 7
    fish = np.append(fish, 9*np.ones(new_fish))

print("Solution 1: ", fish.shape[0])

# Part 2

# 0 through 6 are valid ages for non-new fish
fish_cohorts = [0 for _ in range(7)] 
for fish_age in input_fish:
    fish_cohorts[fish_age] += 1
fish_count_7 = 0
fish_count_8 = 0

current_cohort = 0 # index of fish currently 0 value
new_fish_next_round = fish_cohorts[0]
num_rounds = 256
for i in range(256):
    # make sure state is right
    current_cohort = (current_cohort + 1) % 7
    fish_cohorts[current_cohort - 1] += fish_count_7 # prev 7s get added to cohorts
    fish_count_7 = fish_count_8# 8s become 7s
    fish_count_8 = new_fish_next_round # new fish become 8s

    # set up next round
    new_fish_next_round = fish_cohorts[current_cohort]

print("Solution 2: ", np.sum(fish_cohorts) + fish_count_7 + fish_count_8)