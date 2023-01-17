import pyautogui, time, string, random
time.sleep(5)
yes="yes"

while yes!="no":
    url="https://prnt.sc/"
    rstrA = random.choice(string.ascii_letters)
    rstrB = random.choice(string.ascii_letters)
    o = random.randint(0000,9999)
    print(rstrA + rstrB + str(o))

    #with pyautogui.hold('ctrl'):
     #   pyautogui.press(['l'])
    #pyautogui.typewrite(str(rstrA + rstrB + o))








    #pyautogui.typewrite(str(num))
    #pyautogui.press("enter")
    #num = num+1 
    #time.sleep(1)
    #counter = counter+1
    #if counter>=100:
     #   time.sleep(120)
     #   counter=0
