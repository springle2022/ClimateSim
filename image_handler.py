import os
import os.path
from tkinter import PhotoImage
from PIL import ImageTk, Image



def load_image(file):
    
    if os.path.exists("images\\" + file) == True:
        if file[len(file)-4:len(file)] == ".png":
            if os.path.exists("images\\" + file + ".txt") == False:
                
                print("image error: no source information")

            return ImageTk.PhotoImage(Image.open("images\\" + file))
        else:
            print("image error: not in '.png' format")

    else:
        print("image error: no such image")
    
    