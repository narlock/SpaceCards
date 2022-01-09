# SpaceCards GUI
# Author: Anthony Narlock

import tkinter as tk
from PIL import Image

#Beginning of interface
root = tk.Tk()

#All elements will be inside of this root object

#Canvas
canvas = tk.Canvas(root, width=500, height=500)
canvas.grid(row = 2)




#Places window in middle of screen
root.eval('tk::PlaceWindow . center')
#Ending of interface
root.mainloop()