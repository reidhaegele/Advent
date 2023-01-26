f = open("input.txt", "r")
max = 0
second_max = 0
third_max = 0
sum = 0
for x in f:
    if (x == "\n"):
        if (sum > max):
            if (max > second_max):
                if (second_max > third_max):
                    third_max = second_max
                second_max = max
            max = sum
        else:
            if (sum > second_max):
                if (max > second_max):
                    third_max = second_max
                second_max = sum
            else:
                if (sum > third_max):
                    third_max = sum
        sum = 0
    else:
        sum += int(x)
f.close()
total = max+second_max+third_max
print(total)
print("MAX:"+(str(max)))
print("SECOND MAX:"+(str(second_max)))
print("THIRD MAX:"+(str(third_max)))
print("TOTAL:"+(str((max+second_max+third_max))))
