def get_priority(c):
    if c.islower():
        return ord(c) - ord('a') + 1
    else:
        return ord(c) - ord('A') + 27

total_priority = 0
with open("03/aoc03.txt") as f:
    for line in f:
        items = set(line[:len(line)//2]) & set(line[len(line)//2:])
        # find the common item type and its priority
        common_item = items.pop()
        priority = get_priority(common_item)
        # add to the sum
        total_priority += priority

print(total_priority)
