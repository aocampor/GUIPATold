#! /usr/bin/env python
from Tkinter import *
import commands
import sys, os, string, fileinput
from sys import argv
from ROOT import *

if __name__ == '__main__':

    RootFile=TFile.Open(str(sys.argv[1]))
#    print str(sys.argv[1])
    wheel = sys.argv[2]
#    item = sys.argv[3]
#    print str(sys.argv[1]) + '_' + str(item) + '.root'
#    RootOut=TFile.Open(str(sys.argv[1]) + '_' + str(wheel) + '_media.root',"RECREATE")
    RootOut=TFile.Open(str(sys.argv[1]) + '_media.root',"RECREATE")
    sectors = ['CH01','CH02','CH03','CH04','CH05','CH06','CH07','CH08','CH09','CH10','CH11','CH12','CH13','CH14','CH15','CH16','CH17','CH18','CH19','CH20','CH21','CH22','CH23','CH24','CH25','CH26','CH27','CH28','CH29','CH30','CH31','CH32','CH33','CH34','CH35','CH36']
    roll = ['R1','R2','R3']
    section = ['A','B','C']
#    for item in layers:
#    for thing in cham:
 #       for thing2 in cham:
    for cosa in sectors:
        for ding in roll:
            for seon in section:
                #histname = str(wheel) + '_' + str(ding) + '_' + str(item) + '_' + str(cosa) + '_' + str(seon)
                histname = str(wheel) + '_' + str(ding) + '_' + str(cosa) + '_' + str(seon)
                print histname
                histo = RootFile.FindObjectAny(histname)
                if(histo):
                    ybins = histo.GetYaxis().GetNbins()
                    histmed = TH1F(histname + '_media',histname + '_media',ybins,0,ybins)
                    xbins = histo.GetXaxis().GetNbins()
                    for i in range(ybins):
                        hist1 = TH1F(histname + '_proy',histname + '_proy',110,0,110)
                        binname = histname + '_' + str(i)  
                        proy = histo.ProjectionX(binname,i+1,i+1)
                        for j in range(xbins):
                            hist1.Fill(proy.GetBinContent(j+1))
#                            print str(proy.GetBinContent(j+1))
                        histmed.SetBinContent(i+1,hist1.GetMean()*1000000/175)
                        del hist1
                    if(RootOut.cd()):
                        histmed.Write()
                    del histmed    
                del histo
                        
    RootOut.Close()
