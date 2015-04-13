#! /usr/bin/env python
from Tkinter import *
from quitter import Quitter
import os
from sys import argv

import tkFileDialog 
import tkSimpleDialog
from tkFileDialog   import askopenfilename        # get standard dialogs
from DrawColWheel import DrawWheel


class Demo(Frame):

    def __init__(self, parent=None):
        Frame.__init__(self, parent)
        self.pack()
##        Label(self, text="Load Root File for Analysis").pack()

        self.counter = 0
        self.var = IntVar()
        self.var = 0
        self.ck = Checkbutton(self,
                         text='RFIO',    
                         variable=self.var,
                         command=(lambda: self.addRFIO())).pack(side=RIGHT)

        self.bt1 = Button(self, text='Open and Load File', command=self.AskOpenFile).pack(side=RIGHT) ##, fill=BOTH)

        self.fields = ['DataSet','Run Number']
        self.ents = self.makeform(self, self.fields)
        self.FileName = ''
 

        self.bind('<Return>', (lambda event: self.fetch(self.ents)))   
        self.btn = Button(self, text='Load Root File', 
                    command= (lambda: self.fetch(self.ents))).pack(side=TOP)

        demosBarrel = {
            'Wheel +2': lambda: self.selectDet(self.FileName,'W+2'),
            'Wheel +1': lambda: self.selectDet(self.FileName,'W+1'),
            'Wheel 0': lambda: self.selectDet(self.FileName,'W+0'),
            'Wheel -1': lambda: self.selectDet(self.FileName,'W-1'),
            'Wheel -2': lambda: self.selectDet(self.FileName,'W-2'),
            }

        demosEndCap = {
            'Disk -1': lambda: self.selectDetDisk(self.FileName,'RE-1'),
            'Disk -2': lambda: self.selectDetDisk(self.FileName,'RE-2'),
            'Disk -3': lambda: self.selectDetDisk(self.FileName,'RE-3'), 
            'Disk +1': lambda: self.selectDetDisk(self.FileName,'RE+1'),
            'Disk +2': lambda: self.selectDetDisk(self.FileName,'RE+2'),
            'Disk +3': lambda: self.selectDetDisk(self.FileName,'RE+3')
            }


        pos = [TOP,LEFT,RIGHT,LEFT,TOP]
        i = 0
        for (key, value) in demosBarrel.items():
            Button(self, text=key, command=value).pack(side=TOP, fill=BOTH)
            i += 1
            
        for (key, value) in demosEndCap.items():
            Button(self, text=key, command=value).pack(side=BOTTOM, fill=BOTH)

    def makeform(self,root, fields):
        entries = []
        i = 0
        default = ['Insert Dataset name','Insert Run Number']

        for field in fields:
            row = Frame(root)                           # make a new row
            lab = Label(row, width=10, text=field)       # add label, entry
            ent = Entry(row)
            ent.insert(0, default[i])
            row.pack(side=TOP, fill=X)                  # pack row on top
            lab.pack(side=LEFT)
            ent.pack(side=RIGHT, expand=YES, fill=X)    # grow horizontal
            entries.append(ent)
            i = i + 1
        return entries

    def addRFIO(self):
        self.counter +=1
        
        if self.counter%2 == 0: self.var = 0
        elif self.counter%2 != 0: self.var = 1

    def fetch(self,entries):
        filename = ''
        inp = []
        for entry in entries:
            inp.append(entry.get())

        ds = str(str(inp[0]).replace('/',"")).strip()
        if self.var == 0:
            filename = '/tmp/trentad/'+ ds +'/'+str(inp[1])+'/root/Merge_tot.root'
            self.FileName = filename
        elif self.var == 1:
            self.FileName = 'rfio:/store/caf/user/ccmuon/RPC/GlobalRuns/'+ds +'/'+str(inp[1])+'/root/Merge_tot_new.root'

    def AskOpenFile(self, title='Choose File', mode='rb', initialdir='.', filetypes=None):
        if filetypes==None:
            filetypes = [
                ('Text File','*.txt'),
                ('Data File','*.dat'),
                ('Output File','*.out'),
                ('Any File','*.*')]
        
        fileobj = askopenfilename(filetypes=[("all files", "*")])
        self.FileName = str(fileobj) # <-- an opened file, or the value None


    def selectDet(self,file_name,wheel):
        cmd = './DrawColWheel.py ' + str(file_name) + ' ' + str(wheel) +'&'
        os.system(cmd)


    def selectDetDisk(self,file_name,wheel):
        cmd = './DrawColDisk.py ' + str(file_name) + ' ' + str(wheel) +'&'
        os.system(cmd)

                        
if __name__ == '__main__': Demo().mainloop()

