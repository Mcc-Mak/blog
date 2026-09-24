from tkinter import *
from PIL import ImageTk, Image

import os


username=""

bg_index=0

DIR =os.getcwd()+r"/Full_game"
backgrounds = [DIR+"/clear_blue_sky.jpg",DIR+"/colourful.jpg",DIR+"/sci.jpg"]

class TKbox(Tk):
    def __init__(self):
        super().__init__()

        self.title("User Interface")
        self.geometry("400x350")
        self.userlabel = Label(self,text="User Name: ")
        self.name = Entry(self)
        self.bgi = 0

        self.btn1 = Button(self,text="next",command=lambda: self.__change_map(1))  #Select Next Map
        self.btn2 = Button(self,text="back",command=lambda: self.__change_map(0))  #Select the Previous Map
        self.img = Image.open(backgrounds[self.bgi])
        self.img = self.img.resize((250,250),Image.ANTIALIAS)
        self.tkimg = ImageTk.PhotoImage(self.img)
        self.label1 = Label(self,image=self.tkimg)


        self.enter = Button(self,text="Enter",anchor="c",width=6,height =1,command=self.__read)

        self.userlabel.grid(row=0,column=0)
        self.name.grid(row=0,column=1)
        self.btn2.grid(row=2, column=0)
        self.label1.grid(row=2,column=1)
        self.btn1.grid(row=2, column=2)
        self.enter.grid(row=3,column=1)

        self.mainloop()
    def __read(self):
        global username
        username = self.name.get()
        if len(username) >=10:
            username = username[:11]
        print(username)
        self.destroy()

    def __change_map(self,flag):
        global bg_index
        if flag == 1:
            if self.bgi == len(backgrounds)-1:
                self.bgi = 0
            else:
                self.bgi+=1
        elif flag == 0:
            if self.bgi == 0:
                self.bgi = len(backgrounds)-1
            else:
                self.bgi-=1

        self.img = Image.open(backgrounds[self.bgi])
        self.img = self.img.resize((250, 250), Image.ANTIALIAS)
        self.tkimg = ImageTk.PhotoImage(self.img)
        self.label1 = Label(self, image=self.tkimg)
        self.label1.grid(row=2, column=1)
        bg_index = self.bgi



