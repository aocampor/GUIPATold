#! /usr/bin/env python
import commands
import sys, os, string, fileinput
from Tkinter import *
from array import array
from ROOT import TCanvas, TH1F, gROOT, TFile, gDirectory, TMath, TGraphErrors, TF1, TMath
from math import sqrt
import ROOT

class HVScan(Frame):
    def __init__(self,dataset,runs,hvlist):

        print "Constructor"

        ROOT.gROOT.SetBatch(ROOT.kTRUE)

        self.RootFileOut = TFile("prova.root","RECREATE")

        self.hvmax = TH1F("Eff Max","Eff max",100,0.,100);
        self.Svalue = TH1F("Svalue","Svalue",400,-0.5,0.5);
        self.HVeff50 = TH1F("HVeff50","HVeff50",100,8500,9500);

        self.hvlist = hvlist
        self.RootFiles = []
        effMap = []

        count = 0
        print "Loop of runs"

        ds = str(dataset).replace('/','')
        
        for run in runs:
            RootFileName = '/castor/cern.ch/cms/store/caf/user/ccmuon/RPC/GlobalRuns/'+ds+'/'+run+'/root/Merge_tot.root'
            print RootFileName
            
            temp = TFile.Open(RootFileName)
            temp.cd()
            self.RootFiles.append(temp)
            count += 1

        detList = self.fillDetList()

        print "Loop of rootfiles"
        for root in self.RootFiles:
            effMap.append(self.createEffMap(root,detList))

        self.producePlots(effMap)

    def func(self,x,par):

        effmax = par[0]
        S = par[1]
        HV50 = par[2]

        return effmax/(1.0 + TMath.Exp( S * ( x[0] - HV50 ))) 

    def producePlots(self,effMap):

        loop = 0
        mast = 0
        for k in (effMap[0]).keys():
            loop += 1
            efferrlist = []
            efflist =[]
            errlist = []
            
            for imap in effMap:
                efferrlist.append(imap.get(k))

            #            print "rollname1 : ", k  , efflist

            for iv in range(len(efferrlist)):
                vals = efferrlist[iv]                
                efflist.append(vals[0])
                errlist.append(vals[1])

            eff = []
            err = []
            hverr = [0,0,0,0]

            hv = array("d",self.hvlist)
            hvr = array("d",hverr)
            eff = array("d",efflist)
            err = array("d",errlist)

            self.RootFileOut.cd()

            nGood = 0
            for vals in eff:
                if vals>0:
                    nGood += 1

            if nGood>3:
                c1 = TCanvas(k,k,1)
                gr = TGraphErrors(len(eff),hv,eff,hvr,err)

                fit_effmax = 90
                fit_S = -0.02
                fit_HV50 = 80

                print "About to fitting: ",k, efflist
                
                self.f1 = TF1("f1",self.func,8500,9500,3)
                self.f1.SetParameter(0,fit_effmax)
                self.f1.SetParLimits(0,0.,100) 
                self.f1.SetParameter(1,fit_S)
                self.f1.SetParLimits(1,-0.5,0.5)  
                self.f1.SetParameter(2,fit_HV50)
                self.f1.SetParLimits(2,8500,9500)
                
                gr.Fit(self.f1)
                gr.Draw("AP*")
                c1.Write()
                
                self.hvmax.Fill(self.f1.GetParameter(0))
                self.Svalue.Fill(self.f1.GetParameter(1))
                self.HVeff50.Fill(self.f1.GetParameter(2))
                
            else: print "Won't fit ", k, efflist
        self.hvmax.Write()
        self.Svalue.Write()
        self.HVeff50.Write()
                    
    def createEffMap(self,rootfile,detList):
        print "Inside create map"
        detMap = {}
        wheels = ["W-2","W-1","W+0","W+1","W+2"]
        for wheel in wheels:
            for det in detList:
                chname = wheel+'_'+det
                histoname = 'LocalEfficiencyFromSegments_'+chname
                efferr = self.getMedia(rootfile,histoname)
                eff = efferr[0]
                err = efferr[1]
                detMap[chname+'_Forward'] = [eff[0],err[0]]
                detMap[chname+'_Backward'] = [eff[1],err[1]]

                if len(eff) == 3:
                    detMap[chname+'_Middle'] = [eff[2],err[2]]

        return detMap
        
    def getMedia(self,rootfile,histoname):
        inputname = histoname.rstrip().split("_")

        histo_back = histoname + '_Backward'
        histo_for = histoname + '_Forward'
        rolls_in_chamber = [histo_for,histo_back]

        if cmp(inputname[1],'W-2') == 0 and cmp(inputname[2],'RB2out') == 0:
            histo_middle = histoname + '_Middle'
            rolls_in_chamber.append(histo_middle)
        elif cmp(inputname[1],'W+2') == 0 and cmp(inputname[2],'RB2out') == 0:
            histo_middle = histoname + '_Middle'
            rolls_in_chamber.append(histo_middle)    
        elif (cmp(inputname[1],'W-1') == 0 or cmp(inputname[1],'W+0') == 0 or cmp(inputname[1],'W+1') == 0) and cmp(inputname[2],'RB2in') == 0: 
            histo_middle = histoname + '_Middle'
            rolls_in_chamber.append(histo_middle)

        meanvalue = []
        errvalue = []
        mediavals = []
        rootfile.cd()
        for roll in rolls_in_chamber:
            try:
                histo = gDirectory.FindObjectAny(roll)
                eff = 0
                err = 0
                media = 0
                ermedia = 0
                strips = histo.GetNbinsX()
                dead = 0
                gnum = 0

                for j in range(histo.GetNbinsX()):
                    eff = eff + histo.GetBinContent(j+1)
                    err = err + (histo.GetBinError(j+1))**2

                    if histo.GetBinContent(j+1) == 0:
                        dead += 1 
                gnum = strips - dead
                deadPerc=float(gnum)/float(strips)
                if deadPerc>0.5 and gnum > 0:   
                    media = eff/gnum
                    ermedia = sqrt(err/float(gnum))
                    meanvalue.append(media)
                    errvalue.append(ermedia)
                else:
                    meanvalue.append(0)
                    errvalue.append(0)
                    #print "roll ",roll," strips ",strips," dead ",dead," gnum ",gnum," deadPerc ",deadPerc
            except AttributeError:
                #print "missing ",roll
                meanvalue.append(-1)
                errvalue.append(-1)

        mediavals.append(meanvalue)
        mediavals.append(errvalue)
        return mediavals
        
    def fillDetList(self):

        print "inside fillDetLIst"
        
        cmd = "pwd"
        homedir = [item[:-1] for item in os.popen(cmd)]
        f = open(str(homedir[0])+'/wheel_coord.txt', 'r')
        
        detList = []
        for line in f:
            coord = line.rstrip().split("  ")
            detList.append(coord[0])

        f.close()
        return detList


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
        f = open(str(homedir[0])+'/wheel_coord.txt', 'r')
        
        detMap = []
        for line in f:
            coord = line.rstrip().split("  ")
            chname = ''
            detMap.append(str(coord[0]))

        f.close()            
        return detMap

    def fillListEndcap(self):

        cmd = "pwd"
        homedir = [item[:-1] for item in os.popen(cmd)]
        f = open(str(homedir[0])+'/disk_coord.txt', 'r')
        
        detMap = []
        for line in f:
            coord = line.rstrip().split("  ")
            chname = ''
            detMap.append(str(coord[0]))

        f.close()            
        return detMap
        
if __name__ == "__main__":

    runs = [ "69253","68021","68276","69797" ]
#    runs = [ "69797","69797","69797","69797" ]
    hvlist   = [ 8900,9000,9100,9200 ]
    hvlist_1 = [ 9000,9100,9200 ]
    hvlist_2 = [ 8900,9100,9200 ]
    hvlist_3 = [ 8900,9000,9200 ]
    hvlist_4 = [ 8900,9000,9100 ]

    HVScan('CosmicsCommissioning08_CRAFT_ALL_V4_ReReco-v1RECO',runs,hvlist)
    
