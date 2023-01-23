f = open("inputDay6.txt", "r")
fourteenLetters = []
success = False
result = 0
for x in f:
        for char in x:
                result+=1
                if(len(fourteenLetters) < 14):
                        fourteenLetters.append(char)
                else:
                        temp = []
                        for a in range(len(fourteenLetters)):
                                if(a<13):
                                        temp.append(fourteenLetters[a+1])
                        fourteenLetters.clear()
                        fourteenLetters = temp
                        fourteenLetters.append(char)
                
                if(len(fourteenLetters)==14):
                        if(len(set(fourteenLetters)) == len(fourteenLetters)): 
                                success = True
                                break
        if(success): break

print(result)
f.close()