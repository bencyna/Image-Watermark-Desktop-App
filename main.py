from tkinter import *
from PIL import Image, ImageTk
import os, sys

# ToDo 3. When user clicks on image, add text should come up with options (size, colour, font etc)
def place_text(x, y):
    pass;

# get location of click
def get_origin(event_origin):
    global x, y
    x = event_origin.x
    y = event_origin.y
    place_text(x, y)



# ToDo 1. Setup tkinter window
window = Tk()
window.config(padx=50, pady=50, width=900, height=700, background='#3D9970')
window.title("Flashcards")
canvas = Canvas(width=900, height=700, highlightthickness=0, background="#3D9970")
canvas.grid(row=1, columnspan=1)
# window.columnconfigure("")

## on click call function that gets click
window.bind("<Button 1>", get_origin)

# title
title = Label(text="Add your watermark!", font=("Times New Roman", 20), background="#3D9970", justify='center')
title.grid(column=0, row=0)
title = Label(text="Click anywhere to add to your image", font=("Arial", 10, "italic"), background="#3D9970", justify='center')
title.grid(column=0, row=1)


# ToDo 2. Allow users to upload an image
# Image
load = Image.open(r"assets/Screenshot1.png")
render = ImageTk.PhotoImage(image=load)
img = Label(window, image=render)
img.grid(row=2, column=0, columnspan=2)




# ToDo 4. User needs to be able to save the image


window.mainloop()
