from PIL import Image, ImageEnhance, ImageFilter
from pathlib import Path
import os

path = Path('./imgs')
pathOut = Path('./editedImgs')
os.makedirs(pathOut, exist_ok = True)
os.makedirs(path, exist_ok = True)



def main():
    print(welcome_message)
    instance()

def instance():
    for filename in os.listdir(path):
    img = Image.open(f"{path}/{filename}")
    clean_name = os.path.splitext(filename)[0]
    os.makedirs(f"{pathOut}/{clean_name}", exist_ok = True)

    sharpened_img = img.filter(ImageFilter.SHARPEN)
    sharpened_img.save(f"{pathOut}/{clean_name}/{clean_name}_sharpened.png")

    grayscaled_img = sharpened_img.convert('L')
    grayscaled_img.save(f"{pathOut}/{clean_name}/{clean_name}_grayscale.png")
    
    angle = int(input("Please enter angle to rotate picture by in Degrees: "))
    rotated_img = rotate(sharpened_img, angle)
    rotated_img.save(f"{pathOut}/{clean_name}/{clean_name}_rotated({angle}).png")

def rotate(img, angle):
    image = img.rotate(angle)
    return image

def contrast(factor = int(input("Please enter factor of contrast: ")), img):
    enhancer = ImageEnhance.Contast(edit)
    edit = enhancer.enhance(factor)

    
if __name__ == "__main__":
    main()