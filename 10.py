# part 1
score = 0
points = {')': 3, ']': 57, '}': 1197, '>': 25137}

with open('project_files/10_puzzle1.txt', 'r') as f:
    while True:
        line = f.readline()
        if not line:
            break

        stack = []
        line = line.strip()
        for char in line:
            if char in ['(', '[', '{', '<']:
                stack.append(char)
            else:
                char_match = stack.pop()
                if char_match == '(' and char == ')' or char_match == '[' and char == ']' or char_match == '{' and char == '}' or char_match == '<' and char == '>':
                    continue
                else:
                    score += points[char]
                    break

print("Solution 1: ", score)

# part 2
scores = []
points = {'(': 1, '[': 2, '{': 3, '<': 4}

with open('project_files/10_puzzle1.txt', 'r') as f:
    while True:
        line = f.readline()
        if not line:
            break

        stack = []
        line = line.strip()
        line_corrupt = False
        for char in line:
            if char in ['(', '[', '{', '<']:
                stack.append(char)
            else:
                char_match = stack.pop()
                if char_match == '(' and char == ')' or char_match == '[' and char == ']' or char_match == '{' and char == '}' or char_match == '<' and char == '>':
                    continue
                else:
                    line_corrupt = True
                    break
        if line_corrupt == False:
            score_temp = 0
            for i in range(len(stack)-1, -1, -1):
                score_temp *= 5
                score_temp += points[stack[i]]
            scores.append(score_temp)

sorted_scores = sorted(scores)
solution_2 = sorted_scores[int(len(sorted_scores)/2)]

print("Solution 2: ", solution_2)