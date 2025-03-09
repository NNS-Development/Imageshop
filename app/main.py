from PIL import Image, ImageEnhance, ImageFilter
from pathlib import Path
import os
import struct
import math

pathIn = Path('app/imgs')
pathOut = Path('app/editedImgs')
os.makedirs(pathOut, exist_ok=True)
os.makedirs(pathIn, exist_ok=True)

welcome_message = "Welcome!"

def choose_pathOut():
    global pathOut 
    pathOut = Path(input("Please enter output directory for images: "))
    os.makedirs(pathOut, exist_ok=True)
    
def choose_pathIn():
    global pathIn 
    pathIn = Path(input("Please enter input directory for images: "))
    
def choose_imageIn():
    global imageIn
    imageIn = Path(input("Please enter in the directory of your image: "))
    
def single_edit_mode():
    filename = input("Please enter the filename of the image to edit: ")
    fileIn = pathIn / filename
    clean_name = os.path.splitext(filename)[0]
    fileOut = pathOut / clean_name
    os.makedirs(fileOut, exist_ok=True)

    while True:
        choice = input(
            '''
Please choose an edit option:
    1. Contrast
    2. Sharpen
    3. Grayscale
    4. Rotate
    5. Quit
'''
        )
        if choice == '1':
            contrast(fileIn, fileOut, clean_name)
        elif choice == '2':
            sharpen(fileIn, fileOut, clean_name)
        elif choice == '3':
            grayscale(fileIn, fileOut, clean_name)
        elif choice == '4':
            angle = int(input("Please enter the rotation angle: "))
            rotate(fileIn, fileOut, clean_name, angle)
        elif choice == '5':
            print("Exiting single edit mode.")
            break
        else:
            print("Invalid input. Please enter a valid number.")
    

def load_image(file_path):
    return Image.open(file_path)

def save_image(image, file_path):
    image.save(file_path)

def contrast(fileIn, fileOut, clean_name):
    image = load_image(fileIn)
    enhancer = ImageEnhance.Contrast(image)
    enhanced_image = enhancer.enhance(2)  # Increase contrast
    save_image(enhanced_image, fileOut / f"{clean_name}_contrast.png")

def sharpen(fileIn, fileOut, clean_name):
    image = load_image(fileIn)
    enhancer = ImageEnhance.Sharpness(image)
    enhanced_image = enhancer.enhance(2)  # Increase sharpness
    save_image(enhanced_image, fileOut / f"{clean_name}_sharpen.png")

def grayscale(fileIn, fileOut, clean_name):
    image = load_image(fileIn)
    grayscale_image = image.convert("L")  # Convert to grayscale
    save_image(grayscale_image, fileOut / f"{clean_name}_grayscale.png")

def rotate(fileIn, fileOut, clean_name, angle):
    image = load_image(fileIn)
    rotated_image = image.rotate(angle)  # Rotate image
    save_image(rotated_image, fileOut / f"{clean_name}_rotate.png")

def main():
    print(welcome_message)
    askout = input("Would you like to change the output directory? (y/n): ")
    if askout == 'y':
        choose_pathOut()
    askin = input("Would you like to change the input directory? (y/n): ")
    if askin == 'y':
        choose_pathIn()
    instance()

def instance():
    choice = input(
'''
Please enter in the corresponding number:
    1. Change Output Directory
    2. Mass edit mode
    3. Single edit mode
    4. Quit
'''
    )
    if choice == '1':
        choose_pathOut()
        instance()
    elif choice == '2':
        mass_edit_mode()
        instance()
    elif choice == '3':
        single_edit_mode()
        instance()
    elif choice == '4':
        print("Goodbye!")
    else:
        print("Invalid input. Please enter a valid number.")
        instance()
    
if __name__ == "__main__":
    main()