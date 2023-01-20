f = open("inputDay2.txt", "r")
total = 0
round = 0
for x in f:
        round = 0
        opponent = x[0]
        me = x[2]
        if(me=='X'):#rock
                round += 1
                if(opponent=='A'):#rock
                        round+=3
                if(opponent=='B'):#paper
                        round+=0
                if(opponent=='C'):#scissors
                        round+=6
        elif(me == 'Y'):#paper
                round += 2
                if(opponent=='A'):#rock
                        round+=6
                if(opponent=='B'):#paper
                        round+=3
                if(opponent=='C'):#scissors
                        round+=0
        elif(me=='Z'):#scissors
                round+=3
                if(opponent=='A'):#rock
                        round+=0
                if(opponent=='B'):#paper
                        round+=6
                if(opponent=='C'):#scissors
                        round+=3
        total+=round
print(total)
f.close()