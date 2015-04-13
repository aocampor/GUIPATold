#! /usr/bin/env python
from Tkinter import *
import commands
import sys, os, string, fileinput
from sys import argv
from ROOT import *

if __name__ == '__main__':

    RootFile=TFile.Open(str(sys.argv[1]))#"97003_noise_v4.root")
    RootOut=TFile.Open(str(sys.argv[1]) + '_davide.root',"RECREATE")
    run = str(sys.argv[2])

    wheels = ['RE-3','RE-2','RE-1','W-2','W-1','W+0','W+1','W+2','RE+1','RE+2','RE+3']
    whe = ['m13','m12','m11','0m2','0m1','00','01','02','11','12','13']
#    wheel = sys.argv[2]
#    whe = -2
#    c1 = TCanvas('c1','c1',1)
    histo = TH1F('distribution','distribution',100,0,1)
    cont = 0
    for item in wheels:
#        title1 = str(item) + '_Far_Side'+run+'_'+str(whe[cont])+'.root_'+str(item)+'_media.root'
        title1 = str(item) + '_Far_Side'+run+'_media.root'
#        title2 = str(item) + '_Near_Side'+run+'_'+str(whe[cont])+'.root_'+str(item)+'_media.root'
        title2 = str(item) + '_Near_Side'+run+'_media.root'
        print str(title1)
        plot1 = RootFile.FindObjectAny(title1)
        plot2 = RootFile.FindObjectAny(title2)
        if (plot1 and plot2):
         nbin1 = plot1.GetXaxis().GetNbins()
         nbin2 = plot2.GetXaxis().GetNbins()
         print 'bin1: ' + str(nbin1) + 'bin2: ' + str(nbin2)
         for i in range(nbin1):
            mean1 = plot1.GetBinContent(i + 1)
            if(mean1 != 0):
                histo.Fill(mean1/30000)
         for i in range(nbin2):
            mean2 = plot2.GetBinContent(i+1)
            if(mean2 != 0):
                histo.Fill(mean2/30000)

        cont = cont + 1        
    histo.Write()
    #c1.SaveAs('davide.C')
    
