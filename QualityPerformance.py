#! /usr/bin/env python
from ROOT import TCanvas,TH1F,gROOT,TFile,gDirectory
from Tkinter import *
from math import *

class Diagnostic(object):

    def __init__(self,root_file_name):
        self.RootFile=TFile.Open(root_file_name)
        print root_file_name
        
    def getMeanValue(self,histoname):
        inputname = histoname.rstrip().split("_")

        histo_back = histoname + '_Backward'
        histo_for = histoname + '_Forward'
        rolls_in_chamber = [histo_for,histo_back]

        if (cmp(inputname[1],'W+2') == 0 or cmp(inputname[1],'W-2') == 0) and cmp(inputname[2],'RB2out') == 0:
            histo_middle = histoname + '_Middle'
            rolls_in_chamber.append(histo_middle)
        elif (cmp(inputname[1],'W-1')==0 or cmp(inputname[1],'W0')==0 or cmp(inputname[1],'W+1')==0) and cmp(inputname[2],'RB2in')==0:
            histo_middle = histoname + '_Middle'
            rolls_in_chamber.append(histo_middle)

        meanvalue = []
        for roll in rolls_in_chamber:
            try:
                histo = gDirectory.FindObjectAny(roll)
                meanvalue.append(histo.GetMean())
            except AttributeError:
                meanvalue.append(-100)
        return meanvalue


    def getMedia(self,histoname):
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
        elif (cmp(inputname[1],'W-1')==0 or cmp(inputname[1],'W0')==0 or cmp(inputname[1],'W+1')==0) and cmp(inputname[2],'RB2in')==0:
            histo_middle = histoname + '_Middle'
            rolls_in_chamber.append(histo_middle)

        meanvalue = []
        for roll in rolls_in_chamber:
            try:
                
                histo = gDirectory.FindObjectAny(roll)
                eff = 0
                for j in range(histo.GetNbinsX()):
                    eff = eff + histo.GetBinContent(j+1)
                media=eff/histo.GetNbinsX()
                meanvalue.append(media)
                print roll , meanvalue
            except AttributeError:
                meanvalue.append(-100)
                
        return meanvalue
                    
    def getStatistics(self,histoname):
        histo = gDirectory.FindObjectAny(histoname)
        sul = histo.GetBinContent(1)
        return sul

        
    def getMaskedStrip(self,histoname):
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
        elif (cmp(inputname[1],'W-1')==0 or cmp(inputname[1],'W0')==0 or cmp(inputname[1],'W+1')==0) and cmp(inputname[2],'RB2in')==0:
            histo_middle = histoname + '_Middle'
            rolls_in_chamber.append(histo_middle)

        meanvalue = []
        for roll in rolls_in_chamber:
            try:
                histo = gDirectory.FindObjectAny(roll)
                counter = 0
                for j in range(histo.GetNbinsX()):
                    if histo.GetBinContent(j+1) == 0: counter += 1
                    
                meanvalue.append(counter)
            except AttributeError:
                meanvalue.append(-100)
        return meanvalue



    def getNoise(self,histoname):
        inputname = histoname.rstrip().split("_")

        histo_back = histoname + '_Backward'
        histo_for = histoname + '_Forward'
        rolls_in_chamber = [histo_for,histo_back]

        if (cmp(inputname[1],'W-2') == 0 or cmp(inputname[1],'W+2') == 0)and cmp(inputname[2],'RB2out') == 0:
            histo_middle = histoname + '_Middle'
            rolls_in_chamber.append(histo_middle)
        elif (cmp(inputname[1],'W-1')==0 or cmp(inputname[1],'W0')==0 or cmp(inputname[1],'W+1')==0) and cmp(inputname[2],'RB2in')==0:
            histo_middle = histoname + '_Middle'
            rolls_in_chamber.append(histo_middle)

        meanvalue = []
        for roll in rolls_in_chamber:
            try:
                histo = gDirectory.FindObjectAny(roll)
                
                value_atpeak = histo.GetBinContent(histo.GetMaximumBin())
                left_edge = histo.FindBin(-3.0)
                right_edge = histo.FindBin(3.0)
                
                value_for_left_edge = histo.GetBinContent(left_edge)
                value_for_right_edge = histo.GetBinContent(right_edge)
                if value_atpeak != 0:
                    delta = fabs(value_for_left_edge - value_for_right_edge)
                    minvalue = min(value_for_left_edge,value_for_right_edge)
                    maxvalue = max(value_for_left_edge,value_for_right_edge)
                    errmin = sqrt(minvalue)

                    if fabs(maxvalue-minvalue) <= errmin: 
                        delta1 = 100.0-(100.0*(value_atpeak - value_for_left_edge)/value_atpeak)
                        delta2 = 100.0-(100.0*(value_atpeak - value_for_right_edge)/value_atpeak)
                        meanvalue.append(max(delta1,delta2))
                    else:
                        meanvalue.append(1.)
            except AttributeError:
                meanvalue.append(-100)
        return meanvalue

    def plotHisto(self,histoname):
        c1 = TCanvas('c1','Imported ROOT histogram',200,10,700,500)    
        h1 = gDirectory.FindObjectAny(histoname)
        print h1.GetMean()
        h1.Draw()
        c1.Update()
        return c1

##    def setColour(self,mean_bx,mean_cls,glob_eff):
    def setColour(self,mean_bx,mean_cls,noise,eff,masked):
        colour =''
        countRed = 0
        countGreen = 0
        countBlack = 0
        for value in mean_bx:
            if -3 < float(value) < -1. or 1. < float(value) < 3: countRed += 1
            elif -1. < float(value) < 1.: countGreen += 1
            elif float(value) == -100: countBlack += 1

        for value in mean_cls:
            if 2.5 < float(value): countRed += 1
            elif 1 <= float(value) <= 2.5: countGreen += 1
            elif float(value) == -100 or float(value) == 0.0: countBlack += 1

        for value in noise:
            if float(value) > 20: countRed += 1
            elif  0. <= float(value) <= 20: countGreen += 1
            elif float(value) == -100: countBlack += 1

        for value in eff:
            if 0 <= float(value) < 90: countRed += 1
            elif 90 <= float(value) <= 100: countGreen += 1
            elif float(value) == -100: countBlack += 1

        for value in masked:
            if float(value) > 4.: countRed += 1
            elif 0. <= float(value) <= 4.: countGreen += 1
            elif float(value) == -100: countBlack += 1
            
        if countRed == 1 and countBlack == 0: colour = 'yellow'
        elif countRed == 2 and countBlack == 0: colour = 'orange'
        elif countRed > 2 and countBlack == 0: colour = 'red'
        elif countBlack > 0: colour = 'black'
        elif countGreen > 0 and countBlack == 0 and countRed == 0: colour = 'green'
        
        return colour

    def setColourBx(self,mean_bx):
        colour =''
        countRed = 0
        countGreen = 0
        countBlack = 0
        for value in mean_bx:
            if -3 < float(value) < -1. or 1. < float(value) < 3: countRed += 1
            elif -1. <= float(value) <= 1.: countGreen += 1
            elif float(value) == -100: countBlack += 1

        if countRed == 1 and countBlack == 0: colour = 'yellow'
        elif countRed >= 2 and countBlack == 0: colour = 'red'
        elif countBlack > 0: colour = 'black'
        elif countGreen > 0 and countBlack == 0 and countRed == 0: colour = 'green'
        
        return colour

    def setColourCls(self,mean_cls):
        colour =''       
        countRed = 0
        countGreen = 0
        countBlack = 0

        for value in mean_cls:
            if 2.5 < float(value): countRed += 1
            elif 1 <= float(value) <= 2.5: countGreen += 1
            elif float(value) == -100 or float(value) == 0.0: countBlack += 1

        if countRed == 1 and countBlack == 0: colour = 'yellow'
        elif countRed >= 2 and countBlack == 0: colour = 'red'
        elif countBlack > 0: colour = 'black'
        elif countGreen > 0 and countBlack == 0 and countRed == 0: colour = 'green'
        
        return colour
    
    def setColourEff(self,eff):
        colour =''
        countRed = 0
        countGreen = 0
        countBlack = 0

        for value in eff:
            if 0 <= float(value) < 90: countRed += 1
            elif 90 <= float(value) <= 100: countGreen += 1
            elif float(value) == -100: countBlack += 1

        if countRed == 1 and countBlack == 0: colour = 'yellow'
        elif countRed >= 2 and countBlack == 0: colour = 'red'
        elif countBlack > 0: colour = 'black'
        elif countGreen > 0 and countBlack == 0 and countRed == 0: colour = 'green'
        
        return colour
    
    def setColourNoise(self,noise):
        colour =''
        countRed = 0
        countGreen = 0
        countBlack = 0

        for value in noise:
            if float(value) > 20.: countRed += 1
            elif 0. <= float(value) <= 20.: countGreen += 1
            elif float(value) == -100: countBlack += 1

        if countRed == 1 and countBlack == 0: colour = 'yellow'
        elif countRed >= 2 and countBlack == 0: colour = 'red'
        elif countBlack > 0: colour = 'black'
        elif countGreen > 0 and countBlack == 0 and countRed == 0: colour = 'green'

        return colour

    def setColourMasked(self,masked):
        colour =''
        countRed = 0
        countGreen = 0
        countBlack = 0

        for value in masked:
            if float(value) > 4.: countRed += 1
            elif 0. <= float(value) <= 4.: countGreen += 1
            elif float(value) == -100: countBlack += 1

        if countRed == 1 and countBlack == 0: colour = 'yellow'
        elif countRed >= 2 and countBlack == 0: colour = 'red'
        elif countBlack > 0: colour = 'black'
        elif countGreen > 0 and countBlack == 0 and countRed == 0: colour = 'green'

        return colour
