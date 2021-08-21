#%%
from tkinter import *
import os

def create_message_window(title:str, message: str):

    """Creates and displays a helpful window message. 
    Splits the message into lines if it contains newline characters."""
    
    root = Tk()
    root.title(title)
    root.iconbitmap(r"C:\Users\User\Desktop\python-various-automations\GUIs\images\python.ico")

    #create a label widget for each message part
    for line in message.split("\n"):       

        msg = Label(root, text = line)
        msg.pack()

    button = Button(root, text = "Close", command = root.destroy)
    button.pack()
    root.mainloop()

create_message_window("Alert", "Test message\n This should be on a new line\n Yeah, newline here. \n Also new line.")
# %%
