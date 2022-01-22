import pyautogui
import time


time.sleep(1)

# mouse
location = pyautogui.position()
print(location)
x, y = location

pyautogui.click(x, y+100)
pyautogui.doubleClick(x, y+200)
pyautogui.moveTo(x, y+300, duration=1)
pyautogui.dragTo(x, y+400, duration=1)


# keyboard
pyautogui.write('hello world')
pyautogui.hotkey('alt', 'tab')

# imgae locatioon
pyautogui.locateOnScreen('wow.jpg')

# pop up
pyautogui.password()
