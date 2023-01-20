f = open("inputDay4.txt", "r")
sum=0
total = 0
for x in f:
        total+=1
        dash1 = x.find('-')
        comma = x.find(',')
        dash2 = x.find('-', comma)
        
        low1 = int(x[:dash1])
        high1 = int(x[(dash1+1):comma])
        
        low2 = int(x[(comma+1):dash2])
        high2 = int(x[(dash2+1):])

        # print("---------")
        # print(low1)
        # print(high1)
        # print("--")
        # print(low2)
        # print(high2)

        if(low1 >= low2 and low1 <= high2):
                sum+=1
        elif(low2 >= low1 and low2 <= high1):
                sum+=1
        elif(high1 >= low2 and high1 <= high2):
                sum+=1
        elif(high2 >= low1 and high2 <= high1):
                sum+=1

f.close()
print("SUM:")
print(sum)
print("Total Lines:")
print(total)