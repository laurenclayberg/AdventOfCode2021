from collections import Counter

class LinkedList:
    node_prev = None
    node_next = None
    node_value = None
    potential_next_value = None

    def __init__(self, value):
        self.node_prev = None
        self.node_next = None
        self.node_value = value
        self.potential_next_value = None

    def hasNext(self):
        if self.node_next is not None:
            return True
        return False

# read in the input
starting_string  = []
insert_rules = {}

with open('project_files/14_puzzle_toy.txt', 'r') as f:
    for line in f:
        line = line.strip()
        if len(line) == 0:
            continue
        elif '-' in line:
            line_split = line.split(' -> ')
            insert_rules[line_split[0]] = line_split[1]
        else:
            starting_string = list(line)

# turn the starting string into a linked list
linked_list_nodes = [LinkedList(val) for val in starting_string]

def connect_list_of_nodes(list_of_nodes):
    for n in range(len(list_of_nodes)-1):
        node_1 = list_of_nodes[n]
        node_2 = list_of_nodes[n+1]
        node_1.node_next = node_2
        node_2.node_prev = node_1

connect_list_of_nodes(linked_list_nodes)

linked_list_start = linked_list_nodes[0]

# methods to do potential inserts and redefine linked list
def find_potential_inserts(linked_list_start, insert_rules):
    cur_node = linked_list_start
    while cur_node.hasNext():
        lookup = cur_node.node_value + cur_node.node_next.node_value
        insert = insert_rules[lookup]

        if insert is not None:
            cur_node.potential_next_value = insert
        
        cur_node = cur_node.node_next

def insert_potential_values(linked_list_start):
    cur_node = linked_list_start
    while cur_node.hasNext():
        next_node = cur_node.node_next
        if cur_node.potential_next_value is not None:
            potential_next_node = LinkedList(cur_node.potential_next_value)

            # insert into the main list
            cur_node.node_next = potential_next_node
            potential_next_node.node_prev = cur_node

            next_node.node_prev = potential_next_node
            potential_next_node.node_next = next_node

        cur_node = next_node

def print_list(linked_list_start):
    cur_node = linked_list_start
    string = ''
    while cur_node is not None:
        string += cur_node.node_value
        cur_node = cur_node.node_next
    return string

NUM_STEPS = 40
for i in range(NUM_STEPS):
    print(i)
    find_potential_inserts(linked_list_start, insert_rules)
    insert_potential_values(linked_list_start)

result_string = print_list(linked_list_start)
char_counts = Counter(result_string)

min_count = None
max_count = None
for char in char_counts.keys():
    if min_count is None:
        min_count = char_counts[char]
        max_count = char_counts[char]
    min_count = min(char_counts[char],min_count)
    max_count = max(char_counts[char],max_count)

print("Solution 1:", max_count - min_count)