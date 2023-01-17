import time

myFile =open('highscores.txt','rt')

findname = input('Please enter the name of the player you want to delete. ')

notdeletedlist=[]

namefound = False

for line in myFile:
    line = line.rstrip("\n")
    name,score= line.split(",")
    if not(name==findname):
            notdeletedlist.append(name)
            notdeletedlist.append(score)
    else:
        namefound   = True


if namefound == False:
    print(findname + ' is not on the list')

myFile.close()

myFile = open('highscores.txt','wt')

for line in range(0,len(notdeletedlist)//2):
    myFile.write(notdeletedlist[2*i]+','+ notdeletedlist[2*i+1]+ '\n')

myFile.close()

time.sleep(5)

