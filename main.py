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
        self.title_image = self.title_image.resize((295, 135), Image.ANTIALIAS)
        self.title_image = ImageTk.PhotoImage(self.title_image)
        self.heading_label=Label(parent, image=self.title_image, border=0)#add label for title image 
        self.heading_label.place(x=170, y=110)
