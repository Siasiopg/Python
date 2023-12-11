import pyautogui
import time

print("Ustaw kursor w odpowiednim miejscu: ")
time.sleep(5)

x, y = pyautogui.position()

for i in range(1000):
    pyautogui.click(x, y)
