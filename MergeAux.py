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
        Label(self, text="Merge").pack()

        self.bind('<Return>', (lambda event: self.fet()))
        self.bind('<Return>', (lambda event: self.fetch1()))
        self.bind('<Return>', (lambda event: self.fetch2()))
        self.btn = Button(self, text='Large Run',command= (lambda: self.fet())).pack(side=TOP)
        self.btn1 = Button(self, text='Old Method',command= (lambda: self.fetch1())).pack(side=TOP)
        self.btn2 = Button(self, text='Merge Several Runs',command=(lambda: self.fetch2())).pack(side=TOP)
        
    def fet(self):
        cmd = './MergeFrame.new.py '  
        os.system(cmd)
        
    def fetch1(self):
        cmd = './MergeFrame.py '
        os.system(cmd)

    def fetch2(self):
        os.system('./MergeFrameForSeveralJobs.py')
                
        
if __name__ == '__main__': Demo().mainloop()

