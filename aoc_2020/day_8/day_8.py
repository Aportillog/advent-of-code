import copy
# --- Part One ---

test_input = """nop +0
acc +1
jmp +4
acc +3
jmp -3
acc -99
acc +1
jmp -4
acc +6"""


def parse_input(txt_input):
    code = []
    for line in txt_input.split('\n'):
        ins, arg = line.split(' ')
        code.append({'ins': ins, 'arg': int(arg), 'exec': False})
    return code


def execute(code, acc=0, stack_pointer=0):
    accumulator = acc
    end_program = False
    # Instrucction already executed
    if code[stack_pointer]['exec']:
        return accumulator, False
    if stack_pointer == len(code) - 1:
        end_program = True

    code[stack_pointer]['exec'] = True
    ins = code[stack_pointer]['ins']
    arg = code[stack_pointer]['arg']
    if ins == 'nop':
        stack_pointer += 1
    elif ins == 'acc':
        stack_pointer += 1
        accumulator += arg
    elif ins == 'jmp':
        stack_pointer += arg

    if end_program:
        return accumulator, True

    return execute(code, accumulator, stack_pointer)


code = parse_input(test_input)
res, exit_code = execute(code)

assert 5 == res, "Incorrect acc value {}".format(res)

file = open("input", 'r')
txt_input = file.read()
file.close()

code = parse_input(txt_input)
solution, exit_code = execute(code)

print("Part 1 solution: {}".format(solution))


# --- Part Two ---

def get_bug_indexes(code):
    res = []
    for i, line in enumerate(code):
        if line['ins'] in ['nop', 'jmp']:
            res.append(i)
    return res


def fix_code(code, bug_index):
    fixed_code = copy.deepcopy(code)
    if fixed_code[bug_index]['ins'] == 'nop':
        fixed_code[bug_index]['ins'] = 'jmp'
    elif fixed_code[bug_index]['ins'] == 'jmp':
        fixed_code[bug_index]['ins'] = 'nop'
    return fixed_code


test_input = """nop +0
acc +1
jmp +4
acc +3
jmp -3
acc -99
acc +1
jmp -4
acc +6"""

code = parse_input(test_input)
indexes = get_bug_indexes(code)

for idx in indexes:
    fixed_code = fix_code(code, idx)
    solution, exit_code = execute(fixed_code)
    if exit_code:
        break

assert 8 == solution, "Incorrect acc value {}".format(solution)


code = parse_input(txt_input)
indexes = get_bug_indexes(code)

for idx in indexes:
    fixed_code = fix_code(code, idx)
    solution, exit_code = execute(fixed_code)
    if exit_code:
        break

print("Part 2 solution: {}".format(solution))
