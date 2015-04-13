#! /usr/bin/env python
from Tkinter import *
import commands
import sys, os, string, fileinput
from sys import argv
from ROOT import *

if __name__ == '__main__':

    RootFile=TFile.Open(str(sys.argv[1]))#"97003_noise_v4.root")
    wheel = sys.argv[2]
    RootOut=TFile.Open(str(sys.argv[1]) + '_' + str(wheel) + '_summary_out.root',"RECREATE")

#    wheels = ['W-2','W-1','W+0','W+1','W+2']

    #sectors = ['S01','S02','S03','S04','S05','S06']
    cham = ['A','B','C']
    roll = ['R1','R2','R3']
    layers = ['CH31','CH32','CH33','CH34','CH35','CH36','CH01','CH02','CH03','CH04','CH05','CH06','CH07','CH08','CH09','CH10','CH11','CH12','CH13','CH14','CH15','CH16','CH17','CH18','CH19','CH20','CH21','CH22','CH23','CH24','CH25','CH26','CH27','CH28','CH29','CH30']
    title2 = 'wheels_summary_' + str(sys.argv[1])
    plot2 = TH1F(title2,title2,5,0,5)
    bin2 = 1
    
    title1 = str(wheel) + '_summary' + str(sys.argv[1])
    titlel = str(wheel) + '_layer_summary' + str(sys.argv[1])
    plotl = TH1F(titlel,titlel,3,0,3)
    plot1 = TH1F(title1,title1,36,0,36)
    title2 = 'noise_distribution'
    plot2 = TH1F(title2,title2,10000,0,20000)
    bins = 1
    for ob in layers:
        if(ob == 'CH31' or ob == 'CH13'):
            bin = 1
            if(ob=='CH31'):
                title = str(wheel)+'_Near_Side'+ str(sys.argv[1])
            else:
                title = str(wheel)+'_Far_Side'+ str(sys.argv[1])
            plot = TH1F(title,title,110,0,110)
        for ding in roll:    
            #for item in layers:
                for thing in cham:
                            #histname = str(wheel) + '_' + str(ding) + '_' + str(ob) + '_' + str(item) + '_' + str(thing) + '_media'
                            histname = str(wheel) + '_' + str(ding) + '_' + str(ob) + '_' + str(thing) + '_media'
                            #binname = str(wheel) + '_' +  str(ding) + '_' + str(ob) + '_' + str(item) + '_' + str(thing)
                            binname = str(wheel) + '_' +  str(ding) + '_' + str(ob) + '_' + str(thing) 
                            histo = RootFile.FindObjectAny(histname)
                            if(histo):
                                histmed = TH1F(histname + '_frq_dist',histname + '_media',1000,0,1000)
                                xbins = histo.GetXaxis().GetNbins()
                                plot.GetXaxis().SetBinLabel(bin,binname)
                                plot1.GetXaxis().SetBinLabel(bins,str(wheel)+'_'+str(ob))
                                for i in range(xbins):
                                    histmed.Fill(histo.GetBinContent(i+1))
                                nmean = histmed.GetMean()
                                sigma = histmed.GetRMS()
                                for i in range(xbins):
                                    num = histo.GetBinContent(i+1)
                                    if (num < nmean + 3*sigma):
                                        plot.Fill(bin-1,num)
                                        plot1.Fill(bins-1,num)
                                bin = bin + 1
                                plot.GetXaxis().SetLabelSize(0.03)
                                plot.GetYaxis().SetTitle('Hz')
        bins = bins + 1                        
        if(ob == 'CH30' or ob == 'CH12'):
            plot.GetXaxis().LabelsOption("V")
            gStyle.SetOptStat(0)    
            if(RootOut.cd()):
                plot.Write()
    plot1.Write()            

