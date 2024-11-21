#PIL (Python Imaging Library) provides image editing capabilities to the python interpreter
from tkinter import *
from PIL import Image, ImageTk

#create a window with a title bar and set its geometry as well
root = Tk()
root.title('image')
root.geometry('400x400')

#Now use Image.open to open and identify the given image file.
upload = Image.open("3.jpg")

#convert this image to Tkinter compatible image
image = ImageTk.PhotoImage(upload)

#add image to Tkinter Label
label = Label(root, image=image, height = 350, width = 300)
label.place(x = 50, y = 0)
label2 = Label(root, text = "This is how you add image in Tkinter window")
label2.place(x = 40, y = 360)

#run the application 
root.mainloop()