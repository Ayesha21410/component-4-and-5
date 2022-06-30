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
  