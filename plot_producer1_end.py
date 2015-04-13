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
#    layers = ['S01','S02','S03','S04','S05','S06']
    lay = ['R1','R2','R3']
    sectors = ['CH01','CH02','CH03','CH04','CH05','CH06','CH07','CH08','CH09','CH10','CH11','CH12','CH13','CH14','CH15','CH16','CH17','CH18','CH19','CH20','CH21','CH22','CH23','CH24','CH25','CH26','CH27','CH28','CH29','CH30','CH31','CH32','CH33','CH34','CH35','CH36']
    cham = ['A','B','C']
    histob = TH1I('noisystrips', 'noisystrips', 100,0,100)
    histog = TH1I('goodstrips', 'goodstrips', 100,0,100)
    histod = TH1I('deathstrips', 'deathstrips', 100,0,100)
 #   for item in layers:
    for thing in cham:
            for cosa in sectors:
                for ding in lay:
                    #histname = str(wheel) + '_' + str(ding) + '_' + str(item) +'_'+ str(cosa) + '_' + str(thing) + '_media'
                    histname = str(wheel) + '_' + str(ding) + '_' + str(cosa) + '_' + str(thing) + '_media' 
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
