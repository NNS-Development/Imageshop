from PIL import Image, ImageEnhance
from pathlib import Path
from os import makedirs, path, listdir

def choose_directory(prompt):
    path = Path(input(prompt))
    makedirs(path, exist_ok=True)
    return path

def load_image(file_path):
    return Image.open(file_path)

def save_image(image, file_path):
    image.save(file_path)

def enhance_image(fileIn, fileOut, clean_name, enhancement, factor, suffix):
    image = load_image(fileIn)
    enhancer = enhancement(image)
    enhanced_image = enhancer.enhance(factor)
    save_image(enhanced_image, fileOut / f"{clean_name}_{suffix}.png")

def contrast(fileIn, fileOut, clean_name):
    enhance_image(fileIn, fileOut, clean_name, ImageEnhance.Contrast, 2, "contrast")

def sharpen(fileIn, fileOut, clean_name):
    enhance_image(fileIn, fileOut, clean_name, ImageEnhance.Sharpness, 2, "sharpen")

def grayscale(fileIn, fileOut, clean_name):
    image = load_image(fileIn)
    grayscale_image = image.convert("L")
    save_image(grayscale_image, fileOut / f"{clean_name}_grayscale.png")

def rotate(fileIn, fileOut, clean_name, angle):
    image = load_image(fileIn)
    rotated_image = image.rotate(angle)
    save_image(rotated_image, fileOut / f"{clean_name}_rotate.png")

def edit_image(fileIn, fileOut, clean_name, edit_function, *args):
    makedirs(fileOut, exist_ok=True)
    edit_function(fileIn, fileOut, clean_name, *args)

def single_edit_mode(pathIn, pathOut):
    filename = input("Please enter the filename of the image to edit: ")
    fileIn = pathIn / filename
    clean_name = path.splitext(filename)[0]
    fileOut = pathOut / clean_name

    edit_options = {
        '1': contrast,
        '2': sharpen,
        '3': grayscale,
        '4': rotate,
        '5': lambda *args: print("Exiting single edit mode.")
    }

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
        if choice in edit_options:
            if choice == '4':
                angle = int(input("Please enter the rotation angle: "))
                edit_image(fileIn, fileOut, clean_name, edit_options[choice], angle)
            elif choice == '5':
                edit_options[choice]()
                break
            else:
                edit_image(fileIn, fileOut, clean_name, edit_options[choice])
        else:
            print("Invalid input. Please enter a valid number.")

def mass_edit_mode(pathIn, pathOut):
    edit_options = {
        '1': contrast,
        '2': sharpen,
        '3': grayscale,
        '4': rotate,
        '5': lambda: print("Exiting mass edit mode.")
    }

    while True:
        choice = input(
'''
Please choose an edit option for all images:
    1. Contrast
    2. Sharpen
    3. Grayscale
    4. Rotate
    5. Quit
'''
        )
        if choice in edit_options:
            if choice == '4':
                angle = int(input("Please enter the rotation angle: "))
                for filename in listdir(pathIn):
                    fileIn = pathIn / filename
                    clean_name = path.splitext(filename)[0]
                    fileOut = pathOut / clean_name
                    edit_image(fileIn, fileOut, clean_name, edit_options[choice], angle)
            elif choice == '5':
                edit_options[choice]()
                break
            else:
                for filename in listdir(pathIn):
                    fileIn = pathIn / filename
                    clean_name = path.splitext(filename)[0]
                    fileOut = pathOut / clean_name
                    edit_image(fileIn, fileOut, clean_name, edit_options[choice])
        else:
            print("Invalid input. Please enter a valid number.")

def main():
    print("Welcome!")
    pathOut = choose_directory("Please enter output directory for images: ") if input("Would you like to change the output directory? (y/n): ") == 'y' else Path('app/editedImgs')
    pathIn = choose_directory("Please enter input directory for images: ") if input("Would you like to change the input directory? (y/n): ") == 'y' else Path('app/imgs')

    options = {
        '1': lambda: choose_directory("Please enter output directory for images: "),
        '2': lambda: mass_edit_mode(pathIn, pathOut),
        '3': lambda: single_edit_mode(pathIn, pathOut),
        '4': lambda: print("Goodbye!")
    }

    while True:
        choice = input(
'''
Please enter in the corresponding number:
    1. Change Output Directory
    2. Mass edit mode
    3. Single edit mode
    4. Quit
'''
        )
        if choice in options:
            options[choice]()
            if choice == '4':
                break
        else:
            print("Invalid input. Please enter a valid number.")

if __name__ == "__main__":
    main()