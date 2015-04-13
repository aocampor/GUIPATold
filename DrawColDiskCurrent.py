#! /usr/bin/env python

##import commands
import sys, os, string, fileinput, math
from math import sqrt, atan
import time
from Tkinter import *
from CurrentMonitoringDisk import CurrentMonitoring
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
############ LEGEND ####################

        self.canvas.create_text(750,10,text='Legend for single parameter',font=('times',15,'bold italic'))
        
        self.canvas.create_rectangle(620,50,690,55, outline='black', fill='green')
        self.canvas.create_text(850,52.5,text='Variable in proper range',font=('times',11,'bold italic'))
        self.canvas.create_text(850,72.5,text='Average Current < 7.0 uA, no variation > 1.0 uA',font=('times',11,'italic'))
        self.canvas.create_text(850,92.5,text='Average Temperature < 23°, no variation > 5°',font=('times',11,'italic'))

        self.canvas.create_rectangle(620,220,690,225, outline='black', fill='red')
        self.canvas.create_text(850,222.5,text='Variable out of proper range',font=('times',11,'bold italic'))
        self.canvas.create_text(850,242.5,text='Average Current > 7.0 uA or variation > 1 uA',font=('times',11,'italic'))
        self.canvas.create_text(850,262.5,text='Average Temperature > 23° or variation > 5°',font=('times',11,'italic'))

        self.canvas.create_rectangle(620,310,690,315, outline='black', fill='black')
        self.canvas.create_text(850,312.5,text='Double Gap is missing',font=('times',11,'bold italic'))

        self.canvas.create_text(750,350,text='Legend for all parameters',font=('times',15,'bold italic'))
        
        self.canvas.create_rectangle(620,390,690,395, outline='black', fill='green')
        self.canvas.create_text(850,392.5,text='Variable in proper range',font=('times',11,'bold italic'))

        self.canvas.create_rectangle(620,410,690,415, outline='black', fill='pink')
        self.canvas.create_text(850,412.5,text='Temperature is absent but current is ok',font=('times',11,'bold italic'))

        self.canvas.create_rectangle(620,430,690,435, outline='black', fill='orange')
        self.canvas.create_text(850,432.5,text='One of variable out of proper range',font=('times',11,'bold italic'))
        self.canvas.create_text(850,242.5,text='Average Current > 7.0 uA or variation > 1 uA',font=('times',11,'italic'))
        self.canvas.create_text(850,262.5,text='Average Temperature > 23° or variation > 5°',font=('times',11,'italic'))
        
        self.canvas.create_rectangle(620,450,690,455, outline='black', fill='red')
        self.canvas.create_text(850,452.5,text='All variables out of proper range',font=('times',11,'bold italic'))
        self.canvas.create_text(850,242.5,text='Average Current > 7.0 uA or variation > 1 uA',font=('times',11,'italic'))
        self.canvas.create_text(850,262.5,text='Average Temperature > 23° or variation > 5°',font=('times',11,'italic'))
        
        self.canvas.create_rectangle(620,470,690,475, outline='black', fill='black')
        self.canvas.create_text(850,472.5,text='Double Gap is missing',font=('times',11,'bold italic'))
        
        
#######################################
        
        for (key, value) in self.demosBarrel.items():
            self.bt1 = Button(self, text=key, command=value).pack(side=TOP, fill=BOTH)
        
        cmd = "pwd"
        homedir = [item[:-1] for item in os.popen(cmd)]
        f=open(str(homedir[0])+'/disk_coord.txt', 'r')
        
        for line in f:
            coord = line.rstrip().split("  ")
            detname = self.Wheel+'_' + coord[0]

            print detname,self.currentMonitor.getValues(detname)
            
            if self.currentMonitor.getValues(detname) != 0 and self.currentMonitor.getValuesTemp(detname) != 0:
                colour = self.setColour(self.currentMonitor.getValues(detname), self.currentMonitor.getValuesTemp(detname))
            elif self.currentMonitor.getValues(detname) != 0 and self.currentMonitor.getValuesTemp(detname) == 0:
                colour = 'pink'
            elif self.currentMonitor.getValues(detname) == 0:
                colour = 'black'

            pol=self.canvas.create_polygon(20+0.85*int(coord[1]),-5+0.85*int(coord[2]),20+0.85*int(coord[3]),
                                           -5+0.85*int(coord[4]),20+0.85*int(coord[5]),-5+0.85*int(coord[6]),
                                           20+0.85*int(coord[7]),-5+0.85*int(coord[8]), outline='black', fill=colour)
            
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

                if self.currentMonitor.getValuesTemp(self.Wheel+'_'+selected_ch) != 0:
                    t2 = self.currentMonitor.getMapElementTemp(self.Wheel+'_'+selected_ch)[0]
                    temp = self.currentMonitor.getMapElementTemp(self.Wheel+'_'+selected_ch)[1]
                else:
                    t2 = [0]
                    temp = [0]

                dp = DisplayPlots(selected_ch,t1,curr,selected_ch,t2,temp)
                dp.plotHisto()
            except TypeError:
                pass


    def fillMap(self):

        cmd = "pwd"
        homedir = [item[:-1] for item in os.popen(cmd)]
        f=open(str(homedir[0])+'/disk_coord.txt', 'r')
        
        detMap = {}
        for line in f:
            coord = line.rstrip().split("  ")
            chname = ''
            pos = [ int(coord[1]),int(coord[2]),int(coord[3]),int(coord[4]),int(coord[5]),int(coord[6]),int(coord[7]),int(coord[8]) ]
            detMap[str(coord[0])] = pos
            
        return detMap

              
    def indet(self,x1,y1,x2,y2,x3,y3,x4,y4,x,y):
        
        inside = False
        x0 = 296.675
        y0 = 276.35
        
        x1 = 20 +0.85*x1
        x2 = 20 +0.85*x2
        x3 = 20 +0.85*x3
        x4 = 20 +0.85*x4
        
        y1 = (-5 +0.85*y1) 
        y2 = (-5 +0.85*y2) 
        y3 = (-5 +0.85*y3) 
        y4 = (-5 +0.85*y4)
        
        X = [x1,x2,x3,x4]
        X.sort()
        Y = [y1,y2,y3,y4]
        Y.sort()

        mediumX = (X[3]+X[0])/2
        mediumY = (Y[3]+Y[0])/2
        
        R = [sqrt((x1-x0)*(x1-x0)+(y1-y0)*(y1-y0)),sqrt((x2-x0)*(x2-x0)+(y2-y0)*(y2-y0)),sqrt((x3-x0)*(x3-x0)+(y3-y0)*(y3-y0)),sqrt((x4-x0)*(x4-x0)+(y4-y0)*(y4-y0))]
        R.sort()

        phi1 = 0.
        phi2 = 0.
        phi3 = 0.
        phi4 = 0.
        mediumPhi = 0.

        if mediumX-x0>0 and mediumY-y0>=0:
            mediumPhi = atan((mediumY-y0)/(mediumX-x0))
        elif mediumX-x0>0 and mediumY-y0<0:
            mediumPhi = atan((mediumY-y0)/(mediumX-x0))+2*3.14
        elif mediumX-x0<0:
            mediumPhi = atan((mediumY-y0)/(mediumX-x0))+3.14
        elif mediumX-x0==0 and mediumY-y0>0:
            mediumPhi = 3.14/2
        elif mediumX-x0==0 and mediumY-y0<0:
            mediumPhi = 3*3.14/2
        
        if x1-x0>0 and y1-y0>=0:
            phi1 = atan((y1-y0)/(x1-x0))
        elif x1-x0>0 and y1-y0<0:
            phi1 = atan((y1-y0)/(x1-x0))+2*3.14
        elif x1-x0<0:
            phi1 = atan((y1-y0)/(x1-x0))+3.14
        elif x1-x0==0 and y1-y0>0:
            phi1 = 3.14/2
        elif x1-x0==0 and y1-y0<0:
            phi1 = 3*3.14/2

        if x2-x0>0 and y2-y0>=0:
            phi2 = atan((y2-y0)/(x2-x0))
        elif x2-x0>0 and y2-y0<0:
            phi2 = atan((y2-y0)/(x2-x0))+2*3.14
        elif x2-x0<0:
            phi2 = atan((y2-y0)/(x2-x0))+3.14
        elif x2-x0==0 and y2-y0>0:
            phi2 = 3.14/2
        elif x2-x0==0 and y2-y0<0:
            phi2 = 3*3.14/2

        if x3-x0>0 and y3-y0>=0:
            phi3 = atan((y3-y0)/(x3-x0))
        elif x3-x0>0 and y3-y0<0:
            phi3 = atan((y3-y0)/(x3-x0))+2*3.14
        elif x3-x0<0:
            phi3 = atan((y3-y0)/(x3-x0))+3.14
        elif x3-x0==0 and y3-y0>0:
            phi3 = 3.14/2
        elif x3-x0==0 and y3-y0<0:
            phi3 = 3*3.14/2

        if x4-x0>0 and y4-y0>=0:
            phi4 = atan((y4-y0)/(x4-x0))
        elif x4-x0>0 and y4-y0<0:
            phi4 = atan((y4-y0)/(x4-x0))+2*3.14
        elif x4-x0<0:
            phi4 = atan((y4-y0)/(x4-x0))+3.14
        elif x4-x0==0 and y4-y0>0:
            phi4 = 3.14/2
        elif x4-x0==0 and y4-y0<0:
            phi4 = 3*3.14/2

        PHI = [phi1,phi2,phi3,phi4]
        PHI.sort()
        
        r = sqrt((x-x0)*(x-x0)+(y-y0)*(y-y0))
        phi = 0.
        if x-x0>0 and y-y0>=0:
            phi = atan((y-y0)/(x-x0))
        elif x-x0>0 and y-y0<0:
            phi = atan((y-y0)/(x-x0))+2*3.14
        elif x-x0<0:
            phi = atan((y-y0)/(x-x0))+3.14
        elif x-x0==0 and y-y0>0:
            phi = 3.14/2
        elif x-x0==0 and y-y0<0:
            phi = 3*3.14/2

        if  R[0] <= r <= R[3] and (PHI[3]-PHI[0]) < 1:
            if PHI[0] <= phi <= PHI[3] and PHI[0] <= phi <= PHI[3]:
                inside = True
        elif R[0] <= r <= R[3] and (PHI[3]-PHI[0]) > 1:
            if 0 <= phi <= PHI[0] or  PHI[2] <= phi <= 6.28:
                inside = True

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
        f=open(str(homedir[0])+'/disk_coord.txt', 'r')

        if par_type == 'All':

            for line in f:
                coord = line.rstrip().split("  ")
                detname = self.Wheel+'_' + coord[0]

                if self.currentMonitor.getValues(detname) != 0 and self.currentMonitor.getValuesTemp(detname) != 0:
                    colour = self.setColour(self.currentMonitor.getValues(detname),self.currentMonitor.getValuesTemp(detname))
                elif self.currentMonitor.getValues(detname) != 0 and self.currentMonitor.getValuesTemp(detname) == 0:
                    colour = 'pink'    
                elif self.currentMonitor.getValues(detname) == 0:
                    colour = 'black'

                pol=self.canvas.create_polygon(20+0.85*int(coord[1]),-5+0.85*int(coord[2]),20+0.85*int(coord[3]),
                                               -5+0.85*int(coord[4]),20+0.85*int(coord[5]),-5+0.85*int(coord[6]),
                                               20+0.85*int(coord[7]),-5+0.85*int(coord[8]), outline='black', fill=colour)    
                self.canvas.bind('<Double-1>', self.click_canvasNew)

        if par_type == 'Current':

            for line in f:
                coord = line.rstrip().split("  ")
                detname = self.Wheel+'_' + coord[0]
                if self.currentMonitor.getValues(detname) != 0:
                    colour = self.setColourCurrent(self.currentMonitor.getValues(detname))
                else:
                    colour = 'black'

                pol=self.canvas.create_polygon(20+0.85*int(coord[1]),-5+0.85*int(coord[2]),20+0.85*int(coord[3]),
                                               -5+0.85*int(coord[4]),20+0.85*int(coord[5]),-5+0.85*int(coord[6]),
                                               20+0.85*int(coord[7]),-5+0.85*int(coord[8]), outline='black', fill=colour)    

                self.canvas.bind('<Double-1>', self.click_canvasNew)

        if par_type == 'Temp':

            for line in f:
                coord = line.rstrip().split("  ")
                detname = self.Wheel+'_' + coord[0]

                if self.currentMonitor.getValuesTemp(detname) != 0:
                    colour = self.setColourTemp(self.currentMonitor.getValuesTemp(detname))
                else:
                    colour = 'black'

                pol=self.canvas.create_polygon(20+0.85*int(coord[1]),-5+0.85*int(coord[2]),20+0.85*int(coord[3]),
                                               -5+0.85*int(coord[4]),20+0.85*int(coord[5]),-5+0.85*int(coord[6]),
                                               20+0.85*int(coord[7]),-5+0.85*int(coord[8]), outline='black', fill=colour) 

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
