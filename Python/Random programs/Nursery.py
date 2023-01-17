

start = 5456 

while start!='end':

    start = input('What would you like to do? ')

    if start == "add":
        myFile =open('nursery.txt','a')

        name = input('Please add a name ')
        age = int(input('Please type the age of '+ name+ ':'))

        myFile.write(name +","+ str(age)+ "\n")
        myFile.close()

    if start == "read":

        myFile =open('nursery.txt','rt')

        for line in myFile:
            line = line.strip("\n\n")
            name,age= line.split(",")
            print(name+ " is in the nursery and is "+ age + " yeears old.")
        
        myFile.close()
    
    if start == "find":

        myFile =open('nursery.txt','rt')

        findname = input('Enter th name you want:')
        
        for line in myFile:
            line = line.strip("\n\n")
            name,age= line.split(",")
            foundname = true
        
        myFile.close()
       
