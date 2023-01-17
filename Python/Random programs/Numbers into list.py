import time                                     #imports the time module which allows the program to stop for a set time.


myFile = open('numbers.txt', 'rt')              #opens the file 'numbers.txt' and reads it


numlist = []                                    #creats a empty list

for line in myFile:                             #loops through every line of the file
    number = int(line.rstrip("\n"))             #strips the number from the file and casts it as a integer and puts in speech marks(formats it).
    numlist.append(number)                      #puts the formatted integer into the numlist


maxi = max(numlist)                             #sets the variable 'maxi' to the max of 'numlist'
mini = min(numlist)                             #sets the variable 'mini' to the min of 'numlist'
total = sum(numlist)                            #sets the variable 'total' to the sum of 'numlist'

print(numlist)                                  #it prints the number list
time.sleep(0.5)                                 #stops the program for 0.5 seconds
print("The largest number is: "+ str(maxi))     #prints the largest number (maxi) as a string
time.sleep(0.5)                                 #stops the program for 0.5 seconds
print("The smallest number is: "+ str(mini))    #prints the smallest number (mini) as a string
time.sleep(0.5)                                 #stops the program for 0.5 seconds
print("The total is: "+ str(total))             #prints the total (total) as a string
time.sleep(2)                                   #stops the program for 2 seconds



myFile.close()                                  #closes the file
