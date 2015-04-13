#! /usr/bin/env python
#import commands
#import sys, os, string, fileinput
from Tkinter import *
import ROOT
from ROOT import TCanvas,TH1F,gROOT,TFile,gDirectory,TGraph, TDatime,TPaveText,TText
from array import array
#import time

class DisplayPlots(Frame):
    def __init__(self,select_ch,t1,current,select_ch1,t2,temp,parent=None):

        self.select_ch = select_ch
        self.select_ch1 = select_ch1
        self.t1 = t1
        self.t2 = t2
        self.current = current
        self.temp = temp
        
        Frame.__init__(self, parent)
        self.pack()

        self.calendar = {"Jan":1,"Feb":2,"Mar":3,"Apr":4,"May":5,"Jun":6,"Jul":7,"Aug":8,"Sep":9,"Oct":10,"Nov":11,"Dec":12}

    def plotHisto(self):
        
        canvas = TCanvas(str(self.select_ch),str(self.select_ch),200,10,700,500)
        canvas.Divide(1,2)

        ROOT.gStyle.SetTitleFont(32)
        ROOT.gStyle.SetTitleColor(8)
        ROOT.gStyle.SetTitleSize(18)


        try:

            hcurr = TGraph(len(self.t1),array("d",self.t1),array("d",self.current))
            hcurr.SetName(str(self.select_ch))
            hcurr.SetTitle(str(self.select_ch))
            
            hcurr.SetMarkerColor(8)
            hcurr.SetMarkerStyle(20)
            hcurr.SetMarkerSize(0.8)
            hcurr.SetMinimum(0)
            hcurr.SetMaximum(10)
            
            hcurr.GetXaxis().SetLabelFont(32);
            hcurr.GetXaxis().SetLabelSize(0.03);
            hcurr.GetXaxis().SetTitleFont(32);
            hcurr.GetYaxis().SetTitle("Current (#mu A)");
            hcurr.GetYaxis().SetLabelFont(32);
            hcurr.GetYaxis().SetTitleFont(32);
            
            hcurr.GetXaxis().SetNdivisions(-503); 
            hcurr.GetXaxis().SetTimeDisplay(1)
            hcurr.GetXaxis().SetTimeFormat("%d\/%m\/%y %H:%M")
            hcurr.GetXaxis().SetTimeOffset(0,"gmt")
            
            htemp = TGraph(len(self.t2),array("d",self.t2),array("d",self.temp))
            htemp.SetName(str(self.select_ch1))
            htemp.SetTitle(str(self.select_ch1))
            
            htemp.SetMarkerColor(42)
            htemp.SetMarkerStyle(20)
            htemp.SetMarkerSize(0.8)
            htemp.SetMinimum(0)
            htemp.SetMaximum(50)
            
            htemp.GetXaxis().SetLabelFont(32);
            htemp.GetXaxis().SetLabelSize(0.03);
            htemp.GetXaxis().SetTitleFont(32);
            htemp.GetYaxis().SetTitle("Temperature (°C)");
            htemp.GetYaxis().SetLabelFont(32);
            htemp.GetYaxis().SetTitleFont(32);
            
            htemp.GetXaxis().SetNdivisions(-503); 
            htemp.GetXaxis().SetTimeDisplay(1)
            htemp.GetXaxis().SetTimeFormat("%d\/%m\/%y %H:%M")
            htemp.GetXaxis().SetTimeOffset(0,"gmt")
            
            canvas.cd(1)
            hcurr.Draw("AP")
            canvas.cd(2)
            htemp.Draw("AP")
            
        except:
            pass

        self.mainloop()

