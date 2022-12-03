from functools import reduce

def get_priority(c):
    if c.islower():
        return ord(c) - ord('a') + 1
    else:
        return ord(c) - ord('A') + 27

total_priority = 0
with open("03/aoc03.txt") as f:
    for l1, l2, l3 in zip(f, f, f):
        items = reduce(lambda a, b: a & b, [set(l.rstrip()) for l in [l1, l2, l3]])
        if items:
            priority = get_priority(items.pop())
            total_priority += priority

print(total_priority)
