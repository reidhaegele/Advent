f = open("inputDay5.txt", "r")
one = ['Q', 'F', 'M', 'R', 'L', 'W', 'C', 'V']
two = ['D', 'Q', 'L']
three = ['P', 'S', 'R', 'G', 'W', 'C', 'N', 'B']
four = ['L', 'C', 'D', 'H', 'B', 'Q', 'G']
five = ['V', 'G', 'L', 'F', 'Z', 'S']
six = ['D', 'G', 'N', 'P']
seven = ['D', 'Z', 'P', 'V', 'F', 'C', 'W']
eight = ['C', 'P', 'D', 'M', 'S']
nine = ['Z', 'N', 'W', 'T', 'V', 'M', 'P', 'C']
towers = [one, two, three, four, five, six, seven, eight, nine]


def moveBlocks(count, away, to):
    to -= 1
    away -= 1
    crates = []

    for a in range(count):
        crates.append(towers[away].pop())
    for a in range(count):
        towers[to].append(crates.pop())


for x in f:
    space2 = x.find(' ', 5)
    c = int(x[5:space2])
    space3 = x.find(' ', 9)
    a = int(x[space3+1])
    t = int(x[len(x)-2])
    moveBlocks(c, a, t)
print(towers)
f.close()
