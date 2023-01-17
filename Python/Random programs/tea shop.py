import random
import time
import os

x = input('Do you want to buy something from my tea shop ')
password='no'
while x!=password:

        time.sleep(0)

        cookienumber=0

        name = input("What is your name? ")


        print ("hello " + name )

        time.sleep(1)

        tea = input("would you like any tea? ")

        if tea == "yes":
                teanumber = int(input("okay, how many cups of tea would you like "))
                


        if tea == "no":
                print("then get out my shop NOW!!")
                exit()

        cookies = input("would you like any cookies? ")

        if cookies == "yes":
                cookienumber = int(input("okay, how many cookies would you like "))


        

        time.sleep(1)

        print ("please take a seat whist i make your food ")

        c=(teanumber*1.5)+(cookienumber*0.5)

        time.sleep(3)


        print ("your food is ready ")

        time.sleep(3)

        moretea = input("Would you like any more tea? ")

        if moretea == "yes":
                print("well you cant have anymore fatty ")       

        time.sleep(1)

 
        print ("your {teanumber} cups of tea are ready".format(teanumber=teanumber))

        time.sleep(1)



        print('Yor total price is: £'+str (c))

        time.sleep(3)

        x = input('would you like to buy from my shop again ')
        
        password1='no'

        while x!=password1:

                time.sleep(0)

                cookienumber=0

                name = input("What is your name? ")


                print ("hello " + name )

                time.sleep(1)

                tea = input("would you like any tea? ")

                if tea == "yes":
                        teanumber = int(input("okay, how many cups of tea would you like "))
                


                if tea == "no":
                        print("then get out my shop NOW!!")
                        exit()

                cookies = input("would you like any cookies? ")

                if cookies == "yes":
                        cookienumber = int(input("okay, how many cookies would you like "))


        

                time.sleep(1)

                print ("please take a seat whist i make your food ")

                c=(teanumber*1.5)+(cookienumber*0.5)

                time.sleep(3)


                print ("your food is ready ")
        
                time.sleep(3)

                moretea = input("Would you like any more tea? ")

                if moretea == "yes":
                        print("well you cant have anymore")       

                time.sleep(1)

 
                print ("your {teanumber} cups of tea are ready".format(teanumber=teanumber))

                time.sleep(1)



                print('Yor total price is: £'+str (c))

                time.sleep(3)
                

