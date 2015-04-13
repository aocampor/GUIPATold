#! /usr/bin/env python
import commands
import sys, os, string, fileinput
from Tkinter import *
from ROOT import TCanvas,TH1F,gROOT,TFile,gDirectory
from math import *

class EfficiencyPlotProduction(Frame):
    def __init__(self,root_file_name,wheel,parent=None):
        print root_file_name
        self.RootFile=TFile(root_file_name)
        Frame.__init__(self, parent)
        self.pack()
        self.NewRootFile=TFile('prova.root','RECREATE')
        self.createEffHisto(self.fillDetList())
        self.NewRootFile.Write()
        self.NewRootFile.Close()
        
    def fillDetList(self):

        cmd = "pwd"
        homedir = [item[:-1] for item in os.popen(cmd)]
        f=open(str(homedir[0])+'/disk_coord.txt', 'r')
        
        detList = []
        for line in f:
            coord = line.rstrip().split("  ")
            detList.append(str(coord[0]))

        f.close()
        return detList

    def createEffHisto(self,detlist):

        for ch in detlist:
            inputname = ch.rstrip().split("_")
#            histoname = sys.argv[2] + '_' + ch
            histoname = sys.argv[2] + '_' + inputname[0] + '_' + inputname[2]

            #print inputname

            histo_prefix1 = ['ExpectedOccupancyFromCSC_','RPCDataOccupancyFromCSC_']
            histo_prefix2 = ['ExpOcc_','RealOcc5_']
                    
            histo_A = histoname + '_A'
            histo_B = histoname + '_B'
            histo_C = histoname + '_C'
            rolls_in_chamber = [histo_A,histo_B,histo_C]

            for roll in rolls_in_chamber:
                histo1 = []
                histo2 = []
                
                try:
                    self.RootFile.cd()

                    for h in histo_prefix1:
                        histo1.append(gDirectory.FindObjectAny(h+roll))

                    for h in histo_prefix2:
                        histo2.append(gDirectory.FindObjectAny(h+roll))                        
                        
                    histoEff1 = TH1F('LocalEfficiencyFromSegments_'+roll,'LocalEfficiencyFromSegments_'+roll,histo1[0].GetNbinsX(), 0, histo1[0].GetNbinsX()-1)
                    histoEff2 = TH1F('LocalEfficiencyFromTrack_'+roll,'LocalEfficiencyFromTrack_'+roll,histo1[0].GetNbinsX(), 0, histo1[0].GetNbinsX()-1)
                                        
                    for j in range(histo1[0].GetNbinsX()):
                        exp_value = histo1[0].GetBinContent(j+1)
                        real_value = histo1[1].GetBinContent(j+1)
                        #print exp_value,real_value
                        if exp_value != 0:
                            eff = 100*(real_value/exp_value)
                            #print eff
                            err = sqrt(100*(100-eff)/exp_value)
                            #print err
                            histoEff1.SetBinContent(j+1,eff)
                            histoEff1.SetBinError(j+1,err)
                    try:

                        for j in range(histo2[0].GetNbinsX()):
                            exp_value = histo2[0].GetBinContent(j+1)
                            real_value = histo2[1].GetBinContent(j+1)
                            #print exp_value,real_value
                            if exp_value != 0:
                                eff = 100*(real_value/exp_value)
                                #print eff
                                err = sqrt(100*(100-eff)/exp_value)
                                #print err
                                histoEff2.SetBinContent(j+1,eff)
                                histoEff2.SetBinError(j+1,err)
                    except:
                        pass
                            
                    self.NewRootFile.cd()
                    histoEff1.Write()
                    histoEff2.Write()
                    
                except AttributeError:
                    pass
                        
#
# main
#

if __name__ == "__main__":  EfficiencyPlotProduction(sys.argv[1],sys.argv[2])
