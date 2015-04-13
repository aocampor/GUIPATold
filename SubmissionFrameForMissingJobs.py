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
        Label(self, text="Submit jobs for Run Number").pack()

        self.fields = 'CMSSW Release', 'Dataset', 'Run Number'
        self.ents = self.makeform(self, self.fields)
        self.bind('<Return>', (lambda event: self.fetch(self.ents)))   
        self.btn = Button(self, text='Submit', 
                    command= (lambda: self.fetch(self.ents))).pack(side=TOP)

        self.var1 = IntVar()
        self.var2 = IntVar()
        self.var3 = IntVar()
        self.var4 = IntVar()
        self.var5 = IntVar()
        self.var6 = IntVar()
        self.var7 = IntVar()        
        
        self.ck1 = Checkbutton(self,
                               text='Efficiency by STAMuon',    
                               variable=self.var1,
                               command=(lambda: self.report() )).pack(side=LEFT)

        self.ck2 = Checkbutton(self,
                               text='Efficiency by DT',    
                               variable=self.var2,
                               command=(lambda: self.report() )).pack(side=LEFT)

        self.ck3 = Checkbutton(self,
                               text='DQM',
                               variable=self.var3,
                               command=(lambda: self.report() )).pack(side=LEFT)

        self.ck4 = Checkbutton(self,
                               text='Noise',    
                               variable=self.var4,
                               command=(lambda: self.report() )).pack(side=LEFT)

        self.ck5 = Checkbutton(self,
                               text='Trigger',    
                               variable=self.var5,
                               command=(lambda: self.report() )).pack(side=LEFT)

        self.ck6 = Checkbutton(self,
                               text='Strip Occupancy',    
                               variable=self.var6,
                               command=(lambda: self.report() )).pack(side=LEFT)

        self.ck7 = Checkbutton(self,
                               text='Trigger Efficiency',    
                               variable=self.var7,
                               command=(lambda: self.report() )).pack(side=LEFT)        


    def report(self):
        pass
##        for var in self.vars:
##            print var.get(),   # current toggle settings: 1 or 0
##        print



    def fetch(self,entries):
        try:
            inp = []
            for entry in entries:
                inp.append(entry.get())

            cmd = './filecounter.py ' + inp[0] + ' ' + inp[1] + ' ' + inp[2] + ' ' + str(self.var1.get())+ ' '+str(self.var2.get())+ ' '+str(self.var3.get())+ ' '+str(self.var4.get())+ ' '+str(self.var5.get()) + ' '+str(self.var6.get()) + ' ' +str(self.var7.get()) +'&'

            os.system(cmd)
            return 1
        except ValueError:
            tkMessageBox.showwarning(
                "Wrong input format",
                "Please insert the right input:"
                "Release: CMSSW_2_2_9"
                "Dataset: /Cosmics/Commissioning08-CRUZET4_v1/RECO"
                "Run Number: 58555"
                "Run of job to submit: 58555"
                )
            return 0

    def makeform(self,root, fields):
        entries = []
        i = 0
#       default = ['CMSSW_2_1_10','/Cosmics/Commissioning09-PromptReco-v1/RECO ','79045']
        default = ['CMSSW_3_1_0','/StreamExpress/Commissioning09-RpcCalHLT-v5/ALCARECO ','108265']
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

