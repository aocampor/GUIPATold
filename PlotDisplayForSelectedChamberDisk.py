#! /usr/bin/env python
import commands
import sys, os, string, fileinput
from Tkinter import *
from ROOT import TCanvas,TH1F,gROOT,TFile,gDirectory

class DisplayPlots(Frame):
    def __init__(self,root_file_name,parent=None):
        print root_file_name
        self.RootFile=TFile.Open(root_file_name)
        Frame.__init__(self, parent)
        self.pack()
        self.canvas = Canvas(self,width = 300, height = 200, bg = 'darkgreen')
        self.canvas.pack(expand = YES, fill = BOTH)

    def plotHisto(self,histoname):
        inputname = histoname.rstrip().split("_")

        histo_prefix = ['BXN_','ClusterSize_','Occupancy_']

        histo_A = histoname + '_A'
        histo_B = histoname + '_B'
        histo_C = histoname + '_C'
        rolls_in_chamber = [histo_A,histo_B,histo_C]
        
        listCanvas = [TCanvas(histo_A,histo_A,200,10,700,500),
                      TCanvas(histo_B,histo_B,200,10,700,500),
                      TCanvas(histo_C,histo_C,200,10,700,500)]

        j = 0    
        for roll in rolls_in_chamber:
            listCanvas[j].Divide(2,2)
            i = 1
            for h in histo_prefix:
                try:
                    histo = gDirectory.FindObjectAny(h+roll)
                    listCanvas[j].cd(i)
                    histo.Draw()
                    i += 1
                except AttributeError:
                    pass

            try:    
                listCanvas[j].cd(4)
                histo = gDirectory.FindObjectAny('LocalEfficiencyFromTrack_'+roll)
                histo.SetLineColor(4)
                histo.SetMarkerColor(4)
                histo.Draw()

                histo1 = gDirectory.FindObjectAny('LocalEfficiencyFromSegments_'+roll)
                histo1.SetLineColor(2)
                histo1.SetMarkerColor(2)
                histo1.Draw()
            except AttributeError:
                pass
            j += 1
            
        self.mainloop()

