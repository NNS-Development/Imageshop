from PIL import Image, ImageEnhance, ImageFilter
from pathlib import Path
import os

pathIn = Path('./imgs')
pathOut = Path('./editedImgs')
os.makedirs(pathOut, exist_ok = True)
os.makedirs(pathIn, exist_ok = True)

welcome_message = "Welcome!"

def choose_pathOut():
    global pathOut 
    pathOut = Path(input("Please enter output directory for images: "))
    os.makedirs(pathOut, exist_ok = True)
    
def choose_pathIn():
    global pathIn 
    pathIn = Path(input("Please enter input directory for images: "))
    
def choose_imageIn():
    global imageIn
    imageIn = Path(input("Please enter in the directory of your image: "))
    
def single_edit_mode(filename):
    clean_name = os.pathIn.splitext(filename)[0]
    os.makedirs(f"{pathOut}/{clean_name}", exist_ok = True)

def contrast(fileIn, fileOut, clean_name):
    img = Image.open(fileIn)
    
    factor = int(input("Please enter factor of contrast: "))
    enhancer = ImageEnhance.Contast(img)
    contrasted_img = enhancer.enhance(factor)
    
    contrasted_img.save(f"{fileOut}/{clean_name}_contrasted().png")
    
    
    
def sharpen(fileIn, fileOut, clean_name):
    img = Image.open(fileIn)
    
    sharpened_img = img.filter(ImageFilter.SHARPEN)
    
    sharpened_img.save(f"{fileOut}/{clean_name}_sharpened.png")

def grayscale(fileIn, fileOut, clean_name):
    img = Image.open(fileIn)
    
    grayscaled_img = img.convert('L')
    
    grayscaled_img.save(f"{fileOut}/{clean_name}_grayscale.png")
    
def rotate(fileIn, fileOut, clean_name):
    img = Image.open(fileIn)
    
    angle = int(input("Please enter angle to rotate picture(s) by in Degrees: "))
    rotated_img = rotate(img, angle)
    
    rotated_img.save(f"{fileOut}/{clean_name}_rotated({angle}).png")
 
 
    
    
    
    
    
def main():
    print(welcome_message)
    choose_pathOut()
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
    
    if choice == 2: ...
    
    



    
if __name__ == "__main__":
    main()