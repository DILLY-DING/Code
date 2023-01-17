import pyautogui, time, string, random
time.sleep(5)
yes="yes"

while yes!="no":
    url="https://prnt.sc/"
    rstrA = random.choice(string.ascii_lowercase)
    rstrB = random.choice(string.ascii_lowercase)
    o = random.randint(0000,9999)
    with pyautogui.hold('ctrl'):
        pyautogui.press(['l'])
    time.sleep(0.2)
    pyautogui.typewrite(url + rstrA + rstrB + str(o))
    time.sleep(0.2)
    pyautogui.press("enter")
    time.sleep(5)
