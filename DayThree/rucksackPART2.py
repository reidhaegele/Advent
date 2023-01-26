f = open("inputDay3.txt", "r")
sum = 0
num = 0
s1 = ""
s2 = ""
s3 = ""
for x in f:
    num += 1
    success = False
    if (num == 1):
        s1 = x
    elif (num == 2):
        s2 = x
    elif (num == 3):
        s3 = x
        num = 0
        for c1 in s1:
            for c2 in s2:
                for c3 in s3:
                    if (c1 == c2 == c3):
                        if (ord(c1) < 95):
                            sum += (ord(c1)-38)
                            print("-----------")
                            print(c1)
                            print(ord(c1)-38)
                            print("-----------")
                        else:
                            sum += (ord(c1)-96)
                            print("-----------")
                            print(c1)
                            print(ord(c1)-96)
                            print("-----------")
                        success = True
                        break
                    if (success):
                        break
                if (success):
                    break
            if (success):
                break
        s1 = ""
        s2 = ""
        s3 = ""
f.close()
print(sum)
