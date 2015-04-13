#! /usr/bin/env python
from Tkinter import *
from quitter import Quitter
import os

class ScrolledList(Frame):
    def __init__(self, options, heigth, width,parent=None):
        my_window = Toplevel()
        Frame.__init__(self, my_window)
        self.pack(expand=YES, fill=BOTH)
        self.makeWidgets(options, heigth, width)
    def handleList(self, event):
        index = self.listbox.curselection()               # on list double-click
        label = self.listbox.get(index)                   # fetch selection text
        self.runCommand(label)                            # and call action here
    def makeWidgets(self, options, heigth, width):                       # or get(ACTIVE)
        sbar = Scrollbar(self)
        list = Listbox(self, relief=SUNKEN)
        sbar.config(command=list.yview)                   # xlink sbar and list
        list.config(yscrollcommand=sbar.set)              # move one moves other
        sbar.pack(side=RIGHT, fill=Y)                     # pack first=clip last
        list.pack(side=LEFT, expand=1, fill=BOTH, ipadx =width, ipady =heigth)         # list clipped first
        pos = 0
        for label in options:                             # add to list-box
            list.insert(pos, label)                       # or insert(END,label)
            pos += 1
       #list.config(selectmode=SINGLE, setgrid=1)         # select,resize modes
        list.bind('<Double-1>', self.handleList)          # set event handler
        self.listbox = list

    def runCommand(self, selection):                      # redefine me lower
        try:
            first= int(selection)
            cmd = './aSearchCLI --dbsInst=cms_dbs_prod_global --input \"find file where run = ' + selection + '" --limit=-1 '
            the_files = [item[:-1] for item in os.popen(cmd)]
            ScrolledList(the_files,200,300).pack()
            return 1
        except ValueError:
            cmd =  './aSearchCLI --dbsInst=cms_dbs_prod_global --limit=-1 --input \"find run where dataset like ' + selection + ' \" '
            the_files = [item[:-1] for item in os.popen(cmd)]
            the_files.sort() 
            ScrolledList(the_files,100,50).mainloop()
            return 0


class Demo(Frame):
##    def __init__(self, options, parent=None):
    def __init__(self, parent=None):
        my_window = Toplevel()
        Frame.__init__(self, my_window)
        self.pack(expand=YES, fill=BOTH)
        Label(self, text="Search Dataset").pack()
        self.ent = Entry(self)
        self.ent.insert(0, 'Cosmics')                   # set text
        self.ent.pack(side=TOP, fill=X)                         # grow horiz
        self.ent.focus()                                        # save a click
        self.ent.bind('<Return>', (lambda event: self.fetch()))      # on enter key
        self.btn = Button(self, text='Search', command=self.fetch)    # and on button 
        self.btn.pack(side=TOP)
    
    def fetch(self):
        cmd =  './aSearchCLI --dbsInst=cms_dbs_prod_global --limit=-1 --input \"find dataset where dataset like ' + '*' +self.ent.get() + '*' + '\" | egrep \"[a-Z]\" | grep -v \"Found\" '
        the_files = [item[:-1] for item in os.popen(cmd)]
        
        ScrolledList(the_files,200,300).mainloop()
        
if __name__ == '__main__': Demo().mainloop()
