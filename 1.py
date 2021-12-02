depths_1 = []

with open('project_files/1_puzzle1.txt', 'r') as f:
    while True:
        line = f.readline()
        if line == " ":
            continue
        if not line:
            break
        depths_1.append(int(line.strip()))

def day_one_puzzle_1(input):
    count = 0
    for i in range(1, len(input)):
        if input[i] > input[i-1]:
            count +=1
    return count

print(day_one_puzzle_1(depths_1))

def day_one_puzzle_2(input):
    count = 0
    for i in range(3, len(input)):
        if input[i] > input[i-3]:
            count += 1
    return count

print(day_one_puzzle_2(depths_1))

