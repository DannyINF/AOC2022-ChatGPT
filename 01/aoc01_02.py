with open("01/aoc01.txt") as f:
    calories = [sum(int(line.strip()) for line in group.strip().split('\n')) for group in f.read().split('\n\n') if group.strip()]
    top_three = sorted(calories, reverse=True)[:3]
    print(sum(top_three))