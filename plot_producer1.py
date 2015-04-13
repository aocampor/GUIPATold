#! /usr/bin/env python
from Tkinter import *
import commands
import sys, os, string, fileinput
from sys import argv
from ROOT import *

if __name__ == '__main__':

    RootFile=TFile.Open(str(sys.argv[1]))
    wheel = sys.argv[2]
    RootOut=TFile.Open(str(sys.argv[1]) + '_plots.root',"RECREATE")
    layers = ['RB1in','RB1out','RB2in','RB2out','RB3','RB4']
#    layers = ['RB1in','RB1out']
    sectors = ['S04','S05','S06','S07','S08','S09','S10','S11','S12','S01','S02','S03']
    cham = ['+','-','']
    roll = ['Forward','Backward','Middle']
    histob = TH1I('noisystrips', 'noisystrips', 100,0,100)
    histog = TH1I('goodstrips', 'goodstrips', 100,0,100)
    histod = TH1I('deathstrips', 'deathstrips', 100,0,100)
    for item in layers:
        for thing in cham:
            for thing2 in cham:
                for cosa in sectors:
                    for ding in roll:
                        histname = str(wheel) + '_' + str(item) + str(thing) + str(thing2) + '_' + str(cosa) + '_' + str(ding) + '_media' 
 #                       print histname
                        histo = RootFile.FindObjectAny(histname)
                        if(histo):
                            histmed = TH1F(histname + '_frq_dist',histname + '_media',1000,0,1000)
                            xbins = histo.GetXaxis().GetNbins()
                            for i in range(xbins):
                                histmed.Fill(histo.GetBinContent(i+1))
                            nmean = histmed.GetMean()
                            sigma = histmed.GetRMS()
                            contb = 0
                            contd = 0
                            for i in range(xbins):
                                num = histo.GetBinContent(i+1)
                                if num == 0 :
                                    contd = contd + 1
                                if (num > nmean + 3*sigma):
                                    contb = contb + 1
#                                    print histname + ' has the noisy strip ' + str(i+1)
                            histob.Fill(contb)
                            histog.Fill(xbins-contb)
                            if contd!= 0 :
                                histod.Fill(contd)
                            #if(RootOut.cd()):
                             #   histmed.Write()
                            del histmed    
                        del histo
    if(RootOut.cd()):
        histob.Write()
        histog.Write()
        histod.Write()
    RootOut.Close()
