# Open the input file
with open("04/aoc04.txt", "r") as file:
    # Read all lines from the file
    lines = file.readlines()

# Initialize the counter for the number of pairs
num_pairs = 0

# Iterate through each line in the file
for line in lines:
    # Split the line on the comma character
    sections = line.strip().split(",")

    # Iterate through each pair of sections
    for i in range(len(sections)):
        for j in range(i + 1, len(sections)):
            # Split the sections on the hyphen character to get the start and end values
            start1, end1 = map(int, sections[i].split("-"))
            start2, end2 = map(int, sections[j].split("-"))

            # Check if the ranges overlap
            if end1 >= start2 and end2 >= start1:
                # If they do, increment the counter
                num_pairs += 1

# Print the result
print(num_pairs)
