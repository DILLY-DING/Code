

myFile = open('numbers.txt', 'rt')

numlist = []

for line in myFile:
    num = int(line.rstrip("\n"))             
    numlist.append(num)

numlist.sort()

for item in numlist:
    print(item)

myFile.close()

myFile = open('numbers.txt', 'wt')

for item in numlist:
    myFile.write(str(item) + '\n')

myFile.close()
