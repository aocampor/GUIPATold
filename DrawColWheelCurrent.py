#! /usr/bin/env python

##import commands
import sys, os, string, fileinput
import time
from Tkinter import *
from CurrentMonitoring import CurrentMonitoring
from PlotDisplayForSelectedChamberCurrent import DisplayPlots

class DrawWheel(Frame):
    def __init__(self,wheel,timeStart,timeEnd,parent=None):

        Frame.__init__(self, parent)
        self.pack()
        
        self.detMap = self.fillMap()
        self.Wheel = wheel

        self.currentMonitor = CurrentMonitoring(int(timeStart),int(timeEnd))

        self.demosBarrel = {
            'Current': lambda: self.ReDrawWheel('Current'),
            'Temperature': lambda: self.ReDrawWheel('Temp'),
            'All': lambda: self.ReDrawWheel('All'),
            }

        self.canvas = Canvas(self,width =1000, height=800,bg = 'white')

        self.canvas.create_text(290,290,text=self.Wheel,font=('times',30,'bold italic'))
        
        for (key, value) in self.demosBarrel.items():
            self.bt1 = Button(self, text=key, command=value).pack(side=TOP, fill=BOTH)
        
        cmd = "pwd"
        homedir = [item[:-1] for item in os.popen(cmd)]
        f=open(str(homedir[0])+'/wheel_coord.txt', 'r')
        
        for line in f:
            coord = line.rstrip().split("  ")
            detname = self.Wheel+'_' + coord[0]

            if detname.find("out"): detname1 = detname.replace("out","in")
            if detname.find("-"): detname1 = detname1.replace("-","")
            if detname1.find("+"): detname1 = detname1.replace("+","")
            
            if self.currentMonitor.getValues(detname) != 0 and self.currentMonitor.getValuesTemp(detname1) != 0:
                colour = self.setColour(self.currentMonitor.getValues(detname), self.currentMonitor.getValuesTemp(detname1))
            elif self.currentMonitor.getValues(detname) != 0 and self.currentMonitor.getValuesTemp(detname1) == 0:
                colour = 'pink'
            elif self.currentMonitor.getValues(detname) == 0:
                colour = 'black'

            pol=self.canvas.create_polygon(20+1.05*int(coord[1]),-5+1.05*int(coord[2]),20+1.05*int(coord[3]),-5+1.05*int(coord[4]),
                                           20+1.05*int(coord[5]),-5+1.05*int(coord[6]),20+1.05*int(coord[7]),-5+1.05*int(coord[8]), outline='black', fill=colour)
            
            self.canvas.bind('<Double-1>', self.click_canvasNew)
            
        self.canvas.pack()
        
    def click_canvasNew(self,event):
        selected_ch = ''
        for k, v in self.detMap.iteritems():
            if self.indet(v[0],v[1],v[2],v[3],v[4],v[5],v[6],v[7],event.x,event.y) == True:
                selected_ch = k
                break

        if selected_ch != '':
            try:
                t1 = self.currentMonitor.getMapElement(self.Wheel+'_'+selected_ch)[0]
                curr = self.currentMonitor.getMapElement(self.Wheel+'_'+selected_ch)[1]

                if selected_ch.find("out"): selected_ch1 = selected_ch.replace("out","in")
                if selected_ch.find("-"): selected_ch1 = selected_ch1.replace("-","")
                if selected_ch1.find("+"): selected_ch1 = selected_ch1.replace("+","")

                if self.currentMonitor.getValuesTemp(self.Wheel+'_'+selected_ch1) != 0:
                    t2 = self.currentMonitor.getMapElementTemp(self.Wheel+'_'+selected_ch1)[0]
                    temp = self.currentMonitor.getMapElementTemp(self.Wheel+'_'+selected_ch1)[1]
                else:
                    t2 = [0]
                    temp = [0]

                dp = DisplayPlots(selected_ch,t1,curr,selected_ch1,t2,temp)
                dp.plotHisto()
            except TypeError:
                pass
              



    def fillMap(self):

        cmd = "pwd"
        homedir = [item[:-1] for item in os.popen(cmd)]
        f=open(str(homedir[0])+'/wheel_coord.txt', 'r')
        
        detMap = {}
        for line in f:
            coord = line.rstrip().split("  ")
            chname = ''
            pos = [ int(coord[1]),int(coord[2]),int(coord[3]),int(coord[4]),int(coord[5]),int(coord[6]),int(coord[7]),int(coord[8]) ]
            detMap[str(coord[0])] = pos
            
        return detMap
              
    def indet(self,x1,y1,x2,y2,x3,y3,x4,y4,x,y):
      inside = False
      
      x1 = 20 + 1.05*x1
      x2 = 20 + 1.05*x2
      x3 = 20 + 1.05*x3
      x4 = 20 + 1.05*x4
      
      y1 = (-5 +1.05*y1) 
      y2 = (-5 +1.05*y2) 
      y3 = (-5 +1.05*y3) 
      y4 = (-5 +1.05*y4)
          
      if x1 == x2 or x3 == x2:
        if y1 <= y <= y2 or y2 <= y <= y1:
          if x4 <= x <= x1 or x1 <= x <= x4:
            inside = True
        elif y2 <= y <= y3 or y3 <= y <= y2:
          if x1 <= x <= x2 or x2 <= x <= x1:
            inside = True
                  
      elif x1 != x2 and x3 != x2:
    
        m1 = (float(y2)-float(y1))/(float(x2)-float(x1))
        m2 = -(1/m1)
        
        k1 = []
        k2 = []
        k1.append(y2-m1*x2)
        k1.append(y3-m1*x3)
        k2.append(y2-m2*x2)
        k2.append(y1-m2*x1)
        y_k1min = m1*x+min(k1)
        y_k1max = m1*x+max(k1)
        y_k2min = m2*x+min(k2)
        y_k2max = m2*x+max(k2)

        if y_k1min <= y <= y_k1max and y_k2min <= y <= y_k2max: inside = True

      return inside

    def setColour(self,current,temp):
        colour =''
        redcol = 0
        
        if 7 < float(current[1]) or float(current[2]) > 1. or bool(current[3]):
            redcol += 1
        if 23 < float(temp[1]) or float(temp[2]) > 1. or bool(temp[3]):
            redcol += 1

        if redcol == 0: colour = 'green'
        if redcol == 1: colour = 'orange'
        if redcol == 2: colour = 'red'
        
        return colour

    def setColourCurrent(self,current):
        colour =''

        if 7 < float(current[1]) or float(current[2]) > 1. or bool(current[3]):
            colour = 'red'
        else:
            colour = 'green'

        return colour

    def setColourTemp(self,temp):
        colour =''
        
        if 23 < float(temp[1]) or float(temp[2]) > 1. or bool(temp[3]):
            colour = 'red'
        else:
            colour = 'green'

        return colour

    def ReDrawWheel(self,par_type):

        for (key, value) in self.demosBarrel.items():
            self.bt1 = Button(self, text=key, command=value).pack(side=TOP, fill=BOTH)

        cmd = "pwd"
        homedir = [item[:-1] for item in os.popen(cmd)]
        f=open(str(homedir[0])+'/wheel_coord.txt', 'r')

        if par_type == 'All':

            for line in f:
                coord = line.rstrip().split("  ")
                detname = self.Wheel+'_' + coord[0]

                if detname.find("out"): detname1 = detname.replace("out","in")
                if detname.find("-"): detname1 = detname1.replace("-","")
                if detname1.find("+"): detname1 = detname1.replace("+","")
                
                if self.currentMonitor.getValues(detname) != 0 and self.currentMonitor.getValuesTemp(detname1) != 0:
                    colour = self.setColour(self.currentMonitor.getValues(detname),self.currentMonitor.getValuesTemp(detname1))
                elif self.currentMonitor.getValues(detname) != 0 and self.currentMonitor.getValuesTemp(detname1) == 0:
                    colour = 'pink'    
                elif self.currentMonitor.getValues(detname) == 0:
                    colour = 'black'
                pol=self.canvas.create_polygon(20+1.05*int(coord[1]),-5+1.05*int(coord[2]),20+1.05*int(coord[3]),
                                               -5+1.05*int(coord[4]),20+1.05*int(coord[5]),-5+1.05*int(coord[6]),
                                               20+1.05*int(coord[7]),-5+1.05*int(coord[8]), outline='black', fill=colour)
                self.canvas.bind('<Double-1>', self.click_canvasNew)

        if par_type == 'Current':

            for line in f:
                coord = line.rstrip().split("  ")
                detname = self.Wheel+'_' + coord[0]
                if self.currentMonitor.getValues(detname) != 0:
                    colour = self.setColourCurrent(self.currentMonitor.getValues(detname))
                else:
                    colour = 'black'
                pol=self.canvas.create_polygon(20+1.05*int(coord[1]),-5+1.05*int(coord[2]),20+1.05*int(coord[3]),
                                               -5+1.05*int(coord[4]),20+1.05*int(coord[5]),-5+1.05*int(coord[6]),
                                               20+1.05*int(coord[7]),-5+1.05*int(coord[8]), outline='black', fill=colour)
                self.canvas.bind('<Double-1>', self.click_canvasNew)

        if par_type == 'Temp':

            for line in f:
                coord = line.rstrip().split("  ")
                detname = self.Wheel+'_' + coord[0]

                if detname.find("out"): detname1 = detname.replace("out","in")
                if detname.find("-"): detname1 = detname1.replace("-","")
                if detname1.find("+"): detname1 = detname1.replace("+","")
                
                if self.currentMonitor.getValuesTemp(detname1) != 0:
                    colour = self.setColourTemp(self.currentMonitor.getValuesTemp(detname1))
                else:
                    colour = 'black'
                pol=self.canvas.create_polygon(20+1.05*int(coord[1]),-5+1.05*int(coord[2]),20+1.05*int(coord[3]),
                                               -5+1.05*int(coord[4]),20+1.05*int(coord[5]),-5+1.05*int(coord[6]),
                                               20+1.05*int(coord[7]),-5+1.05*int(coord[8]), outline='black', fill=colour)
                self.canvas.bind('<Double-1>', self.click_canvasNew)

        self.canvas.pack()

#
# main
#

if __name__ == "__main__": 

##    timeStart = time.mktime((2008, 11, 9, 4, 10, 0,0,0,0))
##    timeEnd = time.mktime((2008, 11, 10, 5, 10, 0,0,0,0))

##    timeStart = time.mktime((2008, 11, 9, 4, 10, 0,0,0,0))
##    timeEnd = time.mktime((2008, 11, 10, 5, 10, 0,0,0,0))

##    DrawWheel('W2',time.mktime((2009, 05, 30, 2, 0, 0,0,0,0)),time.mktime((2009, 05, 31, 5, 10, 0,0,0,0))).mainloop()

##    print "DrawCol",sys.argv[1],sys.argv[2],sys.argv[3]
    
    DrawWheel(sys.argv[1],sys.argv[2],sys.argv[3]).mainloop()
