f = open("input.txt", "r")
max = 0
sum = 0
for x in f:
    if (x == "\n"):
        if (sum > max):
            max = sum
        sum = 0
    else:
        sum += int(x)
f.close()
print(max)
