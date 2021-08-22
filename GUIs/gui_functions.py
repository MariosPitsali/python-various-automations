
from tkinter import *
import os
from PIL import Image, ImageTk
import time

def generic_message_window(title:str, message: str):

    """Creates and displays a helpful window message. 
    Splits the message into lines if it contains newline characters."""
    
    root = Tk()
    root.title(title)
    root.iconbitmap(r"images\python.ico")

    #create a label widget for each message part
    for line in message.split("\n"):       

        msg = Label(root, text = line)
        msg.pack()

    button = Button(root, text = "Close", command = root.destroy)
    button.pack()
    root.mainloop()


def display_image_content_in_file(folder_path:str):

    """Function to be used when some operation of editing image files is involved.
    Displays state of all image files in given folder, with relevant file details."""

    def display_next():
        pass

    def display_previous():
        pass
    
    root = Tk()
    root.title("Image Gallery")
    root.iconbitmap("images/images.ico")

    try:
        image_list = [Image.open(os.path.join(folder_path, item.name)) for item in os.scandir(folder_path) if item.name.endswith('jpg')]

        img = ImageTk.PhotoImage(image_list[2])
        image_label = Label(image = img)
        image_details_label = Label(text = 'Image Size: {}, Image Format: {}.'.format(image_list[2].size, image_list[2].format))
        image_label.grid(row = 1, column = 1)
        image_details_label.grid(row = 2, column = 1)

        # for i, image in enumerate(image_list):
        #     tk_image = ImageTk.PhotoImage(image)
        #     image_label = Label(image = tk_image)
        #     image_label.grid(row=i, column = i)
        #     time.sleep(3)

    except IOError:
        label = Label(text = "Ooops")
        label.pack()
    
    root.mainloop()

display_image_content_in_file(r"C:\Users\User\Desktop\LIEBE ANTA")