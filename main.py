# Idea: I can factorize the distances by the minimal distance provided in the sequence:
# Idea: When populating the path just add +1, this way I can now if the pass was crossed of value > 1 is appearing

import numpy as np


def calc_distances(path):

    right_turns = 'NESW'
    left_turns = 'NWSE'

    tot_dist = [0, 0]
    max_dist = [0, 0]
    min_dist = [0, 0]

    cur_direction = 'E'

    for i, element in enumerate(path):
        if element.isdigit():
            if cur_direction == 'E':
                tot_dist[0] += int(element)
            elif cur_direction == 'W':
                tot_dist[0] -= int(element)
            if cur_direction == 'S':
                tot_dist[1] += int(element)
            elif cur_direction == 'N':
                tot_dist[1] -= int(element)

            max_dist[0] = max(tot_dist[0], max_dist[0])
            max_dist[1] = max(tot_dist[1], max_dist[1])

            min_dist[0] = min(tot_dist[0], min_dist[0])
            min_dist[1] = min(tot_dist[1], min_dist[1])

        else:
            if element == 'R':
                cur_turns = right_turns
            else:
                cur_turns = left_turns

            cur_direction_ind = cur_turns.index(cur_direction)
            new_direction_ind = (cur_direction_ind + 1) % 4
            cur_direction = cur_turns[new_direction_ind]

        if tot_dist == (0, 0) and i < len(path) - 1:
            return None

    return max_dist, min_dist


def trace_house(house, path):

    right_turns = 'NESW'
    left_turns = 'NWSE'

    prev_x = int(np.floor(house.shape[1]/2))
    prev_y = int(np.floor(house.shape[0]/2))

    cur_direction = 'E'

    for i, element in enumerate(path):
        if element.isdigit():
            step = int(element)
            if cur_direction == 'E':
                new_x = prev_x + step
                new_y = prev_y
            elif cur_direction == 'W':
                new_x = prev_x - step
                new_y = prev_y
            elif cur_direction == 'S':
                new_x = prev_x
                new_y = prev_y + step
            elif cur_direction == 'N':
                new_x = prev_x
                new_y = prev_y - step
            else:
                print('No such direction!')

            house[prev_x:new_x][prev_y:new_y] += 1

        else:
            if element == 'R':
                cur_turns = right_turns
            else:
                cur_turns = left_turns

            cur_direction_ind = cur_turns.index(cur_direction)
            new_direction_ind = (cur_direction_ind + 1) % 4
            cur_direction = cur_turns[new_direction_ind]

    return house


def mouse_path(path):
    path = path.replace('L', ',L,').replace('R', ',R,')
    path = [el for el in path.split(',')]

    # Calculate different distance metrics from the mouse path:
    max_dist, min_dist = calc_distances(path)

    # Determine the maximal dimensions of the house and create a NumPy array to represent it:
    dimension = np.array(max_dist) - np.array(min_dist)
    house = np.zeros([4*dimension[0], 4*dimension[1]])

    # Trace the path of the mouse on the np array of the house:
    trace_house(house, path)

    return max_dist, min_dist


print('Example Tests')

example_tests = (
    ('4R2R4R2', 8),
    ('4R2L1R5R9R4R4L3', 49),
    ('1000000R1000000R1000000R1000000', 1000000000000),
    ('10R5R5R10L5L5', None),
    ('12R6R2R2R1L1L1R2L1L1R4R2L1L5R1L3R6R2R1L2R2L4', None),
    ('14R11R10R4L1L4R3R7R10R3R3L1L4L5L11R3', 132),
    ('4L10L20L30L30L50L40L60L60L85L77L10L67R72R45R47R33R30R17R15R5R5', 2950)
)

result1 = mouse_path(example_tests[0][0])
# print(result1)


for inp, out in example_tests:
    print(mouse_path(inp))

print('<COMPLETEDIN::>')
