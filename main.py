import time
import pyautogui


def main():
    res = pyautogui.password(title="Project Deck", text="Enter your password")
    if res == "nggyu":
        return
    else:
        pyautogui.hotkey("winleft", "1")
        pyautogui.hotkey("ctrl", "shiftleft", "n")
        pyautogui.hotkey("ctrl", "l")
        pyautogui.typewrite("https://www.youtube.com/watch?v=dQw4w9WgXcQ")
        pyautogui.press("enter")
        time.sleep(2.5)
        pyautogui.press("f")


if __name__ == "__main__":
    main()
