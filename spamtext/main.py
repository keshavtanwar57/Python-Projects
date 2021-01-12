import pyautogui,time
time.sleep(10)
f = open("abc.txt",'r')
for word in f:
    pyautogui.typewrite(word)
    pyautogui.press("enter")
