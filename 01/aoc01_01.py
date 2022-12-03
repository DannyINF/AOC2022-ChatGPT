with open("01/aoc01.txt") as f:
    calories = [sum(int(line.strip()) for line in group.strip().split('\n')) for group in f.read().split('\n\n') if group.strip()]
    print(max(calories))
