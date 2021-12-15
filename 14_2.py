char_counts = {}
insert_rules = {}
cur_char_combos = {}

with open('project_files/14_puzzle1.txt', 'r') as f:
    for line in f:
        line = line.strip()
        if len(line) == 0:
            continue
        elif '-' in line:
            line_split = line.split(' -> ')
            insert_rules[line_split[0]] = line_split[1]
        else:
            for char in line:
                if char not in char_counts:
                    char_counts[char] = 0
                char_counts[char] += 1
            for i in range(len(line) - 1):
                char_combo = line[i] + line[i+1]
                if char_combo not in cur_char_combos:
                    cur_char_combos[char_combo] = 0
                cur_char_combos[char_combo] += 1

def simulate_one_step(char_counts, cur_char_combos):
    new_char_combos = {}
    for combo in cur_char_combos.keys():
        new_letter = insert_rules[combo]

        if new_letter is not None:
            count_of_new_letters = cur_char_combos[combo]

            # count all the new letters added
            if new_letter not in char_counts:
                char_counts[new_letter] = 0
            char_counts[new_letter] += count_of_new_letters

            # count new char combos
            combo_left = combo[0] + new_letter
            combo_right = new_letter + combo[1]
            if combo_left not in new_char_combos:
                new_char_combos[combo_left] = 0
            if combo_right not in new_char_combos:
                new_char_combos[combo_right] = 0
            new_char_combos[combo_left] += count_of_new_letters
            new_char_combos[combo_right] += count_of_new_letters

    return new_char_combos

NUM_STEPS = 40
for i in range(NUM_STEPS):
    cur_char_combos = simulate_one_step(char_counts, cur_char_combos)

min_count = None
max_count = None
for char in char_counts.keys():
    if min_count is None:
        min_count = char_counts[char]
        max_count = char_counts[char]
    min_count = min(char_counts[char],min_count)
    max_count = max(char_counts[char],max_count)

print("Solution:", max_count - min_count)