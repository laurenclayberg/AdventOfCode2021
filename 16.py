# Parse the inputs
inputs = []
with open('project_files/16_puzzle1.txt', 'r') as f:
    for line in f:
        inputs.append(line.strip())

hex_to_binary = {'0': '0000', '1': '0001', '2': '0010', '3': '0011', '4': '0100', '5': '0101', '6': '0110', '7': '0111', '8': '1000', '9': '1001', 'A': '1010', 'B': '1011', 'C': '1100', 'D': '1101', 'E': '1110', 'F': '1111'}

def convert_hex_to_binary(string):
    result = ''
    for char in string:
        result += hex_to_binary[char]
    return result

inputs = [convert_hex_to_binary(x) for x in inputs]

# Set up AST
class Operator:
    version = None
    type_id = None
    children = None

    def __init__(self, version, type_id):
        self.version = version
        self.type_id = type_id
        self.children = []

    def add_child(self, child):
        self.children.append(child)

    def compute(self):
        if self.type_id == 0: # sum
            return sum([child.compute() for child in self.children])
        elif self.type_id == 1: # product
            result = 1
            for child in self.children:
                result *= child.compute()
            return result
        elif self.type_id == 2: # minimum
            return min([child.compute() for child in self.children])
        elif self.type_id == 3: # maximum
            return max([child.compute() for child in self.children])
        elif self.type_id == 5: # greater than
            if self.children[0].compute() > self.children[1].compute():
                return 1
            return 0
        elif self.type_id == 6: # less than
            if self.children[0].compute() < self.children[1].compute():
                return 1
            return 0
        elif self.type_id == 7: # less than
            if self.children[0].compute() == self.children[1].compute():
                return 1
            return 0

    def version_sum(self):
        return self.version

    def print(self):
        return "\nOperator: [Type] " + str(self.type_id) + " [Ver.] " + str(self.version) + " "

class Literal:
    version = None
    value = None
    children = None

    def __init__(self, version, value):
        self.version = version
        self.value = value
    
    def compute(self):
        return self.value

    def version_sum(self):
        return self.version

    def print(self):
        return "\nLiteral: [Val.] " + str(self.value) + " [Ver.] " + str(self.version) + " "

def generate_ast(message):
    def parse_literal(message, version):
        packet_length = 6 # header is 6 bits
        value = ''
        i = 0
        while(message[i] == '1'):
            packet_length += 5
            value += message[i+1:i+5]
            i += 5
        packet_length += 5
        value += message[i+1:i+5]
        return Literal(version, int(value, 2)), packet_length

    def parse_operator_15bit(message, version, type_id):
        node = Operator(version, type_id)
        index = 0
        while(index < len(message)):
            child, length = generate_ast(message[index:])
            node.add_child(child)
            index += length
        return node

    def parse_operator_11bit(message, version, type_id, num_children):
        node = Operator(version, type_id)
        index = 0
        for i in range(num_children):
            child, length = generate_ast(message[index:])
            node.add_child(child)
            index += length
        return node, index

    # first parse header
    version, type_id = int(message[:3], 2), int(message[3:6], 2)

    # if the type is 4, then the message currently is a literal
    if type_id == 4:
        node, length = parse_literal(message[6:], version)
        return node, length

    # if the type is not 4, further parse the message
    type_op = message[6]
    if type_op == '0':
        length = int(message[7:7+15], 2)
        node = parse_operator_15bit(message[7+15:7+15+length], version, type_id)
        return node, 7+15+length
    else:
        num_children = int(message[7:7+11], 2)
        node, length = parse_operator_11bit(message[7+11:], version, type_id, num_children)
        return node, 7+11+length

# Get solutions
def calculate_version_sum(ast):
    nodes = [ast]
    index = 0
    while (index < len(nodes)):
        if nodes[index].children != None:
            nodes.extend(nodes[index].children)
        index += 1
    version_sum = 0
    for node in nodes:
        version_sum += node.version_sum()
    return version_sum

for i in inputs:
    ast, _ = generate_ast(i)
    print(calculate_version_sum(ast), ast.compute())

