#! /usr/bin/env python
import commands
import sys, os, string, fileinput
from Tkinter import *
from QualityPerformance import Diagnostic
from ROOT import TCanvas,TH1F,gROOT,TFile,gDirectory
from PlotDisplayForSelectedChamber import DisplayPlots

class DrawWheel(Frame):
    def __init__(self,root_file_name,wheel,parent=None):

        Frame.__init__(self, parent)
        self.pack()

        self.detMap = self.fillMap()
        self.Wheel = wheel
        self.RootFileName = root_file_name

        self.demosBarrel = {
            'Bunch Crossing': lambda: self.ReDrawWheel('Bunch Crossing'),
            'Cluster Size': lambda: self.ReDrawWheel('Cluster Size'),
            'Efficiency': lambda: self.ReDrawWheel('Efficiency'),
            'Noise': lambda: self.ReDrawWheel('Noise'),
            'Masked Strips': lambda: self.ReDrawWheel('Masked Strips'),
            'All Parameters': lambda: self.ReDrawWheel('All Parameters')
            }
       
        self.canvas = Canvas(self,width =1000, height=800,bg = 'white')

        self.canvas.create_text(290,290,text=self.Wheel,font=('times',30,'bold italic'))

############ LEGEND ####################
        self.canvas.create_text(750,10,text='Legend for single parameter',font=('times',15,'bold italic'))
        
        self.canvas.create_rectangle(620,50,690,55, outline='black', fill='green')
        self.canvas.create_text(850,52.5,text='Variable in proper range',font=('times',11,'bold italic'))
        self.canvas.create_text(850,72.5,text='-1.0 < Bx < 1.0',font=('times',11,'italic'))
        self.canvas.create_text(850,92.5,text='Cls < 2.5',font=('times',11,'italic'))
        self.canvas.create_text(850,112.5,text='90% < Eff < 100%',font=('times',11,'italic'))
       # self.canvas.create_text(850,132.5,text='Noise <= 1.0 Hz/cm2',font=('times',11,'italic'))
        
        self.canvas.create_rectangle(620,135,690,140, outline='black', fill='yellow')
        self.canvas.create_text(850,135.5,text='1 DG with variable out of proper range',font=('times',11,'bold italic'))
        self.canvas.create_text(850,155.5,text='Bx < -1.0 or Bx > 1.0',font=('times',11,'italic'))
        self.canvas.create_text(850,177.5,text='Cls > 2.5',font=('times',11,'italic'))
        self.canvas.create_text(850,195.5,text='Eff < 90%',font=('times',11,'italic'))
       # self.canvas.create_text(850,232.5,text='Noise > 1.0 Hz/cm2',font=('times',11,'italic'))

        self.canvas.create_rectangle(620,220,690,225, outline='black', fill='red')
        self.canvas.create_text(850,222.5,text='2/3 DG with variable out of proper range',font=('times',11,'bold italic'))
        self.canvas.create_text(850,242.5,text='Bx < -1.0 or Bx > 1.0',font=('times',11,'italic'))
        self.canvas.create_text(850,262.5,text='Cls > 2.5',font=('times',11,'italic'))
        self.canvas.create_text(850,282.5,text='Eff < 90%',font=('times',11,'italic'))
#        self.canvas.create_text(850,332.5,text='Noise > 1.0 Hz/cm2',font=('times',11,'italic'))

        self.canvas.create_rectangle(620,310,690,315, outline='black', fill='black')
        self.canvas.create_text(850,312.5,text='At least one DG is missing',font=('times',11,'bold italic'))

        self.canvas.create_text(750,350,text='Legend for all parameters',font=('times',15,'bold italic'))
        
        self.canvas.create_rectangle(620,390,690,395, outline='black', fill='green')
        self.canvas.create_text(850,392.5,text='Variable in proper range',font=('times',11,'bold italic'))

        self.canvas.create_rectangle(620,410,690,415, outline='black', fill='yellow')
        self.canvas.create_text(850,412.5,text='1 DG with variable out of proper range',font=('times',11,'bold italic'))

        self.canvas.create_rectangle(620,430,690,435, outline='black', fill='orange')
        self.canvas.create_text(850,432.5,text='2 DG with variable out of proper range',font=('times',11,'bold italic'))

        self.canvas.create_rectangle(620,450,690,455, outline='black', fill='red')
        self.canvas.create_text(850,452.5,text='3 DG with variable out of proper range',font=('times',11,'bold italic'))

        self.canvas.create_rectangle(620,470,690,475, outline='black', fill='black')
        self.canvas.create_text(850,472.5,text='At least one DG is missing',font=('times',11,'bold italic'))
        
        
#######################################

        self.diagn = Diagnostic(self.RootFileName)

        numsta = self.diagn.getStatistics('Statistics')
        self.canvas.create_text(290,330,text='Statistics ' +str(int(numsta)),font=('times',15,'bold italic'))
        
        for (key, value) in self.demosBarrel.items():
            self.bt1 = Button(self, text=key, command=value).pack(side=TOP, fill=BOTH)

        cmd = "pwd"
        homedir = [item[:-1] for item in os.popen(cmd)]
        f=open(str(homedir[0])+'/wheel_coord.txt', 'r')

        for line in f:
            coord = line.rstrip().split("  ")
            histoname_bx = 'BXN_'+self.Wheel+'_' + coord[0]
            histoname_cls = 'ClusterSize_'+self.Wheel+'_'+coord[0]
            histoname_occ = 'Occupancy_'+self.Wheel+'_'+coord[0]
            histoname_Eff = 'LocalEfficiencyFromSegments_'+self.Wheel+'_' + coord[0]
            colour = self.diagn.setColour(self.diagn.getMeanValue(histoname_bx),self.diagn.getMeanValue(histoname_cls),self.diagn.getNoise(histoname_bx),self.diagn.getMedia(histoname_Eff),self.diagn.getMaskedStrip(histoname_occ))

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
          dp = DisplayPlots(sys.argv[1])
          dp.plotHisto(sys.argv[2]+'_'+selected_ch)


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


    def ReDrawWheel(self,par_type):

        for (key, value) in self.demosBarrel.items():
            self.bt1 = Button(self, text=key, command=value).pack(side=TOP, fill=BOTH)

        cmd = "pwd"
        homedir = [item[:-1] for item in os.popen(cmd)]
        f=open(str(homedir[0])+'/wheel_coord.txt', 'r')

        if par_type == 'Bunch Crossing':

            for line in f:
                coord = line.rstrip().split("  ")
                histoname_bx = 'BXN_'+self.Wheel+'_' + coord[0]
                colour = self.diagn.setColourBx(self.diagn.getMeanValue(histoname_bx))
                pol=self.canvas.create_polygon(20+1.05*int(coord[1]),-5+1.05*int(coord[2]),20+1.05*int(coord[3]),
                                               -5+1.05*int(coord[4]),20+1.05*int(coord[5]),-5+1.05*int(coord[6]),
                                               20+1.05*int(coord[7]),-5+1.05*int(coord[8]), outline='black', fill=colour)
#                self.canvas.create_rectangle(260,330,320,350, outline='white', fill='white')
 #               self.canvas.create_text(290,340,text='Bunch Crossing',font=('times',15,'bold italic'))
                self.canvas.bind('<Double-1>', self.click_canvasNew)

        elif par_type == 'Cluster Size':

            for line in f:
                coord = line.rstrip().split("  ")
                histoname_cls = 'ClusterSize_'+self.Wheel+'_' + coord[0]
                colour = self.diagn.setColourCls(self.diagn.getMeanValue(histoname_cls))
                pol=self.canvas.create_polygon(20+1.05*int(coord[1]),-5+1.05*int(coord[2]),20+1.05*int(coord[3]),
                                               -5+1.05*int(coord[4]),20+1.05*int(coord[5]),-5+1.05*int(coord[6]),
                                               20+1.05*int(coord[7]),-5+1.05*int(coord[8]), outline='black', fill=colour)
  #              self.canvas.create_text(290,340,text='Cluster Size',font=('times',15,'bold italic'))
                self.canvas.bind('<Double-1>', self.click_canvasNew)

        elif par_type == 'Noise':
            for line in f:
                coord = line.rstrip().split("  ")
                histoname_bx = 'BXN_'+self.Wheel+'_' + coord[0]
                colour = self.diagn.setColourNoise(self.diagn.getNoise(histoname_bx))
                pol=self.canvas.create_polygon(20+1.05*int(coord[1]),-5+1.05*int(coord[2]),20+1.05*int(coord[3]),
                                               -5+1.05*int(coord[4]),20+1.05*int(coord[5]),-5+1.05*int(coord[6]),
                                               20+1.05*int(coord[7]),-5+1.05*int(coord[8]), outline='black', fill=colour)
   #             self.canvas.create_text(290,340,text='Noise',font=('times',15,'bold italic'))
                self.canvas.bind('<Double-1>', self.click_canvasNew)


        elif par_type == 'Efficiency':
            for line in f:
                coord = line.rstrip().split("  ")
                histoname_Eff = 'LocalEfficiencyFromSegments_'+self.Wheel+'_' + coord[0]
                colour = self.diagn.setColourEff(self.diagn.getMedia(histoname_Eff))
                pol=self.canvas.create_polygon(20+1.05*int(coord[1]),-5+1.05*int(coord[2]),20+1.05*int(coord[3]),
                                               -5+1.05*int(coord[4]),20+1.05*int(coord[5]),-5+1.05*int(coord[6]),
                                               20+1.05*int(coord[7]),-5+1.05*int(coord[8]), outline='black', fill=colour)
    #            self.canvas.create_text(290,340,text='Efficiency',font=('times',15,'bold italic'))
                self.canvas.bind('<Double-1>', self.click_canvasNew)


        elif par_type == 'Masked Strips':
            for line in f:
                coord = line.rstrip().split("  ")
                histoname_occ = 'Occupancy_'+self.Wheel+'_' + coord[0]
                colour = self.diagn.setColourNoise(self.diagn.getMaskedStrip(histoname_occ))
                pol=self.canvas.create_polygon(20+1.05*int(coord[1]),-5+1.05*int(coord[2]),20+1.05*int(coord[3]),
                                               -5+1.05*int(coord[4]),20+1.05*int(coord[5]),-5+1.05*int(coord[6]),
                                               20+1.05*int(coord[7]),-5+1.05*int(coord[8]), outline='black', fill=colour)
     #           self.canvas.create_text(290,340,text='Masked Strips',font=('times',15,'bold italic'))                
                self.canvas.bind('<Double-1>', self.click_canvasNew)

                

        elif par_type == 'All Parameters':
            for line in f:
                coord = line.rstrip().split("  ")
                histoname_bx = 'BXN_'+self.Wheel+'_' + coord[0]
                histoname_cls = 'ClusterSize_'+self.Wheel+'_'+coord[0]
                histoname_occ = 'Occupancy_'+self.Wheel+'_'+coord[0]
                histoname_Eff = 'LocalEfficiencyFromSegments_'+self.Wheel+'_' + coord[0]
                colour = self.diagn.setColour(self.diagn.getMeanValue(histoname_bx),
                                              self.diagn.getMeanValue(histoname_cls),
                                              self.diagn.getNoise(histoname_bx),self.diagn.getMedia(histoname_Eff),
                                              self.diagn.getMaskedStrip(histoname_occ))

                pol=self.canvas.create_polygon(20+1.05*int(coord[1]),-5+1.05*int(coord[2]),20+1.05*int(coord[3]),
                                               -5+1.05*int(coord[4]),20+1.05*int(coord[5]),-5+1.05*int(coord[6]),
                                               20+1.05*int(coord[7]),-5+1.05*int(coord[8]), outline='black', fill=colour)                
      #          self.canvas.create_text(290,340,text='All parameters',font=('times',15,'bold italic'))
                self.canvas.bind('<Double-1>', self.click_canvasNew)

        self.canvas.pack()

#
# main
#

if __name__ == "__main__": DrawWheel(sys.argv[1],sys.argv[2]).mainloop()

