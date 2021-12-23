import ast

class SnailFish():

    def __init__(self, left, right, parent=None, is_left=None):
        self.parent = parent
        self.is_left = is_left

        if isinstance(left, int):
            self.left = left
        elif isinstance(left, SnailFish):
            self.left = left
            self.left.is_left = True
            self.left.parent = self
        else:
            self.left = SnailFish(left[0], left[1], parent=self, is_left=True)

        if isinstance(right, int):
            self.right = right
        elif isinstance(right, SnailFish):
            self.right = right
            self.right.is_left = False
            self.right.parent = self
        else:
            self.right = SnailFish(right[0], right[1], parent=self, is_left=False)

    def print(self):
        left = str(self.left) if isinstance(self.left, int) else self.left.print()
        right = str(self.right) if isinstance(self.right, int) else self.right.print()
        return '[' + left + ',' + right + ']'

    def magnitude(self):
        if isinstance(self.left, SnailFish):
            left_magnitude = self.left.magnitude()
        else:
            left_magnitude = self.left
        if isinstance(self.right, SnailFish):
            right_magnitude = self.right.magnitude()
        else:
            right_magnitude = self.right
        return 3 * left_magnitude + 2 * right_magnitude


    def explode(self, level):
        if level == 3:
            # Check for explosions
            if isinstance(self.left, SnailFish):
                left_val = self.left.left
                right_val = self.left.right
                self.left = 0

                self.add_left(left_val)
                if isinstance(self.right, int):
                    self.right += right_val
                else:
                    self.right.add_right(right_val, skip=True)
                return True
            if isinstance(self.right, SnailFish):
                left_val = self.right.left
                right_val = self.right.right
                self.right = 0

                self.add_right(right_val)
                self.left += left_val
                return True
            if isinstance(self.left, int) and isinstance(self.right, int):
                return False

        next_level = level + 1
        if isinstance(self.left, SnailFish):
            left_explode = self.left.explode(next_level)
            if left_explode:
                return True
        if isinstance(self.right, SnailFish):
            right_explode = self.right.explode(next_level)
            if right_explode:
                return True
        return False

    def add_left(self, value):
        node = self
        
        # Go up until there is a new left node
        while node.is_left == True and node.parent is not None:
            node = node.parent

        # If you reached the top (parent is None) then there is no more to go
        if node.parent is None:
            return

        # Check if the parent left is a number, if yes you are done
        if isinstance(node.parent.left, int):
            node.parent.left += value
            return

        # If not then go to the left and then go down and right until you find a number
        node = node.parent.left
        while isinstance(node.right, SnailFish):
            node = node.right
        node.right += value

    def add_right(self, value, skip=False):
        node = self

        if not skip:
            # Go up until there is a new right node
            while node.is_left == False and node.parent is not None:
                node = node.parent

            # If you reached the top (parent is None) then there is no more to go
            if node.parent is None:
                return

            # Check if the parent left is a number, if yes you are done
            if isinstance(node.parent.right, int):
                node.parent.right += value
                return

            # If not then go to the right and then go down and left until you find a number
            node = node.parent.right
        while isinstance(node.left, SnailFish):
            node = node.left
        node.left += value

    def split(self):
        if isinstance(self.left, SnailFish):
            left_split = self.left.split()
            if left_split:
                return True
        else:
            if self.left >= 10:
                self.left = SnailFish(int(self.left/2), self.left - int(self.left/2), parent=self, is_left=True)
                return True
        if isinstance(self.right, SnailFish):
            right_split = self.right.split()
            if right_split:
                return True
        else:
            if self.right >= 10:
                self.right = SnailFish(int(self.right/2), self.right - int(self.right/2), parent=self, is_left=False)
                return True
        return False


def parse(string_input):
    ''' Parse the input and return a new SnailFish
    '''
    snail_fish_list = ast.literal_eval(string_input)
    new_snail_fish_number = SnailFish(snail_fish_list[0],snail_fish_list[1])
    return new_snail_fish_number

def add(snail_fish_left, snail_fish_right):
    ''' Creates a new snail fish from left and right
        and returns the new snail fish
    '''
    return SnailFish(snail_fish_left, snail_fish_right)

def explode(snail_fish):
    ''' Determines if snail fish needs to explode
        and returns pair (if_exploded, new_snail_fish)
    '''
    return snail_fish.explode(0), snail_fish

def split(snail_fish):
    ''' Determines if the snail fish needs to split
        and returns pair (if_split, new_snail_fish)
    '''
    return snail_fish.split(), snail_fish

def perform_add(snail_fish_left, snail_fish_right):
    ''' Perform the addition of two snail fish and
        return the fully reduced snail fish
    '''
    add_done = False

    new_snail_fish = add(snail_fish_left, snail_fish_right)
    while not add_done:
        action_done, new_snail_fish = explode(new_snail_fish)

        if action_done:
            continue
        
        action_done, new_snail_fish = split(new_snail_fish)

        if action_done:
            continue
        
        add_done = True

    return new_snail_fish

snail_fish = []
with open('project_files/18_puzzle1.txt', 'r') as f:
    for line in f:
        snail_fish.append(parse(line.strip()))

snail_fish_result = snail_fish[0]
for i in range(1, len(snail_fish)):
    snail_fish_result = perform_add(snail_fish_result, snail_fish[i])

print("Solution 1:", snail_fish_result.magnitude())

snail_fish = []
with open('project_files/18_puzzle1.txt', 'r') as f:
    for line in f:
        snail_fish.append(line.strip())

best_max = 0
for i in range(len(snail_fish)):
    for j in range(len(snail_fish)):
        if i != j:
            best_max = max(best_max, perform_add(parse(snail_fish[i]), parse(snail_fish[j])).magnitude())

print("Solution 2:", best_max)