with open("02/aoc02.txt") as f:
    lines = f.readlines()

opponent_scores = {"A": 1, "B": 2, "C": 3}
player_scores = {"X": 1, "Y": 2, "Z": 3}

total_score = 0

for line in lines:
    opponent_shape, my_shape = line.strip().split()
    opponent_score = opponent_scores[opponent_shape]
    my_score = player_scores[my_shape]

    if opponent_score == my_score:
        round_score = my_score + 3
    elif (opponent_score == 1 and my_score == 2) or (opponent_score == 2 and my_score == 3) or (opponent_score == 3 and my_score == 1):
        round_score = my_score + 6
    else:
        round_score = my_score

    total_score += round_score

print(total_score)
