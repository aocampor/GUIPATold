#! /usr/bin/env python
from Tkinter import *
import commands
import sys, os, string, fileinput
from sys import argv
from ROOT import *

if __name__ == '__main__':

    RootFile=TFile.Open(str(sys.argv[1]))
    wheel = sys.argv[2]
    item = sys.argv[3]
    RootOut=TFile.Open(str(sys.argv[1]) + '_' + str(item) + '.root',"RECREATE")
    sectors = ['S04','S05','S06','S07','S08','S09','S10','S11','S12','S01','S02','S03']
    roll = ['Forward','Backward','Middle']
#    for item in layers:
#    for thing in cham:
 #       for thing2 in cham:
    for cosa in sectors:
        for ding in roll:
            histname = str(wheel) + '_' + str(item) + '_' + str(cosa) + '_' + str(ding)
#            print histname
            histo = RootFile.FindObjectAny(histname)
            if(histo):
                ybins = histo.GetYaxis().GetNbins()
                histmed = TH1F(histname + '_media',histname + '_media',ybins,0,ybins)
                xbins = histo.GetXaxis().GetNbins()
                for i in range(ybins):
                    hist1 = TH1F(histname + '_proy',histname + '_proy',100,0,100)
                    binname = histname + '_' + str(i)  
                    proy = histo.ProjectionX(binname,i+1,i+1)
                    for j in range(xbins):
                        hist1.Fill(proy.GetBinContent(j+1))
                    histmed.SetBinContent(i+1,hist1.GetMean()*1000000/175)
                    del hist1
                if(RootOut.cd()):
                    histmed.Write()
                    del histmed    
            del histo
                        
    RootOut.Close()
