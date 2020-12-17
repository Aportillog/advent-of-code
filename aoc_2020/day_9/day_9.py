# --- Part One ---

def check_valid(num, preamble):
    valid = False
    for n in preamble:
        if num - n in preamble:
            valid = True
            break
    return valid


def get_invalid_number(data, preamble_len):
    preamble = data[:preamble_len]
    check_idx = preamble_len
    for num in data[preamble_len:]:
        if not check_valid(num, preamble):
            break
        check_idx += 1
        preamble = data[check_idx - preamble_len:check_idx]
    return num


test_input = """35
20
15
25
47
40
62
55
65
95
102
117
150
182
127
219
299
277
309
576"""

test_data = [int(l) for l in test_input.split('\n')]
test_preamble = 5

test_sol_1 = get_invalid_number(test_data, test_preamble)

assert 127 == test_sol_1, "Incorrect value {}".format(test_sol_1)


file = open("input", 'r')
txt_data = [int(l) for l in file.readlines()]
file.close()

txt_preamble = 25

solution_1 = get_invalid_number(txt_data, txt_preamble)

print("Part 1 solution: {}".format(solution_1))


def get_sum_set(number, data):
    for i, num in enumerate(data):
        set_sum = 0
        j = 0
        while set_sum < number and i+j < len(data) - 1:
            j += 1
            set_sum = sum(data[i:i+j])
        if set_sum == number:
            print("Bingo!", num, data[i], data[i + j])
            break
    valid_set = data[i:i+j]
    print(valid_set)
    return max(valid_set) + min(valid_set)


# --- Part Two ---
test_sol_2 = get_sum_set(test_sol_1, test_data)

assert 62 == test_sol_2, "Incorrect value {}".format(test_sol_2)

solution_2 = get_sum_set(solution_1, txt_data)

print("Part 2 solution: {}".format(solution_2))
