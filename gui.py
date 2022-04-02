import tkinter as tk
from tkinter import Frame, Grid, Label, Button, Checkbutton, Radiobutton, Entry,messagebox #can add more direct imports here

class interface:
    root = tk.Tk()
    root.title("Climate Sim") #sets the title of the window
    root.geometry("800x600") #sets the size of the window


    home_frame = Frame(root) #creates the home frame
    home_frame.grid(column=0,row=0,sticky="NEW")

    def new_frame(self,parent,gridx,gridy,sticky):
        frame = Frame(parent)
        frame.grid(row=gridx,column=gridy,padx=5,pady=5,sticky=sticky)
        return frame

    def new_label(self,parent,text,gridx,gridy,sticky):
        label = Label(parent,text=text)
        label.grid(row=gridx,column=gridy,padx=5,pady=5,sticky=sticky)
        return label


    #label_1 = Label(home_frame,text="Hello World") #creates the first label
    #label_1.grid(row=0,column=0)

    
    def new_button(self,parent,text,cmd,gridx,gridy,sticky):
        button = Button(parent,text=text,command=cmd)
        button.grid(row=gridx,column=gridy,sticky=sticky)
        return button

    def new_entry(self,parent,textvar,width,gridx,gridy,sticky):
        entry = Entry(parent,textvariable=textvar,width=width)
        entry.grid(row=gridx,column=gridy,sticky=sticky)
        return entry

    #Commands for handling yes or no questions in a new window

    
    def confirm(self,text="Confirm?"):
        return messagebox.askyesno(title="Confirm",message=text)
        

