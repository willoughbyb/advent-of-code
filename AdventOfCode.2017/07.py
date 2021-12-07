import re


def parse():
    info_pattern = re.compile(r'^(\w+) \((\d+)\)')
    rela_pattern = re.compile(r'[>,] (\w+)')
    for line in lines:
        info_matches = info_pattern.match(line)
        key = info_matches.group(1)
        weight = info_matches.group(2)
        all[key] = int(weight)

        rela_matches = rela_pattern.findall(line)
        if len(rela_matches) > 0:
            relations[key] = rela_matches


def find_parent(key):
    for parent, children in relations.items():
        if key in children:
            return parent
    return None


def get_weight(key, num_spaces=0):
    weight = all[key]
    if key in relations.keys():
        child_weights = []
        for child in relations[key]:
            child_weights.append(get_weight(child, num_spaces + 1))

        for cw in child_weights:
            weight += cw

        if len(set(child_weights)) > 1:
            print('unbalanced {} ({}) ({}) {} {}'.format(
                key, all[key], weight, relations[key], child_weights))
            unbalanced.append(key)

    return weight


def print_tree(key, num_spaces=0):
    print('{}{} {}'.format(''.join(['  '] * num_spaces), key, all[key]))
    if key in relations.keys():
        for child in relations[key]:
            print_tree(child, num_spaces + 1)


with open('07.input') as f:
    lines = f.read().split('\n')

all = {}
relations = {}
unbalanced = []

parse()

root = None
# find the key that doesn't exist in the children?
for parent, child in relations.items():
    if find_parent(parent) == None:
        root = parent
        break

print(root)

get_weight(root)

print(unbalanced)

print_tree('gexwzw')
