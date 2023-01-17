import time
name= input("what is your name")

print("hello " + name )

mark= int(input("so what did you get in your maths test Out of 100? ".format(name=name)))

if mark >=0 and mark <40:
    print("you got a U")

elif mark >=40 and mark <50:
    print("you got a D")


elif mark >=50 and mark <60:
    print("you got a C")

elif mark >=60 and mark <70:
    print("you got a B")

elif mark >=70 and mark <100:
    print("you got a A")
time.sleep(5)
