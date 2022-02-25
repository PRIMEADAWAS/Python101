import pyautogui

im1 = pyautogui.screenshot()
# im1 = pyautogui.screenshot(region=(660, 350, 600, 400))
im1.save(r"./Clickbot/savedimage.png")
