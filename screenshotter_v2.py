import time
import pyautogui
from PIL import ImageGrab, ImageOps, Image, ImageEnhance
import os

#region=(1275,17.2, 1025, 1400) for right
#region=(250,17.2, 1025, 1400) for left
#region=(250,17.2, 2050, 1400) for orig

def take_screenshot_left(image_number):
    screenshot_path = os.path.join("Histo_Images", f"Histo_Image_{image_number}.png")
    pyautogui.screenshot(screenshot_path, region=(250,17.2, 1025, 1400))
    convert(screenshot_path)

def take_screenshot_right(image_number):
    screenshot_path = os.path.join("Histo_Images", f"Histo_Image_{image_number}.png")
    pyautogui.screenshot(screenshot_path, region=(1275,17.2, 1025, 1400))
    convert(screenshot_path)
    print(f"Screenshot taken and saved as '{screenshot_path}'.")

def convert(image_path):
    image = Image.open(image_path)
    
    contrast = ImageEnhance.Contrast(image)
    image = contrast.enhance(2.0)
    
    sharpness = ImageEnhance.Sharpness(image)
    image = sharpness.enhance(2.0)  
    
    image = ImageOps.grayscale(image)
    image.save(image_path)
    print(f"Image edited.")

def start_countdown():
    print("Type 'START' to begin the automated screenshot process.")
    while True:
        user_input = input().strip().lower()
        if user_input == 'start':
            break
        else:
            print("Invalid input. Type 'START' to begin.")

    print("Starting automated screenshot process in:")
    for i in range(3, 0, -1):
        print(i)
        time.sleep(1)

def automate_screenshot():
    print("Automated screenshot process started. Press 'Esc' to stop.")

    if not os.path.exists("Histo_Images"):
        os.makedirs("Histo_Images")

    image_number = 1
    start_countdown()
    
    while True:
        take_screenshot_left(image_number)
        print('Screenshotted left!')
        image_number += 1

        take_screenshot_right(image_number)
        print('Screenshotted right!')
        image_number += 1

        time.sleep(1.5)
        pyautogui.click()
        print("Mouse clicked.")
        time.sleep(1.5)

        if pyautogui.press("esc"):
            print("Automated screenshot process stopped.")
            break


if __name__ == "__main__":
    automate_screenshot()
