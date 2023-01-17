import time

myFile = open('numbers.txt', 'rt')
total =0
items =0
for line in myFile:
    number = int(line.strip("\n"))
    total = total + number
    items = items + 1


average = total/items
print("The average of all the numbers in the file (numbers.txt) is: " + str(average))

myFile.close()

time.sleep(5)
