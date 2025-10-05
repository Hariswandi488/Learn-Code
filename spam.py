import pyautogui
import time
import random

massage = {
    "1" : "Testing Spam # ",
    "2" : "Sorry yoo Sadang Test Code :v # ",
    "3" : "Den Test Spam Acak # ",
    "4" : "Jan Berang Dih :v # ",
    "5" : "Hitam Hitam Hitam Hitam Hitam #",
    "6" : "Kini Spam Nyo Labiah Capek Pado Patang # "
}

print("Memulai Spam Dalam 5 Detik")
time.sleep(5.0)


def spam(msg: str,delay: float):
    pyautogui.write("Memulai Spam Dalam 3 Detik")
    pyautogui.hotkey("enter")

    time.sleep(delay)

    for i in range(1, 12):
        rng = random.randint(1, 6)

        pyautogui.write(msg[str(rng)])
        pyautogui.write(str(i))

        time.sleep(1.0)

        pyautogui.hotkey("enter")

    pyautogui.write("abis")
    pyautogui.hotkey("enter")

spam(massage,3.0)