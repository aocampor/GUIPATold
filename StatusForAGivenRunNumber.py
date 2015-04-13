#! /usr/bin/env python
from Tkinter import *
import commands
import sys, os, string, fileinput

class ScrolledList(Frame):
    def __init__(self, options, parent=None):
        Frame.__init__(self, parent)
        self.pack(expand=YES, fill=BOTH)
        self.makeWidgets(options)

    def handleList(self, event):
        index = self.listbox.curselection()
        label = self.listbox.get(index)
        self.runCommand(label)

    def makeWidgets(self, options):
        sbar = Scrollbar(self)
        list = Listbox(self, relief=SUNKEN)
        sbar.config(command=list.yview)
        list.config(yscrollcommand=sbar.set)
        sbar.pack(side=RIGHT, fill=Y)
        list.pack(side=LEFT, expand=YES, fill=BOTH)
        pos = 0
        for label in options:
            list.insert(pos, label)
            pos = pos + 1
        list.bind('<Double-1>', self.handleList)
        self.listbox = list

    def runCommand(self, selection):
        print 'You selected:', selection

class ScrolledCanvas(Frame):
    def __init__(self, parent=None, color='gray'):
        Frame.__init__(self, parent)
        self.pack(expand=YES, fill=BOTH)
        canv = Canvas(self, bg=color, relief=SUNKEN)
        canv.config(width=600, height=300)
        canv.config(scrollregion=(0,0,1000,1000))
        canv.config(highlightthickness=0)
        
        sbar = Scrollbar(self)
        sbar.config(command=canv.yview)
        canv.config(yscrollcommand=sbar.set)
        sbar.pack(side=RIGHT, fill=Y)
        canv.pack(side=LEFT, expand=YES, fill=BOTH)
    
        canv.create_text(300, 20, text='Status ', fill='black')

        ds = str(sys.argv[1]).replace('/','')
        path1 = '/castor/cern.ch/cms/store/caf/user/ccmuon/RPC/GlobalRuns/' + ds + '/' + str(sys.argv[2]) + '/' + 'root/'
        print path1

        cmd = "echo $HOME"
        cmd1= './aSearchCLI --dbsInst=cms_dbs_prod_global --limit=10000 --input \" find file where dataset = ' + str(sys.argv[1]) + ' and run = ' + str(sys.argv[2]) + ' \" | egrep \"[a-Z]\" | grep \-v \"Found\" | wc | awk \'{print $1}\'| awk \'{print $1}\''
        num = [item[:-1] for item in os.popen(cmd1)]
        canv.create_text(10, 40, text='Number of Jobs to submit: ' + str(num[0]), fill='black',anchor='w')
        cmd3 = 'rfdir ' + path1 + ' | grep SRPC | grep -v Merge | wc | awk \'{print $1}\''
        nums = [item[:-1] for item in os.popen(cmd3)]
        canv.create_text(10, 60, text='Number of Finished jobs for Efficiency: ' + str(nums[0]), fill='black', anchor ='w')
        cmd4 = 'rfdir ' + path1 + ' | grep DQM | grep -v Merge | wc | awk \'{print $1}\''
        numd = [item[:-1] for item in os.popen(cmd4)]
        canv.create_text(10, 80, text='Number of Finished for DQM: ' + str(numd[0]), fill='black', anchor ='w')
        cmd5 = 'bjobs | wc | awk \'{print $1}\''
        still = [item[:-1] for item in os.popen(cmd5)]
        canv.create_text(10, 100, text='Number of jobs still running ' + str(still[0]), fill='black', anchor ='w')

                                                            
        canv.bind('<Double-1>', self.onDoubleClick)       # set event handler
        self.canvas = canv
        
    def onDoubleClick(self, event):
        print event.x, event.y
        print self.canvas.canvasx(event.x), self.canvas.canvasy(event.y)
                
#
# main
#
if __name__ == "__main__": 

   
    ScrolledCanvas().mainloop()

    
#    job_finalpath = str(homedir[0]) + '/scratch2/'+ str(sys.argv[2]) + '/job/job_info.txt'
#    job_finalpath1 = str(homedir[0]) + '/scratch2/'+ str(sys.argv[2]) + '/job/job_tmp.txt'
#    print job_finalpath
#    cmd2 = 'touch ' + job_finalpath1 
#    os.system(cmd2)
#    file = open(job_finalpath,'r')
    #root = Tk()
    
#    for line in file.readlines():
#        line1 = line.split("<")[1]
#        jobId = line1.split(">")[0]
#        cmd1 = 'bjobs ' + jobId
#        status = [item[:-1] for item in os.popen(cmd1)]
#        print status
#        if (status == None ):
#            cmd3 = 'echo "Job Finished" >> ' + job_finalpath1
#            os.system(cmd3)
#        else:    
#            status1 = str(status[1])
#            print status1
           #w = Label(root, text = status1)
            #w.pack()
#            options = map((lambda x: status1), range(1))
#    ScrolledList(options).mainloop()    
    #root.mainloop()
    
#    file.close()



















