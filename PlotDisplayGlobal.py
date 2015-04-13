#! /usr/bin/env python
import commands
import sys, os, string, fileinput
from Tkinter import *
from ROOT import TCanvas,TH1F,gROOT,TFile,gDirectory
from QualityPerformance import Diagnostic

class DisplayPlotsGlobal(Frame):
    def __init__(self,root_file_name,parent=None):
        print root_file_name
        self.RootFileName=TFile.Open(root_file_name)
        Frame.__init__(self, parent)
        self.pack()
        self.canvas = Canvas(self,width = 300, height = 200, bg = 'darkgreen')
        self.canvas.pack(expand = YES, fill = BOTH)

    def plotHisto(self):
        listWheel = ['W-2','W-1','W+0','W+1','W+2']
        listBarrel = self.fillListBarrel()
        histoBx = TH1F("Barrel Bunch Crossing","",16,-7.5,7.5)
        diagn = Diagnostic(self.RootFileName)
        for k in listWheel:
            for j in listBarrel:
                
                histoname_bx = 'BXN_'+k+'_' + j
                
                histoBx.Fill(diagn.getMeanValue(histoname_bx)[0])
                histoBx.Fill(diagn.getMeanValue(histoname_bx)[1])
        c1 = TCanvas("c1","c1",1)        
        histoBx.Draw()
        c1.SaveAs("/tmp/trentad/Barrel_Bx.gif")


    def fillListBarrel(self):

        cmd = "pwd"
        homedir = [item[:-1] for item in os.popen(cmd)]
        f=open(str(homedir[0])+'/wheel_coord.txt', 'r')
        
        detMap = []
        for line in f:
            coord = line.rstrip().split("  ")
            chname = ''
            detMap.append(str(coord[0]))
            
        return detMap

    def fillListEndcap(self):

        cmd = "pwd"
        homedir = [item[:-1] for item in os.popen(cmd)]
        f=open(str(homedir[0])+'/disk_coord.txt', 'r')
        
        detMap = []
        for line in f:
            coord = line.rstrip().split("  ")
            chname = ''
            detMap.append(str(coord[0]))
            
        return detMap
        
