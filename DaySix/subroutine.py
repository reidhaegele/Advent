f = open("inputDay6.txt", "r")
one   = ''
two   = ''
three = ''
four  = ''
fourLetters = []
success = False
result = 0
for x in f:
        for char in x:
                result+=1
                print(result)
                if(len(fourLetters) < 4):
                        fourLetters.append(char)
                else:
                        temp = []
                        for a in range(len(fourLetters)):
                                if(a<3):
                                        temp.append(fourLetters[a+1])
                        fourLetters.clear()
                        fourLetters = temp
                        fourLetters.append(char)
                
                if(len(fourLetters)==4):
                        if(len(set(fourLetters)) == len(fourLetters)): 
                                success = True
                                break
                if(success): break
        if(success): break

print("-=-=-=-=-")
print(result)
f.close()