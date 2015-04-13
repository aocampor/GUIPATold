#! /usr/bin/env python   

from Tkinter import *
from quitter import Quitter
import sys,os,string,fileinput
from tkMessageBox import *

class Demo(Frame):
    def __init__(self, options, parent=None):
        my_window = Toplevel()
        Frame.__init__(self, my_window)
        self.pack(expand=YES, fill=BOTH)
        Label(self, text="Making noise file").pack()

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
            cdi = os.getcwd()    
            list = ['----RUN-NUMBER----',inp[1],'----RELEASE----','CMSSW_2_2_4','----WORKING-ORT----',cdi,'----DATA-SET----',inp[0]]
#            os.system('rm jobnoise_*.job')
            self.replaceStringInFile('jobnoise.job','jobnoise_' + inp[1] + '.job',list)
            os.system('chmod a+x jobnoise_*.job')
            cmd = 'bsub -q cmscaf jobnoise_' + inp[1] + '.job'
            ch = "echo $HOME"
            homedir = [item[:-1] for item in os.popen(ch)]
            job_finalpath = str(homedir[0]) + '/scratch2/'+ str(inp[1]) + '/job'
            job_cerr = job_finalpath + '/Mergeerr.cerr'
            job_cout = job_finalpath + '/Mergeout.cout'
#            cmd = 'bsub -q cmscaf -e ' + job_cerr  + ' -o ' + job_cout + '-J ' + ' MergeJobForAGivenRunNumber.py ' + inp[0] + ' ' + inp[1] + ' ' + inp[2]
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
        default = ['Insert Dataset name','Insert Run Number','-1','0']
        
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


    def replaceStringInFile(self,namein,nameout,list):
        fin=open(namein, 'r')
        fout=open(nameout, 'w')
        for line in fin:
            for ilist in range(len(list)):
                if ilist%2 == 0:
                    lineno1 = 0
                    lineno1 = string.find(line, list[ilist])
                    if lineno1 > 0:
                        line =line.replace(list[ilist], list[ilist+1])
            fout.write(line)
     
if __name__ == '__main__': Demo().mainloop()

