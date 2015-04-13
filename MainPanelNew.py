#! /usr/bin/env python
from Tkinter import *              # get base widget set
import tkFont
from myDialogTableSearch import demos1      # button callback handlers
from myDialogTableSubmission import demos2      # button callback handlers
from myDialogTableMerging import demos3      # button callback handlers
from myDialogTableAnalysis import demos4      # button callback handlers

from tkMessageBox import *
from Tkinter import *
from glob import glob
from tkFileDialog import askopenfilename
import random



from quitter import Quitter        # attach a quit object to me

class Demo(Frame):
    def __init__(self, demos,parent=None):
        Frame.__init__(self, parent,bd=6,bg="red",relief=SUNKEN)
        self.pack(side=TOP, fill=BOTH)
        for (key, value) in demos.items():
            Button(self, text=key, command=value).pack(side=TOP, fill=BOTH)


if __name__ == '__main__':
    root = Tk()
    root.configure(bg="#aaaFFFbbb")

    font1 = tkFont.Font(family="Times",size = 13,weight = "bold")
    Label(root, text="RPC PROMPT ANALYSIS TOOL",font=font1,bg="#EEEFFFbbb",relief=SUNKEN).pack(side=TOP)
    Quitter(root).pack(side=TOP)
    
    img = PhotoImage(file="cms_higgs_event.gif")
    can = Canvas(root)
    can.pack(fill=BOTH,side=RIGHT)
    can.create_image(2, 2, image=img, anchor=NW)
    can.config(height=img.height(), width=img.width())

    Demo(demos1,root)
    Demo(demos2,root)
    Demo(demos3,root)
    Demo(demos4,root)



    root.mainloop()








