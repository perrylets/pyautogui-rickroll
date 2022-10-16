import time
import pyautogui
import webbrowser


def main():
    res = pyautogui.password(title="Project Deck", text="Enter your password")
    if res == "nggyu":
        return
    else:
        webbrowser.open("https://www.youtube.com/watch?v=dQw4w9WgXcQ")
        time.sleep(2.5)
        pyautogui.press("f")


if __name__ == "__main__":
    main()
