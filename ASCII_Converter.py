from PIL import Image
import tkinter as tk
from tkinter import filedialog
import time

ASCII_CHARS = '@%#*+=-:. '

def resize_image(image, new_width=100):
    width, height = image.size
    ratio = height / width / 1.65
    new_height = int(new_width * ratio)
    resized_image = image.resize((new_width, new_height))
    return resized_image

def grayscale_image(image):
    return image.convert('L')

def map_pixels_to_ascii(image, range_width=25):
    pixels = image.getdata()
    ascii_str = ''
    for pixel_value in pixels:
        char_index = int(pixel_value / range_width)
        if char_index >= len(ASCII_CHARS):
            char_index = len(ASCII_CHARS) - 1
        ascii_str += ASCII_CHARS[char_index]
    return ascii_str

def convert_image_to_ascii(image):
    image = resize_image(image)
    image = grayscale_image(image)
    ascii_str = map_pixels_to_ascii(image)
    img_width = image.width
    ascii_str_len = len(ascii_str)
    ascii_img = ''
    for i in range(0, ascii_str_len, img_width):
        ascii_img += ascii_str[i:i+img_width] + '\n'
    return ascii_img

def print_custom_text():
    custom_text = (".:::    :::   ::    .::.    :::       .::.       :::.   .::.  ::. .::::::.\n"
                   "             %@@@-  .@@@* -@@=  .@@@@:  .@@@.    :#@@@@@+  .*@@@@@#. *@@+ .@@+ %@@@%%%*\n"
                   "            +@@@@%  .@@@@*=@@=  *@@@@#  .@@@.   .@@@= #@@* #@@+ =#*= *@@+ .@@+ %@@=\n"
                   "           .%@+#@@= .@@@@@@@@= .@@+%@@- .@@@.   =@@@. =@@%-@@@:=*++= *@@+ .@@+ %@@@%%#\n"
                   "          +@@%%@@% .@@++@@@@= *@@#@@@% .@@@.   -@@@: *@@#.@@@-=#@@% *@@* .@@+ %@@+::.\n"
                   "         :@@#==%@@=.@@+ =@@@=:@@*==@@@-.@@@*+++ +@@%*@@%: =@@@*%@@% =@@@*#@@: %@@#+++=\n"
                   "\n"
                   "\n"
                   "   :==: -===. .===:   .==-      :-=-:   -==: -==.  -=:   :==-   -======.:==:   :-=-:   :==:  -=-\n"
                   "   #@@* %@@@# #@@@#   %@@@*   -%@@%@@%. %@@+ %@@@: @@#   %@@@+  +#@@@%#:#@@+ :%@@%@@%: *@@@= %@@\n"
                   "   *@@* %@@@@=@@@@#  -@@@@@: .@@@- -+: #@@+ %@@@@=@@#  =@@@@@.   #@@-  #@@+.@@@= +@@% *@@@@+%@%\n"
                   "   *@@* %@@@@@@@@@#  %@*+@@# -@@@.*###+ #@@+ %@@@@@@@#  %@*+@@*   #@@-  #@@+:@@@: -@@@.*@@%@@@@%\n"
                   "   *@@* %@##@@@+@@# =@@@@@@@:.@@@--#@@# #@@+ %@#:%@@@# =@@@@@@@:  #@@-  #@@+.@@@= +@@% *@%:#@@@%\n"
                   "   #@@* %@#:@@*-@@#.@@#::*@@# =%@@#@@@# %@@+ %@# .%@@#.@@#::*@@#  %@@-  #@@+ :%@@%@@#. *@@  #@@@\n"
                   "   :==: -=- -=..==:.==.   ===   :==-:=- -==: -=-  .==:.==.  .===  -==.  -==:   :===:   :=-   -=-\n")
    print(custom_text)

def select_image():
    print_custom_text()
    print("Press 'y' to upload a photo, or any other key to exit.")
    user_input = input()
    if user_input.lower() == 'y':
        while True:
            root = tk.Tk()
            root.withdraw()

            file_path = filedialog.askopenfilename(filetypes=[("Image Files", "*.jpg;*.jpeg;*.png")])
            if file_path:
                try:
                    image = Image.open(file_path)
                    print("Loading image...")

                    # İlerleme çubuğu
                    progress_bar_width = 30
                    for i in range(progress_bar_width + 1):
                        progress = i / progress_bar_width * 100
                        print(f"[{'=' * i}{' ' * (progress_bar_width - i)}] {progress:.1f}%\r", end='')
                        time.sleep(0.1)  # 0.1 saniye bekleme

                    print("\nImage loaded successfully.")
                    ascii_img = convert_image_to_ascii(image)
                    print(ascii_img)
                except Exception as e:
                    print(e)
                user_input = input("Press 'y' to upload another photo, or any other key to exit.")
                if user_input.lower() != 'y':
                    break
            else:
                print("No image selected.")
                break
    else:
        print("Exiting...")

if __name__ == '__main__':
    select_image()
