def string_contains_chars(string, char_list):
    for char in char_list:
        if char not in string:
            return False
    return True

def decode_signals(input_strings, output_strings):
    inputs = [''.join(sorted(x)) for x in input_strings]
    outputs = [''.join(sorted(x)) for x in output_strings]
    decoder = {}

    # add easy numbers to decoder
    for x in inputs:
        if len(x) == 2:
            decoder[x] = 1
            decoder[1] = x
        if len(x) == 3:
            decoder[x] = 7
            decoder[7] = x
        if len(x) == 4:
            decoder[x] = 4
            decoder[4] = x
        if len(x) == 7:
            decoder[x] = 8
            decoder[8] = x

    # signals left: len5 (2, 3, 5), len6 (0, 6, 9)
    # len6: 9 contains 4, 0 contains 1, 6 not contains 1
    len_6_inputs = [x for x in inputs if len(x) == 6]
    #    first check for which contains 4
    for x in len_6_inputs:
        if (string_contains_chars(x, decoder[4])):
            decoder[9] = x
            decoder[x] = 9
            len_6_inputs.remove(x)
            break
    #    next check for which contains 1
    for x in len_6_inputs:
        if (string_contains_chars(x, decoder[1])):
            decoder[0] = x
            decoder[x] = 0
            len_6_inputs.remove(x)
            break
    decoder[6] = len_6_inputs[0]
    decoder[len_6_inputs[0]] = 6

    # len5: 3 contains 1, 5 is all of 6 minus 1 letter
    len_5_inputs = [x for x in inputs if len(x) == 5]
    #    first check for which contains 1
    for x in len_5_inputs:
        if (string_contains_chars(x, decoder[1])):
            decoder[3] = x
            decoder[x] = 3
            len_5_inputs.remove(x)
            break
    #    next check which contains all but one of 6
    for x in len_5_inputs:
        if (string_contains_chars(decoder[6], x)):
            decoder[5] = x
            decoder[x] = 5
            len_5_inputs.remove(x)
            break
    decoder[2] = len_5_inputs[0]
    decoder[len_5_inputs[0]] = 2

    # decode output string
    output_num = ''
    for x in outputs:
        output_num += str(decoder[x])
    return int(output_num, 10)

counts = 0
output_signals_total = 0

with open('project_files/8_puzzle1.txt', 'r') as f:
    while True:
        line = f.readline()
        if not line:
            break

        line = line.strip()
        line_split = line.split('|')

        # Solve Q2
        output_signals_total += decode_signals(line_split[0].strip().split(), line_split[1].strip().split())

        # Solve Q1
        line = line_split[1]
        line_split = line.strip().split(' ')
        for val in line_split:
            if len(val) in [2,3,4,7]:
                counts += 1

print("Solution 1: ", counts)
print("Solution 2: ", output_signals_total)