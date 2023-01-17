

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
    myFile.write(str(user) +","+ str(password) +","+ str(score))
    myFile.close()
    

else:
    enteredusername='na'
    user="na"
    score="na"
    while enteredusername!=user:
        enteredusername = input('Please enter your username :')
        if enteredusername==user:
            enteredpass = input ('Please enter your password :')
            if enteredpass==password:
                r4 = input('Do you want to take a Geography Quiz :')
                if r4=='yes':
                    score=0
                    myFile =open('GeographyQuiz.txt','rt')

                    for line in myFile:
                        line = line.strip("\n")
                        detail=line.split(",")
                        print(detail[0]+"\n")
                        print(detail[1]+"\n")
                        print(detail[2]+"\n")
                        print(detail[3]+"\n")
                        answer1 = input('Please input an answer :a, b or c :'+"\n")
                        if answer1==detail[4]:
                            print('Correct'+"\n")
                            score=score+1


                    print('your score is '+str (score))

                    if score ==0:
                        print("you got a U")

                    elif score ==1:
                        print("you got a D")

                    elif score ==2:
                        print("you got a C")
                        
                    elif score ==3:
                        print("you got a B")

                    elif score ==4:
                        print("you got an A")

                    myFile.close()
                    myFile =open('Database.txt','a')

                   
                    myFile.write(str(enteredusername) +","+ str(enteredpass) +","+ str(score))
                    myFile.close()
    
        
    
