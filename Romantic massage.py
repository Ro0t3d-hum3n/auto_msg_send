import pyautogui
import time
message = 10
while message > 0:
    time.sleep(3)
    pyautogui.typewrite('I am really sorry please forgive me please'
                        ' ')
    time.sleep(3)
    pyautogui.press('enter')
    message = message - 1