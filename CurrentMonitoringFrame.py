#! /usr/bin/env python   

from Tkinter import *
from quitter import Quitter
import os,time
import tkMessageBox
from tkMessageBox import *
from DrawColWheelCurrent import DrawWheel

class Demo(Frame):
    def __init__(self, parent=None):
        my_window = Toplevel()
        Frame.__init__(self, my_window)
        self.pack(expand=YES, fill=BOTH)
        Label(self, text="Panel for Current Monitoring").pack()

        self.fields = 'Start Time', 'End Time', 'Wheel/Disk'
        self.ents = self.makeform(self, self.fields)
        self.bind('<Return>', (lambda event: self.fetch(self.ents)))   
        self.btn = Button(self, text='Submit', 
                    command= (lambda: self.fetch(self.ents))).pack(side=TOP)

    def fetch(self,entries):
        try:
            inp = []
            for entry in entries:
                inp.append(entry.get())

            dataStart = ((inp[0]).split(" ")[0]).split("-")
            tStart = ((inp[0]).split(" ")[1]).split(":")

            dataEnd = ((inp[1]).split(" ")[0]).split("-")
            tEnd = ((inp[1]).split(" ")[1]).split(":")
                        
            timeStart = time.mktime((int(dataStart[0]),int(dataStart[1]),int(dataStart[2]),int(tStart[0]),int(tStart[1]),int(tStart[2]),0,0,0))
            timeEnd = time.mktime((int(dataEnd[0]),int(dataEnd[1]),int(dataEnd[2]),int(tEnd[0]),int(tEnd[1]),int(tEnd[2]),0,0,0))

            print timeStart,timeEnd,time.ctime(int(timeStart)),time.ctime(int(timeEnd))
            
            if str(inp[2]).count("W") != 0:
                cmd = './DrawColWheelCurrent.py ' + str(inp[2]) + ' ' + str(int(timeStart)) + ' ' +str(int(timeEnd))+'&'
                os.system(cmd)
            elif str(inp[2]).count("RE") != 0:
                cmd = './DrawColDiskCurrent.py ' + str(inp[2]) + ' ' + str(int(timeStart)) + ' ' +str(int(timeEnd))+'&'
                os.system(cmd)
            else:
                tkMessageBox.showwarning(
                    "WARNING!",
                    "Wrong input format for Wheel or Disk",
                    "Please, specify W or RE: ex. W2 or RE-1"
                    )
            return 1
        except ValueError:
            tkMessageBox.showwarning(
                "WARNING!",
                "Wrong input format"
                )
            return 0


    def makeform(self,root, fields):
        entries = []
        i = 0
        default = ['2009-06-01 02:00:00','2009-06-02 05:10:00','W2']
        for field in fields:
            row = Frame(root)                           # make a new row
            lab = Label(row, width=25, text=field)       # add label, entry
            ent = Entry(row)
            ent.insert(0, default[i])
            row.pack(side=TOP, fill=X)                  # pack row on top
            lab.pack(side=LEFT)
            ent.pack(side=RIGHT, expand=YES, fill=X)    # grow horizontal
            entries.append(ent)
            i = i + 1
        return entries
     
if __name__ == '__main__': Demo().mainloop()

