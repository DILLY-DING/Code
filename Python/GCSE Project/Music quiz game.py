import random
import time

r1 = input('Do you want to generate a username :')
if r1=='yes':
    name1 = input('Please enter your first name in lowercase :')
    name2 = input('Please enter your second name in lowercase :')
    birthdate = input('Please enter your year of birth :')
    user=birthdate[2]+birthdate[3]+name1[0]+name2
    print('Congratulations your generated username is '+str (user))
    password = input('please input a password :')   
    print('Thank you, your account has been created, please login :')
    score=0
    myFile =open('Users.txt','a')
    myFile.write("\n" + str(user) +","+ str(password))
    myFile.close()

    myFile =open('Users.txt','rt')
    for line in myFile:
        line = line.strip("\n\n")
        user,spassword= line.split(",")
    
        
    myFile.close()
    enteredusername="3541"
    print("\n-----------------------Please log in!!---------------------")
    while enteredusername!=user:
        enteredusername = input('\nPlease enter your username :')
        if enteredusername==user:
            enteredpass = input ('\nPlease enter your password :')
            if enteredpass==spassword:
                r4 = input('\nDo you want to take a Music Quiz :')
                if r4=='yes':
                    score=0
                    chances=2
                    number=0

            

                    

                    while chances >0:
                        chances = 2
                        lines = open('MusicQuiz.txt').read().splitlines()
                        myline =random.choice(lines)
                        line = myline
                        detail=line.split(",")
                        songname = detail[1]
                        time.sleep(0.5)
                        print("\n------------------------------------------------------------")
                        time.sleep(0.5)
                        print("\n"+str(number)+") "+detail[0]+"\n")
                        time.sleep(0.5)
                        print(songname[0]+" is the first letter of the song title.\n")
                        for x in range (0,len(songname)):
                            if songname[x] == " ":
                                letter = songname[x+1]
                                if letter != " ":
                                    print(letter+" is another letter in the song title!\n")
                        time.sleep(0.5)
                        answer1 = input("What is the name of the song? You have "+ str(chances) + " lives left!!"+"\n\n")
                        if answer1==detail[1]:
                            time.sleep(0.5)
                            print("\n---------------------------Correct--------------------------\n")
                            score=score+3
                            time.sleep(0.5)
                            print('-----------------------Your score is '+str(score)+"----------------------\n")
                        if answer1!=detail[1]:
                            time.sleep(0.5)
                            print("--------------------------Incorrect--------------------------"+"\n")
                            chances=chances-1
                            time.sleep(0.5)
                            print("-------------------You have "+ str(chances) + " lives left!!------------------"+"\n")
                            answer1 = input("\n\n---------------------Please try again!!---------------------\n\nWhat is the name of the song? You have "+ str(chances) + " lives left!!"+"\n\n")
                            if answer1==detail[1]:
                                time.sleep(0.5)
                                print("\n---------------------------Correct--------------------------\n")
                                score=score+1
                                time.sleep(0.5)
                                print('-----------------------Your score is '+str(score)+"----------------------\n")
                            if answer1!=detail[1]:
                                time.sleep(0.5)
                                print("--------------------------Incorrect--------------------------"+"\n")
                                chances=chances-1
                                time.sleep(0.5)
                                print("-------------------You have "+ str(chances) + " lives left!!------------------"+"\n")
                        myFile.close()
                                

                    

                    myFile =open('Highscore.txt','r')
                    hlist=[]
                    for line in myFile:
                        line = line.strip("\n")
                        hname,hscore= line.split(",")
                        hlist.append(hname)
                        hlist.append(int(hscore))
                    myFile.close()
                    jscore=[]
                    noscores = int(len(hlist)/2)
                    for i in range(0,noscores):
                        jscore.append(hlist[1+2*i])
                    jscore.sort()
                    jscore.reverse()
                    print("The first 5 Highscores are:\n")
                    for x in range(0,5):
                        for y in range(0,noscores):
                            if hlist[1+2*y] == jscore[x]:
                                print(hlist[2*y]+ " is: " + str(jscore[x]))
                    didwin=0
                    pono=0
                    lol=0
                    
                    while lol!=5:
                        if score>=jscore[lol]:
                            pono=lol+1
                            didwin=1
                            lol=5
                        else:
                            lol=lol+1

                    

                    if didwin==1:
                        nname = input("\n\nWell done!! You score is " + str(score) + " and your position number is "+ str(pono) + "\n\nWhat is your name?: ")
                        f=open('Highscore.txt','r')
                        data = f.readlines()
                        data[pono-1] = ((nname) + "," + str(score)+ "\n")
                        myFile.close()
                        with open('Highscore.txt', 'w') as file:
                            file.writelines( data )
                        myFile.close()
                        print("\nGAME OVER!!! You won "+ nname)

                    else:
                        print("\nGAME OVER!!! You did not win!!!")
                                
                            
                    
                else:
                    bruh="poo"
                    while bruh!="2":
                        print("Ok Bye!!!!")

            else:
                print("\n-----Acess Denied-----\n")
    
    

    

else:
    myFile =open('Users.txt','rt')
    for line in myFile:
        line = line.strip("\n\n")
        user,spassword= line.split(",")
    
        
    myFile.close()
    enteredusername="3541"
    print("\n-----------------------Please log in!!---------------------")
    while enteredusername!=user:
        enteredusername = input('\nPlease enter your username :')
        if enteredusername==user:
            enteredpass = input ('\nPlease enter your password :')
            if enteredpass==spassword:
                r4 = input('\nDo you want to take a Music Quiz :')
                if r4=='yes':
                    score=0
                    chances=2
                    number=0

            

                    

                    while chances >0:
                        chances = 2
                        lines = open('MusicQuiz.txt').read().splitlines()
                        myline =random.choice(lines)
                        line = myline
                        detail=line.split(",")
                        songname = detail[1]
                        time.sleep(0.5)
                        print("\n------------------------------------------------------------")
                        time.sleep(0.5)
                        print("\n"+str(number)+") "+detail[0]+"\n")
                        time.sleep(0.5)
                        print(songname[0]+" is the first letter of the song title.\n")
                        for x in range (0,len(songname)):
                            if songname[x] == " ":
                                letter = songname[x+1]
                                if letter != " ":
                                    print(letter+" is another letter in the song title!\n")
                        time.sleep(0.5)
                        answer1 = input("What is the name of the song? You have "+ str(chances) + " lives left!!"+"\n\n")
                        if answer1==detail[1]:
                            time.sleep(0.5)
                            print("\n---------------------------Correct--------------------------\n")
                            score=score+3
                            time.sleep(0.5)
                            print('-----------------------Your score is '+str(score)+"----------------------\n")
                        if answer1!=detail[1]:
                            time.sleep(0.5)
                            print("--------------------------Incorrect--------------------------"+"\n")
                            chances=chances-1
                            time.sleep(0.5)
                            print("-------------------You have "+ str(chances) + " lives left!!------------------"+"\n")
                            answer1 = input("\n\n---------------------Please try again!!---------------------\n\nWhat is the name of the song? You have "+ str(chances) + " lives left!!"+"\n\n")
                            if answer1==detail[1]:
                                time.sleep(0.5)
                                print("\n---------------------------Correct--------------------------\n")
                                score=score+1
                                time.sleep(0.5)
                                print('-----------------------Your score is '+str(score)+"----------------------\n")
                            if answer1!=detail[1]:
                                time.sleep(0.5)
                                print("--------------------------Incorrect--------------------------"+"\n")
                                chances=chances-1
                                time.sleep(0.5)
                                print("-------------------You have "+ str(chances) + " lives left!!------------------"+"\n")
                        myFile.close()
                                

                    

                    myFile =open('Highscore.txt','r')
                    hlist=[]
                    for line in myFile:
                        line = line.strip("\n")
                        hname,hscore= line.split(",")
                        hlist.append(hname)
                        hlist.append(int(hscore))
                    myFile.close()
                    jscore=[]
                    noscores = int(len(hlist)/2)
                    for i in range(0,noscores):
                        jscore.append(hlist[1+2*i])
                    jscore.sort()
                    jscore.reverse()
                    print("The first 5 Highscores are:\n")
                    for x in range(0,5):
                        for y in range(0,noscores):
                            if hlist[1+2*y] == jscore[x]:
                                print(hlist[2*y]+ " is: " + str(jscore[x]))
                    didwin=0
                    pono=0
                    lol=0
                    
                    while lol!=5:
                        if score>=jscore[lol]:
                            pono=lol+1
                            didwin=1
                            lol=5
                        else:
                            lol=lol+1

                    

                    if didwin==1:
                        nname = input("\n\nWell done!! You score is " + str(score) + " and your position number is "+ str(pono) + "\n\nWhat is your name?: ")
                        f=open('Highscore.txt','r')
                        data = f.readlines()
                        data[pono-1] = ((nname) + "," + str(score)+ "\n")
                        myFile.close()
                        with open('Highscore.txt', 'w') as file:
                            file.writelines( data )
                        myFile.close()
                        print("\nGAME OVER!!! You won "+ nname)

                    else:
                        print("\nGAME OVER!!! You did not win!!!")
                                
                            
                    
                else:
                    loop="true"
                    while loop!="false":
                        print("Ok Bye!!!!")

            else:
                print("\n-----Acess Denied-----\n")
    
