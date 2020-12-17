# --- Part One ---

test_input = """abc

a
b
c

ab
ac

a
a
a
a

b"""


def clean_duplicates(group):
    return "".join(set(group))


def count_answers(groups):
    count = 0
    for group in groups:
        count += len(group)
    return count


groups = [clean_duplicates(gr.replace('\n', '')) for gr in test_input.split('\n\n')]

count = count_answers(groups)
assert 11 == count

file = open("input", 'r')
groups = [clean_duplicates(gr.replace('\n', '')) for gr in file.read().split('\n\n')]
file.close()

print("Part one solution: " + str(count_answers(groups)))
