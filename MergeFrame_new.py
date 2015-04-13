#! /usr/bin/env python   

from Tkinter import *
from quitter import Quitter
import os
from tkMessageBox import *

class Demo(Frame):
##    def __init__(self, options, parent=None):
    def __init__(self, parent=None):        
        my_window = Toplevel()
        Frame.__init__(self, my_window)
        self.pack(expand=YES, fill=BOTH)
        Label(self, text="Faster Merge for long Runs").pack()

        self.fields = ['DataSet','Run Number']
        self.ents = self.makeform(self, self.fields)
        self.bind('<Return>', (lambda event: self.fetch(self.ents)))   
        self.btn = Button(self, text='Submit', 
                    command= (lambda: self.fetch(self.ents))).pack(side=TOP)

    def fetch(self,entries):
        try:
            inp = []
            for entry in entries:
                inp.append(entry.get())
                
            cmd = './MergeJobForAGivenRunNumber_new.py ' + inp[0] + ' '+ inp[1] + ' &' 
            ch = "echo $HOME"
            homedir = [item[:-1] for item in os.popen(ch)]
            job_finalpath = str(homedir[0]) + '/scratch0/'+ str(inp[1]) + '/job'
            job_cerr = job_finalpath + '/Mergeerr.cerr'
            job_cout = job_finalpath + '/Mergeout.cout'

            os.system(cmd)
            return 1
        except ValueError:
            tkMessageBox.showwarning(
                "Wrong input format",
                "Please insert the Run Number"
                )
            return 0
     
    def makeform(self,root, fields):
        entries = []
        i = 0
        default = ['/StreamExpress/CRAFT09-RpcCalHLT-v1/ALCARECO','109146']
        
        for field in fields:
            row = Frame(root)                           # make a new row
            lab = Label(row, width=20, text=field)       # add label, entry
            ent = Entry(row)
            ent.insert(0, default[i])
            row.pack(side=TOP, fill=X)                  # pack row on top
            lab.pack(side=LEFT)
            ent.pack(side=RIGHT, expand=YES, fill=X)    # grow horizontal
            entries.append(ent)
            i = i + 1
        return entries
     
if __name__ == '__main__': Demo().mainloop()

