f = open("DayTwo\inputDay2.txt", "r")
total = 0
round = 0
for x in f:
    round = 0
    opponent = x[0]
    me = x[2]
    if (me == 'X'):  # lose
        round += 0
        if (opponent == 'A'):  # rock
            round += 3
        if (opponent == 'B'):  # paper
            round += 1
        if (opponent == 'C'):  # scissors
            round += 2
    elif (me == 'Y'):  # draw
        round += 3
        if (opponent == 'A'):  # rock
            round += 1
        if (opponent == 'B'):  # paper
            round += 2
        if (opponent == 'C'):  # scissors
            round += 3
    elif (me == 'Z'):  # win
        round += 6
        if (opponent == 'A'):  # rock
            round += 2
        if (opponent == 'B'):  # paper
            round += 3
        if (opponent == 'C'):  # scissors
            round += 1
    total += round
print(total)
f.close()
