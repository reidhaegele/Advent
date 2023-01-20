f = open("inputDay3.txt", "r")
sum = 0
for x in f:
        success = False
        length = len(x)
        middle = int(length/2)
        left = x[:middle]
        right = x[middle:]
        for charLeft in left:
                for charRight in right:
                        if (charLeft == charRight):
                                if(ord(charLeft)<95):
                                        sum+=(ord(charLeft)-38)
                                        print("-----------")
                                        print(charLeft)
                                        print(ord(charLeft)-38)
                                        print("-----------")
                                else:
                                        sum+=(ord(charLeft)-96)
                                        print("-----------")
                                        print(charLeft)
                                        print(ord(charLeft)-96)
                                        print("-----------")
                                success=True
                                break
                        if(success):break
                if(success):break
        
f.close()
print(sum)
