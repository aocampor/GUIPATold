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

        histo_prefix = ['BXN_','ClusterSize_','Occupancy_']#,'LocalEfficiencyFromTrack_','LocalEfficiencyFromSegments_']
        
        histo_back = histoname + '_Backward'
        histo_for = histoname + '_Forward'
        rolls_in_chamber = [histo_for,histo_back]
        listCanvas = [TCanvas(histo_for,histo_for,200,10,700,500),
                      TCanvas(histo_back,histo_back,200,10,700,500)]

        if (cmp(inputname[0],'W+2') == 0 or cmp(inputname[0],'W-2') == 0) and cmp(inputname[1],'RB2out') == 0:
            histo_middle = histoname + '_Middle'
            rolls_in_chamber.append(histo_middle)
            listCanvas.append(TCanvas(histo_middle,histo_middle,200,10,700,500))
        elif (cmp(inputname[0],'W-1')==0 or cmp(inputname[0],'W+0')==0 or cmp(inputname[0],'W+1')==0) and cmp(inputname[1],'RB2in')==0:
            histo_middle = histoname + '_Middle'
            rolls_in_chamber.append(histo_middle)
            listCanvas.append(TCanvas(histo_middle,histo_middle,200,10,700,500))

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
                histo1.SetLineColor(1)
                histo1.SetMarkerColor(1)
                histo1.Draw("same")
            except AttributeError:
                pass
            j += 1
            
        self.mainloop()

