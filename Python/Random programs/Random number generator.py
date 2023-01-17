
import random
import time



password = input('do you want another number')

x='1234'
while x!=password:
    d = random.randint(447000000000,447999999999)
    print("my phone number is: "+str (d))
    password = input('do you want another number')
   
