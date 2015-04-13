#! /usr/bin/env python   

from Tkinter import *
from quitter import Quitter
import os
from tkMessageBox import *

from StatusReport import StatusReport

class StatusReportFrame(Frame):
    def __init__(self, root_file_name,ds,run,parent=None):
        my_window = Toplevel()
        Frame.__init__(self, my_window)
        self.pack(expand=YES, fill=BOTH)
        Label(self, text="Status report frame").pack()

        self.RootFileName = root_file_name
        self.ds = ds
        self.run = run
        
        self.fields = 'Bx min', 'Bx max', 'Cls min','Cls max', 'Eff min', 'Eff max', 'Masked strip min', 'Masked strip max'
        self.ents = self.makeform(self, self.fields)
        self.bind('<Return>', (lambda event: self.fetch(self.ents)))   
        self.btn = Button(self, text='Submit', 
                    command= (lambda: self.fetch(self.ents))).pack(side=TOP)

    def report(self):
        pass

    def fetch(self,entries):
        try:
            inp = []
            for entry in entries:
                inp.append(entry.get())

            values = [str(self.ds),str(self.run)]

            for i in inp:
                values.append(float(i))

            StatusReport(self.RootFileName,values)

            return 1
        except ValueError:
            tkMessageBox.showwarning(
                "Wrong input format",
                "Please insert the right input!"
                )
            return 0


    def makeform(self,root, fields):
        entries = []
        i = 0
        default = ['-3','+3','1','10','0','100','0','90']
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
     
##if __name__ == '__main__': Demo().mainloop()

