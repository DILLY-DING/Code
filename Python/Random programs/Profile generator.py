
import random
import time



password = input('what is the password ')

x='1234'
while x!=password:
    print('Access denied')
    time.sleep(0.1)
    password = input('what is the password ')
if x==password:
    request = input('do you want another profile (type stop to end the program)') 
    while request!='stop':
        time.sleep(0.2)
        print('access granted')
        name_list = ['Ernesto Allisson Diaz', 'Harvey Jeffries', 'Farhan Hussain', 'Hammaad Ashfaq', 'Paul Randhawa', 'Gavin Sidhu', 'Allisson Soto', 'Branden Kidd', 'Destiney Dillon', 'Dalton Estes', 'Declan Banks', 'Javier Daugherty', 'Ansley Nichols', 'Bailey Hanna', 'Bailey Mueller', 'Katie Griffin', 'Kason Chen', 'Makhi Lam', 'Justice Fuller', 'Edith Pugh', 'Derek Adams', 'Caroline Lyons']
        print('Here are Their personal details')
        time.sleep(0.2)
        print("Their account name is:    ", random.choice(name_list))
        d = random.randint(447000000000,447999999999)
        print("Their phone number is:     "+str (d))
        c = random.randint(4000000000000000,4999999999999999)
        print("Their card number is:      "+str (c))
        o = random.randint(000,999)
        print("Their cvv is:              "+str (o))
        yearlist = ('01/2021', '02/2021', '03/2021', '04/2021', '05/2021', '06/2021', '07/2021', '08/2021', '09/2021', '10/2021', '11/2021', '12/2021')
        print("Their card expiry date is:", random.choice(yearlist))
        request = input('do you want another profile (type stop to end the program)')
