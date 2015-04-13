#! /usr/bin/env python   

from Tkinter import *
from quitter import Quitter
import os
from gui import *
from tkMessageBox import *

class Demo(Frame):

    def __init__(self, parent=None):
        Frame.__init__(self, parent)
        self.pack()
        Label(self, text="Search").pack()

        self.bind('<Return>', (lambda event: self.fet()))
        self.bind('<Return>', (lambda event: self.fetch1()))
        self.bind('<Return>', (lambda event: self.fetch2()))
        self.btn = Button(self, text='Search Dataset Name',command= (lambda: self.fet())).pack(side=TOP)
        self.btn1 = Button(self, text='Search dataset for a run',command= (lambda: self.fetch1())).pack(side=TOP)
        self.btn2 = Button(self, text='Search run for a dataset',command=(lambda: self.fetch2())).pack(side=TOP)
        
    def fet(self):
        cmd = './SearchDataSet.py '  
        os.system(cmd)
        
    def fetch1(self):
        cmd = './SearchDSFromRun.py '
        os.system(cmd)

    def fetch2(self):
        os.system('./SearchRun.py')
                
        
if __name__ == '__main__': Demo().mainloop()

