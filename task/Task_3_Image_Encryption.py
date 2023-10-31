# -*- coding: utf-8 -*-
"""
Created on Wed Sep  6 19:39:40 2023

@author: saksh
"""

from tkinter import *
from tkinter import filedialog

root = Tk()
root.geometry("300x300")
root.title("Image Encryption")

def encrypt_decrypt_image():
    file1 = filedialog.askopenfile(mode="r",filetype=[('jpg file','*.jpg')])
    if file1 is not None:
        #print(file)
        file_name = file1.name
        print(file_name)
        key = entry1.get(1.0,END)
        print(file_name,key)
        fi = open(file_name,'rb')
        image = fi.read()
        fi.close()
        image = bytearray(image)
        for index,values in enumerate(image):
            image[index] = values^int(key)
        fi1 = open(file_name,'wb')
        image = fi1.write(image)
        fi1.close()
        
    
key_label = Label(text="Enter a key : ",font=20)
key_label.place(x=35,y=25)

entry1 = Text(root,height=1,width=10,font=15,borderwidth=3)
entry1.place(x=90,y=80)

b1 = Button(root,text="Encrypt",font=20,borderwidth=3,bg="aqua",bd=3,command=encrypt_decrypt_image)
b1.place(x=100,y=150)

b1 = Button(root,text="Decrypt",font=20,borderwidth=3,bg="aqua",bd=3,command=encrypt_decrypt_image)
b1.place(x=100,y=200)

root.mainloop()


