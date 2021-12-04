count_numbers = 0
vertical_sums = None
all_numbers = []

with open('project_files/3_puzzle1.txt', 'r') as f:
    while True:
        line = f.readline()
        if line == " ":
            continue
        if not line:
            break
        line = line.strip()
        all_numbers.append(line)

        if vertical_sums == None:
            vertical_sums = [0 for i in range(len(line))]
        for c in range(len(line)):
            vertical_sums[c] += int(line[c])
        count_numbers += 1

gamma_rate = ''
epsilon_rate = ''
for s in vertical_sums:
    if s >= count_numbers / 2:
        gamma_rate += '1'
        epsilon_rate += '0'
    else:
        gamma_rate += '0'
        epsilon_rate += '1'

print("Solution part 1")
print (int(gamma_rate, 2) * int(epsilon_rate, 2))

length_binary = len(vertical_sums)
oxygen_generator_rating = None
co2_scrubber_rating = None

candidates = all_numbers
for i in range(length_binary):
    if len(candidates) == 1:
        break
    temp_a = []
    temp_b = []
    for c in candidates:
        if c[i] == '1':
            temp_a.append(c)
        else:
            temp_b.append(c)
    if len(temp_a) >= len(temp_b):
        candidates = temp_a
    else:
        candidates = temp_b
oxygen_generator_rating = candidates[0]

candidates = all_numbers
for i in range(length_binary):
    if len(candidates) == 1:
        break
    temp_a = []
    temp_b = []
    for c in candidates:
        if c[i] == '1':
            temp_a.append(c)
        else:
            temp_b.append(c)
    if len(temp_a) >= len(temp_b):
        candidates = temp_b
    else:
        candidates = temp_a
co2_scrubber_rating = candidates[0]

print("Solution part 2")
print (int(oxygen_generator_rating, 2) * int(co2_scrubber_rating, 2))