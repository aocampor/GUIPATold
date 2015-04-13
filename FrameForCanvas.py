#! /usr/bin/env python
from Tkinter import *
from quitter import Quitter
import os
from sys import argv

class Demo(Frame):

    def __init__(self,parent=None):
        Frame.__init__(self, parent)
        self.pack()
        Label(self, text="Useful Web links for Prompt Analysis",font=('times',13,'bold italic')).pack()
        self.frame(self,BOTTOM)

    def frame(self,root,side):
	w = Frame(root)
	w.pack(side=side,expand = YES,fill =BOTH)
        self.can = Canvas(self,width =750, height=400,bg = 'white')
        self.can.create_text(315,30,text="LHC STATUS    http://ab-dep-op.web.cern.ch/ab-dep-op/vistar.php?usr=LHC",font=('times',13,'italic'))
        self.can.create_text(360,100,text="DAQ MONITOR   http://cmsonline.cern.ch/daqStatusSCX/aDAQmon/DAQstatusGre.jpg",font=('times',13,'italic'))
        self.can.create_text(204,170,text="RPC ELOG   https://cmsdaq.cern.ch/elog/RPC/",font=('times',13,'italic'))
        self.can.create_text(364,240,text="TWIKI for ANALYSIS   https://twiki.cern.ch/twiki/bin/view/CMS/RPCPromptAnalysisTools",font=('times',13,'italic'))
        self.can.create_text(330,310,text="CONTROL ROOM SHIFTER MOBILE: 165508",font=('times',13,'italic'))
        self.can.pack()
	return w

        
if __name__ == '__main__':    Demo().mainloop()

