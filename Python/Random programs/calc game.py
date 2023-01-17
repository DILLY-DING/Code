import random
from random import randint
import os, time

score=2

while score>=1:
    
    number = (randint(0, 150))
    number1 = (randint(0, 30))
    print("Your first number is: "+str (number))
    print("Your second number is: "+str (number1))


    d = random.randint(1,4)

    if d == 1:
        c=number+number1
        print("add them")


    elif d == 2:
        c=number-number1
        print("subtract them")


    elif d == 3:
        c=number/number1
        print("divide them")

    elif d == 4:
        c=number*number1
        print("multiply them")


    answer = int (input ("what is the answer? "))



    if c==answer:
        print("You are corect!!")
        score=score+1
        print("Your score is: " + str(score) + "\n\n")

    else:
        print("Nope...")
        score=score-1
        print("Your score is: " + str(score) + "\n\n")


print("GAME OVER!!!!!!!")

time.sleep(5)
