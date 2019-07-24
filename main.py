# Idea: I can factorize the distances by the minimal distance provided in the sequence:
# Idea: When populating the path just add +1, this way I can now if the pass was crossed of value > 1 is appearing
import numpy as np


def mouse_path(path):
    path = path.replace('L', ',L,').replace('R', ',R,')
    path = [el for el in path.split(',')]

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

            if tot_dist[0] > max_dist[0]:
                max_dist[0] = tot_dist[0]
            if tot_dist[1] > max_dist[1]:
                max_dist[1] = tot_dist[1]
            if tot_dist[0] < min_dist[0]:
                min_dist[0] = tot_dist[0]
            if tot_dist[1] < min_dist[1]:
                min_dist[1] = tot_dist[1]

        else:
            if element == 'R':
                cur_direction_ind = right_turns.index(cur_direction)
                new_direction_ind = (cur_direction_ind + 1) % 4
                cur_direction = right_turns[new_direction_ind]

            elif element == 'L':
                cur_direction_ind = left_turns.index(cur_direction)
                new_direction_ind = (cur_direction_ind + 1) % 4
                cur_direction = left_turns[new_direction_ind]

        if tot_dist == (0, 0) and i < len(path)-1:
            return None

    return max_dist, min_dist

    """
    prev_turn = 'S'
    prev_dist = 0
    total = 0

    for element in path:
        if element == 'R' or element == 'L':
            cur_turn = element
        else:
            if prev_turn == 'R' and cur_turn == 'R':
    """



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

result1 = mouse_path(example_tests[2][0])
# print(result1)


for inp, out in example_tests:
    print(mouse_path(inp))

print('<COMPLETEDIN::>')

