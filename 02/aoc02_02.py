with open("02/aoc02.txt") as f:
    lines = f.readlines()

scores = {"A": 1, "B": 2, "C": 3}
outcomes = {"X": 0, "Y": 3, "Z": 6}

total_score = 0

for line in lines:
    opponent_shape, outcome = line.strip().split()
    opponent_score = scores[opponent_shape]

    if outcome == "X":
        my_score = (opponent_score + 1) % 3 + 1
    elif outcome == "Y":
        my_score = opponent_score
    else:
        my_score = opponent_score % 3 + 1

    round_score = my_score + outcomes[outcome]

    total_score += round_score

print(total_score)
