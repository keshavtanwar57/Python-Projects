import pyautogui,time

# it will start spamming after 10 sec
time.sleep(10)

# abc is the text file used for the spamming
f = open("abc.txt",'r')
for word in f:
    pyautogui.typewrite(word)
    pyautogui.press("enter")
