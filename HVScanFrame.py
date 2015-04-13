#! /usr/bin/env python   

from Tkinter import *
from quitter import Quitter
import os
from tkMessageBox import *

from HVScan import HVScan

class Demo(Frame):
##    def __init__(self, options, parent=None):
    def __init__(self, parent=None):
        my_window = Toplevel()
        Frame.__init__(self, my_window)
        self.pack(expand=YES, fill=BOTH)
        Label(self, text="Panel for HV or Threshold scan").pack()

        self.fields = 'Dataset', '1° Run Number', '2° Run Number', '3° Run Number','4° Run Number','5° Run Number','1° HV value (Volt)','2° HV value (Volt)','3° HV value (Volt)', '4° HV value (Volt)', '5° HV value (Volt)' 
        self.ents = self.makeform(self, self.fields)
        self.bind('<Return>', (lambda event: self.fetch(self.ents)))   
        self.btn = Button(self, text='HV or Threshold scan', 
                    command= (lambda: self.fetch(self.ents))).pack(side=TOP)

    def report(self):
        pass

    def fetch(self,entries):
        try:
            inp = []
            for entry in entries:
                inp.append(entry.get())


##            runs = [str(inp[1]),str(inp[2]),str(inp[3]),str(inp[4]),str(inp[5])]
##            hvlist = [float(inp[6]),float(inp[7]),float(inp[8]),float(inp[9]),float(inp[10])]

            runs = []
            hvlist = []

            count = 0
            for i in inp:
                if  0 < count < 6 and cmp(str(i),'') != 0:
                    runs.append(str(i))
                elif count >= 6 and cmp(str(i),'') != 0:   
                    hvlist.append(float(i))
                count += 1
               
            HVScan(str(inp[0]),runs,hvlist)

            return 1
        except ValueError:
            tkMessageBox.showwarning(
                "Wrong input format",
                "Please insert the right input:"
                "Dataset: /Cosmics/Commissioning09-CRUZET4_v2/RECO"
                "1° Run Number: 69797"
                "2° Run Number: 69797"
                "3° Run Number: 69797"
                "4° Run Number: 69797"
                "5° Run Number: 69797"
                "1° HV value (Volt): 8900"
                "2° HV value (Volt): 9000"
                "3° HV value (Volt): 9100"
                "4° HV value (Volt): 9200"
                "5° HV value (Volt): 9300"
                )
            return 0


    def makeform(self,root, fields):
        entries = []
        i = 0

        default = ['/Cosmics/Commissioning08-PromptReco-v2/RECO','','','','','','8900','9000','9100','9200','9300']
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

