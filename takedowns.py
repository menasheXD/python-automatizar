import pyautogui
import time

while True:
    pyautogui.PAUSE = 0.5

    time.sleep(2)
    pyautogui.moveTo(x=649, y=616)
    pyautogui.click(x=649, y=616)
    time.sleep(2)
    pyautogui.moveTo(x=775, y=171)
    pyautogui.click(x=775, y=171)

    time.sleep(22)
    pyautogui.moveTo(x=719, y=367)
    pyautogui.press("3")
    pyautogui.click(x=719, y=367)
    time.sleep(60)
    pyautogui.press("t")
    pyautogui.press("t")
    pyautogui.press("t")

    time.sleep(22)
    pyautogui.moveTo(x=557, y=352)
    pyautogui.press("5")
    pyautogui.click(x=557, y=352)
    time.sleep(32)
    pyautogui.press("t")
    time.sleep(60)
    pyautogui.click(x=588, y=358)
    time.sleep(1)
    pyautogui.click(x=881, y=322)
    time.sleep(1)
    pyautogui.click(x=719, y=367)
    time.sleep(450)