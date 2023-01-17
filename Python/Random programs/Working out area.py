import time
height= int(input ('what is the height of your shape(if it has one)'))
width= int(input ('what is the width/diameter of your shape'))
shape = input("what shape is it")
pi=3.14159265358979323846264

if shape == "square":
        c=height*width
        print ("the area of your square is: "+str (c))
elif shape == "triangle":
        c=(height*width)/2
        print ("the area of your triangle is: "+str (c))
elif shape == "parallelogram":
        c=height*width
        print ("the area of your parallelogram is: "+str (c))
elif shape == "circle":
	c= pi * (width/2) * (width/2)
	print ("the area of your circle is: "+str (c))
elif shape == "rectangle":
        c=height*width
        print ("the area of your rectangle is: "+str (c))

time.sleep(5)
