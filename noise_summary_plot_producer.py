#! /usr/bin/env python
from Tkinter import *
import commands
import sys, os, string, fileinput
from sys import argv
from ROOT import *

if __name__ == '__main__':  

    #print 'ahi vamos'

    RootFile=TFile.Open(str(sys.argv[1]))#"97003_noise_v4.root")
    outname = str(sys.argv[1]) + '_summary_out.root'
    RootOut=TFile.Open(outname,"RECREATE")
    #    file=open("rolls.txt")

    #    print "Creating a text file with the write() method."
    #   text_file = open("output_rolls.txt", "w")
    
    #  while 1:
    #     line = file.readline()
    #    if not line: break
    #process(line)
    #   print str(line)
    wheels = ['W-2','W-1','W+0','W+1','W+2']
    sectors = ['S04','S05','S06','S07','S08','S09','S10','S11','S12','S01','S02','S03']
    #ch1 = TCanvas("Resume","Resumen",1200,600)
    title2 = 'wheels_summary_' + str(sys.argv[1])
    plot2 = TH1F(title2,title2,5,0,5)
    bin2 = 1
    for item in wheels:
#        print str(item)
        cont2 = 0
        ncont2 = 0
        title1 = str(item) + '_summary' + str(sys.argv[1])
        titlel = str(item) + '_layer_summary' + str(sys.argv[1])
        plotl = TH1F(titlel,titlel,4,0,4)
        plot1 = TH1F(title1,title1,12,0,12)
        bin1 = 1
        contl1 = 0
        ncontl1 = 0
        contl2 = 0
        ncontl2 = 0
        contl3 = 0
        ncontl3 = 0
        contl4 = 0
        ncontl4 = 0
        for ob in sectors:
#            print str(ob)
            cont1 = 0
            ncont1 = 0
            if(ob == 'S04' or ob == 'S10'):
                bin = 1
                if(ob=='S04'):
                    title = str(item)+'_Far_Side'+ str(sys.argv[1])
                else:
                    title = str(item)+'_Near_Side'+ str(sys.argv[1])
                plot = TH1F(title,title,110,0,110)
            histname = str(item)+'_'+str(ob)
            print histname
            histo = RootFile.FindObjectAny(histname)
            NumBins = histo.GetYaxis().GetNbins()
            #print NumBins
            for i in range(NumBins):
                binname = histo.GetYaxis().GetBinLabel(i+1)
#                print str(binname)
                proy = histo.ProjectionX(binname,i+1,i+1)
                #proy.GetXaxis().SetRangeUser(0,200)
                #proy.Draw()
                #ch1.SaveAs(binname+'.png')
                pnumbins = proy.GetXaxis().GetNbins()
                cont = 0
                ncont = 0
                for j in range(pnumbins):
                    if proy.GetBinContent(j+1) != 0 :
                        cont = cont + proy.GetBinContent(j+1)*1000000/175#*3.333
                        ncont = ncont + 1
                        cont1 = cont1 + proy.GetBinContent(j+1)*1000000/175#*3.333
                        ncont1 = ncont1 + 1
                        cont2 = cont2 + proy.GetBinContent(j+1)*1000000/175#*3.333
                        ncont2 = ncont2 + 1
    
                        if binname[6] == '1':
                            contl1 = contl1 + proy.GetBinContent(j+1)*1000000/175#*3.333
                            ncontl1 = ncontl1 + 1
#                            print 'Value of the proyeccion ' + str(proy.GetBinContent(j+1))
 #                           print 'Value of contl1 ' + str(contl1)
  #                          print ncontl1
                        else:
                            if binname[6] == '2':
#                                print binname
                  #              print 'contl antes ' + str(contl2)
                   #             print  'ncontl antes ' + str(ncontl2)
                    #            print 'rate '+str(proy.GetBinContent(j+1)*1000000#*3.333/175)
                                contl2 = contl2 + proy.GetBinContent(j+1)*1000000/175#*3.333
                                ncontl2 = ncontl2 + 1
                     #           print 'depues ' + str(contl2)
                      #          print  'despues ' + str(ncontl2)                                
                            else:
                                if binname[6] == '3':
                                    contl3 = contl3 + proy.GetBinContent(j+1)*1000000/175#*3.333
                                    ncontl3 = ncontl3 + 1
                                else:
                                    if binname[6] == '4':
                                        contl4 = contl4 + proy.GetBinContent(j+1)*1000000/175#*3.333
                                        ncontl4 = ncontl4 + 1
                if ncont == 0 :
                    #print 'No hay datos pa este roll'
                    plot.GetXaxis().SetBinLabel(bin,binname)
                    plot.SetBinContent(bin,0)
                else:
                    plot.GetXaxis().SetBinLabel(bin,binname)
                    plot.SetBinContent(bin,cont/ncont)
                bin = bin + 1
                plot.GetXaxis().SetLabelSize(0.03)
                plot.GetYaxis().SetTitle('Hz')
            if(ob == 'S09' or ob == 'S03'):
                plot.GetXaxis().LabelsOption("V")
                #ch1.SetBottomMargin(0.35)
                #ch1.SetLogy(1)
                gStyle.SetOptStat(0)
#                plot.GetYaxis().SetRangeUser(0.1,1000000)
                #plot.Draw()
                if(RootOut.cd()):
                   plot.Write()
                #ch1.SaveAs(title+'.png')
            if ncont1 == 0:
                plot1.GetXaxis().SetBinLabel(bin1,str(item)+'_'+str(ob))
                plot1.SetBinContent(bin1,0)
            else:
                plot1.GetXaxis().SetBinLabel(bin1,str(item)+'_'+str(ob))
                plot1.SetBinContent(bin1,cont1/ncont1)
            bin1 = bin1 +1    
        plot1.GetXaxis().LabelsOption("V")
        plot1.GetXaxis().SetLabelSize(0.03)
        plot1.GetYaxis().SetTitle('Hz')
        #ch1.SetLogy(1)
#        plot1.GetYaxis().SetRangeUser(0.1,1000000)
        #plot1.Draw()
        #ch1.SaveAs(title1+'.png')
        if(RootOut.cd()):
            plot1.Write()
        if ncont2 == 0:
            plot2.GetXaxis().SetBinLabel(bin2,str(item))
            plot2.SetBinContent(bin2,0)
            bin2 = bin2 + 1
        else:
            plot2.GetXaxis().SetBinLabel(bin2,str(item))
            plot2.SetBinContent(bin2,cont2/ncont2)
            bin2 = bin2 +1
        if ncontl1 == 0:
            plotl.GetXaxis().SetBinLabel(1,'Layer 1')
            plotl.SetBinContent(1,0)
        else:
            plotl.GetXaxis().SetBinLabel(1,'Layer 1')
            plotl.SetBinContent(1,contl1/ncontl1)
        if ncontl2 == 0:
            plotl.GetXaxis().SetBinLabel(2,'Layer 2')
            plotl.SetBinContent(2,0)
        else:
            #print str(contl2/ncontl2)
#            print 'bin name ' + str(item)+'_'+str(ob)
 #           print 'values of countl1 ncountl1 and ratiol1 ' + str(contl1) + ' ' + str(ncontl1) + ' ' + str(contl1/ncontl1)
            plotl.GetXaxis().SetBinLabel(2,'Layer 2')
            plotl.SetBinContent(2,contl2/ncontl2)
        if ncontl3 == 0:
            plotl.GetXaxis().SetBinLabel(3,'Layer 3')
            plotl.SetBinContent(3,0)
        else:
            plotl.GetXaxis().SetBinLabel(3,'Layer 3')
            plotl.SetBinContent(3,contl3/ncontl3)
        if ncontl4 == 0:
            plotl.GetXaxis().SetBinLabel(4,'Layer 4')
            plotl.SetBinContent(4,0)
        else:
            plotl.GetXaxis().SetBinLabel(4,'Layer 4')
            plotl.SetBinContent(4,contl4/ncontl4)
        #ch1.SetLogy(1)
        plotl.GetYaxis().SetTitle('Hz')
 #       plotl.GetYaxis().SetRangeUser(0.1,1000000)        
        #plotl.Draw()
        #ch1.SaveAs(titlel+'.png')
        if(RootOut.cd()):
            plotl.Write()
    plot2.GetYaxis().SetTitle('Hz')
    #ch1.SetLogy(1)
  #  plot2.GetYaxis().SetRangeUser(0.1,1000000)
    #plot2.Draw()
    #ch1.SaveAs(title2+'.png')
    if(RootOut.cd()):
        plot2.Write()
            #entries = histo.GetEntries()
    #   deadstrips = []
    #  
    #      print str(i)
    #text_file.write("Line 1\n")
    
    #  file.close()
    #  text_file.close()
