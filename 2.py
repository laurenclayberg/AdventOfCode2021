depth = 0
position = 0

with open('project_files/2_puzzle1.txt', 'r') as f:
    while True:
        line = f.readline()
        if line == " ":
            continue
        if not line:
            break
        line_split = line.strip().split(" ")
        instruction = line_split[0]
        value = int(line_split[1])

        if instruction == 'forward':
            position += value
        if instruction == 'down':
            depth += value
        if instruction == 'up':
            depth -= value

print(depth * position)

aim = 0
depth = 0
position = 0

with open('project_files/2_puzzle1.txt', 'r') as f:
    while True:
        line = f.readline()
        if line == " ":
            continue
        if not line:
            break
        line_split = line.strip().split(" ")
        instruction = line_split[0]
        value = int(line_split[1])

        if instruction == 'forward':
            position += value
            depth += value * aim
        if instruction == 'down':
            aim += value
        if instruction == 'up':
            aim -= value

print(depth * position)
