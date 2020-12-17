# --- Part One ---
def get_jolt_dist(data):
    data.append(0)
    data.append(max(data) + 3)
    data.sort()
    diff_1_count = 0
    diff_3_count = 0
    for i, dev in enumerate(data[:-1]):
        diff = data[i + 1] - dev
        if diff == 1:
            diff_1_count += 1
        if diff == 3:
            diff_3_count += 1

    return diff_1_count * diff_3_count


test_input = """16
10
15
5
1
11
7
19
6
12
4"""

test_data = [int(l) for l in test_input.split('\n')]

test_sol = get_jolt_dist(test_data)

assert 7 * 5 == test_sol

file = open("input", 'r')
txt_data = [int(l) for l in file.readlines()]
file.close()

solution_1 = get_jolt_dist(txt_data)

print("Part 1 solution: {}".format(solution_1))
