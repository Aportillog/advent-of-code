# --- Day 3: Toboggan Trajectory ---
#
# With the toboggan login problems resolved, you set off toward the airport. While travel by toboggan
# might be easy, it's certainly not safe: there's very minimal steering and the area is covered in
# trees. You'll need to see which angles will take you near the fewest trees.
#
# Due to the local geology, trees in this area only grow on exact integer coordinates in a grid. You make a
# map (your puzzle input) of the open squares (.) and trees (#) you can see. For example:
#
# ..##.......
# #...#...#..
# .#....#..#.
# ..#.#...#.#
# .#...##..#.
# ..#.##.....
# .#.#.#....#
# .#........#
# #.##...#...
# #...##....#
# .#..#...#.#
#
# These aren't the only trees, though; due to something you read about once involving arboreal
# genetics and biome stability, the same pattern repeats to the right many times:
#
# ..##.........##.........##.........##.........##.........##.......  --->
# #...#...#..#...#...#..#...#...#..#...#...#..#...#...#..#...#...#..
# .#....#..#..#....#..#..#....#..#..#....#..#..#....#..#..#....#..#.
# ..#.#...#.#..#.#...#.#..#.#...#.#..#.#...#.#..#.#...#.#..#.#...#.#
# .#...##..#..#...##..#..#...##..#..#...##..#..#...##..#..#...##..#.
# ..#.##.......#.##.......#.##.......#.##.......#.##.......#.##.....  --->
# .#.#.#....#.#.#.#....#.#.#.#....#.#.#.#....#.#.#.#....#.#.#.#....#
# .#........#.#........#.#........#.#........#.#........#.#........#
# #.##...#...#.##...#...#.##...#...#.##...#...#.##...#...#.##...#...
# #...##....##...##....##...##....##...##....##...##....##...##....#
# .#..#...#.#.#..#...#.#.#..#...#.#.#..#...#.#.#..#...#.#.#..#...#.#  --->
#
# You start on the open square (.) in the top-left corner and need to reach the bottom
# (below the bottom-most row on your map).
#
# The toboggan can only follow a few specific slopes (you opted for a cheaper model that prefers rational numbers);
# start by counting all the trees you would encounter for the slope right 3, down 1:
#
# From your starting position at the top-left, check the position that is right 3 and down 1. Then, check
# the position that is right 3 and down 1 from there, and so on until you go past the bottom of the map.
#
# The locations you'd check in the above example are marked here with O where there was an open square
# and X where there was a tree:
#
# ..##.........##.........##.........##.........##.........##.......  --->
# #..O#...#..#...#...#..#...#...#..#...#...#..#...#...#..#...#...#..
# .#....X..#..#....#..#..#....#..#..#....#..#..#....#..#..#....#..#.
# ..#.#...#O#..#.#...#.#..#.#...#.#..#.#...#.#..#.#...#.#..#.#...#.#
# .#...##..#..X...##..#..#...##..#..#...##..#..#...##..#..#...##..#.
# ..#.##.......#.X#.......#.##.......#.##.......#.##.......#.##.....  --->
# .#.#.#....#.#.#.#.O..#.#.#.#....#.#.#.#....#.#.#.#....#.#.#.#....#
# .#........#.#........X.#........#.#........#.#........#.#........#
# #.##...#...#.##...#...#.X#...#...#.##...#...#.##...#...#.##...#...
# #...##....##...##....##...#X....##...##....##...##....##...##....#
# .#..#...#.#.#..#...#.#.#..#...X.#.#..#...#.#.#..#...#.#.#..#...#.#  --->
#
# In this example, traversing the map using this slope would cause you to encounter 7 trees.
#
# Starting at the top-left corner of your map and following a slope of right 3 and down 1,
# how many trees would you encounter?

OBSTACLE = 'X'
PATH = 'O'
OPEN_SQUARE = '.'
TREE = '#'


def parse_puzzle_input(pattern):
    rows = pattern.splitlines()
    field = list()
    for i, row in enumerate(rows):
        field.append([ch for ch in row])

    return field


def print_field_map(field):
    for row in field:
        print(''.join([ch for ch in row]))


def trace_path(pattern, right: int, down: int):
    row_offset = 0
    col_offset = 0
    field = parse_puzzle_input(pattern)
    # print_field_map(field_map)
    for i, row in enumerate(field):
        if i != col_offset:
            continue
        col_offset += down
        if col_offset + 1 > len(field):
            break

        row_offset += right
        if row_offset + 1 > len(row):
            new_block = parse_puzzle_input(pattern)
            for j, line in enumerate(new_block):
                field[j].extend(line)

        if field[i + down][row_offset] == TREE:
            field[i + down][row_offset] = OBSTACLE
        else:
            field[i + down][row_offset] = PATH

    return field


def count_obstacles(field):
    obstacles = 0
    for row in field:
        obstacles += row.count(OBSTACLE)
    return obstacles


test_pattern = """..##.......
#...#...#..
.#....#..#.
..#.#...#.#
.#...##..#.
..#.##.....
.#.#.#....#
.#........#
#.##...#...
#...##....#
.#..#...#.#"""

test_field_map = trace_path(test_pattern, right=3, down=1)

assert 7 == count_obstacles(test_field_map)

# --- Part One ---

file = open("input", 'r')
pattern = file.read()
file.close()

field_map = trace_path(pattern, right=3, down=1)

print("Part one solution: " + str(count_obstacles(field_map)))


# --- Part Two ---
#
# Time to check the rest of the slopes - you need to minimize the probability of a sudden arboreal stop, after all.
#
# Determine the number of trees you would encounter if, for each of the following slopes, you
# start at the top-left corner and traverse the map all the way to the bottom:
#
#     Right 1, down 1.
#     Right 3, down 1. (This is the slope you already checked.)
#     Right 5, down 1.
#     Right 7, down 1.
#     Right 1, down 2.
#
# In the above example, these slopes would find 2, 7, 3, 4, and 2 tree(s) respectively; multiplied together,
# these produce the answer 336.
#
# What do you get if you multiply together the number of trees encountered on each of the listed slopes?

test_input = [
    {"right": 1, "down": 1, "count": 2},
    {"right": 3, "down": 1, "count": 7},
    {"right": 5, "down": 1, "count": 3},
    {"right": 7, "down": 1, "count": 4},
    {"right": 1, "down": 2, "count": 2},
]


test_total_obstacles = 1

for test in test_input:
    test_field_map = trace_path(test_pattern, right=test["right"], down=test["down"])
    count = count_obstacles(test_field_map)
    test_total_obstacles *= count
    assert test["count"] == count

assert 336 == test_total_obstacles

part_two_input = [
    {"right": 1, "down": 1},
    {"right": 3, "down": 1},
    {"right": 5, "down": 1},
    {"right": 7, "down": 1},
    {"right": 1, "down": 2},
]

total_obstacles = 1

for entry in part_two_input:
    field_map = trace_path(pattern, right=entry["right"], down=entry["down"])
    count = count_obstacles(field_map)
    total_obstacles *= count


print("Part two solution: " + str(total_obstacles))
