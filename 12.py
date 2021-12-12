cave_paths = {}
small_caves = 'abcdefghijklmnopqrstuvwxyz'

def all_path_to_cave(key, value):
    if key not in cave_paths:
        cave_paths[key] = []
    cave_paths[key].append(value)

with open('project_files/12_puzzle1.txt', 'r') as f:
    for line in f:
        first, second = line.strip().split('-')

        if first == 'start':
            all_path_to_cave(first, second)
        elif second == 'start':
            all_path_to_cave(second, first)
        elif first == 'end':
            all_path_to_cave(second, first)
        elif second == 'end':
            all_path_to_cave(first, second)
        else:
            all_path_to_cave(first, second)
            all_path_to_cave(second, first)

def find_all_paths(current_loc, prev_paths):
    next_loc_options = cave_paths[current_loc]

    all_new_paths = []
    for next_loc in next_loc_options:
        is_small_cave = next_loc[0] in small_caves

        new_paths = [x + ',' + next_loc for x in prev_paths if not is_small_cave or next_loc not in x]
        if len(new_paths) == 0:
            continue

        if next_loc != 'end':
            new_paths = find_all_paths(next_loc, set(new_paths))
        all_new_paths.extend(new_paths)

    return set(all_new_paths)

solution_1_paths = find_all_paths('start', set(['start']))
solution_1 = len(solution_1_paths)
print("Solution 1: ", solution_1)

def find_all_paths_2(current_loc, prev_paths, doubled_small_cave):
    next_loc_options = cave_paths[current_loc]

    all_new_paths = []
    for next_loc in next_loc_options:
        is_small_cave = next_loc[0] in small_caves

        if next_loc == 'end':
            new_paths = [x + ',end' for x in prev_paths]
        elif is_small_cave:
            if doubled_small_cave: # we already saw a small cave twice
                new_paths = [x + ',' + next_loc for x in prev_paths if next_loc not in x]
                if len(new_paths) == 0:
                    continue
                new_paths = find_all_paths_2(next_loc, set(new_paths), doubled_small_cave)
            else: # we have not yet seen a small cave twice
                new_paths = []
                new_paths_no_doup = [x + ',' + next_loc for x in prev_paths if next_loc not in x]
                if len(new_paths_no_doup) != 0:
                    new_paths.extend(find_all_paths_2(next_loc, set(new_paths_no_doup), False))
                new_paths_with_doup = [x + ',' + next_loc for x in prev_paths]
                new_paths.extend(find_all_paths_2(next_loc, set(new_paths_with_doup), True))
        else:
            new_paths = [x + ',' + next_loc for x in prev_paths]
            new_paths = find_all_paths_2(next_loc, set(new_paths), doubled_small_cave)

        all_new_paths.extend(new_paths)

    return set(all_new_paths)

solution_2_paths = find_all_paths_2('start', set(['start']), False)
solution_2 = len(solution_2_paths)
print("Solution 2: ", solution_2)