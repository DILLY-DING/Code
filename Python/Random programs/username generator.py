

r1 = input('Would you like to login :')
if r1=='yes':
    enteredusername = 'na'
    
    while enteredusername!=user:
        enteredusername = input('Please enter your username :')
        if enteredusername==user:
            enteredpass = input ('Please enter your password :')
            if enteredpass==password:
                print("You're in")



if r1=='no':
    newacc = input('Would you like to create a new account :')
    if newacc=='yes':
        name1 = input('Please enter your first name in lowercase :')
        name2 = input('Please enter your second name in lowercase :')
        birthdate = input('Please enter your year of birth :')
        user=birthdate[2]+birthdate[3]+name1[0]+name2
        print('Congratulations your generated username is '+str (user))
        password = input('please input a password :')   
        print('Thank you, your account has been created, please login :')
        enteredusername = 'na'
    
        while enteredusername!=user:
            enteredusername = input('Please enter your username :')
            if enteredusername==user:
                enteredpass = input ('Please enter your password :')
                if enteredpass==password:
                    print("You're in")

    else:
        print('Goodbye! ')
        exit()

    
else:
    print('Goodbye! ')
    exit()
    
        
    
