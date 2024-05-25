import os
import pytesseract
import argparse
import cv2
from PIL import Image

#NOTE TO FUTURE ME: if you're using this in another mac, please note the following:
#Download Brew or MacPort (i downloaded brew)
#go to their web, and paste the link to your terminal
#dont forget to donwload xcode and agree to them ( totally will not get hacked in the future)
#also side note, have you made that app yet?

ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", required=True,
    help="path to input image to be OCR'd")
args = vars(ap.parse_args())

def read_text_from_image(image_path):
    print('read_text_from_image')
    with Image.open(image_path) as img:
        text = pytesseract.image_to_string(img)
        return text

def save_text_to_file(text, folder_path, file_name):
    print('save_text_to_file')
    file_path = os.path.join(folder_path, file_name)
    
    with open(file_path, "w") as file:
       file.write(text)

if __name__ == "__main__":
    desktop_path = os.path.join(os.path.expanduser("~"), "Desktop")
    folder_name = "Readable_Files_for_Histo"
    folder_path = os.path.join(desktop_path, folder_name)
    images_folder = os.path.join(desktop_path, "Histo_Images")
    print(images_folder)
    
    if not os.path.exists(folder_path):
        print('this works part 1')
        os.makedirs(folder_path)
        print(f"Folder '{folder_name}' created on the desktop.")
    
    if os.path.exists(images_folder):
        print('this works part 2')
        file_counter = 1
        while True:
            for filename in os.listdir(images_folder):
                current_name = f"Histo_Image_{file_counter}.png"
                if filename == current_name:
                    print(current_name)
                    print('inner loop')
                    image_path = os.path.join(images_folder, filename)
                    extracted_text = read_text_from_image(image_path)
                    
                    text_file_name = f"text_file{file_counter}.txt"
                    save_text_to_file(extracted_text, folder_path, text_file_name)
                    print(f"Text extracted from {filename} and saved to {folder_name}/{text_file_name}")
                    file_counter += 1
                
    else:
        print("Images folder not found on the desktop.")
