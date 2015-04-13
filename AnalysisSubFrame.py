#! /usr/bin/env python
from Tkinter import *
from quitter import Quitter
import os
from sys import argv

demoModules = ['KeyBoardForDetector','FrameForCanvas']

parts = []

class Demo(Frame):

    def __init__(self, parent=None):
        Frame.__init__(self, parent)
        self.pack()
        Label(self, text="RPC Prompt Analysis Tool",font=('times',15,'bold italic')).pack()
        
        self.addComponents(self)
        
    def addComponents(self,root):
        i = 0
        position = [LEFT,LEFT,LEFT,LEFT]
        for demo in demoModules:
            module = __import__(demo)                     # import by name string
            part = module.Demo(root)                      # attach an instance
            part.config(bd=2, relief=GROOVE)
            if i == 1 :
                part.pack(side=position[i],after=parts[0], fill=BOTH)
            else:
                part.pack(side=position[i], fill=BOTH)
            parts.append(part)
            i = i + 1

    def dumpState():
        for part in parts:                                # run demo report if any
            print part.__module__ + ':',
            if hasattr(part, 'report'):
                part.report()
            else:
                print 'none'

    def fetch(self):
        print "ciccio"


if __name__ == '__main__': Demo().mainloop()
