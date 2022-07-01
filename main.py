#Imports module
from tkinter import *  #represents all the functions and built-in modules in the tkinter library
from PIL import Image, ImageTk # for Images
from tkinter import messagebox  # for error messages
import random  # random function incode for the questions.
names_list = [] #List used to append names in results pages.
asked=[] #List used to append the questions.
 
#Component 1
# inserting first class which is QuizStarter.
class QuizStarter:
  def __init__(self, parent):#constructor, The __init__() function is called automatically every time the class is being used to create a new object.
        background_color1="#f0dff2" #bg color1
        background_color="#a3e4fa"  #bg color2
        
        #inserting title image 
        self.title_image = Image.open("Title.png") #need to use Image if need to resize 
        self.title_image = self.title_image.resize((295, 135), Image.ANTIALIAS) #To resize the image with width and height dimensions
        self.title_image = ImageTk.PhotoImage(self.title_image)
        self.heading_label=Label(parent, image=self.title_image, border=0)#Making the title image file the label in window.
        self.heading_label.place(x=170, y=110)#placement
        #label for username
        self.user_label=Label(parent, text="Please enter your username below: ", font=("Tw Cen MT","15","bold"),fg="Black",bg=background_color)
        self.user_label.place(x=105, y=260)#placement
        #entry box
        self.entry_box=Entry(parent)
        self.entry_box.place(x=210, y=320) #placement 
         #continue button
        self.continue_button = Button(parent, text="Continue", font=("Helvetica", "13", "bold"), bg="#fca8f9", command=self.name_collection)
        self.continue_button.place(x=245,y=362)#placement
  def name_collection(self):
        name=self.entry_box.get()
        if name == '':
            messagebox.showerror('Name is Vital!!!',
                                 'Please enter your name')
        elif len(name) > 20:

                          

            messagebox.showerror('limit error!!!',
                                 'please enter a name between 1 and 20 characters'
                                 )
        elif name.isnumeric():
            messagebox.showerror('Name error!!!',
                                 'Name can only consist of letters'
                                 )
        elif  not name.isalpha():
                messagebox.showerror('Name error!!',
                'name can not consist of symbols')
        else:
            names_list.append(name)  # add name to names list declared at the beginning