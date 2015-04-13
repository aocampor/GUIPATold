#! /usr/bin/env python
import commands
import sys, os, string, fileinput
from Tkinter import *
from math import *
##sys.argv.append('-b') 
from ROOT import *
import ROOT

from QualityPerformance import Diagnostic

class GlobalPlotsProduction(object):
    def __init__(self,root_file_name,run,path):
        
        self.RootFile=TFile.Open(root_file_name)

        self.NewRootFile=TFile.Open('GlobalPlots.root','RECREATE')
#       self.NewRootFile.cd()
        ROOT.gStyle.SetOptStat(ROOT.kFALSE)
#       ROOT.gROOT.SetBatch(ROOT.kTRUE)
        
##-------------------------------- Plot creation ------------------------------------------
         

#       hBarrel_bx = TH1F("Barrel_bx","Barrel bx",9,-4.5,4.5)
        hBarrel_bx = TH1F("Barrel_bx","Barrel bx",11,-5.5,5.5)
        hBarrel_masked = TH1F("Barrel_MaskedStrips","Barrel masked strips",100,0.,100.)
        ClusterSize_for_Barrel = TH1F("Barrel_ClusterSize","Barrel Cluster Size",100,0.,100.)
        hBarrel_eff = TH1F("Barrel_eff","Barrel eff",100,0.,100.)
        hBarrel_eff_STA = TH1F("Barrel_eff_STA","Barrel eff of STA",100,0.,100.) ##

#       hEndcap_bx = TH1F("Endcap_bx","Endcap bx",9,-4.5,4.5)
        hEndcap_bx = TH1F("Endcap_bx","Endcap bx",11,-5.5,5.5)
        hEndcap_masked = TH1F("Endcap_MaskedStrips","Endcap masked strips",100,0.,100.)
        ClusterSize_for_Endcap_P = TH1F("Endcap_ClusterSize_P","Positive Endcap Cluster Size",100,0.,100.)
        ClusterSize_for_Endcap_N = TH1F("Endcap_ClusterSize_N","Negative Endcap Cluster Size",100,0.,100.)
        hEndcap_eff = TH1F("Endcap_eff","Endcap eff",100,0.,100.)
        hEndcap_eff_STA = TH1F("Endcap_eff_STA","Endcap eff of STA",100,0.,100.) ##

        hWm2Near_eff = TH1F("hWm2Near_eff","W-2 Near",110,0.,110.)
        hWm2Far_eff = TH1F("hWm2Far_eff","W-2 Far",110,0.,110.)
        hWm1Near_eff = TH1F("hWm1Near_eff","W-1 Near",110,0.,110.)
        hWm1Far_eff = TH1F("hWm1Far_eff","W-1 Far",110,0.,110.)
        hW0Near_eff = TH1F("hW0Near_eff","W+0 Near",110,0.,110.)
        hW0Far_eff = TH1F("hW0Far_eff","W+0 Far",110,0.,110.)
        hWp1Near_eff = TH1F("hWp1Near_eff","W+1 Near",110,0.,110.)
        hWp1Far_eff = TH1F("hWp1Far_eff","W+1 Far",110,0.,110.)
        hWp2Near_eff = TH1F("hWp2Near_eff","W+2 Near",110,0.,110.)
        hWp2Far_eff = TH1F("hWp2Far_eff","W+2 Far",110,0.,110.)

        hWm2Near_eff_STA = TH1F("hWm2Near_eff_STA","W-2 Near of STA",110,0.,110.) ##
        hWm2Far_eff_STA = TH1F("hWm2Far_eff_STA","W-2 Far of STA",110,0.,110.) ##
        hWm1Near_eff_STA = TH1F("hWm1Near_eff_STA","W-1 Near of STA",110,0.,110.) ##
        hWm1Far_eff_STA = TH1F("hWm1Far_eff_STA","W-1 Far of STA",110,0.,110.) ##
        hW0Near_eff_STA = TH1F("hW0Near_eff_STA","W+0 Near of STA",110,0.,110.) ##
        hW0Far_eff_STA = TH1F("hW0Far_eff_STA","W+0 Far of STA",110,0.,110.) ##
        hWp1Near_eff_STA = TH1F("hWp1Near_eff_STA","W+1 Near of STA",110,0.,110.) ##
        hWp1Far_eff_STA = TH1F("hWp1Far_eff_STA","W+1 Far of STA",110,0.,110.) ##
        hWp2Near_eff_STA = TH1F("hWp2Near_eff_STA","W+2 Near of STA",110,0.,110.) ##
        hWp2Far_eff_STA = TH1F("hWp2Far_eff_STA","W+2 Far of STA",110,0.,110.) ##

        hWm2Near_masked = TH1F("hWm2Near_masked","W-2 Near",110,0.,110.)
        hWm2Far_masked = TH1F("hWm2Far_masked","W-2 Far",110,0.,110.)
        hWm1Near_masked = TH1F("hWm1Near_masked","W-1 Near",110,0.,110.)
        hWm1Far_masked = TH1F("hWm1Far_masked","W-1 Far",110,0.,110.)
        hW0Near_masked = TH1F("hW0Near_masked","W+0 Near",110,0.,110.)
        hW0Far_masked = TH1F("hW0Far_masked","W+0 Far",110,0.,110.)
        hWp1Near_masked = TH1F("hWp1Near_masked","W+1 Near",110,0.,110.)
        hWp1Far_masked = TH1F("hWp1Far_masked","W+1 Far",110,0.,110.)
        hWp2Near_masked = TH1F("hWp2Near_masked","W+2 Near",110,0.,110.)
        hWp2Far_masked = TH1F("hWp2Far_masked","W+2 Far",110,0.,110.)

        hWm2Near_bx = TH1F("hWm2Near_bx","W-2 Near",110,0.,110.)
        hWm2Far_bx = TH1F("hWm2Far_bx","W-2 Far",110,0.,110.)
        hWm1Near_bx = TH1F("hWm1Near_bx","W-1 Near",110,0.,110.)
        hWm1Far_bx = TH1F("hWm1Far_bx","W-1 Far",110,0.,110.)
        hW0Near_bx = TH1F("hW0Near_bx","W+0 Near",110,0.,110.)
        hW0Far_bx = TH1F("hW0Far_bx","W+0 Far",110,0.,110.)
        hWp1Near_bx = TH1F("hWp1Near_bx","W+1 Near",110,0.,110.)
        hWp1Far_bx = TH1F("hWp1Far_bx","W+1 Far",110,0.,110.)
        hWp2Near_bx = TH1F("hWp2Near_bx","W+2 Near",110,0.,110.)
        hWp2Far_bx = TH1F("hWp2Far_bx","W+2 Far",110,0.,110.)

        hDm1RE1_eff = TH1F("hDm1RE1_eff","D-1 RE1",110,0.,110.)
        hDm1RE2_eff = TH1F("hDm1RE2_eff","D-1 RE2",110,0.,110.)
        hDm1RE3_eff = TH1F("hDm1RE3_eff","D-1 RE3",110,0.,110.)
        hDm2RE1_eff = TH1F("hDm2RE1_eff","D-2 RE1",110,0.,110.)
        hDm2RE2_eff = TH1F("hDm2RE2_eff","D-2 RE2",110,0.,110.)
        hDm2RE3_eff = TH1F("hDm2RE3_eff","D-2 RE3",110,0.,110.)
        hDm3RE1_eff = TH1F("hDm3RE1_eff","D-3 RE1",110,0.,110.)
        hDm3RE2_eff = TH1F("hDm3RE2_eff","D-3 RE2",110,0.,110.)
        hDm3RE3_eff = TH1F("hDm3RE3_eff","D-3 RE3",110,0.,110.)

        hDp1RE1_eff = TH1F("hDp1RE1_eff","D+1 RE1",110,0.,110.)
        hDp1RE2_eff = TH1F("hDp1RE2_eff","D+1 RE2",110,0.,110.)
        hDp1RE3_eff = TH1F("hDp1RE3_eff","D+1 RE3",110,0.,110.)
        hDp2RE1_eff = TH1F("hDp2RE1_eff","D+2 RE1",110,0.,110.)
        hDp2RE2_eff = TH1F("hDp2RE2_eff","D+2 RE2",110,0.,110.)
        hDp2RE3_eff = TH1F("hDp2RE3_eff","D+2 RE3",110,0.,110.)
        hDp3RE1_eff = TH1F("hDp3RE1_eff","D+3 RE1",110,0.,110.)
        hDp3RE2_eff = TH1F("hDp3RE2_eff","D+3 RE2",110,0.,110.)
        hDp3RE3_eff = TH1F("hDp3RE3_eff","D+3 RE3",110,0.,110.)

        hDm1RE1_eff_STA = TH1F("hDm1RE1_eff_STA","D-1 RE1 of STA",110,0.,110.) ##
        hDm1RE2_eff_STA = TH1F("hDm1RE2_eff_STA","D-1 RE2 of STA",110,0.,110.) ##
        hDm1RE3_eff_STA = TH1F("hDm1RE3_eff_STA","D-1 RE3 of STA",110,0.,110.) ##
        hDm2RE1_eff_STA = TH1F("hDm2RE1_eff_STA","D-2 RE1 of STA",110,0.,110.) ##
        hDm2RE2_eff_STA = TH1F("hDm2RE2_eff_STA","D-2 RE2 of STA",110,0.,110.) ##
        hDm2RE3_eff_STA = TH1F("hDm2RE3_eff_STA","D-2 RE3 of STA",110,0.,110.) ##
        hDm3RE1_eff_STA = TH1F("hDm3RE1_eff_STA","D-3 RE1 of STA",110,0.,110.) ##
        hDm3RE2_eff_STA = TH1F("hDm3RE2_eff_STA","D-3 RE2 of STA",110,0.,110.) ##
        hDm3RE3_eff_STA = TH1F("hDm3RE3_eff_STA","D-3 RE3 of STA",110,0.,110.) ##

        hDp1RE1_eff_STA = TH1F("hDp1RE1_eff_STA","D+1 RE1 of STA",110,0.,110.) ##
        hDp1RE2_eff_STA = TH1F("hDp1RE2_eff_STA","D+1 RE2 of STA",110,0.,110.) ##
        hDp1RE3_eff_STA = TH1F("hDp1RE3_eff_STA","D+1 RE3 of STA",110,0.,110.) ##
        hDp2RE1_eff_STA = TH1F("hDp2RE1_eff_STA","D+2 RE1 of STA",110,0.,110.) ##
        hDp2RE2_eff_STA = TH1F("hDp2RE2_eff_STA","D+2 RE2 of STA",110,0.,110.) ##
        hDp2RE3_eff_STA = TH1F("hDp2RE3_eff_STA","D+2 RE3 of STA",110,0.,110.) ##
        hDp3RE1_eff_STA = TH1F("hDp3RE1_eff_STA","D+3 RE1 of STA",110,0.,110.) ##
        hDp3RE2_eff_STA = TH1F("hDp3RE2_eff_STA","D+3 RE2 of STA",110,0.,110.) ##
        hDp3RE3_eff_STA = TH1F("hDp3RE3_eff_STA","D+3 RE3 of STA",110,0.,110.) ##

        hDm1RE1_masked = TH1F("hDm1RE1_masked","D-1 RE1",110,0.,110.)
        hDm1RE2_masked = TH1F("hDm1RE2_masked","D-1 RE2",110,0.,110.)
        hDm1RE3_masked = TH1F("hDm1RE3_masked","D-1 RE3",110,0.,110.)
        hDm2RE1_masked = TH1F("hDm2RE1_masked","D-2 RE1",110,0.,110.)
        hDm2RE2_masked = TH1F("hDm2RE2_masked","D-2 RE2",110,0.,110.)
        hDm2RE3_masked = TH1F("hDm2RE3_masked","D-2 RE3",110,0.,110.)
        hDm3RE1_masked = TH1F("hDm3RE1_masked","D-3 RE1",110,0.,110.)
        hDm3RE2_masked = TH1F("hDm3RE2_masked","D-3 RE2",110,0.,110.)
        hDm3RE3_masked = TH1F("hDm3RE3_masked","D-3 RE3",110,0.,110.)

        hDp1RE1_masked = TH1F("hDp1RE1_masked","D+1 RE1",110,0.,110.)
        hDp1RE2_masked = TH1F("hDp1RE2_masked","D+1 RE2",110,0.,110.)
        hDp1RE3_masked = TH1F("hDp1RE3_masked","D+1 RE3",110,0.,110.)
        hDp2RE1_masked = TH1F("hDp2RE1_masked","D+2 RE1",110,0.,110.)
        hDp2RE2_masked = TH1F("hDp2RE2_masked","D+2 RE2",110,0.,110.)
        hDp2RE3_masked = TH1F("hDp2RE3_masked","D+2 RE3",110,0.,110.)
        hDp3RE1_masked = TH1F("hDp3RE1_masked","D+3 RE1",110,0.,110.)
        hDp3RE2_masked = TH1F("hDp3RE2_masked","D+3 RE2",110,0.,110.)
        hDp3RE3_masked = TH1F("hDp3RE3_masked","D+3 RE3",110,0.,110.)

        hDm1RE1_bx = TH1F("hDm1RE1_bx","D-1 RE1",110,0.,110.)
        hDm1RE2_bx = TH1F("hDm1RE2_bx","D-1 RE2",110,0.,110.)
        hDm1RE3_bx = TH1F("hDm1RE3_bx","D-1 RE3",110,0.,110.)
        hDm2RE1_bx = TH1F("hDm2RE1_bx","D-2 RE1",110,0.,110.)
        hDm2RE2_bx = TH1F("hDm2RE2_bx","D-2 RE2",110,0.,110.)
        hDm2RE3_bx = TH1F("hDm2RE3_bx","D-2 RE3",110,0.,110.)
        hDm3RE1_bx = TH1F("hDm3RE1_bx","D-3 RE1",110,0.,110.)
        hDm3RE2_bx = TH1F("hDm3RE2_bx","D-3 RE2",110,0.,110.)
        hDm3RE3_bx = TH1F("hDm3RE3_bx","D-3 RE3",110,0.,110.)

        hDp1RE1_bx = TH1F("hDp1RE1_bx","D+1 RE1",110,0.,110.)
        hDp1RE2_bx = TH1F("hDp1RE2_bx","D+1 RE2",110,0.,110.)
        hDp1RE3_bx = TH1F("hDp1RE3_bx","D+1 RE3",110,0.,110.)
        hDp2RE1_bx = TH1F("hDp2RE1_bx","D+2 RE1",110,0.,110.)
        hDp2RE2_bx = TH1F("hDp2RE2_bx","D+2 RE2",110,0.,110.)
        hDp2RE3_bx = TH1F("hDp2RE3_bx","D+2 RE3",110,0.,110.)
        hDp3RE1_bx = TH1F("hDp3RE1_bx","D+3 RE1",110,0.,110.)
        hDp3RE2_bx = TH1F("hDp3RE2_bx","D+3 RE2",110,0.,110.)
        hDp3RE3_bx = TH1F("hDp3RE3_bx","D+3 RE3",110,0.,110.)
 
        hWm2_masked = TH1F("Wm2_MaskedStrips","W-2 masked strips",100,0.,100.)
        hWm2_eff = TH1F("Wm2_eff","W-2 eff",100,0.,100.)
        hWm2_eff_STA = TH1F("Wm2_eff_STA","W-2 eff of STA",100,0.,100.)

        hWm1_masked = TH1F("Wm1_MaskedStrips","W-1 masked strips",100,0.,100.)
        hWm1_eff = TH1F("Wm1_eff","W-1 eff",100,0.,100.)
        hWm1_eff_STA = TH1F("Wm1_eff_STA","W-1 eff of STA",100,0.,100.)

        hW0_masked = TH1F("W0_MaskedStrips","W+0 masked strips",100,0.,100.)
        hW0_eff = TH1F("W0_eff","W+0 eff",100,0.,100.)
        hW0_eff_STA = TH1F("W0_eff_STA","W+0 eff of STA",100,0.,100.)

        hWp1_masked = TH1F("Wp1_MaskedStrips","W+1 masked strips",100,0.,100.)
        hWp1_eff = TH1F("Wp1_eff","W+1 eff",100,0.,100.)
        hWp1_eff_STA = TH1F("Wp1_eff_STA","W+1 eff of STA",100,0.,100.)

        hWp2_masked = TH1F("Wp2_MaskedStrips","W+2 masked strips",100,0.,100.)
        hWp2_eff = TH1F("Wp2_eff","W+2 eff",100,0.,100.)
        hWp2_eff_STA = TH1F("Wp2_eff_STA","W+2 eff of STA",100,0.,100.)

        hDm3_masked = TH1F("Dm3_MaskedStrips","D-3 masked strips",100,0.,100.)
        hDm3_eff = TH1F("Dm3_eff","D-3 eff",100,0.,100.)
        hDm3_eff_STA = TH1F("Dm3_eff_STA","D-3 eff of STA",100,0.,100.)

        hDm2_masked = TH1F("Dm2_MaskedStrips","D-2 masked strips",100,0.,100.)
        hDm2_eff = TH1F("Dm2_eff","D-2 eff",100,0.,100.)
        hDm2_eff_STA = TH1F("Dm2_eff_STA","D-2 eff of STA",100,0.,100.)

        hDm1_masked = TH1F("Dm1_MaskedStrips","D-1 masked strips",100,0.,100.)
        hDm1_eff = TH1F("Dm1_eff","D-1 eff",100,0.,100.)
        hDm1_eff_STA = TH1F("Dm1_eff_STA","D-1 eff_STA",100,0.,100.)

        hDp3_masked = TH1F("Dp3_MaskedStrips","D+3 masked strips",100,0.,100.)
        hDp3_eff = TH1F("Dp3_eff","D+3 eff",100,0.,100.)
        hDp3_eff_STA = TH1F("Dp3_eff_STA","D+3 eff of STA",100,0.,100.)

        hDp2_masked = TH1F("Dp2_MaskedStrips","D+2 masked strips",100,0.,100.)
        hDp2_eff = TH1F("Dp2_eff","D+2 eff",100,0.,100.)
        hDp2_eff_STA = TH1F("Dp2_eff_STA","D+2 eff of STA",100,0.,100.)

        hDp1_masked = TH1F("Dp1_MaskedStrips","D+1 masked strips",100,0.,100.)
        hDp1_eff = TH1F("Dp1_eff","D+1 eff",100,0.,100.)
        hDp1_eff_STA = TH1F("Dp1_eff_STA","D+1 eff of STA",100,0.,100.)

        self.RootFile.cd()

#       BxDistribution_Wheel_m2 = ROOT.gROOT.FindObjectAny("BxDistribution_Wheel_-2")
#       BxDistribution_Wheel_m1 = ROOT.gROOT.FindObjectAny("BxDistribution_Wheel_-1")
 #      BxDistribution_Wheel_0 = ROOT.gROOT.FindObjectAny("BxDistribution_Wheel_0")
  #     BxDistribution_Wheel_p1 = ROOT.gROOT.FindObjectAny("BxDistribution_Wheel_+1")
   #    BxDistribution_Wheel_p2 = ROOT.gROOT.FindObjectAny("BxDistribution_Wheel_+2")
    #   BxDistribution_Disk_p1 = ROOT.gROOT.FindObjectAny("BxDistribution_Disk_+1")
     #  BxDistribution_Disk_p2 = ROOT.gROOT.FindObjectAny("BxDistribution_Disk_+2")
      # BxDistribution_Disk_p3 = ROOT.gROOT.FindObjectAny("BxDistribution_Disk_+3")

        TH1F.BxDistribution_Wheel_m2 = gDirectory.FindObjectAny("BxDistribution_Wheel_-2")
        TH1F.BxDistribution_Wheel_m1 = gDirectory.FindObjectAny("BxDistribution_Wheel_-1")
        TH1F.BxDistribution_Wheel_0 = gDirectory.FindObjectAny("BxDistribution_Wheel_0")
        TH1F.BxDistribution_Wheel_p1 = gDirectory.FindObjectAny("BxDistribution_Wheel_1")
        TH1F.BxDistribution_Wheel_p2 = gDirectory.FindObjectAny("BxDistribution_Wheel_2")
        TH1F.BxDistribution_Disk_m1 = gDirectory.FindObjectAny("BxDistribution_Disk_-1")
        TH1F.BxDistribution_Disk_m2 = gDirectory.FindObjectAny("BxDistribution_Disk_-2")
        TH1F.BxDistribution_Disk_m3 = gDirectory.FindObjectAny("BxDistribution_Disk_-3")
        TH1F.BxDistribution_Disk_p1 = gDirectory.FindObjectAny("BxDistribution_Disk_1")
        TH1F.BxDistribution_Disk_p2 = gDirectory.FindObjectAny("BxDistribution_Disk_2")
        TH1F.BxDistribution_Disk_p3 = gDirectory.FindObjectAny("BxDistribution_Disk_3")

#       ClusterSize_Wheel_m2 = ROOT.gROOT.FindObjectAny("ClusterSize_Wheel_-2")
#       ClusterSize_Wheel_m1 = ROOT.gROOT.FindObjectAny("ClusterSize_Wheel_-1")
#       ClusterSize_Wheel_0 = ROOT.gROOT.FindObjectAny("ClusterSize_Wheel_0")
 #      ClusterSize_Wheel_p1 = ROOT.gROOT.FindObjectAny("ClusterSize_Wheel_+1")
  #     ClusterSize_Wheel_p2 = ROOT.gROOT.FindObjectAny("ClusterSize_Wheel_+2")
   #    ClusterSize_Disk_p1 = ROOT.gROOT.FindObjectAny("ClusterSize_Disk_+1")
    #   ClusterSize_Disk_p2 = ROOT.gROOT.FindObjectAny("ClusterSize_Disk_+2")
     #  ClusterSize_Disk_p3 = ROOT.gROOT.FindObjectAny("ClusterSize_Disk_+3")

        TH1F.ClusterSize_for_Barrel  = gDirectory.FindObjectAny("ClusterSize_for_Barrel")
        TH1F.ClusterSize_for_Endcap_P = gDirectory.FindObjectAny("ClusterSize_for_EndcapPositive")
        TH1F.ClusterSize_for_Endcap_N = gDirectory.FindObjectAny("ClusterSize_for_EndcapNegative")
        TH1F.ClusterSize_Wheel_m2 = gDirectory.FindObjectAny("ClusterSize_Wheel_-2")
        TH1F.ClusterSize_Wheel_m1 = gDirectory.FindObjectAny("ClusterSize_Wheel_-1")
        TH1F.ClusterSize_Wheel_0 = gDirectory.FindObjectAny("ClusterSize_Wheel_0")
        TH1F.ClusterSize_Wheel_p1 = gDirectory.FindObjectAny("ClusterSize_Wheel_1")
        TH1F.ClusterSize_Wheel_p2 = gDirectory.FindObjectAny("ClusterSize_Wheel_2")
        TH1F.ClusterSize_Disk_m1 = gDirectory.FindObjectAny("ClusterSize_Disk_-1")
        TH1F.ClusterSize_Disk_m2 = gDirectory.FindObjectAny("ClusterSize_Disk_-2")
        TH1F.ClusterSize_Disk_m3 = gDirectory.FindObjectAny("ClusterSize_Disk_-3")
        TH1F.ClusterSize_Disk_p1 = gDirectory.FindObjectAny("ClusterSize_Disk_1")
        TH1F.ClusterSize_Disk_p2 = gDirectory.FindObjectAny("ClusterSize_Disk_2")
        TH1F.ClusterSize_Disk_p3 = gDirectory.FindObjectAny("ClusterSize_Disk_3")

#---------------------------------------- Bx of Barrel ---------------------------------------------------

        Bx_m2 = []
        Bx_m1 = []
        Bx_0 = []
        Bx_p1 = []
        Bx_p2 = []
        Bx_tot = []
        Bx_mean = []

        self.countwheel = self.getCountWheel()

        for n in range(12):        
            Bx_m2.append(self.getBinEntry("-2")[n])
            Bx_m1.append(self.getBinEntry("-1")[n])
            Bx_0.append(self.getBinEntry("0")[n])
            Bx_p1.append(self.getBinEntry("1")[n])
            Bx_p2.append(self.getBinEntry("2")[n])

            Bx_tot.append(Bx_m2[n] + Bx_m1[n] + Bx_0[n] + Bx_p1[n] + Bx_p2[n])
            Bx_mean.append(Bx_tot[n]/self.countwheel)

        for n in range(1,12):
            hBarrel_bx.SetBinContent(n,Bx_mean[n])

#---------------------------------- Bx of Endcap --------------------------------

        Bx_Dm1 = []
        Bx_Dm2 = []
        Bx_Dm3 = []
        Bx_Dp1 = []
        Bx_Dp2 = []
        Bx_Dp3 = []
        Bx_Dtot = []
        Bx_Dmean = []

        self.countdisk = self.getCountDisk()

        for n in range(12):
            Bx_Dm1.append(self.getBinEntryDisk("-1")[n])
            Bx_Dm2.append(self.getBinEntryDisk("-2")[n])
            Bx_Dm3.append(self.getBinEntryDisk("-3")[n])
            Bx_Dp1.append(self.getBinEntryDisk("1")[n])
            Bx_Dp2.append(self.getBinEntryDisk("2")[n])
            Bx_Dp3.append(self.getBinEntryDisk("3")[n])
  
            Bx_Dtot.append(Bx_Dm1[n] + Bx_Dm2[n] + Bx_Dm3[n] + Bx_Dp1[n] + Bx_Dp2[n] + Bx_Dp3[n])
            if(self.countdisk != 0):
                Bx_Dmean.append(Bx_Dtot[n]/self.countdisk)
            else:
                Bx_Dmean.append(0)
                
        for n in range(1,12):
            hEndcap_bx.SetBinContent(n,Bx_Dmean[n])
             
##------------------------------------ Plot filling -----------------------------------

        listWheel = ['W-2','W-1','W+0','W+1','W+2']
        listDisk = ['RE-3','RE-2','RE-1','RE+1','RE+2','RE+3']

        counterWm2Near = 0
        counterWm2Far = 0
        counterWm1Near = 0
        counterWm1Far = 0
        counterWp2Near = 0
        counterWp2Far = 0
        counterWp1Near = 0
        counterWp1Far = 0
        counterW0Near = 0
        counterW0Far = 0

        counterDm3RE3 = 0
        counterDm3RE2 = 0
        counterDm3RE1 = 0
        counterDm2RE3 = 0
        counterDm2RE2 = 0
        counterDm2RE1 = 0
        counterDm1RE3 = 0
        counterDm1RE2 = 0
        counterDm1RE1 = 0

        counterDp3RE3 = 0
        counterDp3RE2 = 0
        counterDp3RE1 = 0
        counterDp2RE3 = 0
        counterDp2RE2 = 0
        counterDp2RE1 = 0
        counterDp1RE3 = 0
        counterDp1RE2 = 0
        counterDp1RE1 = 0

        for line in self.fillDetListBarrel():
            for el in listWheel:
                coord = line.rstrip().split("  ")
                name = el+'_'+coord[0]
                histoname_bx = 'BXN_'+el+'_' + coord[0]
                histoname_occ = 'Occupancy_'+el+'_'+coord[0]
                histoname_Eff = 'LocalEfficiencyFromSegments_'+el+'_' + coord[0]
                histoname_Eff_STA = 'LocalEfficiencyFromTrack_'+el+'_' + coord[0] ##

#               hBarrel_bx.Fill(self.getMeanValue(histoname_bx)[0])
#               hBarrel_bx.Fill(self.getMeanValue(histoname_bx)[2])
                hBarrel_masked.Fill(self.getMaskedStrip(histoname_occ)[0])
                hBarrel_masked.Fill(self.getMaskedStrip(histoname_occ)[1])
                hBarrel_eff.Fill(self.getMedia(histoname_Eff)[0])
                hBarrel_eff.Fill(self.getMedia(histoname_Eff)[2])
                hBarrel_eff_STA.Fill(self.getMedia(histoname_Eff_STA)[0]) ##
                hBarrel_eff_STA.Fill(self.getMedia(histoname_Eff_STA)[2]) ##

                if len(self.getMedia(histoname_Eff)) == 6:
                    hBarrel_masked.Fill(self.getMaskedStrip(histoname_occ)[2])
                    hBarrel_eff.Fill(self.getMedia(histoname_Eff)[4])
                    hBarrel_eff_STA.Fill(self.getMedia(histoname_Eff_STA)[4]) ##
#                   hBarrel_bx.Fill(self.getMeanValue(histoname_bx)[4])

####-------------------------- Wheel -2 ----------------------------------------------------------------------

                if el == "W-2":
                    if self.findNear(name):
                        name_roll = name + "_For"
                        counterWm2Near+=1

                        if self.getMedia(histoname_Eff)[0] != -100:
                            hWm2Near_eff.SetBinContent(counterWm2Near,self.getMedia(histoname_Eff)[0]) 
                            hWm2Near_eff.SetBinError(counterWm2Near,self.getMedia(histoname_Eff)[1])
                        else:
                            hWm2Near_eff.SetBinContent(counterWm2Near,0)
                            hWm2Near_eff.SetBinError(counterWm2Near,0)

                        hWm2Near_eff.GetXaxis().SetBinLabel(counterWm2Near,name_roll)

                        if self.getMedia(histoname_Eff_STA)[0] != -100: ##
                            hWm2Near_eff_STA.SetBinContent(counterWm2Near,self.getMedia(histoname_Eff_STA)[0]) ##
                            hWm2Near_eff_STA.SetBinError(counterWm2Near,self.getMedia(histoname_Eff_STA)[1]) ##
                        else: ##
                            hWm2Near_eff_STA.SetBinContent(counterWm2Near,0) ##
                            hWm2Near_eff_STA.SetBinError(counterWm2Near,0) ##
                            
                        hWm2Near_eff_STA.GetXaxis().SetBinLabel(counterWm2Near,name_roll) ##

                        hWm2Near_masked.SetBinContent(counterWm2Near,self.getMaskedStrip(histoname_occ)[0])
                        hWm2Near_masked.GetXaxis().SetBinLabel(counterWm2Near,name_roll)
                        hWm2Near_bx.SetBinContent(counterWm2Near,self.getMeanValue(histoname_bx)[0])
                        hWm2Near_bx.SetBinError(counterWm2Near,self.getMeanValue(histoname_bx)[1])
                        hWm2Near_bx.GetXaxis().SetBinLabel(counterWm2Near,name_roll)
                        name_roll = name + "_Back"
                        counterWm2Near += 1
                        
                        if self.getMedia(histoname_Eff)[2] != -100:
                            hWm2Near_eff.SetBinContent(counterWm2Near,self.getMedia(histoname_Eff)[2])
                            hWm2Near_eff.SetBinError(counterWm2Near,self.getMedia(histoname_Eff)[3])
                        else:
                            hWm2Near_eff.SetBinContent(counterWm2Near,0)
                            hWm2Near_eff.SetBinError(counterWm2Near,0)

                        hWm2Near_eff.GetXaxis().SetBinLabel(counterWm2Near,name_roll)

                        if self.getMedia(histoname_Eff_STA)[2] != -100: ##
                            hWm2Near_eff_STA.SetBinContent(counterWm2Near,self.getMedia(histoname_Eff_STA)[2]) ##
                            hWm2Near_eff_STA.SetBinError(counterWm2Near,self.getMedia(histoname_Eff_STA)[3]) ##
                        else:
                            hWm2Near_eff_STA.SetBinContent(counterWm2Near,0) ##
                            hWm2Near_eff_STA.SetBinError(counterWm2Near,0)
                                
                        hWm2Near_eff_STA.GetXaxis().SetBinLabel(counterWm2Near,name_roll)

                        hWm2Near_masked.SetBinContent(counterWm2Near,self.getMaskedStrip(histoname_occ)[1])
                        hWm2Near_masked.GetXaxis().SetBinLabel(counterWm2Near,name_roll)
                        hWm2Near_bx.SetBinContent(counterWm2Near,self.getMeanValue(histoname_bx)[2])
                        hWm2Near_bx.SetBinError(counterWm2Near,self.getMeanValue(histoname_bx)[3])
                        hWm2Near_bx.GetXaxis().SetBinLabel(counterWm2Near,name_roll)
                    if self.findNear(name) == False:
                        name_roll = name + "_For"
                        counterWm2Far+=1

                        if self.getMedia(histoname_Eff)[0] != -100:
                            hWm2Far_eff.SetBinContent(counterWm2Far,self.getMedia(histoname_Eff)[0])
                            hWm2Far_eff.SetBinError(counterWm2Far,self.getMedia(histoname_Eff)[1])
                        else:
                            hWm2Far_eff.SetBinContent(counterWm2Far,0)
                            hWm2Far_eff.SetBinError(counterWm2Far,0)

                        hWm2Far_eff.GetXaxis().SetBinLabel(counterWm2Far,name_roll)

                        if self.getMedia(histoname_Eff_STA)[0] != -100: ##
                            hWm2Far_eff_STA.SetBinContent(counterWm2Far,self.getMedia(histoname_Eff_STA)[0]) ##
                            hWm2Far_eff_STA.SetBinError(counterWm2Far,self.getMedia(histoname_Eff_STA)[1]) ##
                        else:
                            hWm2Far_eff_STA.SetBinContent(counterWm2Far,0) ##
                            hWm2Far_eff_STA.SetBinError(counterWm2Far,0) ##

                        hWm2Far_eff_STA.GetXaxis().SetBinLabel(counterWm2Far,name_roll) ##

                        hWm2Far_masked.SetBinContent(counterWm2Far,self.getMaskedStrip(histoname_occ)[0])
                        hWm2Far_masked.GetXaxis().SetBinLabel(counterWm2Far,name_roll)
                        hWm2Far_bx.SetBinContent(counterWm2Far,self.getMeanValue(histoname_bx)[0])
                        hWm2Far_bx.SetBinError(counterWm2Far,self.getMeanValue(histoname_bx)[1])
                        hWm2Far_bx.GetXaxis().SetBinLabel(counterWm2Far,name_roll)
              
                        counterWm2Far+=1
                        name_roll = name + "_Back"

                        if self.getMedia(histoname_Eff)[2] != -100:
                            hWm2Far_eff.SetBinContent(counterWm2Far,self.getMedia(histoname_Eff)[2])
                            hWm2Far_eff.SetBinError(counterWm2Far,self.getMedia(histoname_Eff)[3])
                        else:
                            hWm2Far_eff.SetBinContent(counterWm2Far,0)
                            hWm2Far_eff.SetBinError(counterWm2Far,0)

                        hWm2Far_eff.GetXaxis().SetBinLabel(counterWm2Far,name_roll)

                        if self.getMedia(histoname_Eff_STA)[2] != -100: ##
                            hWm2Far_eff_STA.SetBinContent(counterWm2Far,self.getMedia(histoname_Eff_STA)[2]) ##
                            hWm2Far_eff_STA.SetBinError(counterWm2Far,self.getMedia(histoname_Eff_STA)[3]) ##
                        else:
                            hWm2Far_eff_STA.SetBinContent(counterWm2Far,0) ##
                            hWm2Far_eff_STA.SetBinError(counterWm2Far,0) ##
                            
                        hWm2Far_eff_STA.GetXaxis().SetBinLabel(counterWm2Far,name_roll) ##
                        
                        hWm2Far_masked.SetBinContent(counterWm2Far,self.getMaskedStrip(histoname_occ)[1])
                        hWm2Far_masked.GetXaxis().SetBinLabel(counterWm2Far,name_roll)
                        hWm2Far_bx.SetBinContent(counterWm2Far,self.getMeanValue(histoname_bx)[2])
                        hWm2Far_bx.SetBinError(counterWm2Far,self.getMeanValue(histoname_bx)[3])
                        hWm2Far_bx.GetXaxis().SetBinLabel(counterWm2Far,name_roll)
                        
                    hWm2_masked.Fill(self.getMaskedStrip(histoname_occ)[0])
                    hWm2_masked.Fill(self.getMaskedStrip(histoname_occ)[1])
                    hWm2_eff.Fill(self.getMedia(histoname_Eff)[0])
                    hWm2_eff.Fill(self.getMedia(histoname_Eff)[2])
                    hWm2_eff_STA.Fill(self.getMedia(histoname_Eff_STA)[0]) ##
                    hWm2_eff_STA.Fill(self.getMedia(histoname_Eff_STA)[2]) ##

                    if len(self.getMedia(histoname_Eff)) == 6:
                        hWm2_masked.Fill(self.getMaskedStrip(histoname_occ)[2])
                        hWm2_eff.Fill(self.getMedia(histoname_Eff_STA)[4])
                        hWm2_eff_STA.Fill(self.getMedia(histoname_Eff_STA)[4])

                        if self.findNear(name):
                            counterWm2Near+=1
                            name_roll = name + "_Middle"
                            if self.getMedia(histoname_Eff)[4] != -100:
                                hWm2Near_eff.SetBinContent(counterWm2Near,self.getMedia(histoname_Eff)[4])
                                hWm2Near_eff.SetBinError(counterWm2Near,self.getMedia(histoname_Eff)[5])
                            else:
                                hWm2Near_eff.SetBinContent(counterWm2Near,0)
                                hWm2Near_eff.SetBinError(counterWm2Near,0)

                            hWm2Near_eff.GetXaxis().SetBinLabel(counterWm2Near,name_roll)

                            if self.getMedia(histoname_Eff_STA)[4] != -100:
                                hWm2Near_eff_STA.SetBinContent(counterWm2Near,self.getMedia(histoname_Eff_STA)[4])
                                hWm2Near_eff_STA.SetBinError(counterWm2Near,self.getMedia(histoname_Eff_STA)[5])
                            else:
                                hWm2Near_eff_STA.SetBinContent(counterWm2Near,0)
                                hWm2Near_eff_STA.SetBinError(counterWm2Near,0)

                            hWm2Near_eff_STA.GetXaxis().SetBinLabel(counterWm2Near,name_roll)

                            hWm2Near_masked.SetBinContent(counterWm2Near,self.getMaskedStrip(histoname_occ)[0])
                            hWm2Near_masked.GetXaxis().SetBinLabel(counterWm2Near,name_roll)
                            hWm2Near_bx.SetBinContent(counterWm2Near,self.getMeanValue(histoname_bx)[4])
                            hWm2Near_bx.SetBinError(counterWm2Near,self.getMeanValue(histoname_bx)[5])
                            hWm2Near_bx.GetXaxis().SetBinLabel(counterWm2Near,name_roll)

                        else:
                            counterWm2Far+=1
                            name_roll = name + "_Middle"

                            if self.getMedia(histoname_Eff)[4] != -100:
                                hWm2Far_eff.SetBinContent(counterWm2Far,self.getMedia(histoname_Eff)[4])
                                hWm2Far_eff.SetBinError(counterWm2Far,self.getMedia(histoname_Eff)[5])
                            else:
                                hWm2Far_eff.SetBinContent(counterWm2Far,0)
                                hWm2Far_eff.SetBinError(counterWm2Far,0)

                            hWm2Far_eff.GetXaxis().SetBinLabel(counterWm2Far,name_roll)

                            if self.getMedia(histoname_Eff_STA)[4] != -100:
                                hWm2Far_eff_STA.SetBinContent(counterWm2Far,self.getMedia(histoname_Eff_STA)[4])
                                hWm2Far_eff_STA.SetBinError(counterWm2Far,self.getMedia(histoname_Eff_STA)[5])
                            else:
                                hWm2Far_eff_STA.SetBinContent(counterWm2Far,0)
                                hWm2Far_eff_STA.SetBinError(counterWm2Far,0)

                            hWm2Far_eff_STA.GetXaxis().SetBinLabel(counterWm2Far,name_roll)

                            hWm2Far_masked.SetBinContent(counterWm2Far,self.getMaskedStrip(histoname_occ)[0])
                            hWm2Far_masked.GetXaxis().SetBinLabel(counterWm2Far,name_roll)
                            hWm2Far_bx.SetBinContent(counterWm2Far,self.getMeanValue(histoname_bx)[4])
                            hWm2Far_bx.SetBinError(counterWm2Far,self.getMeanValue(histoname_bx)[5])
                            hWm2Far_bx.GetXaxis().SetBinLabel(counterWm2Far,name_roll) 


####-------------------------- Wheel -1 ----------------------------------------------------------------------

                if el == "W-1":
                    if self.findNear(name):
                        name_roll = name + "_For"
                        counterWm1Near+=1

                        if self.getMedia(histoname_Eff)[0] != -100:
                            hWm1Near_eff.SetBinContent(counterWm1Near,self.getMedia(histoname_Eff)[0])
                            hWm1Near_eff.SetBinError(counterWm1Near,self.getMedia(histoname_Eff)[1])
                        else:
                            hWm1Near_eff.SetBinContent(counterWm1Near,0)
                            hWm1Near_eff.SetBinError(counterWm1Near,0)
                            
                        hWm1Near_eff.GetXaxis().SetBinLabel(counterWm1Near,name_roll)

                        if self.getMedia(histoname_Eff_STA)[0] != -100:
                            hWm1Near_eff_STA.SetBinContent(counterWm1Near,self.getMedia(histoname_Eff_STA)[0])
                            hWm1Near_eff_STA.SetBinError(counterWm1Near,self.getMedia(histoname_Eff_STA)[1])
                        else:
                            hWm1Near_eff_STA.SetBinContent(counterWm1Near,0)
                            hWm1Near_eff_STA.SetBinError(counterWm1Near,0)

                        hWm1Near_eff_STA.GetXaxis().SetBinLabel(counterWm1Near,name_roll)

                        hWm1Near_masked.SetBinContent(counterWm1Near,self.getMaskedStrip(histoname_occ)[0])
                        hWm1Near_masked.GetXaxis().SetBinLabel(counterWm1Near,name_roll)
                        hWm1Near_bx.SetBinContent(counterWm1Near,self.getMeanValue(histoname_bx)[0])
                        hWm1Near_bx.SetBinError(counterWm1Near,self.getMeanValue(histoname_bx)[1])
                        hWm1Near_bx.GetXaxis().SetBinLabel(counterWm1Near,name_roll)
                        
                        name_roll = name + "_Back"
                        counterWm1Near+=1
                        
                        if self.getMedia(histoname_Eff)[2] != -100:
                            hWm1Near_eff.SetBinContent(counterWm1Near,self.getMedia(histoname_Eff)[2])
                            hWm1Near_eff.SetBinError(counterWm1Near,self.getMedia(histoname_Eff)[3])
                        else:
                            hWm1Near_eff.SetBinContent(counterWm1Near,0)
                            hWm1Near_eff.SetBinError(counterWm1Near,0)
                                
                        hWm1Near_eff.GetXaxis().SetBinLabel(counterWm1Near,name_roll)

                        if self.getMedia(histoname_Eff_STA)[2] != -100:
                            hWm1Near_eff_STA.SetBinContent(counterWm1Near,self.getMedia(histoname_Eff_STA)[2])
                            hWm1Near_eff_STA.SetBinError(counterWm1Near,self.getMedia(histoname_Eff_STA)[3])
                        else:
                            hWm1Near_eff_STA.SetBinContent(counterWm1Near,0)
                            hWm1Near_eff_STA.SetBinError(counterWm1Near,0)

                        hWm1Near_eff_STA.GetXaxis().SetBinLabel(counterWm1Near,name_roll)

                        hWm1Near_masked.SetBinContent(counterWm1Near,self.getMaskedStrip(histoname_occ)[1])
                        hWm1Near_masked.GetXaxis().SetBinLabel(counterWm1Near,name_roll)
                        hWm1Near_bx.SetBinContent(counterWm1Near,self.getMeanValue(histoname_bx)[2])
                        hWm1Near_bx.SetBinError(counterWm1Near,self.getMeanValue(histoname_bx)[3])
                        hWm1Near_bx.GetXaxis().SetBinLabel(counterWm1Near,name_roll)

                    if self.findNear(name) == False:
                        name_roll = name + "_For"
                        counterWm1Far+=1

                        if self.getMedia(histoname_Eff)[0] != -100:
                            hWm1Far_eff.SetBinContent(counterWm1Far,self.getMedia(histoname_Eff)[0])
                            hWm1Far_eff.SetBinError(counterWm1Far,self.getMedia(histoname_Eff)[1])
                        else:
                            hWm1Far_eff.SetBinContent(counterWm1Far,0)
                            hWm1Far_eff.SetBinError(counterWm1Far,0)
                            
                        hWm1Far_eff.GetXaxis().SetBinLabel(counterWm1Far,name_roll)

                        if self.getMedia(histoname_Eff_STA)[0] != -100:
                            hWm1Far_eff_STA.SetBinContent(counterWm1Far,self.getMedia(histoname_Eff_STA)[0])
                            hWm1Far_eff_STA.SetBinError(counterWm1Far,self.getMedia(histoname_Eff_STA)[1])
                        else:
                            hWm1Far_eff_STA.SetBinContent(counterWm1Far,0)
                            hWm1Far_eff_STA.SetBinError(counterWm1Far,0)

                        hWm1Far_eff_STA.GetXaxis().SetBinLabel(counterWm1Far,name_roll)

                        hWm1Far_masked.SetBinContent(counterWm1Far,self.getMaskedStrip(histoname_occ)[0])
                        hWm1Far_masked.GetXaxis().SetBinLabel(counterWm1Far,name_roll)
                        hWm1Far_bx.SetBinContent(counterWm1Far,self.getMeanValue(histoname_bx)[0])
                        hWm1Far_bx.SetBinError(counterWm1Far,self.getMeanValue(histoname_bx)[1])
                        hWm1Far_bx.GetXaxis().SetBinLabel(counterWm1Far,name_roll)
                        
                        counterWm1Far+=1
                        name_roll = name + "_Back"

                        if self.getMedia(histoname_Eff)[2] != -100:
                            hWm1Far_eff.SetBinContent(counterWm1Far,self.getMedia(histoname_Eff)[2])
                            hWm1Far_eff.SetBinError(counterWm1Far,self.getMedia(histoname_Eff)[3])
                        else:
                            hWm1Far_eff.SetBinContent(counterWm1Far,0)
                            hWm1Far_eff.SetBinError(counterWm1Far,0)
                            
                        hWm1Far_eff.GetXaxis().SetBinLabel(counterWm1Far,name_roll)

                        if self.getMedia(histoname_Eff_STA)[2] != -100:
                            hWm1Far_eff_STA.SetBinContent(counterWm1Far,self.getMedia(histoname_Eff_STA)[2])
                            hWm1Far_eff_STA.SetBinError(counterWm1Far,self.getMedia(histoname_Eff_STA)[3])
                        else:
                            hWm1Far_eff_STA.SetBinContent(counterWm1Far,0)
                            hWm1Far_eff_STA.SetBinError(counterWm1Far,0)

                        hWm1Far_eff_STA.GetXaxis().SetBinLabel(counterWm1Far,name_roll)

                        hWm1Far_masked.SetBinContent(counterWm1Far,self.getMaskedStrip(histoname_occ)[1])
                        hWm1Far_masked.GetXaxis().SetBinLabel(counterWm1Far,name_roll)
                        hWm1Far_bx.SetBinContent(counterWm1Far,self.getMeanValue(histoname_bx)[2])
                        hWm1Far_bx.SetBinError(counterWm1Far,self.getMeanValue(histoname_bx)[3])
                        hWm1Far_bx.GetXaxis().SetBinLabel(counterWm1Far,name_roll)

                    hWm1_masked.Fill(self.getMaskedStrip(histoname_occ)[0])
                    hWm1_masked.Fill(self.getMaskedStrip(histoname_occ)[1])
                    hWm1_eff.Fill(self.getMedia(histoname_Eff)[0])
                    hWm1_eff.Fill(self.getMedia(histoname_Eff)[2])
                    hWm1_eff_STA.Fill(self.getMedia(histoname_Eff_STA)[0])
                    hWm1_eff_STA.Fill(self.getMedia(histoname_Eff_STA)[2])

                    if len(self.getMedia(histoname_Eff)) == 6:
                        hWm1_masked.Fill(self.getMaskedStrip(histoname_occ)[2])
                        hWm1_eff.Fill(self.getMedia(histoname_Eff)[4])
                        hWm1_eff_STA.Fill(self.getMedia(histoname_Eff_STA)[4])
                       
                        if self.findNear(name):
                            name_roll = name + "_Middle"
#                            print name_roll
                            counterWm1Near+=1
                            if self.getMedia(histoname_Eff)[4] != -100:
                                hWm1Near_eff.SetBinContent(counterWm1Near,self.getMedia(histoname_Eff)[4])
                                hWm1Near_eff.SetBinError(counterWm1Near,self.getMedia(histoname_Eff)[5])
                            else:
                                hWm1Near_eff.SetBinContent(counterWm1Near,0)
                                hWm1Near_eff.SetBinError(counterWm1Near,0)
                                
                            hWm1Near_eff.GetXaxis().SetBinLabel(counterWm1Near,name_roll)

                            if self.getMedia(histoname_Eff_STA)[4] != -100:
                                hWm1Near_eff_STA.SetBinContent(counterWm1Near,self.getMedia(histoname_Eff_STA)[4])
                                hWm1Near_eff_STA.SetBinError(counterWm1Near,self.getMedia(histoname_Eff_STA)[5])
                            else:
                                hWm1Near_eff_STA.SetBinContent(counterWm1Near,0)
                                hWm1Near_eff_STA.SetBinError(counterWm1Near,0)

                            hWm1Near_eff_STA.GetXaxis().SetBinLabel(counterWm1Near,name_roll)

                            hWm1Near_masked.SetBinContent(counterWm1Near,self.getMaskedStrip(histoname_occ)[0])
                            hWm1Near_masked.GetXaxis().SetBinLabel(counterWm1Near,name_roll)
                            hWm1Near_bx.SetBinContent(counterWm1Near,self.getMeanValue(histoname_bx)[4])
                            hWm1Near_bx.SetBinError(counterWm1Near,self.getMeanValue(histoname_bx)[5])
                            hWm1Near_bx.GetXaxis().SetBinLabel(counterWm1Near,name_roll)

                        else:
                            name_roll = name + "_Middle"
                            counterWm1Far+=1
                            if self.getMedia(histoname_Eff)[4] != -100:
                                hWm1Far_eff.SetBinContent(counterWm1Far,self.getMedia(histoname_Eff)[4])
                                hWm1Far_eff.SetBinError(counterWm1Far,self.getMedia(histoname_Eff)[5])
                            else:
                                hWm1Far_eff.SetBinContent(counterWm1Far,0)
                                hWm1Far_eff.SetBinError(counterWm1Far,0)
                                
                            hWm1Far_eff.GetXaxis().SetBinLabel(counterWm1Far,name_roll)

                            if self.getMedia(histoname_Eff_STA)[4] != -100:
                                hWm1Far_eff_STA.SetBinContent(counterWm1Far,self.getMedia(histoname_Eff_STA)[4])
                                hWm1Far_eff_STA.SetBinError(counterWm1Far,self.getMedia(histoname_Eff_STA)[5])
                            else:
                                hWm1Far_eff_STA.SetBinContent(counterWm1Far,0)
                                hWm1Far_eff_STA.SetBinError(counterWm1Far,0)

                            hWm1Far_eff_STA.GetXaxis().SetBinLabel(counterWm1Far,name_roll)

                            hWm1Far_masked.SetBinContent(counterWm1Far,self.getMaskedStrip(histoname_occ)[0])
                            hWm1Far_masked.GetXaxis().SetBinLabel(counterWm1Far,name_roll)
                            hWm1Far_bx.SetBinContent(counterWm1Far,self.getMeanValue(histoname_bx)[4])
                            hWm1Far_bx.SetBinError(counterWm1Far,self.getMeanValue(histoname_bx)[5])
                            hWm1Far_bx.GetXaxis().SetBinLabel(counterWm1Far,name_roll) 

####-------------------------- Wheel 0 ----------------------------------------------------------------------

                if el == "W+0":
                    if self.findNear(name):
                        name_roll = name + "_For"
                        counterW0Near+=1

                        if self.getMedia(histoname_Eff)[0] != -100:
                            hW0Near_eff.SetBinContent(counterW0Near,self.getMedia(histoname_Eff)[0])
                            hW0Near_eff.SetBinError(counterW0Near,self.getMedia(histoname_Eff)[1])
                        else:
                            hW0Near_eff.SetBinContent(counterW0Near,0)
                            hW0Near_eff.SetBinError(counterW0Near,0)
                            
                        hW0Near_eff.GetXaxis().SetBinLabel(counterW0Near,name_roll)

                        if self.getMedia(histoname_Eff_STA)[0] != -100:
                            hW0Near_eff_STA.SetBinContent(counterW0Near,self.getMedia(histoname_Eff_STA)[0])
                            hW0Near_eff_STA.SetBinError(counterW0Near,self.getMedia(histoname_Eff_STA)[1])
                        else:
                            hW0Near_eff_STA.SetBinContent(counterW0Near,0)
                            hW0Near_eff_STA.SetBinError(counterW0Near,0)

                        hW0Near_eff_STA.GetXaxis().SetBinLabel(counterW0Near,name_roll)

                        hW0Near_masked.SetBinContent(counterW0Near,self.getMaskedStrip(histoname_occ)[0])
                        hW0Near_masked.GetXaxis().SetBinLabel(counterW0Near,name_roll)
                        hW0Near_bx.SetBinContent(counterW0Near,self.getMeanValue(histoname_bx)[0])
                        hW0Near_bx.SetBinError(counterW0Near,self.getMeanValue(histoname_bx)[1])
                        hW0Near_bx.GetXaxis().SetBinLabel(counterW0Near,name_roll)
                        
                        name_roll = name + "_Back"
                        counterW0Near+=1
                        
                        if self.getMedia(histoname_Eff)[2] != -100:
                            hW0Near_eff.SetBinContent(counterW0Near,self.getMedia(histoname_Eff)[2])
                            hW0Near_eff.SetBinError(counterW0Near,self.getMedia(histoname_Eff)[3])
                        else:
                            hW0Near_eff.SetBinContent(counterW0Near,0)
                            hW0Near_eff.SetBinError(counterW0Near,0)
                                
                        hW0Near_eff.GetXaxis().SetBinLabel(counterW0Near,name_roll)

                        if self.getMedia(histoname_Eff_STA)[2] != -100:
                            hW0Near_eff_STA.SetBinContent(counterW0Near,self.getMedia(histoname_Eff_STA)[2])
                            hW0Near_eff_STA.SetBinError(counterW0Near,self.getMedia(histoname_Eff_STA)[3])
                        else:
                            hW0Near_eff_STA.SetBinContent(counterW0Near,0)
                            hW0Near_eff_STA.SetBinError(counterW0Near,0)

                        hW0Near_eff_STA.GetXaxis().SetBinLabel(counterW0Near,name_roll)

                        hW0Near_masked.SetBinContent(counterW0Near,self.getMaskedStrip(histoname_occ)[1])
                        hW0Near_masked.GetXaxis().SetBinLabel(counterW0Near,name_roll)
                        hW0Near_bx.SetBinContent(counterW0Near,self.getMeanValue(histoname_bx)[2])
                        hW0Near_bx.SetBinError(counterW0Near,self.getMeanValue(histoname_bx)[3])
                        hW0Near_bx.GetXaxis().SetBinLabel(counterW0Near,name_roll)

                    if self.findNear(name) == False:
                        name_roll = name + "_For"
                        counterW0Far+=1

                        if self.getMedia(histoname_Eff)[0] != -100:
                            hW0Far_eff.SetBinContent(counterW0Far,self.getMedia(histoname_Eff)[0])
                            hW0Far_eff.SetBinError(counterW0Far,self.getMedia(histoname_Eff)[1])
                        else:
                            hW0Far_eff.SetBinContent(counterW0Far,0)
                            hW0Far_eff.SetBinError(counterW0Far,0)

                        hW0Far_eff.GetXaxis().SetBinLabel(counterW0Far,name_roll)

                        if self.getMedia(histoname_Eff_STA)[0] != -100:
                            hW0Far_eff_STA.SetBinContent(counterW0Far,self.getMedia(histoname_Eff_STA)[0])
                            hW0Far_eff_STA.SetBinError(counterW0Far,self.getMedia(histoname_Eff_STA)[1])
                        else:
                            hW0Far_eff_STA.SetBinContent(counterW0Far,0)
                            hW0Far_eff_STA.SetBinError(counterW0Far,0)
                            
                        hW0Far_eff_STA.GetXaxis().SetBinLabel(counterW0Far,name_roll)

                        hW0Far_masked.SetBinContent(counterW0Far,self.getMaskedStrip(histoname_occ)[0])
                        hW0Far_masked.GetXaxis().SetBinLabel(counterW0Far,name_roll)
                        hW0Far_bx.SetBinContent(counterW0Far,self.getMeanValue(histoname_bx)[0])
                        hW0Far_bx.SetBinError(counterW0Far,self.getMeanValue(histoname_bx)[1])
                        hW0Far_bx.GetXaxis().SetBinLabel(counterW0Far,name_roll)
                        
                        name_roll = name + "_Back"
                        counterW0Far+=1  ##

                        if self.getMedia(histoname_Eff)[2] != -100:
                            hW0Far_eff.SetBinContent(counterW0Far,self.getMedia(histoname_Eff)[2])
                            hW0Far_eff.SetBinError(counterW0Far,self.getMedia(histoname_Eff)[3])
                        else:
                            hW0Far_eff.SetBinContent(counterW0Far,0)
                            hW0Far_eff.SetBinError(counterW0Far,0)
                            
                        hW0Far_eff.GetXaxis().SetBinLabel(counterW0Far,name_roll)

                        if self.getMedia(histoname_Eff_STA)[2] != -100:
                            hW0Far_eff_STA.SetBinContent(counterW0Far,self.getMedia(histoname_Eff_STA)[2])
                            hW0Far_eff_STA.SetBinError(counterW0Far,self.getMedia(histoname_Eff_STA)[3])
                        else:
                            hW0Far_eff_STA.SetBinContent(counterW0Far,0)
                            hW0Far_eff_STA.SetBinError(counterW0Far,0)

                        hW0Far_eff_STA.GetXaxis().SetBinLabel(counterW0Far,name_roll)

                        hW0Far_masked.SetBinContent(counterW0Far,self.getMaskedStrip(histoname_occ)[1])
                        hW0Far_masked.GetXaxis().SetBinLabel(counterW0Far,name_roll)
                        hW0Far_bx.SetBinContent(counterW0Far,self.getMeanValue(histoname_bx)[2])
                        hW0Far_bx.SetBinError(counterW0Far,self.getMeanValue(histoname_bx)[3])
                        hW0Far_bx.GetXaxis().SetBinLabel(counterW0Far,name_roll)
                        
                    hW0_masked.Fill(self.getMaskedStrip(histoname_occ)[0])
                    hW0_masked.Fill(self.getMaskedStrip(histoname_occ)[1])
                    hW0_eff.Fill(self.getMedia(histoname_Eff)[0])
                    hW0_eff.Fill(self.getMedia(histoname_Eff)[2])
                    hW0_eff_STA.Fill(self.getMedia(histoname_Eff_STA)[0])
                    hW0_eff_STA.Fill(self.getMedia(histoname_Eff_STA)[2])

                    if len(self.getMedia(histoname_Eff)) == 6:
                        hW0_masked.Fill(self.getMaskedStrip(histoname_occ)[2])
                        hW0_eff.Fill(self.getMedia(histoname_Eff)[4])
                        hW0_eff_STA.Fill(self.getMedia(histoname_Eff_STA)[4])

                        if self.findNear(name):
                            name_roll = name + "_Middle"
                            counterW0Near+=1 ##

                            if self.getMedia(histoname_Eff)[4] != -100:
                                hW0Near_eff.SetBinContent(counterW0Near,self.getMedia(histoname_Eff)[4])
                                hW0Near_eff.SetBinError(counterW0Near,self.getMedia(histoname_Eff)[5])
                            else:
                                hW0Near_eff.SetBinContent(counterW0Near,0)
                                hW0Near_eff.SetBinError(counterW0Near,0)
                                
                            hW0Near_eff.GetXaxis().SetBinLabel(counterW0Near,name_roll)

                            if self.getMedia(histoname_Eff_STA)[4] != -100:
                                hW0Near_eff_STA.SetBinContent(counterW0Near,self.getMedia(histoname_Eff_STA)[4])
                                hW0Near_eff_STA.SetBinError(counterW0Near,self.getMedia(histoname_Eff_STA)[5])
                            else:
                                hW0Near_eff_STA.SetBinContent(counterW0Near,0)
                                hW0Near_eff_STA.SetBinError(counterW0Near,0)

                            hW0Near_eff_STA.GetXaxis().SetBinLabel(counterW0Near,name_roll)

                            hW0Near_masked.SetBinContent(counterW0Near,self.getMaskedStrip(histoname_occ)[0])
                            hW0Near_masked.GetXaxis().SetBinLabel(counterW0Near,name_roll)
                            hW0Near_bx.SetBinContent(counterW0Near,self.getMeanValue(histoname_bx)[4])
                            hW0Near_bx.SetBinError(counterW0Near,self.getMeanValue(histoname_bx)[5])
                            hW0Near_bx.GetXaxis().SetBinLabel(counterW0Near,name_roll)

                        else:
                            name_roll = name + "_Middle"
                            counterW0Far+=1 ##

                            if self.getMedia(histoname_Eff)[4] != -100:
                                hW0Far_eff.SetBinContent(counterW0Far,self.getMedia(histoname_Eff)[4])
                                hW0Far_eff.SetBinError(counterW0Far,self.getMedia(histoname_Eff)[5])
                            else:
                                hW0Far_eff.SetBinContent(counterW0Far,0)
                                hW0Far_eff.SetBinError(counterW0Far,0)
                                
                            hW0Far_eff.GetXaxis().SetBinLabel(counterW0Far,name_roll)

                            if self.getMedia(histoname_Eff_STA)[4] != -100:
                                hW0Far_eff_STA.SetBinContent(counterW0Far,self.getMedia(histoname_Eff_STA)[4])
                                hW0Far_eff_STA.SetBinError(counterW0Far,self.getMedia(histoname_Eff_STA)[5])
                            else:
                                hW0Far_eff_STA.SetBinContent(counterW0Far,0)
                                hW0Far_eff_STA.SetBinError(counterW0Far,0)

                            hW0Far_eff_STA.GetXaxis().SetBinLabel(counterW0Far,name_roll)

                            hW0Far_masked.SetBinContent(counterW0Far,self.getMaskedStrip(histoname_occ)[0])
                            hW0Far_masked.GetXaxis().SetBinLabel(counterW0Far,name_roll)
                            hW0Far_bx.SetBinContent(counterW0Far,self.getMeanValue(histoname_bx)[4])
                            hW0Far_bx.SetBinError(counterW0Far,self.getMeanValue(histoname_bx)[5])
                            hW0Far_bx.GetXaxis().SetBinLabel(counterW0Far,name_roll) 

####-------------------------- Wheel +1 ----------------------------------------------------------------------

                if el == "W+1":
                    if self.findNear(name):
                        name_roll = name + "_For"
                        counterWp1Near+=1

                        if self.getMedia(histoname_Eff)[0] != -100:
                            hWp1Near_eff.SetBinContent(counterWp1Near,self.getMedia(histoname_Eff)[0])
                            hWp1Near_eff.SetBinError(counterWp1Near,self.getMedia(histoname_Eff)[1])
                        else:
                            hWp1Near_eff.SetBinContent(counterWp1Near,0)
                            hWp1Near_eff.SetBinError(counterWp1Near,0)

                        hWp1Near_eff.GetXaxis().SetBinLabel(counterWp1Near,name_roll)

                        if self.getMedia(histoname_Eff_STA)[0] != -100:
                            hWp1Near_eff_STA.SetBinContent(counterWp1Near,self.getMedia(histoname_Eff_STA)[0])
                            hWp1Near_eff_STA.SetBinError(counterWp1Near,self.getMedia(histoname_Eff_STA)[1])
                        else:
                            hWp1Near_eff_STA.SetBinContent(counterWp1Near,0)
                            hWp1Near_eff_STA.SetBinError(counterWp1Near,0)

                        hWp1Near_eff_STA.GetXaxis().SetBinLabel(counterWp1Near,name_roll)

                        hWp1Near_masked.SetBinContent(counterWp1Near,self.getMaskedStrip(histoname_occ)[0])
                        hWp1Near_masked.GetXaxis().SetBinLabel(counterWp1Near,name_roll)
                        hWp1Near_bx.SetBinContent(counterWp1Near,self.getMeanValue(histoname_bx)[0])
                        hWp1Near_bx.SetBinError(counterWp1Near,self.getMeanValue(histoname_bx)[1])
                        hWp1Near_bx.GetXaxis().SetBinLabel(counterWp1Near,name_roll)
                        
                        name_roll = name + "_Back"
                        counterWp1Near+=1
                        
                        if self.getMedia(histoname_Eff)[2] != -100:
                            hWp1Near_eff.SetBinContent(counterWp1Near,self.getMedia(histoname_Eff)[2])
                            hWp1Near_eff.SetBinError(counterWp1Near,self.getMedia(histoname_Eff)[3])
                        else:
                            hWp1Near_eff.SetBinContent(counterWp1Near,0)
                            hWp1Near_eff.SetBinError(counterWp1Near,0)
                                
                        hWp1Near_eff.GetXaxis().SetBinLabel(counterWp1Near,name_roll)

                        if self.getMedia(histoname_Eff_STA)[2] != -100:
                            hWp1Near_eff_STA.SetBinContent(counterWp1Near,self.getMedia(histoname_Eff_STA)[2])
                            hWp1Near_eff_STA.SetBinError(counterWp1Near,self.getMedia(histoname_Eff_STA)[3])
                        else:
                            hWp1Near_eff_STA.SetBinContent(counterWp1Near,0)
                            hWp1Near_eff_STA.SetBinError(counterWp1Near,0)

                        hWp1Near_eff_STA.GetXaxis().SetBinLabel(counterWp1Near,name_roll)

                        hWp1Near_masked.SetBinContent(counterWp1Near,self.getMaskedStrip(histoname_occ)[1])
                        hWp1Near_masked.GetXaxis().SetBinLabel(counterWp1Near,name_roll)
                        hWp1Near_bx.SetBinContent(counterWp1Near,self.getMeanValue(histoname_bx)[2])
                        hWp1Near_bx.SetBinError(counterWp1Near,self.getMeanValue(histoname_bx)[3])
                        hWp1Near_bx.GetXaxis().SetBinLabel(counterWp1Near,name_roll)

                    if self.findNear(name) == False:
                        name_roll = name + "_For"
                        counterWp1Far+=1

                        if self.getMedia(histoname_Eff)[0] != -100:
                            hWp1Far_eff.SetBinContent(counterWp1Far,self.getMedia(histoname_Eff)[0])
                            hWp1Far_eff.SetBinError(counterWp1Far,self.getMedia(histoname_Eff)[1])
                        else:
                            hWp1Far_eff.SetBinContent(counterWp1Far,0)
                            hWp1Far_eff.SetBinError(counterWp1Far,0)
                            
                        hWp1Far_eff.GetXaxis().SetBinLabel(counterWp1Far,name_roll)

                        if self.getMedia(histoname_Eff_STA)[0] != -100:
                            hWp1Far_eff_STA.SetBinContent(counterWp1Far,self.getMedia(histoname_Eff_STA)[0])
                            hWp1Far_eff_STA.SetBinError(counterWp1Far,self.getMedia(histoname_Eff_STA)[1])
                        else:
                            hWp1Far_eff_STA.SetBinContent(counterWp1Far,0)
                            hWp1Far_eff_STA.SetBinError(counterWp1Far,0)

                        hWp1Far_eff_STA.GetXaxis().SetBinLabel(counterWp1Far,name_roll)

                        hWp1Far_masked.SetBinContent(counterWp1Far,self.getMaskedStrip(histoname_occ)[0])
                        hWp1Far_masked.GetXaxis().SetBinLabel(counterWp1Far,name_roll)
                        hWp1Far_bx.SetBinContent(counterWp1Far,self.getMeanValue(histoname_bx)[0])
                        hWp1Far_bx.SetBinError(counterWp1Far,self.getMeanValue(histoname_bx)[1])
                        hWp1Far_bx.GetXaxis().SetBinLabel(counterWp1Far,name_roll)
                        
                        counterWp1Far+=1
                        name_roll = name + "_Back"

                        if self.getMedia(histoname_Eff)[2] != -100:
                            hWp1Far_eff.SetBinContent(counterWp1Far,self.getMedia(histoname_Eff)[2])
                            hWp1Far_eff.SetBinError(counterWp1Far,self.getMedia(histoname_Eff)[3])
                        else:
                            hWp1Far_eff.SetBinContent(counterWp1Far,0)
                            hWp1Far_eff.SetBinError(counterWp1Far,0)
                            
                        hWp1Far_eff.GetXaxis().SetBinLabel(counterWp1Far,name_roll)

                        if self.getMedia(histoname_Eff_STA)[2] != -100:
                            hWp1Far_eff_STA.SetBinContent(counterWp1Far,self.getMedia(histoname_Eff_STA)[2])
                            hWp1Far_eff_STA.SetBinError(counterWp1Far,self.getMedia(histoname_Eff_STA)[3])
                        else:
                            hWp1Far_eff_STA.SetBinContent(counterWp1Far,0)
                            hWp1Far_eff_STA.SetBinError(counterWp1Far,0)

                        hWp1Far_eff_STA.GetXaxis().SetBinLabel(counterWp1Far,name_roll)

                        hWp1Far_masked.SetBinContent(counterWp1Far,self.getMaskedStrip(histoname_occ)[1])
                        hWp1Far_masked.GetXaxis().SetBinLabel(counterWp1Far,name_roll)
                        hWp1Far_bx.SetBinContent(counterWp1Far,self.getMeanValue(histoname_bx)[2])
                        hWp1Far_bx.SetBinError(counterWp1Far,self.getMeanValue(histoname_bx)[3])
                        hWp1Far_bx.GetXaxis().SetBinLabel(counterWp1Far,name_roll)
                        
                    hWp1_masked.Fill(self.getMaskedStrip(histoname_occ)[0])
                    hWp1_masked.Fill(self.getMaskedStrip(histoname_occ)[1])
                    hWp1_eff.Fill(self.getMedia(histoname_Eff)[0])
                    hWp1_eff.Fill(self.getMedia(histoname_Eff)[2])
                    hWp1_eff_STA.Fill(self.getMedia(histoname_Eff_STA)[0])
                    hWp1_eff_STA.Fill(self.getMedia(histoname_Eff_STA)[2])
                    
                    if len(self.getMedia(histoname_Eff)) == 6:
                        hWp1_masked.Fill(self.getMaskedStrip(histoname_occ)[2])
                        hWp1_eff.Fill(self.getMedia(histoname_Eff)[4])
                        hWp1_eff_STA.Fill(self.getMedia(histoname_Eff_STA)[4])

                        if self.findNear(name):
                            counterWp1Near+=1
                            name_roll = name + "_Middle"
                            if self.getMedia(histoname_Eff)[4] != -100:
                                hWp1Near_eff.SetBinContent(counterWp1Near,self.getMedia(histoname_Eff)[4])
                                hWp1Near_eff.SetBinError(counterWp1Near,self.getMedia(histoname_Eff)[5])
                            else:
                                hWp1Near_eff.SetBinContent(counterWp1Near,0)
                                hWp1Near_eff.SetBinError(counterWp1Near,0)
                                
                            hWp1Near_eff.GetXaxis().SetBinLabel(counterWp1Near,name_roll)

                            if self.getMedia(histoname_Eff_STA)[4] != -100:
                                hWp1Near_eff_STA.SetBinContent(counterWp1Near,self.getMedia(histoname_Eff_STA)[4])
                                hWp1Near_eff_STA.SetBinError(counterWp1Near,self.getMedia(histoname_Eff_STA)[5])
                            else:
                                hWp1Near_eff_STA.SetBinContent(counterWp1Near,0)
                                hWp1Near_eff_STA.SetBinError(counterWp1Near,0)

                            hWp1Near_eff_STA.GetXaxis().SetBinLabel(counterWp1Near,name_roll)

                            hWp1Near_masked.SetBinContent(counterWp1Near,self.getMaskedStrip(histoname_occ)[0])
                            hWp1Near_masked.GetXaxis().SetBinLabel(counterWp1Near,name_roll)
                            hWp1Near_bx.SetBinContent(counterWp1Near,self.getMeanValue(histoname_bx)[4])
                            hWp1Near_bx.SetBinError(counterWp1Near,self.getMeanValue(histoname_bx)[5])
                            hWp1Near_bx.GetXaxis().SetBinLabel(counterWp1Near,name_roll)

                        else:
                            counterWp1Far+=1
                            name_roll = name + "_Middle"

                            if self.getMedia(histoname_Eff)[4] != -100:
                                hWp1Far_eff.SetBinContent(counterWp1Far,self.getMedia(histoname_Eff)[4])
                                hWp1Far_eff.SetBinError(counterWp1Far,self.getMedia(histoname_Eff)[5])
                            else:
                                hWp1Far_eff.SetBinContent(counterWp1Far,0)
                                hWp1Far_eff.SetBinError(counterWp1Far,0)
                                
                            hWp1Far_eff.GetXaxis().SetBinLabel(counterWp1Far,name_roll)

                            if self.getMedia(histoname_Eff_STA)[4] != -100:
                                hWp1Far_eff_STA.SetBinContent(counterWp1Far,self.getMedia(histoname_Eff_STA)[4])
                                hWp1Far_eff_STA.SetBinError(counterWp1Far,self.getMedia(histoname_Eff_STA)[5])
                            else:
                                hWp1Far_eff_STA.SetBinContent(counterWp1Far,0)
                                hWp1Far_eff_STA.SetBinError(counterWp1Far,0)

                            hWp1Far_eff_STA.GetXaxis().SetBinLabel(counterWp1Far,name_roll)

                            hWp1Far_masked.SetBinContent(counterWp1Far,self.getMaskedStrip(histoname_occ)[0])
                            hWp1Far_masked.GetXaxis().SetBinLabel(counterWp1Far,name_roll)
                            hWp1Far_bx.SetBinContent(counterWp1Far,self.getMeanValue(histoname_bx)[4])
                            hWp1Far_bx.SetBinError(counterWp1Far,self.getMeanValue(histoname_bx)[5])
                            hWp1Far_bx.GetXaxis().SetBinLabel(counterWp1Far,name_roll) 


####-------------------------- Wheel +2 ----------------------------------------------------------------------

                if el == "W+2":

                    if self.findNear(name):
                        name_roll = name + "_For"
                        counterWp2Near+=1
                        if self.getMedia(histoname_Eff)[0] != -100:
                            hWp2Near_eff.SetBinContent(counterWp2Near,self.getMedia(histoname_Eff)[0])
                            hWp2Near_eff.SetBinError(counterWp2Near,self.getMedia(histoname_Eff)[1])
                        else:
                            hWp2Near_eff.SetBinContent(counterWp2Near,0)
                            hWp2Near_eff.SetBinError(counterWp2Near,0)
                            
                        hWp2Near_eff.GetXaxis().SetBinLabel(counterWp2Near,name_roll)

                        if self.getMedia(histoname_Eff_STA)[0] != -100:
                            hWp2Near_eff_STA.SetBinContent(counterWp2Near,self.getMedia(histoname_Eff_STA)[0])
                            hWp2Near_eff_STA.SetBinError(counterWp2Near,self.getMedia(histoname_Eff_STA)[1])
                        else:
                            hWp2Near_eff_STA.SetBinContent(counterWp2Near,0)
                            hWp2Near_eff_STA.SetBinError(counterWp2Near,0)

                        hWp2Near_eff_STA.GetXaxis().SetBinLabel(counterWp2Near,name_roll)

                        hWp2Near_masked.SetBinContent(counterWp2Near,self.getMaskedStrip(histoname_occ)[0])
                        hWp2Near_masked.GetXaxis().SetBinLabel(counterWp2Near,name_roll)
                        hWp2Near_bx.SetBinContent(counterWp2Near,self.getMeanValue(histoname_bx)[0])
                        hWp2Near_bx.SetBinError(counterWp2Near,self.getMeanValue(histoname_bx)[1])
                        hWp2Near_bx.GetXaxis().SetBinLabel(counterWp2Near,name_roll)
                        
                        name_roll = name + "_Back"
                        counterWp2Near+=1
                        
                        if self.getMedia(histoname_Eff)[2] != -100:
                            hWp2Near_eff.SetBinContent(counterWp2Near,self.getMedia(histoname_Eff)[2])
                            hWp2Near_eff.SetBinError(counterWp2Near,self.getMedia(histoname_Eff)[3])
                        else:
                            hWp2Near_eff.SetBinContent(counterWp2Near,0)
                            hWp2Near_eff.SetBinError(counterWp2Near,0)
                                
                        hWp2Near_eff.GetXaxis().SetBinLabel(counterWp2Near,name_roll)

                        if self.getMedia(histoname_Eff_STA)[2] != -100:
                            hWp2Near_eff_STA.SetBinContent(counterWp2Near,self.getMedia(histoname_Eff_STA)[2])
                            hWp2Near_eff_STA.SetBinError(counterWp2Near,self.getMedia(histoname_Eff_STA)[3])
                        else:
                            hWp2Near_eff_STA.SetBinContent(counterWp2Near,0)
                            hWp2Near_eff_STA.SetBinError(counterWp2Near,0)

                        hWp2Near_eff_STA.GetXaxis().SetBinLabel(counterWp2Near,name_roll)

                        hWp2Near_masked.SetBinContent(counterWp2Near,self.getMaskedStrip(histoname_occ)[1])
                        hWp2Near_masked.GetXaxis().SetBinLabel(counterWp2Near,name_roll)
                        hWp2Near_bx.SetBinContent(counterWp2Near,self.getMeanValue(histoname_bx)[2])
                        hWp2Near_bx.SetBinError(counterWp2Near,self.getMeanValue(histoname_bx)[3])
                        hWp2Near_bx.GetXaxis().SetBinLabel(counterWp2Near,name_roll)

                    if self.findNear(name) == False:
                        name_roll = name + "_For"
                        counterWp2Far+=1
                        if self.getMedia(histoname_Eff)[0] != -100:
                            hWp2Far_eff.SetBinContent(counterWp2Far,self.getMedia(histoname_Eff)[0])
                            hWp2Far_eff.SetBinError(counterWp2Far,self.getMedia(histoname_Eff)[1])
                        else:
                            hWp2Far_eff.SetBinContent(counterWp2Far,0)
                            hWp2Far_eff.SetBinError(counterWp2Far,0)
                            
                        hWp2Far_eff.GetXaxis().SetBinLabel(counterWp2Far,name_roll)

                        if self.getMedia(histoname_Eff_STA)[0] != -100:
                            hWp2Far_eff_STA.SetBinContent(counterWp2Far,self.getMedia(histoname_Eff_STA)[0])
                            hWp2Far_eff_STA.SetBinError(counterWp2Far,self.getMedia(histoname_Eff_STA)[1])
                        else:
                            hWp2Far_eff_STA.SetBinContent(counterWp2Far,0)
                            hWp2Far_eff_STA.SetBinError(counterWp2Far,0)

                        hWp2Far_eff_STA.GetXaxis().SetBinLabel(counterWp2Far,name_roll)

                        hWp2Far_masked.SetBinContent(counterWp2Far,self.getMaskedStrip(histoname_occ)[0])
                        hWp2Far_masked.GetXaxis().SetBinLabel(counterWp2Far,name_roll)
                        hWp2Far_bx.SetBinContent(counterWp2Far,self.getMeanValue(histoname_bx)[0])
                        hWp2Far_bx.SetBinError(counterWp2Far,self.getMeanValue(histoname_bx)[1])
                        hWp2Far_bx.GetXaxis().SetBinLabel(counterWp2Far,name_roll)
                        
                        counterWp2Far+=1
                        name_roll = name + "_Back"
                        if self.getMedia(histoname_Eff)[2] != -100:
                            hWp2Far_eff.SetBinContent(counterWp2Far,self.getMedia(histoname_Eff)[2])
                            hWp2Far_eff.SetBinError(counterWp2Far,self.getMedia(histoname_Eff)[3])
                        else:
                            hWp2Far_eff.SetBinContent(counterWp2Far,0)
                            hWp2Far_eff.SetBinError(counterWp2Far,0)
                            
                        hWp2Far_eff.GetXaxis().SetBinLabel(counterWp2Far,name_roll)

                        if self.getMedia(histoname_Eff_STA)[2] != -100:
                            hWp2Far_eff_STA.SetBinContent(counterWp2Far,self.getMedia(histoname_Eff_STA)[2])
                            hWp2Far_eff_STA.SetBinError(counterWp2Far,self.getMedia(histoname_Eff_STA)[3])
                        else:
                            hWp2Far_eff_STA.SetBinContent(counterWp2Far,0)
                            hWp2Far_eff_STA.SetBinError(counterWp2Far,0)

                        hWp2Far_eff_STA.GetXaxis().SetBinLabel(counterWp2Far,name_roll)

                        hWp2Far_masked.SetBinContent(counterWp2Far,self.getMaskedStrip(histoname_occ)[1])
                        hWp2Far_masked.GetXaxis().SetBinLabel(counterWp2Far,name_roll)
                        hWp2Far_bx.SetBinContent(counterWp2Far,self.getMeanValue(histoname_bx)[2])
                        hWp2Far_bx.SetBinError(counterWp2Far,self.getMeanValue(histoname_bx)[3])
                        hWp2Far_bx.GetXaxis().SetBinLabel(counterWp2Far,name_roll)
                        
                    hWp2_masked.Fill(self.getMaskedStrip(histoname_occ)[0])
                    hWp2_masked.Fill(self.getMaskedStrip(histoname_occ)[1])
                    hWp2_eff.Fill(self.getMedia(histoname_Eff)[0])
                    hWp2_eff.Fill(self.getMedia(histoname_Eff)[2])
                    hWp2_eff_STA.Fill(self.getMedia(histoname_Eff_STA)[0])
                    hWp2_eff_STA.Fill(self.getMedia(histoname_Eff_STA)[2])

                    if len(self.getMedia(histoname_Eff)) == 6:
                        hWp2_masked.Fill(self.getMaskedStrip(histoname_occ)[2])
                        hWp2_eff.Fill(self.getMedia(histoname_Eff)[4])
                        hWp2_eff_STA.Fill(self.getMedia(histoname_Eff_STA)[4])

                        if self.findNear(name):
                            counterWp2Near+=1
                            name_roll = name + "_Middle"

                            if self.getMedia(histoname_Eff)[4] != -100:
                                hWp2Near_eff.SetBinContent(counterWp2Near,self.getMedia(histoname_Eff)[4])
                                hWp2Near_eff.SetBinError(counterWp2Near,self.getMedia(histoname_Eff)[5])
                            else:
                                hWp2Near_eff.SetBinContent(counterWp2Near,0)
                                hWp2Near_eff.SetBinError(counterWp2Near,0)
                                
                            hWp2Near_eff.GetXaxis().SetBinLabel(counterWp2Near,name_roll)

                            if self.getMedia(histoname_Eff_STA)[4] != -100:
                                hWp2Near_eff_STA.SetBinContent(counterWp2Near,self.getMedia(histoname_Eff_STA)[4])
                                hWp2Near_eff_STA.SetBinError(counterWp2Near,self.getMedia(histoname_Eff_STA)[5])
                            else:
                                hWp2Near_eff_STA.SetBinContent(counterWp2Near,0)
                                hWp2Near_eff_STA.SetBinError(counterWp2Near,0)

                            hWp2Near_eff_STA.GetXaxis().SetBinLabel(counterWp2Near,name_roll)

                            hWp2Near_masked.SetBinContent(counterWp2Near,self.getMaskedStrip(histoname_occ)[0])
                            hWp2Near_masked.GetXaxis().SetBinLabel(counterWp2Near,name_roll)
                            hWp2Near_bx.SetBinContent(counterWp2Near,self.getMeanValue(histoname_bx)[4])
                            hWp2Near_bx.SetBinError(counterWp2Near,self.getMeanValue(histoname_bx)[5])
                            hWp2Near_bx.GetXaxis().SetBinLabel(counterWp2Near,name_roll)

                        else:
                            counterWp2Far+=1
                            name_roll = name + "_Middle"
                            if self.getMedia(histoname_Eff)[4] != -100:
                                hWp2Far_eff.SetBinContent(counterWp2Far,self.getMedia(histoname_Eff)[4])
                                hWp2Far_eff.SetBinError(counterWp2Far,self.getMedia(histoname_Eff)[5])
                            else:
                                hWp2Far_eff.SetBinContent(counterWp2Far,0)
                                hWp2Far_eff.SetBinError(counterWp2Far,0)

                            hWp2Far_eff.GetXaxis().SetBinLabel(counterWp2Far,name_roll)

                            if self.getMedia(histoname_Eff_STA)[4] != -100:
                                hWp2Far_eff_STA.SetBinContent(counterWp2Far,self.getMedia(histoname_Eff_STA)[4])
                                hWp2Far_eff_STA.SetBinError(counterWp2Far,self.getMedia(histoname_Eff_STA)[5])
                            else:
                                hWp2Far_eff_STA.SetBinContent(counterWp2Far,0)
                                hWp2Far_eff_STA.SetBinError(counterWp2Far,0)

                            hWp2Far_eff_STA.GetXaxis().SetBinLabel(counterWp2Far,name_roll)

                            hWp2Far_masked.SetBinContent(counterWp2Far,self.getMaskedStrip(histoname_occ)[0])
                            hWp2Far_masked.GetXaxis().SetBinLabel(counterWp2Far,name_roll)
                            hWp2Far_bx.SetBinContent(counterWp2Far,self.getMeanValue(histoname_bx)[4])
                            hWp2Far_bx.SetBinError(counterWp2Far,self.getMeanValue(histoname_bx)[5])
                            hWp2Far_bx.GetXaxis().SetBinLabel(counterWp2Far,name_roll) 


####-------------------------------------- ENDCAP ----------------------------------------------------
                            
        for line in self.fillDetListEndcap():
            for el in listDisk:
#              for jo in listend:   
                coord = line.rstrip().split("  ")
                coord1 = coord[0].rstrip().split("_")
                name = el+'_'+  coord1[0] + '_' + coord1[2]
                histoname_bx = 'BXN_'+el+'_' + coord1[0] + '_' + coord1[2]
                histoname_occ = 'Occupancy_'+el+'_'+coord1[0] + '_' + coord1[2]
                histoname_Eff = 'LocalEfficiencyFromSegments_'+el+'_' + coord1[0] + '_' + coord1[2]
#                print histoname_Eff
                histoname_Eff_STA = 'LocalEfficiencyFromTrack_'+el+'_' +  coord1[0] + '_' + coord1[2]
                hEndcap_bx.Fill(self.getMeanValueDisk(histoname_bx)[0])
                hEndcap_bx.Fill(self.getMeanValueDisk(histoname_bx)[2])
                hEndcap_bx.Fill(self.getMeanValueDisk(histoname_bx)[4])
                hEndcap_masked.Fill(self.getMaskedStripDisk(histoname_occ)[0])
                hEndcap_masked.Fill(self.getMaskedStripDisk(histoname_occ)[1])
                hEndcap_masked.Fill(self.getMaskedStripDisk(histoname_occ)[2])
                hEndcap_eff.Fill(self.getMediaDisk(histoname_Eff)[0])
                hEndcap_eff.Fill(self.getMediaDisk(histoname_Eff)[2])
                hEndcap_eff.Fill(self.getMediaDisk(histoname_Eff)[4])
                hEndcap_eff_STA.Fill(self.getMediaDisk(histoname_Eff_STA)[0])
                hEndcap_eff_STA.Fill(self.getMediaDisk(histoname_Eff_STA)[2])
                hEndcap_eff_STA.Fill(self.getMediaDisk(histoname_Eff_STA)[4])

##--------------------------------  RE -3 -----------------------------------------------------------------

                if el == "RE-3":

                    hDm3_masked.Fill(self.getMaskedStripDisk(histoname_occ)[0])
                    hDm3_masked.Fill(self.getMaskedStripDisk(histoname_occ)[1])
                    hDm3_masked.Fill(self.getMaskedStripDisk(histoname_occ)[2])
                    hDm3_eff.Fill(self.getMediaDisk(histoname_Eff)[0])
                    hDm3_eff.Fill(self.getMediaDisk(histoname_Eff)[2])
                    hDm3_eff.Fill(self.getMediaDisk(histoname_Eff)[4])
                    hDm3_eff_STA.Fill(self.getMediaDisk(histoname_Eff_STA)[0])
                    hDm3_eff_STA.Fill(self.getMediaDisk(histoname_Eff_STA)[2])
                    hDm3_eff_STA.Fill(self.getMediaDisk(histoname_Eff_STA)[4])

                    if coord1[0] == "R3":

                        name_roll = name + "_A"
                        counterDm3RE3+=1

                        if self.getMediaDisk(histoname_Eff)[0] != -100:
                            hDm3RE3_eff.SetBinContent(counterDm3RE3,self.getMediaDisk(histoname_Eff)[0])
                            hDm3RE3_eff.SetBinError(counterDm3RE3,self.getMediaDisk(histoname_Eff)[1])
                        else:
                            hDm3RE3_eff.SetBinContent(counterDm3RE3,0)
                            hDm3RE3_eff.SetBinError(counterDm3RE3,0)

                        hDm3RE3_eff.GetXaxis().SetBinLabel(counterDm3RE3,name_roll)

                        if self.getMediaDisk(histoname_Eff_STA)[0] != -100:
                            hDm3RE3_eff_STA.SetBinContent(counterDm3RE3,self.getMediaDisk(histoname_Eff_STA)[0])
                            hDm3RE3_eff_STA.SetBinError(counterDm3RE3,self.getMediaDisk(histoname_Eff_STA)[1])
                        else:
                            hDm3RE3_eff_STA.SetBinContent(counterDm3RE3,0)
                            hDm3RE3_eff_STA.SetBinError(counterDm3RE3,0)

                        hDm3RE3_eff_STA.GetXaxis().SetBinLabel(counterDm3RE3,name_roll)

                        hDm3RE3_masked.SetBinContent(counterDm3RE3,self.getMaskedStripDisk(histoname_occ)[0])
                        hDm3RE3_masked.GetXaxis().SetBinLabel(counterDm3RE3,name_roll)
                        hDm3RE3_bx.SetBinContent(counterDm3RE3,self.getMeanValueDisk(histoname_bx)[0])
                        hDm3RE3_bx.SetBinError(counterDm3RE3,self.getMeanValueDisk(histoname_bx)[1])
                        hDm3RE3_bx.GetXaxis().SetBinLabel(counterDm3RE3,name_roll)

                        name_roll = name + "_B"
                        counterDm3RE3+=1

                        if self.getMediaDisk(histoname_Eff)[2] != -100:
                            hDm3RE3_eff.SetBinContent(counterDm3RE3,self.getMediaDisk(histoname_Eff)[2])
                            hDm3RE3_eff.SetBinError(counterDm3RE3,self.getMediaDisk(histoname_Eff)[3])
                        else:
                            hDm3RE3_eff.SetBinContent(counterDm3RE3,0)
                            hDm3RE3_eff.SetBinError(counterDm3RE3,0)

                        hDm3RE3_eff.GetXaxis().SetBinLabel(counterDm3RE3,name_roll)

                        if self.getMediaDisk(histoname_Eff_STA)[2] != -100:
                            hDm3RE3_eff_STA.SetBinContent(counterDm3RE3,self.getMediaDisk(histoname_Eff_STA)[2])
                            hDm3RE3_eff_STA.SetBinError(counterDm3RE3,self.getMediaDisk(histoname_Eff_STA)[3])
                        else:
                            hDm3RE3_eff_STA.SetBinContent(counterDm3RE3,0)
                            hDm3RE3_eff_STA.SetBinError(counterDm3RE3,0)

                        hDm3RE3_eff_STA.GetXaxis().SetBinLabel(counterDm3RE3,name_roll)

                        hDm3RE3_masked.SetBinContent(counterDm3RE3,self.getMaskedStripDisk(histoname_occ)[1])
                        hDm3RE3_masked.GetXaxis().SetBinLabel(counterDm3RE3,name_roll)
                        hDm3RE3_bx.SetBinContent(counterDm3RE3,self.getMeanValueDisk(histoname_bx)[2])
                        hDm3RE3_bx.SetBinError(counterDm3RE3,self.getMeanValueDisk(histoname_bx)[3])
                        hDm3RE3_bx.GetXaxis().SetBinLabel(counterDm3RE3,name_roll)

                        name_roll = name + "_C"
                        counterDm3RE3+=1

                        if self.getMediaDisk(histoname_Eff)[2] != -100:
                            hDm3RE3_eff.SetBinContent(counterDm3RE3,self.getMediaDisk(histoname_Eff)[2])
                            hDm3RE3_eff.SetBinError(counterDm3RE3,self.getMediaDisk(histoname_Eff)[3])
                        else:
                            hDm3RE3_eff.SetBinContent(counterDm3RE3,0)
                            hDm3RE3_eff.SetBinError(counterDm3RE3,0)

                        hDm3RE3_eff.GetXaxis().SetBinLabel(counterDm3RE3,name_roll)

                        if self.getMediaDisk(histoname_Eff_STA)[2] != -100:
                            hDm3RE3_eff_STA.SetBinContent(counterDm3RE3,self.getMediaDisk(histoname_Eff_STA)[2])
                            hDm3RE3_eff_STA.SetBinError(counterDm3RE3,self.getMediaDisk(histoname_Eff_STA)[3])
                        else:
                            hDm3RE3_eff_STA.SetBinContent(counterDm3RE3,0)
                            hDm3RE3_eff_STA.SetBinError(counterDm3RE3,0)

                        hDm3RE3_eff_STA.GetXaxis().SetBinLabel(counterDm3RE3,name_roll)

                        hDm3RE3_masked.SetBinContent(counterDm3RE3,self.getMaskedStripDisk(histoname_occ)[1])
                        hDm3RE3_masked.GetXaxis().SetBinLabel(counterDm3RE3,name_roll)
                        hDm3RE3_bx.SetBinContent(counterDm3RE3,self.getMeanValueDisk(histoname_bx)[2])
                        hDm3RE3_bx.SetBinError(counterDm3RE3,self.getMeanValueDisk(histoname_bx)[3])
                        hDm3RE3_bx.GetXaxis().SetBinLabel(counterDm3RE3,name_roll)

                    if coord1[0] == "R2":

                        name_roll = name + "_A"
                        counterDm3RE2+=1

                        if self.getMediaDisk(histoname_Eff)[0] != -100:
                            hDm3RE2_eff.SetBinContent(counterDm3RE2,self.getMediaDisk(histoname_Eff)[0])
                            hDm3RE2_eff.SetBinError(counterDm3RE2,self.getMediaDisk(histoname_Eff)[1])
                        else:
                            hDm3RE2_eff.SetBinContent(counterDm3RE2,0)
                            hDm3RE2_eff.SetBinError(counterDm3RE2,0)

                        hDm3RE2_eff.GetXaxis().SetBinLabel(counterDm3RE2,name_roll)

                        if self.getMediaDisk(histoname_Eff_STA)[0] != -100:
                            hDm3RE2_eff_STA.SetBinContent(counterDm3RE2,self.getMediaDisk(histoname_Eff_STA)[0])
                            hDm3RE2_eff_STA.SetBinError(counterDm3RE2,self.getMediaDisk(histoname_Eff_STA)[1])
                        else:
                            hDm3RE2_eff_STA.SetBinContent(counterDm3RE2,0)
                            hDm3RE2_eff_STA.SetBinError(counterDm3RE2,0)

                        hDm3RE2_eff_STA.GetXaxis().SetBinLabel(counterDm3RE2,name_roll)

                        hDm3RE2_masked.SetBinContent(counterDm3RE2,self.getMaskedStripDisk(histoname_occ)[0])
                        hDm3RE2_masked.GetXaxis().SetBinLabel(counterDm3RE2,name_roll)
                        hDm3RE2_bx.SetBinContent(counterDm3RE2,self.getMeanValueDisk(histoname_bx)[0])
                        hDm3RE2_bx.SetBinError(counterDm3RE2,self.getMeanValueDisk(histoname_bx)[1])
                        hDm3RE2_bx.GetXaxis().SetBinLabel(counterDm3RE2,name_roll)

                        name_roll = name + "_B"
                        counterDm3RE2+=1

                        if self.getMediaDisk(histoname_Eff)[2] != -100:
                            hDm3RE2_eff.SetBinContent(counterDm3RE2,self.getMediaDisk(histoname_Eff)[2])
                            hDm3RE2_eff.SetBinError(counterDm3RE2,self.getMediaDisk(histoname_Eff)[3])
                        else:
                            hDm3RE2_eff.SetBinContent(counterDm3RE2,0)
                            hDm3RE2_eff.SetBinError(counterDm3RE2,0)

                        hDm3RE2_eff.GetXaxis().SetBinLabel(counterDm3RE2,name_roll)

                        if self.getMediaDisk(histoname_Eff_STA)[2] != -100:
                            hDm3RE2_eff_STA.SetBinContent(counterDm3RE2,self.getMediaDisk(histoname_Eff_STA)[2])
                            hDm3RE2_eff_STA.SetBinError(counterDm3RE2,self.getMediaDisk(histoname_Eff_STA)[3])
                        else:
                            hDm3RE2_eff_STA.SetBinContent(counterDm3RE2,0)
                            hDm3RE2_eff_STA.SetBinError(counterDm3RE2,0)

                        hDm3RE2_eff_STA.GetXaxis().SetBinLabel(counterDm3RE2,name_roll)

                        hDm3RE2_masked.SetBinContent(counterDm3RE2,self.getMaskedStripDisk(histoname_occ)[1])
                        hDm3RE2_masked.GetXaxis().SetBinLabel(counterDm3RE2,name_roll)
                        hDm3RE2_bx.SetBinContent(counterDm3RE2,self.getMeanValueDisk(histoname_bx)[2])
                        hDm3RE2_bx.SetBinError(counterDm3RE2,self.getMeanValueDisk(histoname_bx)[3])
                        hDm3RE2_bx.GetXaxis().SetBinLabel(counterDm3RE2,name_roll)

                        name_roll = name + "_C"
                        counterDm3RE2+=1

                        if self.getMediaDisk(histoname_Eff)[2] != -100:
                            hDm3RE2_eff.SetBinContent(counterDm3RE2,self.getMediaDisk(histoname_Eff)[2])
                            hDm3RE2_eff.SetBinError(counterDm3RE2,self.getMediaDisk(histoname_Eff)[3])
                        else:
                            hDm3RE2_eff.SetBinContent(counterDm3RE2,0)
                            hDm3RE2_eff.SetBinError(counterDm3RE2,0)

                        hDm3RE2_eff.GetXaxis().SetBinLabel(counterDm3RE2,name_roll)

                        if self.getMediaDisk(histoname_Eff)[2] != -100:
                            hDm3RE2_eff_STA.SetBinContent(counterDm3RE2,self.getMediaDisk(histoname_Eff_STA)[2])
                            hDm3RE2_eff_STA.SetBinError(counterDm3RE2,self.getMediaDisk(histoname_Eff_STA)[3])
                        else:
                            hDm3RE2_eff_STA.SetBinContent(counterDm3RE2,0)
                            hDm3RE2_eff_STA.SetBinError(counterDm3RE2,0)

                        hDm3RE2_eff_STA.GetXaxis().SetBinLabel(counterDm3RE2,name_roll)

                        hDm3RE2_masked.SetBinContent(counterDm3RE2,self.getMaskedStripDisk(histoname_occ)[1])
                        hDm3RE2_masked.GetXaxis().SetBinLabel(counterDm3RE2,name_roll)
                        hDm3RE2_bx.SetBinContent(counterDm3RE2,self.getMeanValueDisk(histoname_bx)[2])
                        hDm3RE2_bx.SetBinError(counterDm3RE2,self.getMeanValueDisk(histoname_bx)[3])
                        hDm3RE2_bx.GetXaxis().SetBinLabel(counterDm3RE2,name_roll)

                    if coord1[0] == "R1":

                        name_roll = name + "_A"
                        counterDm3RE1+=1

                        if self.getMediaDisk(histoname_Eff)[0] != -100:
                            hDm3RE1_eff.SetBinContent(counterDm3RE1,self.getMediaDisk(histoname_Eff)[0])
                            hDm3RE1_eff.SetBinError(counterDm3RE1,self.getMediaDisk(histoname_Eff)[1])
                        else:
                            hDm3RE1_eff.SetBinContent(counterDm3RE1,0)
                            hDm3RE1_eff.SetBinError(counterDm3RE1,0)

                        hDm3RE1_eff.GetXaxis().SetBinLabel(counterDm3RE1,name_roll)

                        if self.getMediaDisk(histoname_Eff_STA)[0] != -100:
                            hDm3RE1_eff_STA.SetBinContent(counterDm3RE1,self.getMediaDisk(histoname_Eff_STA)[0])
                            hDm3RE1_eff_STA.SetBinError(counterDm3RE1,self.getMediaDisk(histoname_Eff_STA)[1])
                        else:
                            hDm3RE1_eff_STA.SetBinContent(counterDm3RE1,0)
                            hDm3RE1_eff_STA.SetBinError(counterDm3RE1,0)

                        hDm3RE1_eff_STA.GetXaxis().SetBinLabel(counterDm3RE1,name_roll)

                        hDm3RE1_masked.SetBinContent(counterDm3RE1,self.getMaskedStripDisk(histoname_occ)[0])
                        hDm3RE1_masked.GetXaxis().SetBinLabel(counterDm3RE1,name_roll)
                        hDm3RE1_bx.SetBinContent(counterDm3RE1,self.getMeanValueDisk(histoname_bx)[0])
                        hDm3RE1_bx.SetBinError(counterDm3RE1,self.getMeanValueDisk(histoname_bx)[1])
                        hDm3RE1_bx.GetXaxis().SetBinLabel(counterDm3RE1,name_roll)

                        name_roll = name + "_B"
                        counterDm3RE1+=1

                        if self.getMediaDisk(histoname_Eff)[2] != -100:
                            hDm3RE1_eff.SetBinContent(counterDm3RE1,self.getMediaDisk(histoname_Eff)[2])
                            hDm3RE1_eff.SetBinError(counterDm3RE1,self.getMediaDisk(histoname_Eff)[3])
                        else:
                            hDm3RE1_eff.SetBinContent(counterDm3RE1,0)
                            hDm3RE1_eff.SetBinError(counterDm3RE1,0)

                        hDm3RE1_eff.GetXaxis().SetBinLabel(counterDm3RE1,name_roll)

                        if self.getMediaDisk(histoname_Eff_STA)[2] != -100:
                            hDm3RE1_eff_STA.SetBinContent(counterDm3RE1,self.getMediaDisk(histoname_Eff_STA)[2])
                            hDm3RE1_eff_STA.SetBinError(counterDm3RE1,self.getMediaDisk(histoname_Eff_STA)[3])
                        else:
                            hDm3RE1_eff_STA.SetBinContent(counterDm3RE1,0)
                            hDm3RE1_eff_STA.SetBinError(counterDm3RE1,0)

                        hDm3RE1_eff_STA.GetXaxis().SetBinLabel(counterDm3RE1,name_roll)

                        hDm3RE1_masked.SetBinContent(counterDm3RE1,self.getMaskedStripDisk(histoname_occ)[1])
                        hDm3RE1_masked.GetXaxis().SetBinLabel(counterDm3RE1,name_roll)
                        hDm3RE1_bx.SetBinContent(counterDm3RE1,self.getMeanValueDisk(histoname_bx)[2])
                        hDm3RE1_bx.SetBinError(counterDm3RE1,self.getMeanValueDisk(histoname_bx)[3])
                        hDm3RE1_bx.GetXaxis().SetBinLabel(counterDm3RE1,name_roll)

                        name_roll = name + "_C"
                        counterDm3RE1+=1

                        if self.getMediaDisk(histoname_Eff)[2] != -100:
                            hDm3RE1_eff.SetBinContent(counterDm3RE1,self.getMediaDisk(histoname_Eff)[2])
                            hDm3RE1_eff.SetBinError(counterDm3RE1,self.getMediaDisk(histoname_Eff)[3])
                        else:
                            hDm3RE1_eff.SetBinContent(counterDm3RE1,0)
                            hDm3RE1_eff.SetBinError(counterDm3RE1,0)

                        hDm3RE1_eff.GetXaxis().SetBinLabel(counterDm3RE1,name_roll)

                        if self.getMediaDisk(histoname_Eff_STA)[2] != -100:
                            hDm3RE1_eff_STA.SetBinContent(counterDm3RE1,self.getMediaDisk(histoname_Eff_STA)[2])
                            hDm3RE1_eff_STA.SetBinError(counterDm3RE1,self.getMediaDisk(histoname_Eff_STA)[3])
                        else:
                            hDm3RE1_eff_STA.SetBinContent(counterDm3RE1,0)
                            hDm3RE1_eff_STA.SetBinError(counterDm3RE1,0)

                        hDm3RE1_eff_STA.GetXaxis().SetBinLabel(counterDm3RE1,name_roll)

                        hDm3RE1_masked.SetBinContent(counterDm3RE1,self.getMaskedStripDisk(histoname_occ)[1])
                        hDm3RE1_masked.GetXaxis().SetBinLabel(counterDm3RE1,name_roll)
                        hDm3RE1_bx.SetBinContent(counterDm3RE1,self.getMeanValueDisk(histoname_bx)[2])
                        hDm3RE1_bx.SetBinError(counterDm3RE1,self.getMeanValueDisk(histoname_bx)[3])
                        hDm3RE1_bx.GetXaxis().SetBinLabel(counterDm3RE1,name_roll)

##------------------------------------ RE -2 ----------------------------------------------------------

                if el == "RE-2":
                    hDm2_masked.Fill(self.getMaskedStripDisk(histoname_occ)[0])
                    hDm2_masked.Fill(self.getMaskedStripDisk(histoname_occ)[1])
                    hDm2_masked.Fill(self.getMaskedStripDisk(histoname_occ)[2])
                    hDm2_eff.Fill(self.getMediaDisk(histoname_Eff)[0])
                    hDm2_eff.Fill(self.getMediaDisk(histoname_Eff)[2])
                    hDm2_eff.Fill(self.getMediaDisk(histoname_Eff)[4])
                    hDm2_eff_STA.Fill(self.getMediaDisk(histoname_Eff_STA)[0])
                    hDm2_eff_STA.Fill(self.getMediaDisk(histoname_Eff_STA)[2])
                    hDm2_eff_STA.Fill(self.getMediaDisk(histoname_Eff_STA)[4])

                    if coord1[0] == "R3":
                        name_roll = name + "_A"
                        counterDm2RE3+=1

                        if self.getMediaDisk(histoname_Eff)[0] != -100:
                            hDm2RE3_eff.SetBinContent(counterDm2RE3,self.getMediaDisk(histoname_Eff)[0])
                            hDm2RE3_eff.SetBinError(counterDm2RE3,self.getMediaDisk(histoname_Eff)[1])
                        else:
                            hDm2RE3_eff.SetBinContent(counterDm2RE3,0)
                            hDm2RE3_eff.SetBinError(counterDm2RE3,0)

                        hDm2RE3_eff.GetXaxis().SetBinLabel(counterDm2RE3,name_roll)

                        if self.getMediaDisk(histoname_Eff_STA)[0] != -100:
                            hDm2RE3_eff_STA.SetBinContent(counterDm2RE3,self.getMediaDisk(histoname_Eff_STA)[0])
                            hDm2RE3_eff_STA.SetBinError(counterDm2RE3,self.getMediaDisk(histoname_Eff_STA)[1])
                        else:
                            hDm2RE3_eff_STA.SetBinContent(counterDm2RE3,0)
                            hDm2RE3_eff_STA.SetBinError(counterDm2RE3,0)

                        hDm2RE3_eff_STA.GetXaxis().SetBinLabel(counterDm2RE3,name_roll)

                        hDm2RE3_masked.SetBinContent(counterDm2RE3,self.getMaskedStripDisk(histoname_occ)[0])
                        hDm2RE3_masked.GetXaxis().SetBinLabel(counterDm2RE3,name_roll)
                        hDm2RE3_bx.SetBinContent(counterDm2RE3,self.getMeanValueDisk(histoname_bx)[0])
                        hDm2RE3_bx.SetBinError(counterDm2RE3,self.getMeanValueDisk(histoname_bx)[1])
                        hDm2RE3_bx.GetXaxis().SetBinLabel(counterDm2RE3,name_roll)

                        name_roll = name + "_B"
                        counterDm2RE3+=1

                        if self.getMediaDisk(histoname_Eff)[2] != -100:
                            hDm2RE3_eff.SetBinContent(counterDm2RE3,self.getMediaDisk(histoname_Eff)[2])
                            hDm2RE3_eff.SetBinError(counterDm2RE3,self.getMediaDisk(histoname_Eff)[3])
                        else:
                            hDm2RE3_eff.SetBinContent(counterDm2RE3,0)
                            hDm2RE3_eff.SetBinError(counterDm2RE3,0)

                        hDm2RE3_eff.GetXaxis().SetBinLabel(counterDm2RE3,name_roll)

                        if self.getMediaDisk(histoname_Eff_STA)[2] != -100:
                            hDm2RE3_eff_STA.SetBinContent(counterDm2RE3,self.getMediaDisk(histoname_Eff_STA)[2])
                            hDm2RE3_eff_STA.SetBinError(counterDm2RE3,self.getMediaDisk(histoname_Eff_STA)[3])
                        else:
                            hDm2RE3_eff_STA.SetBinContent(counterDm2RE3,0)
                            hDm2RE3_eff_STA.SetBinError(counterDm2RE3,0)

                        hDm2RE3_eff_STA.GetXaxis().SetBinLabel(counterDm2RE3,name_roll)

                        hDm2RE3_masked.SetBinContent(counterDm2RE3,self.getMaskedStripDisk(histoname_occ)[1])
                        hDm2RE3_masked.GetXaxis().SetBinLabel(counterDm2RE3,name_roll)
                        hDm2RE3_bx.SetBinContent(counterDm2RE3,self.getMeanValueDisk(histoname_bx)[2])
                        hDm2RE3_bx.SetBinError(counterDm2RE3,self.getMeanValueDisk(histoname_bx)[3])
                        hDm2RE3_bx.GetXaxis().SetBinLabel(counterDm2RE3,name_roll)

                        name_roll = name + "_C"
                        counterDm2RE3+=1

                        if self.getMediaDisk(histoname_Eff)[2] != -100:
                            hDm2RE3_eff.SetBinContent(counterDm2RE3,self.getMediaDisk(histoname_Eff)[2])
                            hDm2RE3_eff.SetBinError(counterDm2RE3,self.getMediaDisk(histoname_Eff)[3])
                        else:
                            hDm2RE3_eff.SetBinContent(counterDm2RE3,0)
                            hDm2RE3_eff.SetBinError(counterDm2RE3,0)

                        hDm2RE3_eff.GetXaxis().SetBinLabel(counterDm2RE3,name_roll)

                        if self.getMediaDisk(histoname_Eff_STA)[2] != -100:
                            hDm2RE3_eff_STA.SetBinContent(counterDm2RE3,self.getMediaDisk(histoname_Eff_STA)[2])
                            hDm2RE3_eff_STA.SetBinError(counterDm2RE3,self.getMediaDisk(histoname_Eff_STA)[3])
                        else:
                            hDm2RE3_eff_STA.SetBinContent(counterDm2RE3,0)
                            hDm2RE3_eff_STA.SetBinError(counterDm2RE3,0)

                        hDm2RE3_eff_STA.GetXaxis().SetBinLabel(counterDm2RE3,name_roll)

                        hDm2RE3_masked.SetBinContent(counterDm2RE3,self.getMaskedStripDisk(histoname_occ)[1])
                        hDm2RE3_masked.GetXaxis().SetBinLabel(counterDm2RE3,name_roll)
                        hDm2RE3_bx.SetBinContent(counterDm2RE3,self.getMeanValueDisk(histoname_bx)[2])
                        hDm2RE3_bx.SetBinError(counterDm2RE3,self.getMeanValueDisk(histoname_bx)[3])
                        hDm2RE3_bx.GetXaxis().SetBinLabel(counterDm2RE3,name_roll)


                    if coord1[0] == "R2":
                        name_roll = name + "_A"
                        counterDm2RE2+=1

                        if self.getMediaDisk(histoname_Eff)[0] != -100:
                            hDm2RE2_eff.SetBinContent(counterDm2RE2,self.getMediaDisk(histoname_Eff)[0])
                            hDm2RE2_eff.SetBinError(counterDm2RE2,self.getMediaDisk(histoname_Eff)[1])
                        else:
                            hDm2RE2_eff.SetBinContent(counterDm2RE2,0)
                            hDm2RE2_eff.SetBinError(counterDm2RE2,0)

                        hDm2RE2_eff.GetXaxis().SetBinLabel(counterDm2RE2,name_roll)

                        if self.getMediaDisk(histoname_Eff_STA)[0] != -100:
                            hDm2RE2_eff_STA.SetBinContent(counterDm2RE2,self.getMediaDisk(histoname_Eff_STA)[0])
                            hDm2RE2_eff_STA.SetBinError(counterDm2RE2,self.getMediaDisk(histoname_Eff_STA)[1])
                        else:
                            hDm2RE2_eff_STA.SetBinContent(counterDm2RE2,0)
                            hDm2RE2_eff_STA.SetBinError(counterDm2RE2,0)

                        hDm2RE2_eff_STA.GetXaxis().SetBinLabel(counterDm2RE2,name_roll)


                        hDm2RE2_masked.SetBinContent(counterDm2RE2,self.getMaskedStripDisk(histoname_occ)[0])
                        hDm2RE2_masked.GetXaxis().SetBinLabel(counterDm2RE2,name_roll)
                        hDm2RE2_bx.SetBinContent(counterDm2RE2,self.getMeanValueDisk(histoname_bx)[0])
                        hDm2RE2_bx.SetBinError(counterDm2RE2,self.getMeanValueDisk(histoname_bx)[1])
                        hDm2RE2_bx.GetXaxis().SetBinLabel(counterDm2RE2,name_roll)

                        name_roll = name + "_B"
                        counterDm2RE2+=1

                        if self.getMediaDisk(histoname_Eff)[2] != -100:
                            hDm2RE2_eff.SetBinContent(counterDm2RE2,self.getMediaDisk(histoname_Eff)[2])
                            hDm2RE2_eff.SetBinError(counterDm2RE2,self.getMediaDisk(histoname_Eff)[3])
                        else:
                            hDm2RE2_eff.SetBinContent(counterDm2RE2,0)
                            hDm2RE2_eff.SetBinError(counterDm2RE2,0)

                        hDm2RE2_eff.GetXaxis().SetBinLabel(counterDm2RE2,name_roll)

                        if self.getMediaDisk(histoname_Eff_STA)[2] != -100:
                            hDm2RE2_eff_STA.SetBinContent(counterDm2RE2,self.getMediaDisk(histoname_Eff_STA)[2])
                            hDm2RE2_eff_STA.SetBinError(counterDm2RE2,self.getMediaDisk(histoname_Eff_STA)[3])
                        else:
                            hDm2RE2_eff_STA.SetBinContent(counterDm2RE2,0)
                            hDm2RE2_eff_STA.SetBinError(counterDm2RE2,0)

                        hDm2RE2_eff_STA.GetXaxis().SetBinLabel(counterDm2RE2,name_roll)

                        hDm2RE2_masked.SetBinContent(counterDm2RE2,self.getMaskedStripDisk(histoname_occ)[1])
                        hDm2RE2_masked.GetXaxis().SetBinLabel(counterDm2RE2,name_roll)
                        hDm2RE2_bx.SetBinContent(counterDm2RE2,self.getMeanValueDisk(histoname_bx)[2])
                        hDm2RE2_bx.SetBinError(counterDm2RE2,self.getMeanValueDisk(histoname_bx)[3])
                        hDm2RE2_bx.GetXaxis().SetBinLabel(counterDm2RE2,name_roll)

                        name_roll = name + "_C"
                        counterDm2RE2+=1

                        if self.getMediaDisk(histoname_Eff)[2] != -100:
                            hDm2RE2_eff.SetBinContent(counterDm2RE2,self.getMediaDisk(histoname_Eff)[2])
                            hDm2RE2_eff.SetBinError(counterDm2RE2,self.getMediaDisk(histoname_Eff)[3])
                        else:
                            hDm2RE2_eff.SetBinContent(counterDm2RE2,0)
                            hDm2RE2_eff.SetBinError(counterDm2RE2,0)

                        hDm2RE2_eff.GetXaxis().SetBinLabel(counterDm2RE2,name_roll)

                        if self.getMediaDisk(histoname_Eff_STA)[2] != -100:
                            hDm2RE2_eff_STA.SetBinContent(counterDm2RE2,self.getMediaDisk(histoname_Eff_STA)[2])
                            hDm2RE2_eff_STA.SetBinError(counterDm2RE2,self.getMediaDisk(histoname_Eff_STA)[3])
                        else:
                            hDm2RE2_eff_STA.SetBinContent(counterDm2RE2,0)
                            hDm2RE2_eff_STA.SetBinError(counterDm2RE2,0)

                        hDm2RE2_eff_STA.GetXaxis().SetBinLabel(counterDm2RE2,name_roll)

                        hDm2RE2_masked.SetBinContent(counterDm2RE2,self.getMaskedStripDisk(histoname_occ)[1])
                        hDm2RE2_masked.GetXaxis().SetBinLabel(counterDm2RE2,name_roll)
                        hDm2RE2_bx.SetBinContent(counterDm2RE2,self.getMeanValueDisk(histoname_bx)[2])
                        hDm2RE2_bx.SetBinError(counterDm2RE2,self.getMeanValueDisk(histoname_bx)[3])
                        hDm2RE2_bx.GetXaxis().SetBinLabel(counterDm2RE2,name_roll)

                    if coord1[0] == "R1":
                        name_roll = name + "_A"
                        counterDm2RE1+=1

                        if self.getMediaDisk(histoname_Eff)[0] != -100:
                            hDm2RE1_eff.SetBinContent(counterDm2RE1,self.getMediaDisk(histoname_Eff)[0])
                            hDm2RE1_eff.SetBinError(counterDm2RE1,self.getMediaDisk(histoname_Eff)[1])
                        else:
                            hDm2RE1_eff.SetBinContent(counterDm2RE1,0)
                            hDm2RE1_eff.SetBinError(counterDm2RE1,0)

                        hDm2RE1_eff.GetXaxis().SetBinLabel(counterDm2RE1,name_roll)

                        if self.getMediaDisk(histoname_Eff_STA)[0] != -100:
                            hDm2RE1_eff_STA.SetBinContent(counterDm2RE1,self.getMediaDisk(histoname_Eff_STA)[0])
                            hDm2RE1_eff_STA.SetBinError(counterDm2RE1,self.getMediaDisk(histoname_Eff_STA)[1])
                        else:
                            hDm2RE1_eff_STA.SetBinContent(counterDm2RE1,0)
                            hDm2RE1_eff_STA.SetBinError(counterDm2RE1,0)

                        hDm2RE1_eff_STA.GetXaxis().SetBinLabel(counterDm2RE1,name_roll)

                        hDm2RE1_masked.SetBinContent(counterDm2RE1,self.getMaskedStripDisk(histoname_occ)[0])
                        hDm2RE1_masked.GetXaxis().SetBinLabel(counterDm2RE1,name_roll)
                        hDm2RE1_bx.SetBinContent(counterDm2RE1,self.getMeanValueDisk(histoname_bx)[0])
                        hDm2RE1_bx.SetBinError(counterDm2RE1,self.getMeanValueDisk(histoname_bx)[1])
                        hDm2RE1_bx.GetXaxis().SetBinLabel(counterDm2RE1,name_roll)

                        name_roll = name + "_B"
                        counterDm2RE1+=1

                        if self.getMediaDisk(histoname_Eff)[2] != -100:
                            hDm2RE1_eff.SetBinContent(counterDm2RE1,self.getMediaDisk(histoname_Eff)[2])
                            hDm2RE1_eff.SetBinError(counterDm2RE1,self.getMediaDisk(histoname_Eff)[3])
                        else:
                            hDm2RE1_eff.SetBinContent(counterDm2RE1,0)
                            hDm2RE1_eff.SetBinError(counterDm2RE1,0)

                        hDm2RE1_eff.GetXaxis().SetBinLabel(counterDm2RE1,name_roll)

                        if self.getMediaDisk(histoname_Eff_STA)[2] != -100:
                            hDm2RE1_eff_STA.SetBinContent(counterDm2RE1,self.getMediaDisk(histoname_Eff_STA)[2])
                            hDm2RE1_eff_STA.SetBinError(counterDm2RE1,self.getMediaDisk(histoname_Eff_STA)[3])
                        else:
                            hDm2RE1_eff_STA.SetBinContent(counterDm2RE1,0)
                            hDm2RE1_eff_STA.SetBinError(counterDm2RE1,0)

                        hDm2RE1_eff_STA.GetXaxis().SetBinLabel(counterDm2RE1,name_roll)

                        hDm2RE1_masked.SetBinContent(counterDm2RE1,self.getMaskedStripDisk(histoname_occ)[1])
                        hDm2RE1_masked.GetXaxis().SetBinLabel(counterDm2RE1,name_roll)
                        hDm2RE1_bx.SetBinContent(counterDm2RE1,self.getMeanValueDisk(histoname_bx)[2])
                        hDm2RE1_bx.SetBinError(counterDm2RE1,self.getMeanValueDisk(histoname_bx)[3])
                        hDm2RE1_bx.GetXaxis().SetBinLabel(counterDm2RE1,name_roll)

                        name_roll = name + "_C"
                        counterDm2RE1+=1

                        if self.getMediaDisk(histoname_Eff)[0] != -100:
                            hDm2RE1_eff.SetBinContent(counterDm2RE1,self.getMediaDisk(histoname_Eff)[0])
                            hDm2RE1_eff.SetBinError(counterDm2RE1,self.getMediaDisk(histoname_Eff)[1])
                        else:
                            hDm2RE1_eff.SetBinContent(counterDm2RE1,0)
                            hDm2RE1_eff.SetBinError(counterDm2RE1,0)

                        hDm2RE1_eff.GetXaxis().SetBinLabel(counterDm2RE1,name_roll)

                        if self.getMediaDisk(histoname_Eff_STA)[0] != -100:
                            hDm2RE1_eff_STA.SetBinContent(counterDm2RE1,self.getMediaDisk(histoname_Eff_STA)[0])
                            hDm2RE1_eff_STA.SetBinError(counterDm2RE1,self.getMediaDisk(histoname_Eff_STA)[1])
                        else:
                            hDm2RE1_eff_STA.SetBinContent(counterDm2RE1,0)
                            hDm2RE1_eff_STA.SetBinError(counterDm2RE1,0)

                        hDm2RE1_eff_STA.GetXaxis().SetBinLabel(counterDm2RE1,name_roll)

                        hDm2RE1_masked.SetBinContent(counterDm2RE1,self.getMaskedStripDisk(histoname_occ)[0])
                        hDm2RE1_masked.GetXaxis().SetBinLabel(counterDm2RE1,name_roll)
                        hDm2RE1_bx.SetBinContent(counterDm2RE1,self.getMeanValueDisk(histoname_bx)[0])
                        hDm2RE1_bx.SetBinError(counterDm2RE1,self.getMeanValueDisk(histoname_bx)[1])
                        hDm2RE1_bx.GetXaxis().SetBinLabel(counterDm2RE1,name_roll)

##------------------------------------ RE -1 ----------------------------------------------------------

                if el == "RE-1":
                    hDm1_masked.Fill(self.getMaskedStripDisk(histoname_occ)[0])
                    hDm1_masked.Fill(self.getMaskedStripDisk(histoname_occ)[1])
                    hDm1_masked.Fill(self.getMaskedStripDisk(histoname_occ)[2])
                    hDm1_eff.Fill(self.getMediaDisk(histoname_Eff)[0])
                    hDm1_eff.Fill(self.getMediaDisk(histoname_Eff)[2])
                    hDm1_eff.Fill(self.getMediaDisk(histoname_Eff)[4])
                    hDm1_eff_STA.Fill(self.getMediaDisk(histoname_Eff_STA)[0])
                    hDm1_eff_STA.Fill(self.getMediaDisk(histoname_Eff_STA)[2])
                    hDm1_eff_STA.Fill(self.getMediaDisk(histoname_Eff_STA)[4])

                    if coord1[0] == "R3":
                        name_roll = name + "_A"
                        counterDm1RE3+=1

                        if self.getMediaDisk(histoname_Eff)[0] != -100:
                            hDm1RE3_eff.SetBinContent(counterDm1RE3,self.getMediaDisk(histoname_Eff)[0])
                            hDm1RE3_eff.SetBinError(counterDm1RE3,self.getMediaDisk(histoname_Eff)[1])
                        else:
                            hDm1RE3_eff.SetBinContent(counterDm1RE3,0)
                            hDm1RE3_eff.SetBinError(counterDm1RE3,0)

                        hDm1RE3_eff.GetXaxis().SetBinLabel(counterDm1RE3,name_roll)

                        if self.getMediaDisk(histoname_Eff_STA)[0] != -100:
                            hDm1RE3_eff_STA.SetBinContent(counterDm1RE3,self.getMediaDisk(histoname_Eff_STA)[0])
                            hDm1RE3_eff_STA.SetBinError(counterDm1RE3,self.getMediaDisk(histoname_Eff_STA)[1])
                        else:
                            hDm1RE3_eff_STA.SetBinContent(counterDm1RE3,0)
                            hDm1RE3_eff_STA.SetBinError(counterDm1RE3,0)

                        hDm1RE3_eff_STA.GetXaxis().SetBinLabel(counterDm1RE3,name_roll)

                        hDm1RE3_masked.SetBinContent(counterDm1RE3,self.getMaskedStripDisk(histoname_occ)[0])
                        hDm1RE3_masked.GetXaxis().SetBinLabel(counterDm1RE3,name_roll)
                        hDm1RE3_bx.SetBinContent(counterDm1RE3,self.getMeanValueDisk(histoname_bx)[0])
                        hDm1RE3_bx.SetBinError(counterDm1RE3,self.getMeanValueDisk(histoname_bx)[1])
                        hDm1RE3_bx.GetXaxis().SetBinLabel(counterDm1RE3,name_roll)

                        name_roll = name + "_B"
                        counterDm1RE3+=1

                        if self.getMediaDisk(histoname_Eff)[2] != -100:
                            hDm1RE3_eff.SetBinContent(counterDm1RE3,self.getMediaDisk(histoname_Eff)[2])
                            hDm1RE3_eff.SetBinError(counterDm1RE3,self.getMediaDisk(histoname_Eff)[3])
                        else:
                            hDm1RE3_eff.SetBinContent(counterDm1RE3,0)
                            hDm1RE3_eff.SetBinError(counterDm1RE3,0)

                        hDm1RE3_eff.GetXaxis().SetBinLabel(counterDm1RE3,name_roll)

                        if self.getMediaDisk(histoname_Eff_STA)[2] != -100:
                            hDm1RE3_eff_STA.SetBinContent(counterDm1RE3,self.getMediaDisk(histoname_Eff_STA)[2])
                            hDm1RE3_eff_STA.SetBinError(counterDm1RE3,self.getMediaDisk(histoname_Eff_STA)[3])
                        else:
                            hDm1RE3_eff_STA.SetBinContent(counterDm1RE3,0)
                            hDm1RE3_eff_STA.SetBinError(counterDm1RE3,0)

                        hDm1RE3_eff_STA.GetXaxis().SetBinLabel(counterDm1RE3,name_roll)

                        hDm1RE3_masked.SetBinContent(counterDm1RE3,self.getMaskedStripDisk(histoname_occ)[1])
                        hDm1RE3_masked.GetXaxis().SetBinLabel(counterDm1RE3,name_roll)
                        hDm1RE3_bx.SetBinContent(counterDm1RE3,self.getMeanValueDisk(histoname_bx)[2])
                        hDm1RE3_bx.SetBinError(counterDm1RE3,self.getMeanValueDisk(histoname_bx)[3])
                        hDm1RE3_bx.GetXaxis().SetBinLabel(counterDm1RE3,name_roll)

                        name_roll = name + "_C"
                        counterDm1RE3+=1

                        if self.getMediaDisk(histoname_Eff)[2] != -100:
                            hDm1RE3_eff.SetBinContent(counterDm1RE3,self.getMediaDisk(histoname_Eff)[2])
                            hDm1RE3_eff.SetBinError(counterDm1RE3,self.getMediaDisk(histoname_Eff)[3])
                        else:
                            hDm1RE3_eff.SetBinContent(counterDm1RE3,0)
                            hDm1RE3_eff.SetBinError(counterDm1RE3,0)

                        hDm1RE3_eff.GetXaxis().SetBinLabel(counterDm1RE3,name_roll)

                        if self.getMediaDisk(histoname_Eff_STA)[2] != -100:
                            hDm1RE3_eff_STA.SetBinContent(counterDm1RE3,self.getMediaDisk(histoname_Eff_STA)[2])
                            hDm1RE3_eff_STA.SetBinError(counterDm1RE3,self.getMediaDisk(histoname_Eff_STA)[3])
                        else:
                            hDm1RE3_eff_STA.SetBinContent(counterDm1RE3,0)
                            hDm1RE3_eff_STA.SetBinError(counterDm1RE3,0)

                        hDm1RE3_eff.GetXaxis().SetBinLabel(counterDm1RE3,name_roll)

                        hDm1RE3_masked.SetBinContent(counterDm1RE3,self.getMaskedStripDisk(histoname_occ)[1])
                        hDm1RE3_masked.GetXaxis().SetBinLabel(counterDm1RE3,name_roll)
                        hDm1RE3_bx.SetBinContent(counterDm1RE3,self.getMeanValueDisk(histoname_bx)[2])
                        hDm1RE3_bx.SetBinError(counterDm1RE3,self.getMeanValueDisk(histoname_bx)[3])
                        hDm1RE3_bx.GetXaxis().SetBinLabel(counterDm1RE3,name_roll)

                    if coord1[0] == "R2":
                        name_roll = name + "_A"
                        counterDm1RE2+=1

                        if self.getMediaDisk(histoname_Eff)[0] != -100:
                            hDm1RE2_eff.SetBinContent(counterDm1RE2,self.getMediaDisk(histoname_Eff)[0])
                            hDm1RE2_eff.SetBinError(counterDm1RE2,self.getMediaDisk(histoname_Eff)[1])
                        else:
                            hDm1RE2_eff.SetBinContent(counterDm1RE2,0)
                            hDm1RE2_eff.SetBinError(counterDm1RE2,0)

                        hDm1RE2_eff.GetXaxis().SetBinLabel(counterDm1RE2,name_roll)

                        if self.getMediaDisk(histoname_Eff_STA)[0] != -100:
                            hDm1RE2_eff_STA.SetBinContent(counterDm1RE2,self.getMediaDisk(histoname_Eff_STA)[0])
                            hDm1RE2_eff_STA.SetBinError(counterDm1RE2,self.getMediaDisk(histoname_Eff_STA)[1])
                        else:
                            hDm1RE2_eff_STA.SetBinContent(counterDm1RE2,0)
                            hDm1RE2_eff_STA.SetBinError(counterDm1RE2,0)

                        hDm1RE2_eff_STA.GetXaxis().SetBinLabel(counterDm1RE2,name_roll)

                        hDm1RE2_masked.SetBinContent(counterDm1RE2,self.getMaskedStripDisk(histoname_occ)[0])
                        hDm1RE2_masked.GetXaxis().SetBinLabel(counterDm1RE2,name_roll)
                        hDm1RE2_bx.SetBinContent(counterDm1RE2,self.getMeanValueDisk(histoname_bx)[0])
                        hDm1RE2_bx.SetBinError(counterDm1RE2,self.getMeanValueDisk(histoname_bx)[1])
                        hDm1RE2_bx.GetXaxis().SetBinLabel(counterDm1RE2,name_roll)

                        name_roll = name + "_B"
                        counterDm1RE2+=1

                        if self.getMediaDisk(histoname_Eff)[2] != -100:
                            hDm1RE2_eff.SetBinContent(counterDm1RE2,self.getMediaDisk(histoname_Eff)[2])
                            hDm1RE2_eff.SetBinError(counterDm1RE2,self.getMediaDisk(histoname_Eff)[3])
                        else:
                            hDm1RE2_eff.SetBinContent(counterDm1RE2,0)
                            hDm1RE2_eff.SetBinError(counterDm1RE2,0)

                        hDm1RE2_eff.GetXaxis().SetBinLabel(counterDm1RE2,name_roll)

                        if self.getMediaDisk(histoname_Eff_STA)[2] != -100:
                            hDm1RE2_eff_STA.SetBinContent(counterDm1RE2,self.getMediaDisk(histoname_Eff_STA)[2])
                            hDm1RE2_eff_STA.SetBinError(counterDm1RE2,self.getMediaDisk(histoname_Eff_STA)[3])
                        else:
                            hDm1RE2_eff_STA.SetBinContent(counterDm1RE2,0)
                            hDm1RE2_eff_STA.SetBinError(counterDm1RE2,0)

                        hDm1RE2_eff_STA.GetXaxis().SetBinLabel(counterDm1RE2,name_roll)

                        hDm1RE2_masked.SetBinContent(counterDm1RE2,self.getMaskedStripDisk(histoname_occ)[1])
                        hDm1RE2_masked.GetXaxis().SetBinLabel(counterDm1RE2,name_roll)
                        hDm1RE2_bx.SetBinContent(counterDm1RE2,self.getMeanValueDisk(histoname_bx)[2])
                        hDm1RE2_bx.SetBinError(counterDm1RE2,self.getMeanValueDisk(histoname_bx)[3])
                        hDm1RE2_bx.GetXaxis().SetBinLabel(counterDm1RE2,name_roll)

                        name_roll = name + "_C"
                        counterDm1RE2+=1

                        if self.getMediaDisk(histoname_Eff)[2] != -100:
                            hDm1RE2_eff.SetBinContent(counterDm1RE2,self.getMediaDisk(histoname_Eff)[2])
                            hDm1RE2_eff.SetBinError(counterDm1RE2,self.getMediaDisk(histoname_Eff)[3])
                        else:
                            hDm1RE2_eff.SetBinContent(counterDm1RE2,0)
                            hDm1RE2_eff.SetBinError(counterDm1RE2,0)

                        hDm1RE2_eff.GetXaxis().SetBinLabel(counterDm1RE2,name_roll)

                        if self.getMediaDisk(histoname_Eff_STA)[2] != -100:
                            hDm1RE2_eff_STA.SetBinContent(counterDm1RE2,self.getMediaDisk(histoname_Eff_STA)[2])
                            hDm1RE2_eff_STA.SetBinError(counterDm1RE2,self.getMediaDisk(histoname_Eff_STA)[3])
                        else:
                            hDm1RE2_eff_STA.SetBinContent(counterDm1RE2,0)
                            hDm1RE2_eff_STA.SetBinError(counterDm1RE2,0)

                        hDm1RE2_eff_STA.GetXaxis().SetBinLabel(counterDm1RE2,name_roll)

                        hDm1RE2_masked.SetBinContent(counterDm1RE2,self.getMaskedStripDisk(histoname_occ)[1])
                        hDm1RE2_masked.GetXaxis().SetBinLabel(counterDm1RE2,name_roll)
                        hDm1RE2_bx.SetBinContent(counterDm1RE2,self.getMeanValueDisk(histoname_bx)[2])
                        hDm1RE2_bx.SetBinError(counterDm1RE2,self.getMeanValueDisk(histoname_bx)[3])
                        hDm1RE2_bx.GetXaxis().SetBinLabel(counterDm1RE2,name_roll)

                    if coord1[0] == "R1":
                        name_roll = name + "_A"
                        counterDm1RE1+=1

                        if self.getMediaDisk(histoname_Eff)[0] != -100:
                            hDm1RE1_eff.SetBinContent(counterDm1RE1,self.getMediaDisk(histoname_Eff)[0])
                            hDm1RE1_eff.SetBinError(counterDm1RE1,self.getMediaDisk(histoname_Eff)[1])
                        else:
                            hDm1RE1_eff.SetBinContent(counterDm1RE1,0)
                            hDm1RE1_eff.SetBinError(counterDm1RE1,0)

                        hDm1RE1_eff.GetXaxis().SetBinLabel(counterDm1RE1,name_roll)

                        if self.getMediaDisk(histoname_Eff_STA)[0] != -100:
                            hDm1RE1_eff_STA.SetBinContent(counterDm1RE1,self.getMediaDisk(histoname_Eff_STA)[0])
                            hDm1RE1_eff_STA.SetBinError(counterDm1RE1,self.getMediaDisk(histoname_Eff_STA)[1])
                        else:
                            hDm1RE1_eff_STA.SetBinContent(counterDm1RE1,0)
                            hDm1RE1_eff_STA.SetBinError(counterDm1RE1,0)

                        hDm1RE1_eff_STA.GetXaxis().SetBinLabel(counterDm1RE1,name_roll)

                        hDm1RE1_masked.SetBinContent(counterDm1RE1,self.getMaskedStripDisk(histoname_occ)[0])
                        hDm1RE1_masked.GetXaxis().SetBinLabel(counterDm1RE1,name_roll)
                        hDm1RE1_bx.SetBinContent(counterDm1RE1,self.getMeanValueDisk(histoname_bx)[0])
                        hDm1RE1_bx.SetBinError(counterDm1RE1,self.getMeanValueDisk(histoname_bx)[1])
                        hDm1RE1_bx.GetXaxis().SetBinLabel(counterDm1RE1,name_roll)

                        name_roll = name + "_B"
                        counterDm1RE1+=1

                        if self.getMediaDisk(histoname_Eff)[2] != -100:
                            hDm1RE1_eff.SetBinContent(counterDm1RE1,self.getMediaDisk(histoname_Eff)[2])
                            hDm1RE1_eff.SetBinError(counterDm1RE1,self.getMediaDisk(histoname_Eff)[3])
                        else:
                            hDm1RE1_eff.SetBinContent(counterDm1RE1,0)
                            hDm1RE1_eff.SetBinError(counterDm1RE1,0)

                        hDm1RE1_eff.GetXaxis().SetBinLabel(counterDm1RE1,name_roll)

                        if self.getMediaDisk(histoname_Eff_STA)[2] != -100:
                            hDm1RE1_eff_STA.SetBinContent(counterDm1RE1,self.getMediaDisk(histoname_Eff_STA)[2])
                            hDm1RE1_eff_STA.SetBinError(counterDm1RE1,self.getMediaDisk(histoname_Eff_STA)[3])
                        else:
                            hDm1RE1_eff_STA.SetBinContent(counterDm1RE1,0)
                            hDm1RE1_eff_STA.SetBinError(counterDm1RE1,0)

                        hDm1RE1_eff_STA.GetXaxis().SetBinLabel(counterDm1RE1,name_roll)

                        hDm1RE1_masked.SetBinContent(counterDm1RE1,self.getMaskedStripDisk(histoname_occ)[1])
                        hDm1RE1_masked.GetXaxis().SetBinLabel(counterDm1RE1,name_roll)
                        hDm1RE1_bx.SetBinContent(counterDm1RE1,self.getMeanValueDisk(histoname_bx)[2])
                        hDm1RE1_bx.SetBinError(counterDm1RE1,self.getMeanValueDisk(histoname_bx)[3])
                        hDm1RE1_bx.GetXaxis().SetBinLabel(counterDm1RE1,name_roll)

                        name_roll = name + "_C"
                        counterDm1RE1+=1

                        if self.getMediaDisk(histoname_Eff)[2] != -100:
                            hDm1RE1_eff.SetBinContent(counterDm1RE1,self.getMediaDisk(histoname_Eff)[2])
                            hDm1RE1_eff.SetBinError(counterDm1RE1,self.getMediaDisk(histoname_Eff)[3])
                        else:
                            hDm1RE1_eff.SetBinContent(counterDm1RE1,0)
                            hDm1RE1_eff.SetBinError(counterDm1RE1,0)

                        hDm1RE1_eff.GetXaxis().SetBinLabel(counterDm1RE1,name_roll)

                        if self.getMediaDisk(histoname_Eff_STA)[2] != -100:
                            hDm1RE1_eff_STA.SetBinContent(counterDm1RE1,self.getMediaDisk(histoname_Eff_STA)[2])
                            hDm1RE1_eff_STA.SetBinError(counterDm1RE1,self.getMediaDisk(histoname_Eff_STA)[3])
                        else:
                            hDm1RE1_eff_STA.SetBinContent(counterDm1RE1,0)
                            hDm1RE1_eff_STA.SetBinError(counterDm1RE1,0)

                        hDm1RE1_eff_STA.GetXaxis().SetBinLabel(counterDm1RE1,name_roll)

                        hDm1RE1_masked.SetBinContent(counterDm1RE1,self.getMaskedStripDisk(histoname_occ)[1])
                        hDm1RE1_masked.GetXaxis().SetBinLabel(counterDm1RE1,name_roll)
                        hDm1RE1_bx.SetBinContent(counterDm1RE1,self.getMeanValueDisk(histoname_bx)[2])
                        hDm1RE1_bx.SetBinError(counterDm1RE1,self.getMeanValueDisk(histoname_bx)[3])
                        hDm1RE1_bx.GetXaxis().SetBinLabel(counterDm1RE1,name_roll)

##-----------------------------------  RE +3 -----------------------------------------------------------------
                
                if el == "RE+3":

                    hDp3_masked.Fill(self.getMaskedStripDisk(histoname_occ)[0])
                    hDp3_masked.Fill(self.getMaskedStripDisk(histoname_occ)[1])
                    hDp3_masked.Fill(self.getMaskedStripDisk(histoname_occ)[2])
                    hDp3_eff.Fill(self.getMediaDisk(histoname_Eff)[0])
                    hDp3_eff.Fill(self.getMediaDisk(histoname_Eff)[2])
                    hDp3_eff.Fill(self.getMediaDisk(histoname_Eff)[4])
                    hDp3_eff_STA.Fill(self.getMediaDisk(histoname_Eff_STA)[0])
                    hDp3_eff_STA.Fill(self.getMediaDisk(histoname_Eff_STA)[2])
                    hDp3_eff_STA.Fill(self.getMediaDisk(histoname_Eff_STA)[4])


                    if coord1[0] == "R3":
                        name_roll = name + "_A"

                        counterDp3RE3+=1
                        if self.getMediaDisk(histoname_Eff)[0] != -100:
                            hDp3RE3_eff.SetBinContent(counterDp3RE3,self.getMediaDisk(histoname_Eff)[0])
                            hDp3RE3_eff.SetBinError(counterDp3RE3,self.getMediaDisk(histoname_Eff)[1])
                        else:
                            hDp3RE3_eff.SetBinContent(counterDp3RE3,0)
                            hDp3RE3_eff.SetBinError(counterDp3RE3,0)
                            
                        hDp3RE3_eff.GetXaxis().SetBinLabel(counterDp3RE3,name_roll)

                        if self.getMediaDisk(histoname_Eff_STA)[0] != -100:
                            hDp3RE3_eff_STA.SetBinContent(counterDp3RE3,self.getMediaDisk(histoname_Eff_STA)[0])
                            hDp3RE3_eff_STA.SetBinError(counterDp3RE3,self.getMediaDisk(histoname_Eff_STA)[1])
                        else:
                            hDp3RE3_eff_STA.SetBinContent(counterDp3RE3,0)
                            hDp3RE3_eff_STA.SetBinError(counterDp3RE3,0)

                        hDp3RE3_eff_STA.GetXaxis().SetBinLabel(counterDp3RE3,name_roll)

                        hDp3RE3_masked.SetBinContent(counterDp3RE3,self.getMaskedStripDisk(histoname_occ)[0])
                        hDp3RE3_masked.GetXaxis().SetBinLabel(counterDp3RE3,name_roll)
                        hDp3RE3_bx.SetBinContent(counterDp3RE3,self.getMeanValueDisk(histoname_bx)[0])
                        hDp3RE3_bx.SetBinError(counterDp3RE3,self.getMeanValueDisk(histoname_bx)[1])
                        hDp3RE3_bx.GetXaxis().SetBinLabel(counterDp3RE3,name_roll)
                        
                        name_roll = name + "_B"
                        counterDp3RE3+=1
                        
                        if self.getMediaDisk(histoname_Eff)[2] != -100:
                            hDp3RE3_eff.SetBinContent(counterDp3RE3,self.getMediaDisk(histoname_Eff)[2])
                            hDp3RE3_eff.SetBinError(counterDp3RE3,self.getMediaDisk(histoname_Eff)[3])
                        else:
                            hDp3RE3_eff.SetBinContent(counterDp3RE3,0)
                            hDp3RE3_eff.SetBinError(counterDp3RE3,0)
                                
                        hDp3RE3_eff.GetXaxis().SetBinLabel(counterDp3RE3,name_roll)

                        if self.getMediaDisk(histoname_Eff_STA)[2] != -100:
                            hDp3RE3_eff_STA.SetBinContent(counterDp3RE3,self.getMediaDisk(histoname_Eff_STA)[2])
                            hDp3RE3_eff_STA.SetBinError(counterDp3RE3,self.getMediaDisk(histoname_Eff_STA)[3])
                        else:
                            hDp3RE3_eff_STA.SetBinContent(counterDp3RE3,0)
                            hDp3RE3_eff_STA.SetBinError(counterDp3RE3,0)

                        hDp3RE3_eff_STA.GetXaxis().SetBinLabel(counterDp3RE3,name_roll)

                        hDp3RE3_masked.SetBinContent(counterDp3RE3,self.getMaskedStripDisk(histoname_occ)[1])
                        hDp3RE3_masked.GetXaxis().SetBinLabel(counterDp3RE3,name_roll)
                        hDp3RE3_bx.SetBinContent(counterDp3RE3,self.getMeanValueDisk(histoname_bx)[2])
                        hDp3RE3_bx.SetBinError(counterDp3RE3,self.getMeanValueDisk(histoname_bx)[3])
                        hDp3RE3_bx.GetXaxis().SetBinLabel(counterDp3RE3,name_roll)

                        name_roll = name + "_C"
                        counterDp3RE3+=1
                        
                        if self.getMediaDisk(histoname_Eff)[2] != -100:
                            hDp3RE3_eff.SetBinContent(counterDp3RE3,self.getMediaDisk(histoname_Eff)[2])
                            hDp3RE3_eff.SetBinError(counterDp3RE3,self.getMediaDisk(histoname_Eff)[3])
                        else:
                            hDp3RE3_eff.SetBinContent(counterDp3RE3,0)
                            hDp3RE3_eff.SetBinError(counterDp3RE3,0)
                                
                        hDp3RE3_eff.GetXaxis().SetBinLabel(counterDp3RE3,name_roll)

                        if self.getMediaDisk(histoname_Eff_STA)[2] != -100:
                            hDp3RE3_eff_STA.SetBinContent(counterDp3RE3,self.getMediaDisk(histoname_Eff_STA)[2])
                            hDp3RE3_eff_STA.SetBinError(counterDp3RE3,self.getMediaDisk(histoname_Eff_STA)[3])
                        else:
                            hDp3RE3_eff_STA.SetBinContent(counterDp3RE3,0)
                            hDp3RE3_eff_STA.SetBinError(counterDp3RE3,0)

                        hDp3RE3_eff_STA.GetXaxis().SetBinLabel(counterDp3RE3,name_roll)

                        hDp3RE3_masked.SetBinContent(counterDp3RE3,self.getMaskedStripDisk(histoname_occ)[1])
                        hDp3RE3_masked.GetXaxis().SetBinLabel(counterDp3RE3,name_roll)
                        hDp3RE3_bx.SetBinContent(counterDp3RE3,self.getMeanValueDisk(histoname_bx)[2])
                        hDp3RE3_bx.SetBinError(counterDp3RE3,self.getMeanValueDisk(histoname_bx)[3])
                        hDp3RE3_bx.GetXaxis().SetBinLabel(counterDp3RE3,name_roll)

                    if coord1[0] == "R2":

                        name_roll = name + "_A"
                        counterDp3RE2+=1

                        if self.getMediaDisk(histoname_Eff)[0] != -100:
                            hDp3RE2_eff.SetBinContent(counterDp3RE2,self.getMediaDisk(histoname_Eff)[0])
                            hDp3RE2_eff.SetBinError(counterDp3RE2,self.getMediaDisk(histoname_Eff)[1])
                        else:
                            hDp3RE2_eff.SetBinContent(counterDp3RE2,0)
                            hDp3RE2_eff.SetBinError(counterDp3RE2,0)
                            
                        hDp3RE2_eff.GetXaxis().SetBinLabel(counterDp3RE2,name_roll)

                        if self.getMediaDisk(histoname_Eff_STA)[0] != -100:
                            hDp3RE2_eff_STA.SetBinContent(counterDp3RE2,self.getMediaDisk(histoname_Eff_STA)[0])
                            hDp3RE2_eff_STA.SetBinError(counterDp3RE2,self.getMediaDisk(histoname_Eff_STA)[1])
                        else:
                            hDp3RE2_eff_STA.SetBinContent(counterDp3RE2,0)
                            hDp3RE2_eff_STA.SetBinError(counterDp3RE2,0)

                        hDp3RE2_eff_STA.GetXaxis().SetBinLabel(counterDp3RE2,name_roll)

                        hDp3RE2_masked.SetBinContent(counterDp3RE2,self.getMaskedStripDisk(histoname_occ)[0])
                        hDp3RE2_masked.GetXaxis().SetBinLabel(counterDp3RE2,name_roll)
                        hDp3RE2_bx.SetBinContent(counterDp3RE2,self.getMeanValueDisk(histoname_bx)[0])
                        hDp3RE2_bx.SetBinError(counterDp3RE2,self.getMeanValueDisk(histoname_bx)[1])
                        hDp3RE2_bx.GetXaxis().SetBinLabel(counterDp3RE2,name_roll)
                        
                        name_roll = name + "_B"
                        counterDp3RE2+=1
                        
                        if self.getMediaDisk(histoname_Eff)[2] != -100:
                            hDp3RE2_eff.SetBinContent(counterDp3RE2,self.getMediaDisk(histoname_Eff)[2])
                            hDp3RE2_eff.SetBinError(counterDp3RE2,self.getMediaDisk(histoname_Eff)[3])
                        else:
                            hDp3RE2_eff.SetBinContent(counterDp3RE2,0)
                            hDp3RE2_eff.SetBinError(counterDp3RE2,0)
                                
                        hDp3RE2_eff.GetXaxis().SetBinLabel(counterDp3RE2,name_roll)

                        if self.getMediaDisk(histoname_Eff_STA)[2] != -100:
                            hDp3RE2_eff_STA.SetBinContent(counterDp3RE2,self.getMediaDisk(histoname_Eff_STA)[2])
                            hDp3RE2_eff_STA.SetBinError(counterDp3RE2,self.getMediaDisk(histoname_Eff_STA)[3])
                        else:
                            hDp3RE2_eff_STA.SetBinContent(counterDp3RE2,0)
                            hDp3RE2_eff_STA.SetBinError(counterDp3RE2,0)

                        hDp3RE2_eff_STA.GetXaxis().SetBinLabel(counterDp3RE2,name_roll)

                        hDp3RE2_masked.SetBinContent(counterDp3RE2,self.getMaskedStripDisk(histoname_occ)[1])
                        hDp3RE2_masked.GetXaxis().SetBinLabel(counterDp3RE2,name_roll)
                        hDp3RE2_bx.SetBinContent(counterDp3RE2,self.getMeanValueDisk(histoname_bx)[2])
                        hDp3RE2_bx.SetBinError(counterDp3RE2,self.getMeanValueDisk(histoname_bx)[3])
                        hDp3RE2_bx.GetXaxis().SetBinLabel(counterDp3RE2,name_roll)

                        name_roll = name + "_C"
                        counterDp3RE2+=1
                        
                        if self.getMediaDisk(histoname_Eff)[2] != -100:
                            hDp3RE2_eff.SetBinContent(counterDp3RE2,self.getMediaDisk(histoname_Eff)[2])
                            hDp3RE2_eff.SetBinError(counterDp3RE2,self.getMediaDisk(histoname_Eff)[3])
                        else:
                            hDp3RE2_eff.SetBinContent(counterDp3RE2,0)
                            hDp3RE2_eff.SetBinError(counterDp3RE2,0)
                                
                        hDp3RE2_eff.GetXaxis().SetBinLabel(counterDp3RE2,name_roll)

                        if self.getMediaDisk(histoname_Eff)[2] != -100:
                            hDp3RE2_eff_STA.SetBinContent(counterDp3RE2,self.getMediaDisk(histoname_Eff_STA)[2])
                            hDp3RE2_eff_STA.SetBinError(counterDp3RE2,self.getMediaDisk(histoname_Eff_STA)[3])
                        else:
                            hDp3RE2_eff_STA.SetBinContent(counterDp3RE2,0)
                            hDp3RE2_eff_STA.SetBinError(counterDp3RE2,0)

                        hDp3RE2_eff_STA.GetXaxis().SetBinLabel(counterDp3RE2,name_roll)

                        hDp3RE2_masked.SetBinContent(counterDp3RE2,self.getMaskedStripDisk(histoname_occ)[1])
                        hDp3RE2_masked.GetXaxis().SetBinLabel(counterDp3RE2,name_roll)
                        hDp3RE2_bx.SetBinContent(counterDp3RE2,self.getMeanValueDisk(histoname_bx)[2])
                        hDp3RE2_bx.SetBinError(counterDp3RE2,self.getMeanValueDisk(histoname_bx)[3])
                        hDp3RE2_bx.GetXaxis().SetBinLabel(counterDp3RE2,name_roll)

                    if coord1[0] == "R1":

                        name_roll = name + "_A"
                        counterDp3RE1 += 1

                        if self.getMediaDisk(histoname_Eff)[0] != -100:
                            hDp3RE1_eff.SetBinContent(counterDp3RE1,self.getMediaDisk(histoname_Eff)[0])
                            hDp3RE1_eff.SetBinError(counterDp3RE1,self.getMediaDisk(histoname_Eff)[1])
                        else:
                            hDp3RE1_eff.SetBinContent(counterDp3RE1,0)
                            hDp3RE1_eff.SetBinError(counterDp3RE1,0)
                            
                        hDp3RE1_eff.GetXaxis().SetBinLabel(counterDp3RE1,name_roll)

                        if self.getMediaDisk(histoname_Eff_STA)[0] != -100:
                            hDp3RE1_eff_STA.SetBinContent(counterDp3RE1,self.getMediaDisk(histoname_Eff_STA)[0])
                            hDp3RE1_eff_STA.SetBinError(counterDp3RE1,self.getMediaDisk(histoname_Eff_STA)[1])
                        else:
                            hDp3RE1_eff_STA.SetBinContent(counterDp3RE1,0)
                            hDp3RE1_eff_STA.SetBinError(counterDp3RE1,0)

                        hDp3RE1_eff_STA.GetXaxis().SetBinLabel(counterDp3RE1,name_roll)

                        hDp3RE1_masked.SetBinContent(counterDp3RE1,self.getMaskedStripDisk(histoname_occ)[0])
                        hDp3RE1_masked.GetXaxis().SetBinLabel(counterDp3RE1,name_roll)
                        hDp3RE1_bx.SetBinContent(counterDp3RE1,self.getMeanValueDisk(histoname_bx)[0])
                        hDp3RE1_bx.SetBinError(counterDp3RE1,self.getMeanValueDisk(histoname_bx)[1])
                        hDp3RE1_bx.GetXaxis().SetBinLabel(counterDp3RE1,name_roll)
                        
                        name_roll = name + "_B"
                        counterDp3RE1 += 1
                        
                        if self.getMediaDisk(histoname_Eff)[2] != -100:
                            hDp3RE1_eff.SetBinContent(counterDp3RE1,self.getMediaDisk(histoname_Eff)[2])
                            hDp3RE1_eff.SetBinError(counterDp3RE1,self.getMediaDisk(histoname_Eff)[3])
                        else:
                            hDp3RE1_eff.SetBinContent(counterDp3RE1,0)
                            hDp3RE1_eff.SetBinError(counterDp3RE1,0)
                                
                        hDp3RE1_eff.GetXaxis().SetBinLabel(counterDp3RE1,name_roll)

                        if self.getMediaDisk(histoname_Eff_STA)[2] != -100:
                            hDp3RE1_eff_STA.SetBinContent(counterDp3RE1,self.getMediaDisk(histoname_Eff_STA)[2])
                            hDp3RE1_eff_STA.SetBinError(counterDp3RE1,self.getMediaDisk(histoname_Eff_STA)[3])
                        else:
                            hDp3RE1_eff_STA.SetBinContent(counterDp3RE1,0)
                            hDp3RE1_eff_STA.SetBinError(counterDp3RE1,0)

                        hDp3RE1_eff_STA.GetXaxis().SetBinLabel(counterDp3RE1,name_roll)

                        hDp3RE1_masked.SetBinContent(counterDp3RE1,self.getMaskedStripDisk(histoname_occ)[1])
                        hDp3RE1_masked.GetXaxis().SetBinLabel(counterDp3RE1,name_roll)
                        hDp3RE1_bx.SetBinContent(counterDp3RE1,self.getMeanValueDisk(histoname_bx)[2])
                        hDp3RE1_bx.SetBinError(counterDp3RE1,self.getMeanValueDisk(histoname_bx)[3])
                        hDp3RE1_bx.GetXaxis().SetBinLabel(counterDp3RE1,name_roll)

                        name_roll = name + "_C"
                        counterDp3RE1+=1
                        
                        if self.getMediaDisk(histoname_Eff)[2] != -100:
                            hDp3RE1_eff.SetBinContent(counterDp3RE1,self.getMediaDisk(histoname_Eff)[2])
                            hDp3RE1_eff.SetBinError(counterDp3RE1,self.getMediaDisk(histoname_Eff)[3])
                        else:
                            hDp3RE1_eff.SetBinContent(counterDp3RE1,0)
                            hDp3RE1_eff.SetBinError(counterDp3RE1,0)
                                
                        hDp3RE1_eff.GetXaxis().SetBinLabel(counterDp3RE1,name_roll)

                        if self.getMediaDisk(histoname_Eff_STA)[2] != -100:
                            hDp3RE1_eff_STA.SetBinContent(counterDp3RE1,self.getMediaDisk(histoname_Eff_STA)[2])
                            hDp3RE1_eff_STA.SetBinError(counterDp3RE1,self.getMediaDisk(histoname_Eff_STA)[3])
                        else:
                            hDp3RE1_eff_STA.SetBinContent(counterDp3RE1,0)
                            hDp3RE1_eff_STA.SetBinError(counterDp3RE1,0)

                        hDp3RE1_eff_STA.GetXaxis().SetBinLabel(counterDp3RE1,name_roll)

                        hDp3RE1_masked.SetBinContent(counterDp3RE1,self.getMaskedStripDisk(histoname_occ)[1])
                        hDp3RE1_masked.GetXaxis().SetBinLabel(counterDp3RE1,name_roll)
                        hDp3RE1_bx.SetBinContent(counterDp3RE1,self.getMeanValueDisk(histoname_bx)[2])
                        hDp3RE1_bx.SetBinError(counterDp3RE1,self.getMeanValueDisk(histoname_bx)[3])
                        hDp3RE1_bx.GetXaxis().SetBinLabel(counterDp3RE1,name_roll)


##-------------------------------- RE +2 -----------------------------------------------------------------
                
                if el == "RE+2":

                    hDp2_masked.Fill(self.getMaskedStripDisk(histoname_occ)[0])
                    hDp2_masked.Fill(self.getMaskedStripDisk(histoname_occ)[1])
                    hDp2_masked.Fill(self.getMaskedStripDisk(histoname_occ)[2])
                    hDp2_eff.Fill(self.getMediaDisk(histoname_Eff)[0])
                    hDp2_eff.Fill(self.getMediaDisk(histoname_Eff)[2])                   
                    hDp2_eff.Fill(self.getMediaDisk(histoname_Eff)[4])
                    hDp2_eff_STA.Fill(self.getMediaDisk(histoname_Eff_STA)[0])
                    hDp2_eff_STA.Fill(self.getMediaDisk(histoname_Eff_STA)[2])
                    hDp2_eff_STA.Fill(self.getMediaDisk(histoname_Eff_STA)[4])

                    if coord1[0] == "R3":
                        name_roll = name + "_A"
                        counterDp2RE3+=1

                        if self.getMediaDisk(histoname_Eff)[0] != -100:
                            hDp2RE3_eff.SetBinContent(counterDp2RE3,self.getMediaDisk(histoname_Eff)[0])
                            hDp2RE3_eff.SetBinError(counterDp2RE3,self.getMediaDisk(histoname_Eff)[1])
                        else:
                            hDp2RE3_eff.SetBinContent(counterDp2RE3,0)
                            hDp2RE3_eff.SetBinError(counterDp2RE3,0)
                            
                        hDp2RE3_eff.GetXaxis().SetBinLabel(counterDp2RE3,name_roll)

                        if self.getMediaDisk(histoname_Eff_STA)[0] != -100:
                            hDp2RE3_eff_STA.SetBinContent(counterDp2RE3,self.getMediaDisk(histoname_Eff_STA)[0])
                            hDp2RE3_eff_STA.SetBinError(counterDp2RE3,self.getMediaDisk(histoname_Eff_STA)[1])
                        else:
                            hDp2RE3_eff_STA.SetBinContent(counterDp2RE3,0)
                            hDp2RE3_eff_STA.SetBinError(counterDp2RE3,0)

                        hDp2RE3_eff_STA.GetXaxis().SetBinLabel(counterDp2RE3,name_roll)

                        hDp2RE3_masked.SetBinContent(counterDp2RE3,self.getMaskedStripDisk(histoname_occ)[0])
                        hDp2RE3_masked.GetXaxis().SetBinLabel(counterDp2RE3,name_roll)
                        hDp2RE3_bx.SetBinContent(counterDp2RE3,self.getMeanValueDisk(histoname_bx)[0])
                        hDp2RE3_bx.SetBinError(counterDp2RE3,self.getMeanValueDisk(histoname_bx)[1])
                        hDp2RE3_bx.GetXaxis().SetBinLabel(counterDp2RE3,name_roll)
                        
                        name_roll = name + "_B"
                        counterDp2RE3+=1
                        
                        if self.getMediaDisk(histoname_Eff)[2] != -100:
                            hDp2RE3_eff.SetBinContent(counterDp2RE3,self.getMediaDisk(histoname_Eff)[2])
                            hDp2RE3_eff.SetBinError(counterDp2RE3,self.getMediaDisk(histoname_Eff)[3])
                        else:
                            hDp2RE3_eff.SetBinContent(counterDp2RE3,0)
                            hDp2RE3_eff.SetBinError(counterDp2RE3,0)
                                
                        hDp2RE3_eff.GetXaxis().SetBinLabel(counterDp2RE3,name_roll)

                        if self.getMediaDisk(histoname_Eff_STA)[2] != -100:
                            hDp2RE3_eff_STA.SetBinContent(counterDp2RE3,self.getMediaDisk(histoname_Eff_STA)[2])
                            hDp2RE3_eff_STA.SetBinError(counterDp2RE3,self.getMediaDisk(histoname_Eff_STA)[3])
                        else:
                            hDp2RE3_eff_STA.SetBinContent(counterDp2RE3,0)
                            hDp2RE3_eff_STA.SetBinError(counterDp2RE3,0)

                        hDp2RE3_eff_STA.GetXaxis().SetBinLabel(counterDp2RE3,name_roll)

                        hDp2RE3_masked.SetBinContent(counterDp2RE3,self.getMaskedStripDisk(histoname_occ)[1])
                        hDp2RE3_masked.GetXaxis().SetBinLabel(counterDp2RE3,name_roll)
                        hDp2RE3_bx.SetBinContent(counterDp2RE3,self.getMeanValueDisk(histoname_bx)[2])
                        hDp2RE3_bx.SetBinError(counterDp2RE3,self.getMeanValueDisk(histoname_bx)[3])
                        hDp2RE3_bx.GetXaxis().SetBinLabel(counterDp2RE3,name_roll)

                        name_roll = name + "_C"
                        counterDp2RE3+=1
                        
                        if self.getMediaDisk(histoname_Eff)[2] != -100:
                            hDp2RE3_eff.SetBinContent(counterDp2RE3,self.getMediaDisk(histoname_Eff)[2])
                            hDp2RE3_eff.SetBinError(counterDp2RE3,self.getMediaDisk(histoname_Eff)[3])
                        else:
                            hDp2RE3_eff.SetBinContent(counterDp2RE3,0)
                            hDp2RE3_eff.SetBinError(counterDp2RE3,0)
                                
                        hDp2RE3_eff.GetXaxis().SetBinLabel(counterDp2RE3,name_roll)

                        if self.getMediaDisk(histoname_Eff_STA)[2] != -100:
                            hDp2RE3_eff_STA.SetBinContent(counterDp2RE3,self.getMediaDisk(histoname_Eff_STA)[2])
                            hDp2RE3_eff_STA.SetBinError(counterDp2RE3,self.getMediaDisk(histoname_Eff_STA)[3])
                        else:
                            hDp2RE3_eff_STA.SetBinContent(counterDp2RE3,0)
                            hDp2RE3_eff_STA.SetBinError(counterDp2RE3,0)

                        hDp2RE3_eff_STA.GetXaxis().SetBinLabel(counterDp2RE3,name_roll)

                        hDp2RE3_masked.SetBinContent(counterDp2RE3,self.getMaskedStripDisk(histoname_occ)[1])
                        hDp2RE3_masked.GetXaxis().SetBinLabel(counterDp2RE3,name_roll)
                        hDp2RE3_bx.SetBinContent(counterDp2RE3,self.getMeanValueDisk(histoname_bx)[2])
                        hDp2RE3_bx.SetBinError(counterDp2RE3,self.getMeanValueDisk(histoname_bx)[3])
                        hDp2RE3_bx.GetXaxis().SetBinLabel(counterDp2RE3,name_roll)

                    if coord1[0] == "R2":
                        name_roll = name + "_A"
                        counterDp2RE2+=1

                        if self.getMediaDisk(histoname_Eff)[0] != -100:
                            hDp2RE2_eff.SetBinContent(counterDp2RE2,self.getMediaDisk(histoname_Eff)[0])
                            hDp2RE2_eff.SetBinError(counterDp2RE2,self.getMediaDisk(histoname_Eff)[1])
                        else:
                            hDp2RE2_eff.SetBinContent(counterDp2RE2,0)
                            hDp2RE2_eff.SetBinError(counterDp2RE2,0)
                            
                        hDp2RE2_eff.GetXaxis().SetBinLabel(counterDp2RE2,name_roll)

                        if self.getMediaDisk(histoname_Eff_STA)[0] != -100:
                            hDp2RE2_eff_STA.SetBinContent(counterDp2RE2,self.getMediaDisk(histoname_Eff_STA)[0])
                            hDp2RE2_eff_STA.SetBinError(counterDp2RE2,self.getMediaDisk(histoname_Eff_STA)[1])
                        else:
                            hDp2RE2_eff_STA.SetBinContent(counterDp2RE2,0)
                            hDp2RE2_eff_STA.SetBinError(counterDp2RE2,0)

                        hDp2RE2_eff_STA.GetXaxis().SetBinLabel(counterDp2RE2,name_roll)


                        hDp2RE2_masked.SetBinContent(counterDp2RE2,self.getMaskedStripDisk(histoname_occ)[0])
                        hDp2RE2_masked.GetXaxis().SetBinLabel(counterDp2RE2,name_roll)
                        hDp2RE2_bx.SetBinContent(counterDp2RE2,self.getMeanValueDisk(histoname_bx)[0])
                        hDp2RE2_bx.SetBinError(counterDp2RE2,self.getMeanValueDisk(histoname_bx)[1])
                        hDp2RE2_bx.GetXaxis().SetBinLabel(counterDp2RE2,name_roll)
                        
                        name_roll = name + "_B"
                        counterDp2RE2+=1
                        
                        if self.getMediaDisk(histoname_Eff)[2] != -100:
                            hDp2RE2_eff.SetBinContent(counterDp2RE2,self.getMediaDisk(histoname_Eff)[2])
                            hDp2RE2_eff.SetBinError(counterDp2RE2,self.getMediaDisk(histoname_Eff)[3])
                        else:
                            hDp2RE2_eff.SetBinContent(counterDp2RE2,0)
                            hDp2RE2_eff.SetBinError(counterDp2RE2,0)
                                
                        hDp2RE2_eff.GetXaxis().SetBinLabel(counterDp2RE2,name_roll)

                        if self.getMediaDisk(histoname_Eff_STA)[2] != -100:
                            hDp2RE2_eff_STA.SetBinContent(counterDp2RE2,self.getMediaDisk(histoname_Eff_STA)[2])
                            hDp2RE2_eff_STA.SetBinError(counterDp2RE2,self.getMediaDisk(histoname_Eff_STA)[3])
                        else:
                            hDp2RE2_eff_STA.SetBinContent(counterDp2RE2,0)
                            hDp2RE2_eff_STA.SetBinError(counterDp2RE2,0)

                        hDp2RE2_eff_STA.GetXaxis().SetBinLabel(counterDp2RE2,name_roll)

                        hDp2RE2_masked.SetBinContent(counterDp2RE2,self.getMaskedStripDisk(histoname_occ)[1])
                        hDp2RE2_masked.GetXaxis().SetBinLabel(counterDp2RE2,name_roll)
                        hDp2RE2_bx.SetBinContent(counterDp2RE2,self.getMeanValueDisk(histoname_bx)[2])
                        hDp2RE2_bx.SetBinError(counterDp2RE2,self.getMeanValueDisk(histoname_bx)[3])
                        hDp2RE2_bx.GetXaxis().SetBinLabel(counterDp2RE2,name_roll)

                        name_roll = name + "_C"
                        counterDp2RE2+=1
                        
                        if self.getMediaDisk(histoname_Eff)[2] != -100:
                            hDp2RE2_eff.SetBinContent(counterDp2RE2,self.getMediaDisk(histoname_Eff)[2])
                            hDp2RE2_eff.SetBinError(counterDp2RE2,self.getMediaDisk(histoname_Eff)[3])
                        else:
                            hDp2RE2_eff.SetBinContent(counterDp2RE2,0)
                            hDp2RE2_eff.SetBinError(counterDp2RE2,0)
                                
                        hDp2RE2_eff.GetXaxis().SetBinLabel(counterDp2RE2,name_roll)

                        if self.getMediaDisk(histoname_Eff_STA)[2] != -100:
                            hDp2RE2_eff_STA.SetBinContent(counterDp2RE2,self.getMediaDisk(histoname_Eff_STA)[2])
                            hDp2RE2_eff_STA.SetBinError(counterDp2RE2,self.getMediaDisk(histoname_Eff_STA)[3])
                        else:
                            hDp2RE2_eff_STA.SetBinContent(counterDp2RE2,0)
                            hDp2RE2_eff_STA.SetBinError(counterDp2RE2,0)

                        hDp2RE2_eff_STA.GetXaxis().SetBinLabel(counterDp2RE2,name_roll)

                        hDp2RE2_masked.SetBinContent(counterDp2RE2,self.getMaskedStripDisk(histoname_occ)[1])
                        hDp2RE2_masked.GetXaxis().SetBinLabel(counterDp2RE2,name_roll)
                        hDp2RE2_bx.SetBinContent(counterDp2RE2,self.getMeanValueDisk(histoname_bx)[2])
                        hDp2RE2_bx.SetBinError(counterDp2RE2,self.getMeanValueDisk(histoname_bx)[3])
                        hDp2RE2_bx.GetXaxis().SetBinLabel(counterDp2RE2,name_roll)

                    if coord1[0] == "R1":
                        name_roll = name + "_A"
                        counterDp2RE1+=1

                        if self.getMediaDisk(histoname_Eff)[0] != -100:
                            hDp2RE1_eff.SetBinContent(counterDp2RE1,self.getMediaDisk(histoname_Eff)[0])
                            hDp2RE1_eff.SetBinError(counterDp2RE1,self.getMediaDisk(histoname_Eff)[1])
                        else:
                            hDp2RE1_eff.SetBinContent(counterDp2RE1,0)
                            hDp2RE1_eff.SetBinError(counterDp2RE1,0)
                            
                        hDp2RE1_eff.GetXaxis().SetBinLabel(counterDp2RE1,name_roll)

                        if self.getMediaDisk(histoname_Eff_STA)[0] != -100:
                            hDp2RE1_eff_STA.SetBinContent(counterDp2RE1,self.getMediaDisk(histoname_Eff_STA)[0])
                            hDp2RE1_eff_STA.SetBinError(counterDp2RE1,self.getMediaDisk(histoname_Eff_STA)[1])
                        else:
                            hDp2RE1_eff_STA.SetBinContent(counterDp2RE1,0)
                            hDp2RE1_eff_STA.SetBinError(counterDp2RE1,0)

                        hDp2RE1_eff_STA.GetXaxis().SetBinLabel(counterDp2RE1,name_roll)

                        hDp2RE1_masked.SetBinContent(counterDp2RE1,self.getMaskedStripDisk(histoname_occ)[0])
                        hDp2RE1_masked.GetXaxis().SetBinLabel(counterDp2RE1,name_roll)
                        hDp2RE1_bx.SetBinContent(counterDp2RE1,self.getMeanValueDisk(histoname_bx)[0])
                        hDp2RE1_bx.SetBinError(counterDp2RE1,self.getMeanValueDisk(histoname_bx)[1])
                        hDp2RE1_bx.GetXaxis().SetBinLabel(counterDp2RE1,name_roll)
                        
                        name_roll = name + "_B"
                        counterDp2RE1+=1
                        
                        if self.getMediaDisk(histoname_Eff)[2] != -100:
                            hDp2RE1_eff.SetBinContent(counterDp2RE1,self.getMediaDisk(histoname_Eff)[2])
                            hDp2RE1_eff.SetBinError(counterDp2RE1,self.getMediaDisk(histoname_Eff)[3])
                        else:
                            hDp2RE1_eff.SetBinContent(counterDp2RE1,0)
                            hDp2RE1_eff.SetBinError(counterDp2RE1,0)
                                
                        hDp2RE1_eff.GetXaxis().SetBinLabel(counterDp2RE1,name_roll)

                        if self.getMediaDisk(histoname_Eff_STA)[2] != -100:
                            hDp2RE1_eff_STA.SetBinContent(counterDp2RE1,self.getMediaDisk(histoname_Eff_STA)[2])
                            hDp2RE1_eff_STA.SetBinError(counterDp2RE1,self.getMediaDisk(histoname_Eff_STA)[3])
                        else:
                            hDp2RE1_eff_STA.SetBinContent(counterDp2RE1,0)
                            hDp2RE1_eff_STA.SetBinError(counterDp2RE1,0)

                        hDp2RE1_eff_STA.GetXaxis().SetBinLabel(counterDp2RE1,name_roll)

                        hDp2RE1_masked.SetBinContent(counterDp2RE1,self.getMaskedStripDisk(histoname_occ)[1])
                        hDp2RE1_masked.GetXaxis().SetBinLabel(counterDp2RE1,name_roll)
                        hDp2RE1_bx.SetBinContent(counterDp2RE1,self.getMeanValueDisk(histoname_bx)[2])
                        hDp2RE1_bx.SetBinError(counterDp2RE1,self.getMeanValueDisk(histoname_bx)[3])
                        hDp2RE1_bx.GetXaxis().SetBinLabel(counterDp2RE1,name_roll)

                        name_roll = name + "_C"
                        counterDp2RE1+=1
                        
                        if self.getMediaDisk(histoname_Eff)[2] != -100:
                            hDp2RE1_eff.SetBinContent(counterDp2RE1,self.getMediaDisk(histoname_Eff)[2])
                            hDp2RE1_eff.SetBinError(counterDp2RE1,self.getMediaDisk(histoname_Eff)[3])
                        else:
                            hDp2RE1_eff.SetBinContent(counterDp2RE1,0)
                            hDp2RE1_eff.SetBinError(counterDp2RE1,0)
                                
                        hDp2RE1_eff.GetXaxis().SetBinLabel(counterDp2RE1,name_roll)

                        if self.getMediaDisk(histoname_Eff_STA)[2] != -100:
                            hDp2RE1_eff_STA.SetBinContent(counterDp2RE1,self.getMediaDisk(histoname_Eff_STA)[2])
                            hDp2RE1_eff_STA.SetBinError(counterDp2RE1,self.getMediaDisk(histoname_Eff_STA)[3])
                        else:
                            hDp2RE1_eff_STA.SetBinContent(counterDp2RE1,0)
                            hDp2RE1_eff_STA.SetBinError(counterDp2RE1,0)

                        hDp2RE1_eff_STA.GetXaxis().SetBinLabel(counterDp2RE1,name_roll)

                        hDp2RE1_masked.SetBinContent(counterDp2RE1,self.getMaskedStripDisk(histoname_occ)[1])
                        hDp2RE1_masked.GetXaxis().SetBinLabel(counterDp2RE1,name_roll)
                        hDp2RE1_bx.SetBinContent(counterDp2RE1,self.getMeanValueDisk(histoname_bx)[2])
                        hDp2RE1_bx.SetBinError(counterDp2RE1,self.getMeanValueDisk(histoname_bx)[3])
                        hDp2RE1_bx.GetXaxis().SetBinLabel(counterDp2RE1,name_roll)

##-------------------------------- RE +1 -----------------------------------------------------------------
                
                if el == "RE+1":
                    hDp1_masked.Fill(self.getMaskedStripDisk(histoname_occ)[0])
                    hDp1_masked.Fill(self.getMaskedStripDisk(histoname_occ)[1])
                    hDp1_masked.Fill(self.getMaskedStripDisk(histoname_occ)[2])
                    hDp1_eff.Fill(self.getMediaDisk(histoname_Eff)[0])
                    hDp1_eff.Fill(self.getMediaDisk(histoname_Eff)[2])                   
                    hDp1_eff.Fill(self.getMediaDisk(histoname_Eff)[4])
                    hDp1_eff_STA.Fill(self.getMediaDisk(histoname_Eff_STA)[0])
                    hDp1_eff_STA.Fill(self.getMediaDisk(histoname_Eff_STA)[2])
                    hDp1_eff_STA.Fill(self.getMediaDisk(histoname_Eff_STA)[4])


                    if coord1[0] == "R3":
                        name_roll = name + "_A"
                        counterDp1RE3+=1

                        if self.getMediaDisk(histoname_Eff)[0] != -100:
                            hDp1RE3_eff.SetBinContent(counterDp1RE3,self.getMediaDisk(histoname_Eff)[0])
                            hDp1RE3_eff.SetBinError(counterDp1RE3,self.getMediaDisk(histoname_Eff)[1])
                        else:
                            hDp1RE3_eff.SetBinContent(counterDp1RE3,0)
                            hDp1RE3_eff.SetBinError(counterDp1RE3,0)
                            
                        hDp1RE3_eff.GetXaxis().SetBinLabel(counterDp1RE3,name_roll)

                        if self.getMediaDisk(histoname_Eff_STA)[0] != -100:
                            hDp1RE3_eff_STA.SetBinContent(counterDp1RE3,self.getMediaDisk(histoname_Eff_STA)[0])
                            hDp1RE3_eff_STA.SetBinError(counterDp1RE3,self.getMediaDisk(histoname_Eff_STA)[1])
                        else:
                            hDp1RE3_eff_STA.SetBinContent(counterDp1RE3,0)
                            hDp1RE3_eff_STA.SetBinError(counterDp1RE3,0)

                        hDp1RE3_eff_STA.GetXaxis().SetBinLabel(counterDp1RE3,name_roll)

                        hDp1RE3_masked.SetBinContent(counterDp1RE3,self.getMaskedStripDisk(histoname_occ)[0])
                        hDp1RE3_masked.GetXaxis().SetBinLabel(counterDp1RE3,name_roll)
                        hDp1RE3_bx.SetBinContent(counterDp1RE3,self.getMeanValueDisk(histoname_bx)[0])
                        hDp1RE3_bx.SetBinError(counterDp1RE3,self.getMeanValueDisk(histoname_bx)[1])
                        hDp1RE3_bx.GetXaxis().SetBinLabel(counterDp1RE3,name_roll)
                        
                        name_roll = name + "_B"
                        counterDp1RE3+=1
                        
                        if self.getMediaDisk(histoname_Eff)[2] != -100:
                            hDp1RE3_eff.SetBinContent(counterDp1RE3,self.getMediaDisk(histoname_Eff)[2])
                            hDp1RE3_eff.SetBinError(counterDp1RE3,self.getMediaDisk(histoname_Eff)[3])
                        else:
                            hDp1RE3_eff.SetBinContent(counterDp1RE3,0)
                            hDp1RE3_eff.SetBinError(counterDp1RE3,0)
                                
                        hDp1RE3_eff.GetXaxis().SetBinLabel(counterDp1RE3,name_roll)

                        if self.getMediaDisk(histoname_Eff_STA)[2] != -100:
                            hDp1RE3_eff_STA.SetBinContent(counterDp1RE3,self.getMediaDisk(histoname_Eff_STA)[2])
                            hDp1RE3_eff_STA.SetBinError(counterDp1RE3,self.getMediaDisk(histoname_Eff_STA)[3])
                        else:
                            hDp1RE3_eff_STA.SetBinContent(counterDp1RE3,0)
                            hDp1RE3_eff_STA.SetBinError(counterDp1RE3,0)

                        hDp1RE3_eff_STA.GetXaxis().SetBinLabel(counterDp1RE3,name_roll)

                        hDp1RE3_masked.SetBinContent(counterDp1RE3,self.getMaskedStripDisk(histoname_occ)[1])
                        hDp1RE3_masked.GetXaxis().SetBinLabel(counterDp1RE3,name_roll)
                        hDp1RE3_bx.SetBinContent(counterDp1RE3,self.getMeanValueDisk(histoname_bx)[2])
                        hDp1RE3_bx.SetBinError(counterDp1RE3,self.getMeanValueDisk(histoname_bx)[3])
                        hDp1RE3_bx.GetXaxis().SetBinLabel(counterDp1RE3,name_roll)

                        name_roll = name + "_C"
                        counterDp1RE3+=1
                        
                        if self.getMediaDisk(histoname_Eff)[2] != -100:
                            hDp1RE3_eff.SetBinContent(counterDp1RE3,self.getMediaDisk(histoname_Eff)[2])
                            hDp1RE3_eff.SetBinError(counterDp1RE3,self.getMediaDisk(histoname_Eff)[3])
                        else:
                            hDp1RE3_eff.SetBinContent(counterDp1RE3,0)
                            hDp1RE3_eff.SetBinError(counterDp1RE3,0)
                                
                        hDp1RE3_eff.GetXaxis().SetBinLabel(counterDp1RE3,name_roll)

                        if self.getMediaDisk(histoname_Eff_STA)[2] != -100:
                            hDp1RE3_eff_STA.SetBinContent(counterDp1RE3,self.getMediaDisk(histoname_Eff_STA)[2])
                            hDp1RE3_eff_STA.SetBinError(counterDp1RE3,self.getMediaDisk(histoname_Eff_STA)[3])
                        else:
                            hDp1RE3_eff_STA.SetBinContent(counterDp1RE3,0)
                            hDp1RE3_eff_STA.SetBinError(counterDp1RE3,0)

                        hDp1RE3_eff.GetXaxis().SetBinLabel(counterDp1RE3,name_roll)

                        hDp1RE3_masked.SetBinContent(counterDp1RE3,self.getMaskedStripDisk(histoname_occ)[1])
                        hDp1RE3_masked.GetXaxis().SetBinLabel(counterDp1RE3,name_roll)
                        hDp1RE3_bx.SetBinContent(counterDp1RE3,self.getMeanValueDisk(histoname_bx)[2])
                        hDp1RE3_bx.SetBinError(counterDp1RE3,self.getMeanValueDisk(histoname_bx)[3])
                        hDp1RE3_bx.GetXaxis().SetBinLabel(counterDp1RE3,name_roll)

                    if coord1[0] == "R2":
                        name_roll = name + "_A"
                        counterDp1RE2+=1

                        if self.getMediaDisk(histoname_Eff)[0] != -100:
                            hDp1RE2_eff.SetBinContent(counterDp1RE2,self.getMediaDisk(histoname_Eff)[0])
                            hDp1RE2_eff.SetBinError(counterDp1RE2,self.getMediaDisk(histoname_Eff)[1])
                        else:
                            hDp1RE2_eff.SetBinContent(counterDp1RE2,0)
                            hDp1RE2_eff.SetBinError(counterDp1RE2,0)
                            
                        hDp1RE2_eff.GetXaxis().SetBinLabel(counterDp1RE2,name_roll)

                        if self.getMediaDisk(histoname_Eff_STA)[0] != -100:
                            hDp1RE2_eff_STA.SetBinContent(counterDp1RE2,self.getMediaDisk(histoname_Eff_STA)[0])
                            hDp1RE2_eff_STA.SetBinError(counterDp1RE2,self.getMediaDisk(histoname_Eff_STA)[1])
                        else:
                            hDp1RE2_eff_STA.SetBinContent(counterDp1RE2,0)
                            hDp1RE2_eff_STA.SetBinError(counterDp1RE2,0)

                        hDp1RE2_eff_STA.GetXaxis().SetBinLabel(counterDp1RE2,name_roll)

                        hDp1RE2_masked.SetBinContent(counterDp1RE2,self.getMaskedStripDisk(histoname_occ)[0])
                        hDp1RE2_masked.GetXaxis().SetBinLabel(counterDp1RE2,name_roll)
                        hDp1RE2_bx.SetBinContent(counterDp1RE2,self.getMeanValueDisk(histoname_bx)[0])
                        hDp1RE2_bx.SetBinError(counterDp1RE2,self.getMeanValueDisk(histoname_bx)[1])
                        hDp1RE2_bx.GetXaxis().SetBinLabel(counterDp1RE2,name_roll)
                        
                        name_roll = name + "_B"
                        counterDp1RE2+=1
                        
                        if self.getMediaDisk(histoname_Eff)[2] != -100:
                            hDp1RE2_eff.SetBinContent(counterDp1RE2,self.getMediaDisk(histoname_Eff)[2])
                            hDp1RE2_eff.SetBinError(counterDp1RE2,self.getMediaDisk(histoname_Eff)[3])
                        else:
                            hDp1RE2_eff.SetBinContent(counterDp1RE2,0)
                            hDp1RE2_eff.SetBinError(counterDp1RE2,0)
                                
                        hDp1RE2_eff.GetXaxis().SetBinLabel(counterDp1RE2,name_roll)

                        if self.getMediaDisk(histoname_Eff_STA)[2] != -100:
                            hDp1RE2_eff_STA.SetBinContent(counterDp1RE2,self.getMediaDisk(histoname_Eff_STA)[2])
                            hDp1RE2_eff_STA.SetBinError(counterDp1RE2,self.getMediaDisk(histoname_Eff_STA)[3])
                        else:
                            hDp1RE2_eff_STA.SetBinContent(counterDp1RE2,0)
                            hDp1RE2_eff_STA.SetBinError(counterDp1RE2,0)

                        hDp1RE2_eff_STA.GetXaxis().SetBinLabel(counterDp1RE2,name_roll)

                        hDp1RE2_masked.SetBinContent(counterDp1RE2,self.getMaskedStripDisk(histoname_occ)[1])
                        hDp1RE2_masked.GetXaxis().SetBinLabel(counterDp1RE2,name_roll)
                        hDp1RE2_bx.SetBinContent(counterDp1RE2,self.getMeanValueDisk(histoname_bx)[2])
                        hDp1RE2_bx.SetBinError(counterDp1RE2,self.getMeanValueDisk(histoname_bx)[3])
                        hDp1RE2_bx.GetXaxis().SetBinLabel(counterDp1RE2,name_roll)

                        name_roll = name + "_C"
                        counterDp1RE2+=1
                        
                        if self.getMediaDisk(histoname_Eff)[2] != -100:
                            hDp1RE2_eff.SetBinContent(counterDp1RE2,self.getMediaDisk(histoname_Eff)[2])
                            hDp1RE2_eff.SetBinError(counterDp1RE2,self.getMediaDisk(histoname_Eff)[3])
                        else:
                            hDp1RE2_eff.SetBinContent(counterDp1RE2,0)
                            hDp1RE2_eff.SetBinError(counterDp1RE2,0)
                                
                        hDp1RE2_eff.GetXaxis().SetBinLabel(counterDp1RE2,name_roll)

                        if self.getMediaDisk(histoname_Eff_STA)[2] != -100:
                            hDp1RE2_eff_STA.SetBinContent(counterDp1RE2,self.getMediaDisk(histoname_Eff_STA)[2])
                            hDp1RE2_eff_STA.SetBinError(counterDp1RE2,self.getMediaDisk(histoname_Eff_STA)[3])
                        else:
                            hDp1RE2_eff_STA.SetBinContent(counterDp1RE2,0)
                            hDp1RE2_eff_STA.SetBinError(counterDp1RE2,0)

                        hDp1RE2_eff_STA.GetXaxis().SetBinLabel(counterDp1RE2,name_roll)

                        hDp1RE2_masked.SetBinContent(counterDp1RE2,self.getMaskedStripDisk(histoname_occ)[1])
                        hDp1RE2_masked.GetXaxis().SetBinLabel(counterDp1RE2,name_roll)
                        hDp1RE2_bx.SetBinContent(counterDp1RE2,self.getMeanValueDisk(histoname_bx)[2])
                        hDp1RE2_bx.SetBinError(counterDp1RE2,self.getMeanValueDisk(histoname_bx)[3])
                        hDp1RE2_bx.GetXaxis().SetBinLabel(counterDp1RE2,name_roll)

                    if coord1[0] == "R1":
                        name_roll = name + "_A"
                        counterDp1RE1+=1

                        if self.getMediaDisk(histoname_Eff)[0] != -100:
                            hDp1RE1_eff.SetBinContent(counterDp1RE1,self.getMediaDisk(histoname_Eff)[0])
                            hDp1RE1_eff.SetBinError(counterDp1RE1,self.getMediaDisk(histoname_Eff)[1])
                        else:
                            hDp1RE1_eff.SetBinContent(counterDp1RE1,0)
                            hDp1RE1_eff.SetBinError(counterDp1RE1,0)
                            
                        hDp1RE1_eff.GetXaxis().SetBinLabel(counterDp1RE1,name_roll)

                        if self.getMediaDisk(histoname_Eff_STA)[0] != -100:
                            hDp1RE1_eff_STA.SetBinContent(counterDp1RE1,self.getMediaDisk(histoname_Eff_STA)[0])
                            hDp1RE1_eff_STA.SetBinError(counterDp1RE1,self.getMediaDisk(histoname_Eff_STA)[1])
                        else:
                            hDp1RE1_eff_STA.SetBinContent(counterDp1RE1,0)
                            hDp1RE1_eff_STA.SetBinError(counterDp1RE1,0)

                        hDp1RE1_eff_STA.GetXaxis().SetBinLabel(counterDp1RE1,name_roll)

                        hDp1RE1_masked.SetBinContent(counterDp1RE1,self.getMaskedStripDisk(histoname_occ)[0])
                        hDp1RE1_masked.GetXaxis().SetBinLabel(counterDp1RE1,name_roll)
                        hDp1RE1_bx.SetBinContent(counterDp1RE1,self.getMeanValueDisk(histoname_bx)[0])
                        hDp1RE1_bx.SetBinError(counterDp1RE1,self.getMeanValueDisk(histoname_bx)[1])
                        hDp1RE1_bx.GetXaxis().SetBinLabel(counterDp1RE1,name_roll)
                        
                        name_roll = name + "_B"
                        counterDp1RE1+=1
                        
                        if self.getMediaDisk(histoname_Eff)[2] != -100:
                            hDp1RE1_eff.SetBinContent(counterDp1RE1,self.getMediaDisk(histoname_Eff)[2])
                            hDp1RE1_eff.SetBinError(counterDp1RE1,self.getMediaDisk(histoname_Eff)[3])
                        else:
                            hDp1RE1_eff.SetBinContent(counterDp1RE1,0)
                            hDp1RE1_eff.SetBinError(counterDp1RE1,0)
                                
                        hDp1RE1_eff.GetXaxis().SetBinLabel(counterDp1RE1,name_roll)

                        if self.getMediaDisk(histoname_Eff_STA)[2] != -100:
                            hDp1RE1_eff_STA.SetBinContent(counterDp1RE1,self.getMediaDisk(histoname_Eff_STA)[2])
                            hDp1RE1_eff_STA.SetBinError(counterDp1RE1,self.getMediaDisk(histoname_Eff_STA)[3])
                        else:
                            hDp1RE1_eff_STA.SetBinContent(counterDp1RE1,0)
                            hDp1RE1_eff_STA.SetBinError(counterDp1RE1,0)

                        hDp1RE1_eff_STA.GetXaxis().SetBinLabel(counterDp1RE1,name_roll)

                        hDp1RE1_masked.SetBinContent(counterDp1RE1,self.getMaskedStripDisk(histoname_occ)[1])
                        hDp1RE1_masked.GetXaxis().SetBinLabel(counterDp1RE1,name_roll)
                        hDp1RE1_bx.SetBinContent(counterDp1RE1,self.getMeanValueDisk(histoname_bx)[2])
                        hDp1RE1_bx.SetBinError(counterDp1RE1,self.getMeanValueDisk(histoname_bx)[3])
                        hDp1RE1_bx.GetXaxis().SetBinLabel(counterDp1RE1,name_roll)

                        name_roll = name + "_C"
                        counterDp1RE1+=1
                        
                        if self.getMediaDisk(histoname_Eff)[2] != -100:
                            hDp1RE1_eff.SetBinContent(counterDp1RE1,self.getMediaDisk(histoname_Eff)[2])
                            hDp1RE1_eff.SetBinError(counterDp1RE1,self.getMediaDisk(histoname_Eff)[3])
                        else:
                            hDp1RE1_eff.SetBinContent(counterDp1RE1,0)
                            hDp1RE1_eff.SetBinError(counterDp1RE1,0)
                                
                        hDp1RE1_eff.GetXaxis().SetBinLabel(counterDp1RE1,name_roll)

                        if self.getMediaDisk(histoname_Eff_STA)[2] != -100:
                            hDp1RE1_eff_STA.SetBinContent(counterDp1RE1,self.getMediaDisk(histoname_Eff_STA)[2])
                            hDp1RE1_eff_STA.SetBinError(counterDp1RE1,self.getMediaDisk(histoname_Eff_STA)[3])
                        else:
                            hDp1RE1_eff_STA.SetBinContent(counterDp1RE1,0)
                            hDp1RE1_eff_STA.SetBinError(counterDp1RE1,0)

                        hDp1RE1_eff_STA.GetXaxis().SetBinLabel(counterDp1RE1,name_roll)

                        hDp1RE1_masked.SetBinContent(counterDp1RE1,self.getMaskedStripDisk(histoname_occ)[1])
                        hDp1RE1_masked.GetXaxis().SetBinLabel(counterDp1RE1,name_roll)
                        hDp1RE1_bx.SetBinContent(counterDp1RE1,self.getMeanValueDisk(histoname_bx)[2])
                        hDp1RE1_bx.SetBinError(counterDp1RE1,self.getMeanValueDisk(histoname_bx)[3])
                        hDp1RE1_bx.GetXaxis().SetBinLabel(counterDp1RE1,name_roll)
                        
        self.NewRootFile.cd()

##-------------------------- W-2 -------------------------------------------------
##_near_
##      c_wheel_m2_near = TCanvas("c_wheel_m2_near", "Wheel -2 near",4,25,1445,490)
        c_wheel_m2_near = TCanvas("c_wheel_m2_near", "Wheel -2 near",23,91,1247,400)

        c_wheel_m2_near.SetHighLightColor(2)
        c_wheel_m2_near.Range(-10.26568,-73.24462,111.695,124.805)
        c_wheel_m2_near.SetFillColor(0)
        c_wheel_m2_near.SetBorderMode(0)
        c_wheel_m2_near.SetBorderSize(2)
        c_wheel_m2_near.SetLeftMargin(0.084172)
        c_wheel_m2_near.SetRightMargin(0.05489479)
        c_wheel_m2_near.SetBottomMargin(0.3698297)
        c_wheel_m2_near.SetFrameBorderMode(0)
        c_wheel_m2_near.SetFrameBorderMode(0)

        hWm2Near_eff.SetMaximum(100)
        hWm2Near_eff.SetMinimum(-0.1)
        hWm2Near_eff.SetMarkerColor(1)
        hWm2Near_eff.SetMarkerStyle(22)
        hWm2Near_eff.GetXaxis().SetLabelFont(32)
        hWm2Near_eff.GetXaxis().SetTitleFont(32)
        hWm2Near_eff.GetYaxis().SetTitle("%")
        hWm2Near_eff.GetYaxis().SetLabelFont(32)
        hWm2Near_eff.GetYaxis().SetTitleFont(32)

        hWm2Near_eff.Draw()

        hWm2Near_eff_STA.SetMarkerColor(kBlue) ##
        hWm2Near_eff_STA.SetMarkerStyle(22) ##
        hWm2Near_eff_STA.Draw("same") ##
        hWm2Near_masked.Draw("same")
        c_wheel_m2_near.Update()

        hWm2Near_masked.Draw("same")
        c_wheel_m2_near.Update()

        hWm2Near_bx.SetMarkerColor(ROOT.kRed)
        hWm2Near_bx.SetMarkerStyle(23)
        scale = 110./21.
        hWm2Near_bx.SetLineColor(ROOT.kRed)
        hWm2Near_bx.Scale(scale)
        hWm2Near_bx.Draw("same")
        htemp = hWm2Near_eff.Clone()
        for k in range(htemp.GetNbinsX()+1):
            if k <=100: htemp.SetBinContent(k,scale*10)
        hWm2Near_bx.Add(htemp)

        htemp_STA = hWm2Near_eff_STA.Clone() ##
        for k in range(htemp_STA.GetNbinsX()+1): ##
            if k <= 100: ##
                htemp_STA.SetBinContent(k,scale*10) ##

        axis = TGaxis(ROOT.gPad.GetUxmax(),ROOT.gPad.GetUymin(),ROOT.gPad.GetUxmax(), ROOT.gPad.GetUymax(),-10.,10,510,"+L")
        axis.SetLineColor(ROOT.kRed)
        axis.SetLabelColor(ROOT.kRed)
        axis.SetLabelOffset(0.005)
        axis.SetLabelSize(0.04)
        axis.SetTickSize(0.03)
        axis.SetGridLength(0)
        axis.SetTitleOffset(1)
        axis.SetTitleSize(0.04)
        axis.SetTitleColor(1)
        axis.SetTitleFont(62)

        axis.Draw();
        c_wheel_m2_near.Write()
        c_wheel_m2_near.SaveAs(path+"run"+run+"_c_wheel_m2_near.gif")

##_Far_
##      c_wheel_m2_Far = TCanvas("c_wheel_m2_Far", "Wheel -2 Far",4,25,1445,490)
        c_wheel_m2_Far = TCanvas("c_wheel_m2_Far", "Wheel -2 Far",23,91,1247,400)
        c_wheel_m2_Far.SetHighLightColor(2)
        c_wheel_m2_Far.Range(-10.26568,-73.24462,111.695,124.805)
        c_wheel_m2_Far.SetFillColor(0)
        c_wheel_m2_Far.SetBorderMode(0)
        c_wheel_m2_Far.SetBorderSize(2)
        c_wheel_m2_Far.SetLeftMargin(0.084172)
        c_wheel_m2_Far.SetRightMargin(0.05489479)
        c_wheel_m2_Far.SetBottomMargin(0.3698297)
        c_wheel_m2_Far.SetFrameBorderMode(0)
        c_wheel_m2_Far.SetFrameBorderMode(0)

        hWm2Far_eff.SetMaximum(100)
        hWm2Far_eff.SetMinimum(-0.1)
        hWm2Far_eff.SetMarkerColor(1)
        hWm2Far_eff.SetMarkerStyle(22)
        hWm2Far_eff.GetXaxis().SetLabelFont(32)
        hWm2Far_eff.GetXaxis().SetTitleFont(32)
        hWm2Far_eff.GetYaxis().SetTitle("%")
        hWm2Far_eff.GetYaxis().SetLabelFont(32)
        hWm2Far_eff.GetYaxis().SetTitleFont(32)

        hWm2Far_eff.Draw()

        hWm2Far_eff_STA.SetMarkerColor(kBlue) ##
        hWm2Far_eff_STA.SetMarkerStyle(22) ##
        hWm2Far_eff_STA.Draw("same") ##
        hWm2Far_masked.Draw("same")
        c_wheel_m2_Far.Update()

        hWm2Far_bx.SetMarkerColor(ROOT.kRed)
        hWm2Far_bx.SetMarkerStyle(23)
        scale = 110./21.
        hWm2Far_bx.SetLineColor(ROOT.kRed)
        hWm2Far_bx.Scale(scale)
        hWm2Far_bx.Draw("same")

        htemp = hWm2Far_eff.Clone()
        for k in range(htemp.GetNbinsX()+1):
            if k <= 104:
                htemp.SetBinContent(k,scale*10)
        hWm2Far_bx.Add(htemp)

        htemp_STA = hWm2Far_eff_STA.Clone() ##
        for k in range(htemp_STA.GetNbinsX()+1): ##
            if k <= 104: ##
                htemp_STA.SetBinContent(k,scale*10) ##

        axis = TGaxis(ROOT.gPad.GetUxmax(),ROOT.gPad.GetUymin(),ROOT.gPad.GetUxmax(), ROOT.gPad.GetUymax(),-10.,10,510,"+L")
        axis.SetLineColor(ROOT.kRed)
        axis.SetLabelColor(ROOT.kRed)
        axis.SetLabelOffset(0.005)
        axis.SetLabelSize(0.04)
        axis.SetTickSize(0.03)
        axis.SetGridLength(0)
        axis.SetTitleOffset(1)
        axis.SetTitleSize(0.04)
        axis.SetTitleColor(1)
        axis.SetTitleFont(62)

        axis.Draw();
        c_wheel_m2_Far.Write()
        c_wheel_m2_Far.SaveAs(path+"run"+run+"_c_wheel_m2_Far.gif")
        
##------------------------- W-1 ------------------------------------------------------------------------------------------
        
##      c_wheel_m1_near = TCanvas("c_wheel_m1_near", "Wheel -1 near",4,25,1445,490)
        c_wheel_m1_near = TCanvas("c_wheel_m1_near", "Wheel -1 near",23,91,1247,400)

        c_wheel_m1_near.SetHighLightColor(2)
        c_wheel_m1_near.Range(-10.26568,-73.24462,111.695,124.805)
        c_wheel_m1_near.SetFillColor(0)
        c_wheel_m1_near.SetBorderMode(0)
        c_wheel_m1_near.SetBorderSize(2)
        c_wheel_m1_near.SetLeftMargin(0.084172)
        c_wheel_m1_near.SetRightMargin(0.05489479)
        c_wheel_m1_near.SetBottomMargin(0.3698297)
        c_wheel_m1_near.SetFrameBorderMode(0)
        c_wheel_m1_near.SetFrameBorderMode(0)

        hWm1Near_eff.SetMaximum(100)
        hWm1Near_eff.SetMinimum(-0.1)
        hWm1Near_eff.SetMarkerColor(1)
        hWm1Near_eff.SetMarkerStyle(22)
        hWm1Near_eff.GetXaxis().SetLabelFont(32)
        hWm1Near_eff.GetXaxis().SetTitleFont(32)
        hWm1Near_eff.GetYaxis().SetTitle("%")
        hWm1Near_eff.GetYaxis().SetLabelFont(32)
        hWm1Near_eff.GetYaxis().SetTitleFont(32)

        hWm1Near_eff.Draw()

        hWm1Near_eff_STA.SetMarkerColor(kBlue) ##
        hWm1Near_eff_STA.SetMarkerStyle(22) ##
        hWm1Near_eff_STA.Draw("same") ##
        hWm1Near_masked.Draw("same")
        c_wheel_m1_near.Update()

        hWm1Near_masked.Draw("same")
        c_wheel_m1_near.Update()

        hWm1Near_bx.SetMarkerColor(ROOT.kRed)
        hWm1Near_bx.SetMarkerStyle(23)
        scale = 110./21.
        hWm1Near_bx.SetLineColor(ROOT.kRed)
        hWm1Near_bx.Scale(scale)
        hWm1Near_bx.Draw("same")
        htemp = hWm1Near_eff.Clone()
        for k in range(htemp.GetNbinsX()+1):
            if k <=100: htemp.SetBinContent(k,scale*10)
        hWm1Near_bx.Add(htemp)

        htemp_STA = hWm1Near_eff_STA.Clone() ##
        for k in range(htemp_STA.GetNbinsX()+1): ##
            if k <= 100: ##
                htemp_STA.SetBinContent(k,scale*10) ##
        
        axis = TGaxis(ROOT.gPad.GetUxmax(),ROOT.gPad.GetUymin(),ROOT.gPad.GetUxmax(), ROOT.gPad.GetUymax(),-10.,10,510,"+L")
        axis.SetLineColor(ROOT.kRed)
        axis.SetLabelColor(ROOT.kRed)
        axis.SetLabelOffset(0.005)
        axis.SetLabelSize(0.04)
        axis.SetTickSize(0.03)
        axis.SetGridLength(0)
        axis.SetTitleOffset(1)
        axis.SetTitleSize(0.04)
        axis.SetTitleColor(1)
        axis.SetTitleFont(62)

        axis.Draw();
        c_wheel_m1_near.Write()
        c_wheel_m1_near.SaveAs(path+"run"+run+"_c_wheel_m1_near.gif")

##      c_wheel_m1_Far = TCanvas("c_wheel_m1_Far", "Wheel -1 Far",4,25,1445,490)
        c_wheel_m1_Far = TCanvas("c_wheel_m1_Far", "Wheel -1 Far",23,91,1247,400)
        c_wheel_m1_Far.SetHighLightColor(2)
        c_wheel_m1_Far.Range(-10.26568,-73.24462,111.695,124.805)
        c_wheel_m1_Far.SetFillColor(0)
        c_wheel_m1_Far.SetBorderMode(0)
        c_wheel_m1_Far.SetBorderSize(2)
        c_wheel_m1_Far.SetLeftMargin(0.084172)
        c_wheel_m1_Far.SetRightMargin(0.05489479)
        c_wheel_m1_Far.SetBottomMargin(0.3698297)
        c_wheel_m1_Far.SetFrameBorderMode(0)
        c_wheel_m1_Far.SetFrameBorderMode(0)

        hWm1Far_eff.SetMaximum(100)
        hWm1Far_eff.SetMinimum(-0.1)
        hWm1Far_eff.SetMarkerColor(1)
        hWm1Far_eff.SetMarkerStyle(22)
        hWm1Far_eff.GetXaxis().SetLabelFont(32)
        hWm1Far_eff.GetXaxis().SetTitleFont(32)
        hWm1Far_eff.GetYaxis().SetTitle("%")
        hWm1Far_eff.GetYaxis().SetLabelFont(32)
        hWm1Far_eff.GetYaxis().SetTitleFont(32)

        hWm1Far_eff.Draw()

        hWm1Far_eff_STA.SetMarkerColor(kBlue) ##
        hWm1Far_eff_STA.SetMarkerStyle(22) ##
        hWm1Far_eff_STA.Draw("same") ##
        hWm1Far_masked.Draw("same")
        c_wheel_m1_Far.Update()

        hWm1Far_bx.SetMarkerColor(ROOT.kRed)
        hWm1Far_bx.SetMarkerStyle(23)
        scale = 110./21.
        hWm1Far_bx.SetLineColor(ROOT.kRed)
        hWm1Far_bx.Scale(scale)
        hWm1Far_bx.Draw("same")
        htemp = hWm1Far_eff.Clone()

        for k in range(htemp.GetNbinsX()+1):
            if k <= 104:
                htemp.SetBinContent(k,scale*10)
        hWm1Far_bx.Add(htemp)

        htemp_STA = hWm1Far_eff_STA.Clone() ##
        for k in range(htemp_STA.GetNbinsX()+1): ##
            if k <= 104: ##
                htemp_STA.SetBinContent(k,scale*10) ##
            
        axis = TGaxis(ROOT.gPad.GetUxmax(),ROOT.gPad.GetUymin(),ROOT.gPad.GetUxmax(), ROOT.gPad.GetUymax(),-10.,10,510,"+L")
        axis.SetLineColor(ROOT.kRed)
        axis.SetLabelColor(ROOT.kRed)
        axis.SetLabelOffset(0.005)
        axis.SetLabelSize(0.04)
        axis.SetTickSize(0.03)
        axis.SetGridLength(0)
        axis.SetTitleOffset(1)
        axis.SetTitleSize(0.04)
        axis.SetTitleColor(1)
        axis.SetTitleFont(62)

        axis.Draw();
        c_wheel_m1_Far.Write()
        c_wheel_m1_Far.SaveAs(path+"run"+run+"_c_wheel_m1_Far.gif")
        
##----------------------------- W 0 -----------------------------------------------------------
        
##      c_wheel_0_near = TCanvas("c_wheel_0_near", "Wheel 0 near",4,25,1445,490)
        c_wheel_0_near = TCanvas("c_wheel_0_near", "Wheel 0 near",23,91,1247,400)
        c_wheel_0_near.SetHighLightColor(2)
        c_wheel_0_near.Range(-10.26568,-73.24462,111.695,124.805)
        c_wheel_0_near.SetFillColor(0)
        c_wheel_0_near.SetBorderMode(0)
        c_wheel_0_near.SetBorderSize(2)
        c_wheel_0_near.SetLeftMargin(0.084172)
        c_wheel_0_near.SetRightMargin(0.05489479)
        c_wheel_0_near.SetBottomMargin(0.3698297)
        c_wheel_0_near.SetFrameBorderMode(0)
        c_wheel_0_near.SetFrameBorderMode(0)

        hW0Near_eff.SetMaximum(100)
        hW0Near_eff.SetMinimum(-0.1)
        hW0Near_eff.SetMarkerColor(1)
        hW0Near_eff.SetMarkerStyle(22)
        hW0Near_eff.GetXaxis().SetLabelFont(32)
        hW0Near_eff.GetXaxis().SetTitleFont(32)
        hW0Near_eff.GetYaxis().SetTitle("%")
        hW0Near_eff.GetYaxis().SetLabelFont(32)
        hW0Near_eff.GetYaxis().SetTitleFont(32)

        hW0Near_eff.Draw()
        hW0Near_eff_STA.SetMarkerColor(kBlue) ##
        hW0Near_eff_STA.SetMarkerStyle(22) ##
        hW0Near_eff_STA.Draw("same") ##
        hW0Near_masked.Draw("same")
        c_wheel_0_near.Update()

        hW0Near_bx.SetMarkerColor(ROOT.kRed)
        hW0Near_bx.SetMarkerStyle(23)
        scale = 110./21.
        hW0Near_bx.SetLineColor(ROOT.kRed)
        hW0Near_bx.Scale(scale)
        hW0Near_bx.Draw("same")
        htemp = hW0Near_eff.Clone()
        for k in range(htemp.GetNbinsX()+1):
            if k <=100: htemp.SetBinContent(k,scale*10)
        hW0Near_bx.Add(htemp)

        htemp_STA = hW0Near_eff_STA.Clone() ##
        for k in range(htemp_STA.GetNbinsX()+1): ##
            if k <= 100: ##
                htemp_STA.SetBinContent(k,scale*10) ##
        
        axis = TGaxis(ROOT.gPad.GetUxmax(),ROOT.gPad.GetUymin(),ROOT.gPad.GetUxmax(), ROOT.gPad.GetUymax(),-10.,10,510,"+L")
        axis.SetLineColor(ROOT.kRed)
        axis.SetLabelColor(ROOT.kRed)
        axis.SetLabelOffset(0.005)
        axis.SetLabelSize(0.04)
        axis.SetTickSize(0.03)
        axis.SetGridLength(0)
        axis.SetTitleOffset(1)
        axis.SetTitleSize(0.04)
        axis.SetTitleColor(1)
        axis.SetTitleFont(62)

        axis.Draw();
        c_wheel_0_near.Write()
        c_wheel_0_near.SaveAs(path+"run"+run+"_c_wheel_0_near.gif")

##      c_wheel_0_Far = TCanvas("c_wheel_0_Far", "Wheel 0 Far",4,25,1445,490)
        c_wheel_0_Far = TCanvas("c_wheel_0_Far", "Wheel 0 Far",23,91,1247,400)
        c_wheel_0_Far.SetHighLightColor(2)
        c_wheel_0_Far.Range(-10.26568,-73.24462,111.695,124.805)
        c_wheel_0_Far.SetFillColor(0)
        c_wheel_0_Far.SetBorderMode(0)
        c_wheel_0_Far.SetBorderSize(2)
        c_wheel_0_Far.SetLeftMargin(0.084172)
        c_wheel_0_Far.SetRightMargin(0.05489479)
        c_wheel_0_Far.SetBottomMargin(0.3698297)
        c_wheel_0_Far.SetFrameBorderMode(0)
        c_wheel_0_Far.SetFrameBorderMode(0)

        hW0Far_eff.SetMaximum(100)
        hW0Far_eff.SetMinimum(-0.1)
        hW0Far_eff.SetMarkerColor(1)
        hW0Far_eff.SetMarkerStyle(22)
        hW0Far_eff.GetXaxis().SetLabelFont(32)
        hW0Far_eff.GetXaxis().SetTitleFont(32)
        hW0Far_eff.GetYaxis().SetTitle("%")
        hW0Far_eff.GetYaxis().SetLabelFont(32)
        hW0Far_eff.GetYaxis().SetTitleFont(32)

        hW0Far_eff.Draw()
        hW0Far_eff_STA.SetMarkerColor(kBlue) ##
        hW0Far_eff_STA.SetMarkerStyle(22) ##
        hW0Far_eff_STA.Draw("same") ##
        hW0Far_masked.Draw("same")
        c_wheel_0_Far.Update()

        hW0Far_bx.SetMarkerColor(ROOT.kRed)
        hW0Far_bx.SetMarkerStyle(23)
        scale = 110./21.
        hW0Far_bx.SetLineColor(ROOT.kRed)
        hW0Far_bx.Scale(scale)
        hW0Far_bx.Draw("same")
        htemp = hW0Far_eff.Clone()

        for k in range(htemp.GetNbinsX()+1):
            if k <=104:
                htemp.SetBinContent(k,scale*10)
        hW0Far_bx.Add(htemp)

        htemp_STA = hW0Far_eff_STA.Clone() ##
        for k in range(htemp_STA.GetNbinsX()+1): ##
            if k <=104: ##
                htemp_STA.SetBinContent(k,scale*10) ##
            
        axis = TGaxis(ROOT.gPad.GetUxmax(),ROOT.gPad.GetUymin(),ROOT.gPad.GetUxmax(), ROOT.gPad.GetUymax(),-10.,10,510,"+L")
        axis.SetLineColor(ROOT.kRed)
        axis.SetLabelColor(ROOT.kRed)
        axis.SetLabelOffset(0.005)
        axis.SetLabelSize(0.04)
        axis.SetTickSize(0.03)
        axis.SetGridLength(0)
        axis.SetTitleOffset(1)
        axis.SetTitleSize(0.04)
        axis.SetTitleColor(1)
        axis.SetTitleFont(62)

        axis.Draw();
        c_wheel_0_Far.Write()
        c_wheel_0_Far.SaveAs(path+"run"+run+"_c_wheel_0_Far.gif")
        
##-------------------------------------- W+1 -------------------------------------------------------------------

##      c_wheel_p1_near = TCanvas("c_wheel_p1_near", "Wheel +1 near",4,25,1445,490)
        c_wheel_p1_near = TCanvas("c_wheel_p1_near", "Wheel +1 near",23,91,1247,400)
        c_wheel_p1_near.SetHighLightColor(2)
        c_wheel_p1_near.Range(-10.26568,-73.24462,111.695,124.805)
        c_wheel_p1_near.SetFillColor(0)
        c_wheel_p1_near.SetBorderMode(0)
        c_wheel_p1_near.SetBorderSize(2)
        c_wheel_p1_near.SetLeftMargin(0.084172)
        c_wheel_p1_near.SetRightMargin(0.05489479)
        c_wheel_p1_near.SetBottomMargin(0.3698297)
        c_wheel_p1_near.SetFrameBorderMode(0)
        c_wheel_p1_near.SetFrameBorderMode(0)

        hWp1Near_eff.SetMaximum(100)
        hWp1Near_eff.SetMinimum(-0.1)
        hWp1Near_eff.SetMarkerColor(1)
        hWp1Near_eff.SetMarkerStyle(22)
        hWp1Near_eff.GetXaxis().SetLabelFont(32)
        hWp1Near_eff.GetXaxis().SetTitleFont(32)
        hWp1Near_eff.GetYaxis().SetTitle("%")
        hWp1Near_eff.GetYaxis().SetLabelFont(32)
        hWp1Near_eff.GetYaxis().SetTitleFont(32)

        hWp1Near_eff.Draw()
        hWp1Near_eff_STA.SetMarkerColor(kBlue) ##
        hWp1Near_eff_STA.SetMarkerStyle(22) ##
        hWp1Near_eff_STA.Draw("same") ##
        hWp1Near_masked.Draw("same")
        c_wheel_p1_near.Update()

        hWp1Near_bx.SetMarkerColor(ROOT.kRed)
        hWp1Near_bx.SetMarkerStyle(23)
        scale = 110./21.
        hWp1Near_bx.SetLineColor(ROOT.kRed)
        hWp1Near_bx.Scale(scale)
        hWp1Near_bx.Draw("same")

        htemp = hWp1Near_eff.Clone()
        for k in range(htemp.GetNbinsX()+1):
            if k <=100: htemp.SetBinContent(k,scale*10)
        hWp1Near_bx.Add(htemp)

        htemp_STA = hWp1Near_eff_STA.Clone() ##
        for k in range(htemp_STA.GetNbinsX()+1): ##
            if k <= 100: ##
                htemp_STA.SetBinContent(k,scale*10) ##
        
        axis = TGaxis(ROOT.gPad.GetUxmax(),ROOT.gPad.GetUymin(),ROOT.gPad.GetUxmax(), ROOT.gPad.GetUymax(),-10.,10,510,"+L")
        axis.SetLineColor(ROOT.kRed)
        axis.SetLabelColor(ROOT.kRed)
        axis.SetLabelOffset(0.005)
        axis.SetLabelSize(0.04)
        axis.SetTickSize(0.03)
        axis.SetGridLength(0)
        axis.SetTitleOffset(1)
        axis.SetTitleSize(0.04)
        axis.SetTitleColor(1)
        axis.SetTitleFont(62)

        axis.Draw();
        c_wheel_p1_near.Write()
        c_wheel_p1_near.SaveAs(path+"run"+run+"_c_wheel_p1_near.gif")

##      c_wheel_p1_Far = TCanvas("c_wheel_p1_Far", "Wheel +1 Far",4,25,1445,490)
        c_wheel_p1_Far = TCanvas("c_wheel_p1_Far", "Wheel +1 Far",23,91,1247,400)
        c_wheel_p1_Far.SetHighLightColor(2)
        c_wheel_p1_Far.Range(-10.26568,-73.24462,111.695,124.805)
        c_wheel_p1_Far.SetFillColor(0)
        c_wheel_p1_Far.SetBorderMode(0)
        c_wheel_p1_Far.SetBorderSize(2)
        c_wheel_p1_Far.SetLeftMargin(0.084172)
        c_wheel_p1_Far.SetRightMargin(0.05489479)
        c_wheel_p1_Far.SetBottomMargin(0.3698297)
        c_wheel_p1_Far.SetFrameBorderMode(0)
        c_wheel_p1_Far.SetFrameBorderMode(0)

        hWp1Far_eff.SetMaximum(100)
        hWp1Far_eff.SetMinimum(-0.1)
        hWp1Far_eff.SetMarkerColor(1)
        hWp1Far_eff.SetMarkerStyle(22)
        hWp1Far_eff.GetXaxis().SetLabelFont(32)
        hWp1Far_eff.GetXaxis().SetTitleFont(32)
        hWp1Far_eff.GetYaxis().SetTitle("%")
        hWp1Far_eff.GetYaxis().SetLabelFont(32)
        hWp1Far_eff.GetYaxis().SetTitleFont(32)

        hWp1Far_eff.Draw()
        hWp1Far_eff_STA.SetMarkerColor(kBlue) ##
        hWp1Far_eff_STA.SetMarkerStyle(22) ##
        hWp1Far_eff_STA.Draw("same") ##
        hWp1Far_masked.Draw("same")
        c_wheel_p1_Far.Update()

        hWp1Far_bx.SetMarkerColor(ROOT.kRed)
        hWp1Far_bx.SetMarkerStyle(23)
        scale = 110./21.
        hWp1Far_bx.SetLineColor(ROOT.kRed)
        hWp1Far_bx.Scale(scale)
        hWp1Far_bx.Draw("same")

        htemp = hWp1Far_eff.Clone()

        for k in range(htemp.GetNbinsX()+1):
            if k <= 104:
                htemp.SetBinContent(k,scale*10)
        hWp1Far_bx.Add(htemp)

        htemp_STA = hWp1Far_eff_STA.Clone() ##
        for k in range(htemp_STA.GetNbinsX()+1): ##
            if k <= 104: ##
                htemp_STA.SetBinContent(k,scale*10) ##
            
        axis = TGaxis(ROOT.gPad.GetUxmax(),ROOT.gPad.GetUymin(),ROOT.gPad.GetUxmax(),ROOT.gPad.GetUymax(),-10.,10,510,"+L")
        axis.SetLineColor(ROOT.kRed)
        axis.SetLabelColor(ROOT.kRed)
        axis.SetLabelOffset(0.005)
        axis.SetLabelSize(0.04)
        axis.SetTickSize(0.03)
        axis.SetGridLength(0)
        axis.SetTitleOffset(1)
        axis.SetTitleSize(0.04)
        axis.SetTitleColor(1)
        axis.SetTitleFont(62)

        axis.Draw();
        c_wheel_p1_Far.Write()        
        c_wheel_p1_Far.SaveAs(path+"run"+run+"_c_wheel_p1_Far.gif")
        
##----------------------------------------- W+2 ----------------------------------------------------------------------------

##      c_wheel_p2_near = TCanvas("c_wheel_p2_near", "Wheel +2 near",4,25,1445,490)
        c_wheel_p2_near = TCanvas("c_wheel_p2_near", "Wheel +2 near",23,91,1247,400)
        c_wheel_p2_near.SetHighLightColor(2)
        c_wheel_p2_near.Range(-10.26568,-73.24462,111.695,124.805)
        c_wheel_p2_near.SetFillColor(0)
        c_wheel_p2_near.SetBorderMode(0)
        c_wheel_p2_near.SetBorderSize(2)
        c_wheel_p2_near.SetLeftMargin(0.084172)
        c_wheel_p2_near.SetRightMargin(0.05489479)
        c_wheel_p2_near.SetBottomMargin(0.3698297)
        c_wheel_p2_near.SetFrameBorderMode(0)
        c_wheel_p2_near.SetFrameBorderMode(0)

        hWp2Near_eff.SetMaximum(100)
        hWp2Near_eff.SetMinimum(-0.1)
        hWp2Near_eff.SetMarkerColor(1)
        hWp2Near_eff.SetMarkerStyle(22)
        hWp2Near_eff.GetXaxis().SetLabelFont(32)
        hWp2Near_eff.GetXaxis().SetTitleFont(32)
        hWp2Near_eff.GetYaxis().SetTitle("%")
        hWp2Near_eff.GetYaxis().SetLabelFont(32)
        hWp2Near_eff.GetYaxis().SetTitleFont(32)

        hWp2Near_eff.Draw()

        hWp2Near_eff_STA.SetMarkerColor(ROOT.kBlue) ##
        hWp2Near_eff_STA.SetMarkerStyle(22) ##
        hWp2Near_eff_STA.Draw("same") ##
        hWp2Near_masked.Draw("same")
        c_wheel_p2_near.Update()

        hWp2Near_bx.SetMarkerColor(ROOT.kRed)
        hWp2Near_bx.SetMarkerStyle(23)
        scale = 110./21.
        hWp2Near_bx.SetLineColor(ROOT.kRed)
        hWp2Near_bx.Scale(scale)
        hWp2Near_bx.Draw("same")

        htemp = hWp2Near_eff.Clone()
        for k in range(htemp.GetNbinsX()+1):
            if k <= 100: htemp.SetBinContent(k,scale*10)
        hWp2Near_bx.Add(htemp)
         
        htemp_STA = hWp2Near_eff_STA.Clone()
        for k in range(htemp_STA.GetNbinsX()+1):
            if k <= 100: htemp_STA.SetBinContent(k,scale*10)

        axis = TGaxis(ROOT.gPad.GetUxmax(),ROOT.gPad.GetUymin(),ROOT.gPad.GetUxmax(), ROOT.gPad.GetUymax(),-10.,10,510,"+L")
        axis.SetLineColor(ROOT.kRed)
        axis.SetLabelColor(ROOT.kRed)
        axis.SetLabelOffset(0.005)
        axis.SetLabelSize(0.04)
        axis.SetTickSize(0.03)
        axis.SetGridLength(0)
        axis.SetTitleOffset(1)
        axis.SetTitleSize(0.04)
        axis.SetTitleColor(1)
        axis.SetTitleFont(62)

        axis.Draw();
        c_wheel_p2_near.Write()
        c_wheel_p2_near.SaveAs(path+"run"+run+"_c_wheel_p2_near.gif")

##      c_wheel_p2_Far = TCanvas("c_wheel_p2_Far", "Wheel +2 Far",4,25,1445,490)
        c_wheel_p2_Far = TCanvas("c_wheel_p2_Far", "Wheel +2 Far",23,91,1247,400)
        c_wheel_p2_Far.SetHighLightColor(2)
        c_wheel_p2_Far.Range(-10.26568,-73.24462,111.695,124.805)
        c_wheel_p2_Far.SetFillColor(0)
        c_wheel_p2_Far.SetBorderMode(0)
        c_wheel_p2_Far.SetBorderSize(2)
        c_wheel_p2_Far.SetLeftMargin(0.084172)
        c_wheel_p2_Far.SetRightMargin(0.05489479)
        c_wheel_p2_Far.SetBottomMargin(0.3698297)
        c_wheel_p2_Far.SetFrameBorderMode(0)
        c_wheel_p2_Far.SetFrameBorderMode(0)

        hWp2Far_eff.SetMaximum(100)
        hWp2Far_eff.SetMinimum(-0.1)
        hWp2Far_eff.SetMarkerColor(1)
        hWp2Far_eff.SetMarkerStyle(22)
        hWp2Far_eff.GetXaxis().SetLabelFont(32)
        hWp2Far_eff.GetXaxis().SetTitleFont(32)
        hWp2Far_eff.GetYaxis().SetTitle("%")
        hWp2Far_eff.GetYaxis().SetLabelFont(32)
        hWp2Far_eff.GetYaxis().SetTitleFont(32)

        hWp2Far_eff.Draw()

        hWp2Far_eff_STA.SetMarkerColor(ROOT.kBlue) ##
        hWp2Far_eff_STA.SetMarkerStyle(22) ##
        hWp2Far_eff_STA.Draw("same") ##
        hWp2Far_masked.Draw("same")
        c_wheel_p2_Far.Update()

        hWp2Far_bx.SetMarkerColor(ROOT.kRed)
        hWp2Far_bx.SetMarkerStyle(23)
        scale = 110./21.
        hWp2Far_bx.SetLineColor(ROOT.kRed)
        hWp2Far_bx.Scale(scale)
        hWp2Far_bx.Draw("same")

        htemp = hWp2Far_eff.Clone()
        for k in range(htemp.GetNbinsX()+1):
            if k <= 104: ##
                htemp.SetBinContent(k,scale*10)
        hWp2Far_bx.Add(htemp)
        htemp_STA = hWp2Far_eff_STA.Clone()
        for k in range(htemp_STA.GetNbinsX()+1):
            if k <= 104: htemp_STA.SetBinContent(k,scale*10) ##

        axis = TGaxis(ROOT.gPad.GetUxmax(),ROOT.gPad.GetUymin(),ROOT.gPad.GetUxmax(),ROOT.gPad.GetUymax(),-10.,10.,510,"+L")
        axis.SetLineColor(ROOT.kRed)
        axis.SetLabelColor(ROOT.kRed)
        axis.SetLabelOffset(0.005)
        axis.SetLabelSize(0.04)
        axis.SetTickSize(0.03)
        axis.SetGridLength(0)
        axis.SetTitleOffset(1)
        axis.SetTitleSize(0.04)
        axis.SetTitleColor(1)
        axis.SetTitleFont(62)

        axis.Draw();
        c_wheel_p2_Far.Write()        
        c_wheel_p2_Far.SaveAs(path+"run"+run+"_c_wheel_p2_Far.gif")

##--------------------------------  RE -3 -----------------------------------------------------------------

##      c_disk_m3_RE3 = TCanvas("c_disk_m3_RE3", "Disk -3 RE3",4,25,1445,490)
        c_disk_m3_RE3 = TCanvas("c_disk_m3_RE3", "Disk -3 RE3",23,91,1247,400)
        c_disk_m3_RE3.SetHighLightColor(2)
        c_disk_m3_RE3.Range(-10.26568,-73.24462,111.695,124.805)
        c_disk_m3_RE3.SetFillColor(0)
        c_disk_m3_RE3.SetBorderMode(0)
        c_disk_m3_RE3.SetBorderSize(2)
        c_disk_m3_RE3.SetLeftMargin(0.084172)
        c_disk_m3_RE3.SetRightMargin(0.05489479)
        c_disk_m3_RE3.SetBottomMargin(0.3698297)
        c_disk_m3_RE3.SetFrameBorderMode(0)
        c_disk_m3_RE3.SetFrameBorderMode(0)

        hDm3RE3_eff.SetMaximum(100)
        hDm3RE3_eff.SetMinimum(-0.1)
        hDm3RE3_eff.SetMarkerColor(1)
        hDm3RE3_eff.SetMarkerStyle(22)
        hDm3RE3_eff.GetXaxis().SetLabelFont(32)
        hDm3RE3_eff.GetXaxis().SetTitleFont(32)
        hDm3RE3_eff.GetYaxis().SetTitle("%")
        hDm3RE3_eff.GetYaxis().SetLabelFont(32)
        hDm3RE3_eff.GetYaxis().SetTitleFont(32)

        hDm3RE3_eff.Draw()

        hDm3RE3_eff_STA.SetMarkerColor(ROOT.kBlue) ##
        hDm3RE3_eff_STA.SetMarkerStyle(22) ##
        hDm3RE3_eff_STA.Draw("same") ##
        hDm3RE3_masked.Draw("same")
        c_disk_m3_RE3.Update()

        hDm3RE3_bx.SetMarkerColor(ROOT.kRed)
        hDm3RE3_bx.SetMarkerStyle(23)
        scale = 110./21.
        hDm3RE3_bx.SetLineColor(ROOT.kRed)
        hDm3RE3_bx.Scale(scale)
        hDm3RE3_bx.Draw("same")

        htemp = hDm3RE3_eff.Clone()
        for k in range(htemp.GetNbinsX()+1):
            if k <= 108: htemp.SetBinContent(k,scale*10)
        hDm3RE3_bx.Add(htemp)

        htemp_STA = hDm3RE3_eff_STA.Clone()
        for k in range(htemp_STA.GetNbinsX()+1):
            if k <= 108: htemp_STA.SetBinContent(k,scale*10)

        axis = TGaxis(ROOT.gPad.GetUxmax(),ROOT.gPad.GetUymin(),ROOT.gPad.GetUxmax(), ROOT.gPad.GetUymax(),-10.,10,510,"+L")
        axis.SetLineColor(ROOT.kRed)
        axis.SetLabelColor(ROOT.kRed)
        axis.SetLabelOffset(0.005)
        axis.SetLabelSize(0.04)
        axis.SetTickSize(0.03)
        axis.SetGridLength(0)
        axis.SetTitleOffset(1)
        axis.SetTitleSize(0.04)
        axis.SetTitleColor(1)
        axis.SetTitleFont(62)

        axis.Draw();
        c_disk_m3_RE3.Write()
        c_disk_m3_RE3.SaveAs(path+"run"+run+"_c_disk_m3_RE3.gif")

##      c_disk_m3_RE2 = TCanvas("c_disk_m3_RE2", "Disk -3 RE2",4,25,1445,490)
        c_disk_m3_RE2 = TCanvas("c_disk_m3_RE2", "Disk -3 RE2",23,91,1247,400)
        c_disk_m3_RE2.SetHighLightColor(2)
        c_disk_m3_RE2.Range(-10.26568,-73.24462,111.695,124.805)
        c_disk_m3_RE2.SetFillColor(0)
        c_disk_m3_RE2.SetBorderMode(0)
        c_disk_m3_RE2.SetBorderSize(2)
        c_disk_m3_RE2.SetLeftMargin(0.084172)
        c_disk_m3_RE2.SetRightMargin(0.05489479)
        c_disk_m3_RE2.SetBottomMargin(0.3698297)
        c_disk_m3_RE2.SetFrameBorderMode(0)
        c_disk_m3_RE2.SetFrameBorderMode(0)

        hDm3RE2_eff.SetMaximum(100) 
        hDm3RE2_eff.SetMinimum(-0.1)
        hDm3RE2_eff.SetMarkerColor(1)
        hDm3RE2_eff.SetMarkerStyle(22)
        hDm3RE2_eff.GetXaxis().SetLabelFont(32)
        hDm3RE2_eff.GetXaxis().SetTitleFont(32)
        hDm3RE2_eff.GetYaxis().SetTitle("%")
        hDm3RE2_eff.GetYaxis().SetLabelFont(32)
        hDm3RE2_eff.GetYaxis().SetTitleFont(32)

        hDm3RE2_eff.Draw()
        hDm3RE2_eff_STA.SetMarkerColor(ROOT.kBlue) ##
        hDm3RE2_eff_STA.SetMarkerStyle(22) ##
        hDm3RE2_eff_STA.Draw("same") ##
        hDm3RE2_masked.Draw("same")
        c_disk_m3_RE2.Update()

        hDm3RE2_bx.SetMarkerColor(ROOT.kRed)
        hDm3RE2_bx.SetMarkerStyle(23)
        scale = 110./21.
        hDm3RE2_bx.SetLineColor(ROOT.kRed)
        hDm3RE2_bx.Scale(scale)
        hDm3RE2_bx.Draw("same")

        htemp = hDm3RE2_eff.Clone()
        for k in range(htemp.GetNbinsX()+1):
            if k <=108: htemp.SetBinContent(k,scale*10)
        hDm3RE2_bx.Add(htemp)

        htemp_STA = hDm3RE2_eff_STA.Clone()
        for k in range(htemp_STA.GetNbinsX()+1):
            if k <=108: htemp_STA.SetBinContent(k,scale*10)

        axis = TGaxis(ROOT.gPad.GetUxmax(),ROOT.gPad.GetUymin(),ROOT.gPad.GetUxmax(), ROOT.gPad.GetUymax(),-10.,10,510,"+L")
        axis.SetLineColor(ROOT.kRed)
        axis.SetLabelColor(ROOT.kRed)
        axis.SetLabelOffset(0.005)
        axis.SetLabelSize(0.04)
        axis.SetTickSize(0.03)
        axis.SetGridLength(0)
        axis.SetTitleOffset(1)
        axis.SetTitleSize(0.04)
        axis.SetTitleColor(1)
        axis.SetTitleFont(62)

        axis.Draw();
        c_disk_m3_RE2.Write()
        c_disk_m3_RE2.SaveAs(path+"run"+run+"_c_disk_m3_RE2.gif")

##      c_disk_m3_RE1 = TCanvas("c_disk_m3_RE1", "Disk -3 RE1",4,25,1445,490)
        c_disk_m3_RE1 = TCanvas("c_disk_m3_RE1", "Disk -3 RE1",23,91,1247,400)
        c_disk_m3_RE1.SetHighLightColor(2)
        c_disk_m3_RE1.Range(-10.26568,-73.24462,111.695,124.805)
        c_disk_m3_RE1.SetFillColor(0)
        c_disk_m3_RE1.SetBorderMode(0)
        c_disk_m3_RE1.SetBorderSize(2)
        c_disk_m3_RE1.SetLeftMargin(0.084172)
        c_disk_m3_RE1.SetRightMargin(0.05489479)
        c_disk_m3_RE1.SetBottomMargin(0.3698297)
        c_disk_m3_RE1.SetFrameBorderMode(0)
        c_disk_m3_RE1.SetFrameBorderMode(0)

        hDm3RE1_eff.SetMaximum(100)
        hDm3RE1_eff.SetMinimum(-0.1)
        hDm3RE1_eff.SetMarkerColor(1)
        hDm3RE1_eff.SetMarkerStyle(22)
        hDm3RE1_eff.GetXaxis().SetLabelFont(32)
        hDm3RE1_eff.GetXaxis().SetTitleFont(32)
        hDm3RE1_eff.GetYaxis().SetTitle("%")
        hDm3RE1_eff.GetYaxis().SetLabelFont(32)
        hDm3RE1_eff.GetYaxis().SetTitleFont(32)

        hDm3RE1_eff.Draw()

        hDm3RE1_eff_STA.SetMarkerColor(ROOT.kBlue) ##
        hDm3RE1_eff_STA.SetMarkerStyle(22) ##
        hDm3RE1_eff_STA.Draw("same") ##
        hDm3RE1_masked.Draw("same")
        c_disk_m3_RE1.Update()

        hDm3RE1_bx.SetMarkerColor(ROOT.kRed)
        hDm3RE1_bx.SetMarkerStyle(23)
        scale = 110./21.
        hDm3RE1_bx.SetLineColor(ROOT.kRed)
        hDm3RE1_bx.Scale(scale)
        hDm3RE1_bx.Draw("same")

        htemp = hDm3RE1_eff.Clone()
        for k in range(htemp.GetNbinsX()+1):
            if k <=108: htemp.SetBinContent(k,scale*10)
        hDm3RE1_bx.Add(htemp)

        htemp_STA = hDm3RE1_eff_STA.Clone()
        for k in range(htemp_STA.GetNbinsX()+1):
            if k <=108: htemp_STA.SetBinContent(k,scale*10)

        axis = TGaxis(ROOT.gPad.GetUxmax(),ROOT.gPad.GetUymin(),ROOT.gPad.GetUxmax(), ROOT.gPad.GetUymax(),-10.,10,510,"+L")
        axis.SetLineColor(ROOT.kRed)
        axis.SetLabelColor(ROOT.kRed)
        axis.SetLabelOffset(0.005)
        axis.SetLabelSize(0.04)
        axis.SetTickSize(0.03)
        axis.SetGridLength(0)
        axis.SetTitleOffset(1)
        axis.SetTitleSize(0.04)
        axis.SetTitleColor(1)
        axis.SetTitleFont(62)

        axis.Draw();
        c_disk_m3_RE1.Write()
        c_disk_m3_RE1.SaveAs(path+"run"+run+"_c_disk_m3_RE1.gif")

##------------------------------------ RE -2 ----------------------------------------------------------

##      c_disk_m2_RE3 = TCanvas("c_disk_m2_RE3", "Disk -2 RE3",4,25,1445,490)
        c_disk_m2_RE3 = TCanvas("c_disk_m2_RE3", "Disk -2 RE3",23,91,1247,400)
        c_disk_m2_RE3.SetHighLightColor(2)
        c_disk_m2_RE3.Range(-10.26568,-73.24462,111.695,124.805)
        c_disk_m2_RE3.SetFillColor(0)
        c_disk_m2_RE3.SetBorderMode(0)
        c_disk_m2_RE3.SetBorderSize(2)
        c_disk_m2_RE3.SetLeftMargin(0.084172)
        c_disk_m2_RE3.SetRightMargin(0.05489479)
        c_disk_m2_RE3.SetBottomMargin(0.3698297)
        c_disk_m2_RE3.SetFrameBorderMode(0)
        c_disk_m2_RE3.SetFrameBorderMode(0)

        hDm2RE3_eff.SetMaximum(100)
        hDm2RE3_eff.SetMinimum(-0.1)
        hDm2RE3_eff.SetMarkerColor(1)
        hDm2RE3_eff.SetMarkerStyle(22)
        hDm2RE3_eff.GetXaxis().SetLabelFont(32)
        hDm2RE3_eff.GetXaxis().SetTitleFont(32)
        hDm2RE3_eff.GetYaxis().SetTitle("%")
        hDm2RE3_eff.GetYaxis().SetLabelFont(32)
        hDm2RE3_eff.GetYaxis().SetTitleFont(32)

        hDm2RE3_eff.Draw()

        hDm2RE3_eff_STA.SetMarkerColor(ROOT.kBlue) ##
        hDm2RE3_eff_STA.SetMarkerStyle(22) ##
        hDm2RE3_eff_STA.Draw("same") ##
        hDm2RE3_masked.Draw("same")
        c_disk_m2_RE3.Update()

        hDm2RE3_bx.SetMarkerColor(ROOT.kRed)
        hDm2RE3_bx.SetMarkerStyle(23)
        scale = 110./21.
        hDm2RE3_bx.SetLineColor(ROOT.kRed)
        hDm2RE3_bx.Scale(scale)
        hDm2RE3_bx.Draw("same")

        htemp = hDm2RE3_eff.Clone()
        for k in range(htemp.GetNbinsX()+1):
            if k <=108: htemp.SetBinContent(k,scale*10)
        hDm2RE3_bx.Add(htemp)

        htemp_STA = hDm2RE3_eff_STA.Clone()
        for k in range(htemp_STA.GetNbinsX()+1):
            if k <=108: htemp_STA.SetBinContent(k,scale*10)

        axis = TGaxis(ROOT.gPad.GetUxmax(),ROOT.gPad.GetUymin(),ROOT.gPad.GetUxmax(), ROOT.gPad.GetUymax(),-10.,10,510,"+L")
        axis.SetLineColor(ROOT.kRed)
        axis.SetLabelColor(ROOT.kRed)
        axis.SetLabelOffset(0.005)
        axis.SetLabelSize(0.04)
        axis.SetTickSize(0.03)
        axis.SetGridLength(0)
        axis.SetTitleOffset(1)
        axis.SetTitleSize(0.04)
        axis.SetTitleColor(1)
        axis.SetTitleFont(62)

        axis.Draw();
        c_disk_m2_RE3.Write()
        c_disk_m2_RE3.SaveAs(path+"run"+run+"_c_disk_m2_RE3.gif")

##      c_disk_m2_RE2 = TCanvas("c_disk_m2_RE2", "Disk -2 RE2",4,25,1445,490)
        c_disk_m2_RE2 = TCanvas("c_disk_m2_RE2", "Disk -2 RE2",23,91,1247,400)
        c_disk_m2_RE2.SetHighLightColor(2)
        c_disk_m2_RE2.Range(-10.26568,-73.24462,111.695,124.805)
        c_disk_m2_RE2.SetFillColor(0)
        c_disk_m2_RE2.SetBorderMode(0)
        c_disk_m2_RE2.SetBorderSize(2)
        c_disk_m2_RE2.SetLeftMargin(0.084172)
        c_disk_m2_RE2.SetRightMargin(0.05489479)
        c_disk_m2_RE2.SetBottomMargin(0.3698297)
        c_disk_m2_RE2.SetFrameBorderMode(0)
        c_disk_m2_RE2.SetFrameBorderMode(0)

        hDm2RE2_eff.SetMaximum(100)
        hDm2RE2_eff.SetMinimum(-0.1)
        hDm2RE2_eff.SetMarkerColor(1)
        hDm2RE2_eff.SetMarkerStyle(22)
        hDm2RE2_eff.GetXaxis().SetLabelFont(32)
        hDm2RE2_eff.GetXaxis().SetTitleFont(32)
        hDm2RE2_eff.GetYaxis().SetTitle("%")
        hDm2RE2_eff.GetYaxis().SetLabelFont(32)
        hDm2RE2_eff.GetYaxis().SetTitleFont(32)

        hDm2RE2_eff.Draw()

        hDm2RE2_eff_STA.SetMarkerColor(ROOT.kBlue) ##
        hDm2RE2_eff_STA.SetMarkerStyle(22) ##
        hDm2RE2_eff_STA.Draw("same") ##
        hDm2RE2_masked.Draw("same")
        c_disk_m2_RE2.Update()

        hDm2RE2_bx.SetMarkerColor(ROOT.kRed)
        hDm2RE2_bx.SetMarkerStyle(23)
        scale = 110./21.
        hDm2RE2_bx.SetLineColor(ROOT.kRed)
        hDm2RE2_bx.Scale(scale)
        hDm2RE2_bx.Draw("same")
        htemp = hDm2RE2_eff.Clone()
        for k in range(htemp.GetNbinsX()+1):
            if k <=108: htemp.SetBinContent(k,scale*10)
        hDm2RE2_bx.Add(htemp)

        htemp_STA = hDm2RE2_eff_STA.Clone()
        for k in range(htemp_STA.GetNbinsX()+1):
            if k <=108: htemp_STA.SetBinContent(k,scale*10)

        axis = TGaxis(ROOT.gPad.GetUxmax(),ROOT.gPad.GetUymin(),ROOT.gPad.GetUxmax(), ROOT.gPad.GetUymax(),-10.,10,510,"+L")
        axis.SetLineColor(ROOT.kRed)
        axis.SetLabelColor(ROOT.kRed)
        axis.SetLabelOffset(0.005)
        axis.SetLabelSize(0.04)
        axis.SetTickSize(0.03)
        axis.SetGridLength(0)
        axis.SetTitleOffset(1)
        axis.SetTitleSize(0.04)
        axis.SetTitleColor(1)
        axis.SetTitleFont(62)

        axis.Draw();
        c_disk_m2_RE2.Write()
        c_disk_m2_RE2.SaveAs(path+"run"+run+"_c_disk_m2_RE2.gif")

##      c_disk_m2_RE1 = TCanvas("c_disk_m2_RE1", "Disk -2 RE1",4,25,1445,490)
        c_disk_m2_RE1 = TCanvas("c_disk_m2_RE1", "Disk -2 RE1",23,91,1247,400)
        c_disk_m2_RE1.SetHighLightColor(2)
        c_disk_m2_RE1.Range(-10.26568,-73.24462,111.695,124.805)
        c_disk_m2_RE1.SetFillColor(0)
        c_disk_m2_RE1.SetBorderMode(0)
        c_disk_m2_RE1.SetBorderSize(2)
        c_disk_m2_RE1.SetLeftMargin(0.084172)
        c_disk_m2_RE1.SetRightMargin(0.05489479)
        c_disk_m2_RE1.SetBottomMargin(0.3698297)
        c_disk_m2_RE1.SetFrameBorderMode(0)
        c_disk_m2_RE1.SetFrameBorderMode(0)

        hDm2RE1_eff.SetMaximum(100)
        hDm2RE1_eff.SetMinimum(-0.1)
        hDm2RE1_eff.SetMarkerColor(1)
        hDm2RE1_eff.SetMarkerStyle(22)
        hDm2RE1_eff.GetXaxis().SetLabelFont(32)
        hDm2RE1_eff.GetXaxis().SetTitleFont(32)
        hDm2RE1_eff.GetYaxis().SetTitle("%")
        hDm2RE1_eff.GetYaxis().SetLabelFont(32)
        hDm2RE1_eff.GetYaxis().SetTitleFont(32)

        hDm2RE1_eff.Draw()

        hDm2RE1_eff_STA.SetMarkerColor(ROOT.kBlue) ##
        hDm2RE1_eff_STA.SetMarkerStyle(22) ##
        hDm2RE1_eff_STA.Draw("same") ##
        hDm2RE1_masked.Draw("same")
        c_disk_m2_RE1.Update()

        hDm2RE1_bx.SetMarkerColor(ROOT.kRed)
        hDm2RE1_bx.SetMarkerStyle(23)
        scale = 110./21.
        hDm2RE1_bx.SetLineColor(ROOT.kRed)
        hDm2RE1_bx.Scale(scale)
        hDm2RE1_bx.Draw("same")

        htemp = hDm2RE1_eff.Clone()
        for k in range(htemp.GetNbinsX()+1):
            if k <=108: htemp.SetBinContent(k,scale*10)
        hDm2RE1_bx.Add(htemp)

        htemp_STA = hDm2RE1_eff_STA.Clone()
        for k in range(htemp_STA.GetNbinsX()+1):
            if k <=108: htemp_STA.SetBinContent(k,scale*10)

        axis = TGaxis(ROOT.gPad.GetUxmax(),ROOT.gPad.GetUymin(),ROOT.gPad.GetUxmax(), ROOT.gPad.GetUymax(),-10.,10,510,"+L")
        axis.SetLineColor(ROOT.kRed)
        axis.SetLabelColor(ROOT.kRed)
        axis.SetLabelOffset(0.005)
        axis.SetLabelSize(0.04)
        axis.SetTickSize(0.03)
        axis.SetGridLength(0)
        axis.SetTitleOffset(1)
        axis.SetTitleSize(0.04)
        axis.SetTitleColor(1)
        axis.SetTitleFont(62)

        axis.Draw();
        c_disk_m2_RE1.Write()
        c_disk_m2_RE1.SaveAs(path+"run"+run+"_c_disk_m2_RE1.gif")

##------------------------------------ RE -1 ----------------------------------------------------------

##      c_disk_m1_RE3 = TCanvas("c_disk_m1_RE3", "Disk -1 RE3",4,25,1445,490)
        c_disk_m1_RE3 = TCanvas("c_disk_m1_RE3", "Disk -1 RE3",23,91,1247,400)
        c_disk_m1_RE3.SetHighLightColor(2)
        c_disk_m1_RE3.Range(-10.26568,-73.24462,111.695,124.805)
        c_disk_m1_RE3.SetFillColor(0)
        c_disk_m1_RE3.SetBorderMode(0)
        c_disk_m1_RE3.SetBorderSize(2)
        c_disk_m1_RE3.SetLeftMargin(0.084172)
        c_disk_m1_RE3.SetRightMargin(0.05489479)
        c_disk_m1_RE3.SetBottomMargin(0.3698297)
        c_disk_m1_RE3.SetFrameBorderMode(0)
        c_disk_m1_RE3.SetFrameBorderMode(0)

        hDm1RE3_eff.SetMaximum(100)
        hDm1RE3_eff.SetMinimum(-0.1)
        hDm1RE3_eff.SetMarkerColor(1)
        hDm1RE3_eff.SetMarkerStyle(22)
        hDm1RE3_eff.GetXaxis().SetLabelFont(32)
        hDm1RE3_eff.GetXaxis().SetTitleFont(32)
        hDm1RE3_eff.GetYaxis().SetTitle("%")
        hDm1RE3_eff.GetYaxis().SetLabelFont(32)
        hDm1RE3_eff.GetYaxis().SetTitleFont(32)

        hDm1RE3_eff.Draw()

        hDm1RE3_eff_STA.SetMarkerColor(ROOT.kBlue) ##
        hDm1RE3_eff_STA.SetMarkerStyle(22) ##
        hDm1RE3_eff_STA.Draw("same") ##
        hDm1RE3_masked.Draw("same")
        c_disk_m1_RE3.Update()

        hDm1RE3_bx.SetMarkerColor(ROOT.kRed)
        hDm1RE3_bx.SetMarkerStyle(23)
        scale = 110./21.
        hDm1RE3_bx.SetLineColor(ROOT.kRed)
        hDm1RE3_bx.Scale(scale)
        hDm1RE3_bx.Draw("same")

        htemp = hDm1RE3_eff.Clone()
        for k in range(htemp.GetNbinsX()+1):
            if k <=108: htemp.SetBinContent(k,scale*10)
        hDm1RE3_bx.Add(htemp)

        htemp_STA = hDm1RE3_eff_STA.Clone()
        for k in range(htemp_STA.GetNbinsX()+1):
            if k <=108: htemp_STA.SetBinContent(k,scale*10)

        axis = TGaxis(ROOT.gPad.GetUxmax(),ROOT.gPad.GetUymin(),ROOT.gPad.GetUxmax(), ROOT.gPad.GetUymax(),-10.,10,510,"+L")
        axis.SetLineColor(ROOT.kRed)
        axis.SetLabelColor(ROOT.kRed)
        axis.SetLabelOffset(0.005)
        axis.SetLabelSize(0.04)
        axis.SetTickSize(0.03)
        axis.SetGridLength(0)
        axis.SetTitleOffset(1)
        axis.SetTitleSize(0.04)
        axis.SetTitleColor(1)
        axis.SetTitleFont(62)

        axis.Draw();
        c_disk_m1_RE3.Write()
        c_disk_m1_RE3.SaveAs(path+"run"+run+"_c_disk_m1_RE3.gif")

##      c_disk_m1_RE2 = TCanvas("c_disk_m1_RE2", "Disk -1 RE2",4,25,1445,490)
        c_disk_m1_RE2 = TCanvas("c_disk_m1_RE2", "Disk -1 RE2",23,91,1247,400)
        c_disk_m1_RE2.SetHighLightColor(2)
        c_disk_m1_RE2.Range(-10.26568,-73.24462,111.695,124.805)
        c_disk_m1_RE2.SetFillColor(0)
        c_disk_m1_RE2.SetBorderMode(0)
        c_disk_m1_RE2.SetBorderSize(2)
        c_disk_m1_RE2.SetLeftMargin(0.084172)
        c_disk_m1_RE2.SetRightMargin(0.05489479)
        c_disk_m1_RE2.SetBottomMargin(0.3698297)
        c_disk_m1_RE2.SetFrameBorderMode(0)
        c_disk_m1_RE2.SetFrameBorderMode(0)

        hDm1RE2_eff.SetMaximum(100)
        hDm1RE2_eff.SetMinimum(-0.1)
        hDm1RE2_eff.SetMarkerColor(1)
        hDm1RE2_eff.SetMarkerStyle(22)
        hDm1RE2_eff.GetXaxis().SetLabelFont(32)
        hDm1RE2_eff.GetXaxis().SetTitleFont(32)
        hDm1RE2_eff.GetYaxis().SetTitle("%")
        hDm1RE2_eff.GetYaxis().SetLabelFont(32)
        hDm1RE2_eff.GetYaxis().SetTitleFont(32)

        hDm1RE2_eff.Draw()
        hDm1RE2_eff_STA.SetMarkerColor(ROOT.kBlue) ##
        hDm1RE2_eff_STA.SetMarkerStyle(22) ##
        hDm1RE2_eff_STA.Draw("same") ##
        hDm1RE2_masked.Draw("same")
        c_disk_m1_RE2.Update()

        hDm1RE2_bx.SetMarkerColor(ROOT.kRed)
        hDm1RE2_bx.SetMarkerStyle(23)
        scale = 110./21.
        hDm1RE2_bx.SetLineColor(ROOT.kRed)
        hDm1RE2_bx.Scale(scale)
        hDm1RE2_bx.Draw("same")

        htemp = hDm1RE2_eff.Clone()
        for k in range(htemp.GetNbinsX()+1):
            if k <=108: htemp.SetBinContent(k,scale*10)
        hDm1RE2_bx.Add(htemp)

        htemp_STA = hDm1RE2_eff_STA.Clone()
        for k in range(htemp_STA.GetNbinsX()+1):
            if k <=108: htemp_STA.SetBinContent(k,scale*10)

        axis = TGaxis(ROOT.gPad.GetUxmax(),ROOT.gPad.GetUymin(),ROOT.gPad.GetUxmax(), ROOT.gPad.GetUymax(),-10.,10,510,"+L")
        axis.SetLineColor(ROOT.kRed)
        axis.SetLabelColor(ROOT.kRed)
        axis.SetLabelOffset(0.005)
        axis.SetLabelSize(0.04)
        axis.SetTickSize(0.03)
        axis.SetGridLength(0)
        axis.SetTitleOffset(1)
        axis.SetTitleSize(0.04)
        axis.SetTitleColor(1)
        axis.SetTitleFont(62)

        axis.Draw();
        c_disk_m1_RE2.Write()
        c_disk_m1_RE2.SaveAs(path+"run"+run+"_c_disk_m1_RE2.gif")

##      c_disk_m1_RE1 = TCanvas("c_disk_m1_RE1", "Disk -1 RE1",4,25,1445,490)
        c_disk_m1_RE1 = TCanvas("c_disk_m1_RE1", "Disk -1 RE1",23,91,1247,400)
        c_disk_m1_RE1.SetHighLightColor(2)
        c_disk_m1_RE1.Range(-10.26568,-73.24462,111.695,124.805)
        c_disk_m1_RE1.SetFillColor(0)
        c_disk_m1_RE1.SetBorderMode(0)
        c_disk_m1_RE1.SetBorderSize(2)
        c_disk_m1_RE1.SetLeftMargin(0.084172)
        c_disk_m1_RE1.SetRightMargin(0.05489479)
        c_disk_m1_RE1.SetBottomMargin(0.3698297)
        c_disk_m1_RE1.SetFrameBorderMode(0)
        c_disk_m1_RE1.SetFrameBorderMode(0)

        hDm1RE1_eff.SetMaximum(100)
        hDm1RE1_eff.SetMinimum(-0.1)
        hDm1RE1_eff.SetMarkerColor(1)
        hDm1RE1_eff.SetMarkerStyle(22)
        hDm1RE1_eff.GetXaxis().SetLabelFont(32)
        hDm1RE1_eff.GetXaxis().SetTitleFont(32)
        hDm1RE1_eff.GetYaxis().SetTitle("%")
        hDm1RE1_eff.GetYaxis().SetLabelFont(32)
        hDm1RE1_eff.GetYaxis().SetTitleFont(32)

        hDm1RE1_eff.Draw()

        hDm1RE1_eff_STA.SetMarkerColor(ROOT.kBlue) ##
        hDm1RE1_eff_STA.SetMarkerStyle(22) ##
        hDm1RE1_eff_STA.Draw("same") ##
        hDm1RE1_masked.Draw("same")
        c_disk_m1_RE1.Update()

        hDm1RE1_bx.SetMarkerColor(ROOT.kRed)
        hDm1RE1_bx.SetMarkerStyle(23)
        scale = 110./21.
        hDm1RE1_bx.SetLineColor(ROOT.kRed)
        hDm1RE1_bx.Scale(scale)
        hDm1RE1_bx.Draw("same")
        htemp = hDp1RE1_eff.Clone()
        for k in range(htemp.GetNbinsX()+1):
            if k <=108: htemp.SetBinContent(k,scale*10)
        hDm1RE1_bx.Add(htemp)

        htemp_STA = hDp1RE1_eff_STA.Clone()
        for k in range(htemp_STA.GetNbinsX()+1):
            if k <=108: htemp_STA.SetBinContent(k,scale*10)

        axis = TGaxis(ROOT.gPad.GetUxmax(),ROOT.gPad.GetUymin(),ROOT.gPad.GetUxmax(), ROOT.gPad.GetUymax(),-10.,10,510,"+L")
        axis.SetLineColor(ROOT.kRed)
        axis.SetLabelColor(ROOT.kRed)
        axis.SetLabelOffset(0.005)
        axis.SetLabelSize(0.04)
        axis.SetTickSize(0.03)
        axis.SetGridLength(0)
        axis.SetTitleOffset(1)
        axis.SetTitleSize(0.04)
        axis.SetTitleColor(1)
        axis.SetTitleFont(62)

        axis.Draw();
        c_disk_m1_RE1.Write()
        c_disk_m1_RE1.SaveAs(path+"run"+run+"_c_disk_m1_RE1.gif")


##------------------------------------------------ RE +3 --------------------------------------------------------------------- 
        
##      c_disk_p3_RE3 = TCanvas("c_disk_p3_RE3", "Disk +3 RE3",4,25,1445,490)
        c_disk_p3_RE3 = TCanvas("c_disk_p3_RE3", "Disk +3 RE3",23,91,1247,400)
        c_disk_p3_RE3.SetHighLightColor(2)
        c_disk_p3_RE3.Range(-10.26568,-73.24462,111.695,124.805)
        c_disk_p3_RE3.SetFillColor(0)
        c_disk_p3_RE3.SetBorderMode(0)
        c_disk_p3_RE3.SetBorderSize(2)
        c_disk_p3_RE3.SetLeftMargin(0.084172)
        c_disk_p3_RE3.SetRightMargin(0.05489479)
        c_disk_p3_RE3.SetBottomMargin(0.3698297)
        c_disk_p3_RE3.SetFrameBorderMode(0)
        c_disk_p3_RE3.SetFrameBorderMode(0)

        hDp3RE3_eff.SetMaximum(100)
        hDp3RE3_eff.SetMinimum(-0.1)
        hDp3RE3_eff.SetMarkerColor(1)
        hDp3RE3_eff.SetMarkerStyle(22)
        hDp3RE3_eff.GetXaxis().SetLabelFont(32)
        hDp3RE3_eff.GetXaxis().SetTitleFont(32)
        hDp3RE3_eff.GetYaxis().SetTitle("%")
        hDp3RE3_eff.GetYaxis().SetLabelFont(32)
        hDp3RE3_eff.GetYaxis().SetTitleFont(32)

        hDp3RE3_eff.Draw()

        hDp3RE3_eff_STA.SetMarkerColor(ROOT.kBlue) ##
        hDp3RE3_eff_STA.SetMarkerStyle(22) ##
        hDp3RE3_eff_STA.Draw("same") ##
        hDp3RE3_masked.Draw("same")
        c_disk_p3_RE3.Update()

        hDp3RE3_bx.SetMarkerColor(ROOT.kRed)
        hDp3RE3_bx.SetMarkerStyle(23)
        scale = 110./21.
        hDp3RE3_bx.SetLineColor(ROOT.kRed)
        hDp3RE3_bx.Scale(scale)
        hDp3RE3_bx.Draw("same")
        htemp = hDp3RE3_eff.Clone()
        for k in range(htemp.GetNbinsX()+1):
            if k <=108: htemp.SetBinContent(k,scale*10)
        hDp3RE3_bx.Add(htemp)

        htemp_STA = hDp3RE3_eff_STA.Clone()
        for k in range(htemp_STA.GetNbinsX()+1):
            if k <= 108: htemp_STA.SetBinContent(k,scale*10)
        
        axis = TGaxis(ROOT.gPad.GetUxmax(),ROOT.gPad.GetUymin(),ROOT.gPad.GetUxmax(), ROOT.gPad.GetUymax(),-10.,10,510,"+L")
        axis.SetLineColor(ROOT.kRed)
        axis.SetLabelColor(ROOT.kRed)
        axis.SetLabelOffset(0.005)
        axis.SetLabelSize(0.04)
        axis.SetTickSize(0.03)
        axis.SetGridLength(0)
        axis.SetTitleOffset(1)
        axis.SetTitleSize(0.04)
        axis.SetTitleColor(1)
        axis.SetTitleFont(62)

        axis.Draw();
        c_disk_p3_RE3.Write()
        c_disk_p3_RE3.SaveAs(path+"run"+run+"_c_disk_p3_RE3.gif")


##      c_disk_p3_RE2 = TCanvas("c_disk_p3_RE2", "Disk +3 RE2",4,25,1445,490)
        c_disk_p3_RE2 = TCanvas("c_disk_p3_RE2", "Disk +3 RE2",23,91,1247,400)
        c_disk_p3_RE2.SetHighLightColor(2)
        c_disk_p3_RE2.Range(-10.26568,-73.24462,111.695,124.805)
        c_disk_p3_RE2.SetFillColor(0)
        c_disk_p3_RE2.SetBorderMode(0)
        c_disk_p3_RE2.SetBorderSize(2)
        c_disk_p3_RE2.SetLeftMargin(0.084172)
        c_disk_p3_RE2.SetRightMargin(0.05489479)
        c_disk_p3_RE2.SetBottomMargin(0.3698297)
        c_disk_p3_RE2.SetFrameBorderMode(0)
        c_disk_p3_RE2.SetFrameBorderMode(0)

        hDp3RE2_eff.SetMaximum(100)
        hDp3RE2_eff.SetMarkerColor(1)
        hDp3RE2_eff.SetMarkerStyle(22)
        hDp3RE2_eff.GetXaxis().SetLabelFont(32)
        hDp3RE2_eff.GetXaxis().SetTitleFont(32)
        hDp3RE2_eff.GetYaxis().SetTitle("%")
        hDp3RE2_eff.GetYaxis().SetLabelFont(32)
        hDp3RE2_eff.GetYaxis().SetTitleFont(32)

        hDp3RE2_eff.Draw()
        hDp3RE2_eff_STA.SetMarkerColor(ROOT.kBlue) ##
        hDp3RE2_eff_STA.SetMarkerStyle(22) ##
        hDp3RE2_eff_STA.Draw("same") ##
        hDp3RE2_masked.Draw("same")
        c_disk_p3_RE2.Update()

        hDp3RE2_bx.SetMarkerColor(ROOT.kRed)
        hDp3RE2_bx.SetMarkerStyle(23)
        scale = 110./21.
        hDp3RE2_bx.SetLineColor(ROOT.kRed)
        hDp3RE2_bx.Scale(scale)
        hDp3RE2_bx.Draw("same")

        htemp = hDp3RE2_eff.Clone()
        for k in range(htemp.GetNbinsX()+1):
            if k <=108: htemp.SetBinContent(k,scale*10)
        hDp3RE2_bx.Add(htemp)

        htemp_STA = hDp3RE2_eff_STA.Clone()
        for k in range(htemp_STA.GetNbinsX()+1):
            if k <=108: htemp_STA.SetBinContent(k,scale*10)
        
        axis = TGaxis(ROOT.gPad.GetUxmax(),ROOT.gPad.GetUymin(),ROOT.gPad.GetUxmax(), ROOT.gPad.GetUymax(),-10.,10,510,"+L")
        axis.SetLineColor(ROOT.kRed)
        axis.SetLabelColor(ROOT.kRed)
        axis.SetLabelOffset(0.005)
        axis.SetLabelSize(0.04)
        axis.SetTickSize(0.03)
        axis.SetGridLength(0)
        axis.SetTitleOffset(1)
        axis.SetTitleSize(0.04)
        axis.SetTitleColor(1)
        axis.SetTitleFont(62)

        axis.Draw();
        c_disk_p3_RE2.Write()
        c_disk_p3_RE2.SaveAs(path+"run"+run+"_c_disk_p3_RE2.gif")


##      c_disk_p3_RE1 = TCanvas("c_disk_p3_RE1", "Disk +3 RE1",4,25,1445,490)
        c_disk_p3_RE1 = TCanvas("c_disk_p3_RE1", "Disk +3 RE1",23,91,1247,400)
        c_disk_p3_RE1.SetHighLightColor(2)
        c_disk_p3_RE1.Range(-10.26568,-73.24462,111.695,124.805)
        c_disk_p3_RE1.SetFillColor(0)
        c_disk_p3_RE1.SetBorderMode(0)
        c_disk_p3_RE1.SetBorderSize(2)
        c_disk_p3_RE1.SetLeftMargin(0.084172)
        c_disk_p3_RE1.SetRightMargin(0.05489479)
        c_disk_p3_RE1.SetBottomMargin(0.3698297)
        c_disk_p3_RE1.SetFrameBorderMode(0)
        c_disk_p3_RE1.SetFrameBorderMode(0)

        hDp3RE1_eff.SetMaximum(100)
        hDp3RE1_eff.SetMinimum(-0.1)
        hDp3RE1_eff.SetMarkerColor(1)
        hDp3RE1_eff.SetMarkerStyle(22)
        hDp3RE1_eff.GetXaxis().SetLabelFont(32)
        hDp3RE1_eff.GetXaxis().SetTitleFont(32)
        hDp3RE1_eff.GetYaxis().SetTitle("%")
        hDp3RE1_eff.GetYaxis().SetLabelFont(32)
        hDp3RE1_eff.GetYaxis().SetTitleFont(32)

        hDp3RE1_eff.Draw()

        hDp3RE1_eff_STA.SetMarkerColor(ROOT.kBlue) ##
        hDp3RE1_eff_STA.SetMarkerStyle(22) ##
        hDp3RE1_eff_STA.Draw("same") ##
        hDp3RE1_masked.Draw("same")
        c_disk_p3_RE1.Update()

        hDp3RE1_bx.SetMarkerColor(ROOT.kRed)
        hDp3RE1_bx.SetMarkerStyle(23)
        scale = 110./21.
        hDp3RE1_bx.SetLineColor(ROOT.kRed)
        hDp3RE1_bx.Scale(scale)
        hDp3RE1_bx.Draw("same")

        htemp = hDp3RE1_eff.Clone()
        for k in range(htemp.GetNbinsX()+1):
            if k <=108: htemp.SetBinContent(k,scale*10)
        hDp3RE1_bx.Add(htemp)

        htemp_STA = hDp3RE1_eff_STA.Clone()
        for k in range(htemp_STA.GetNbinsX()+1):
            if k <=108: htemp_STA.SetBinContent(k,scale*10)
        
        axis = TGaxis(ROOT.gPad.GetUxmax(),ROOT.gPad.GetUymin(),ROOT.gPad.GetUxmax(), ROOT.gPad.GetUymax(),-10.,10,510,"+L")
        axis.SetLineColor(ROOT.kRed)
        axis.SetLabelColor(ROOT.kRed)
        axis.SetLabelOffset(0.005)
        axis.SetLabelSize(0.04)
        axis.SetTickSize(0.03)
        axis.SetGridLength(0)
        axis.SetTitleOffset(1)
        axis.SetTitleSize(0.04)
        axis.SetTitleColor(1)
        axis.SetTitleFont(62)

        axis.Draw();
        c_disk_p3_RE1.Write()
        c_disk_p3_RE1.SaveAs(path+"run"+run+"_c_disk_p3_RE1.gif")

##------------------------------------ RE +2 ----------------------------------------------------------
        
##      c_disk_p2_RE3 = TCanvas("c_disk_p2_RE3", "Disk +2 RE3",4,25,1445,490)
        c_disk_p2_RE3 = TCanvas("c_disk_p2_RE3", "Disk +2 RE3",23,91,1247,400)
        c_disk_p2_RE3.SetHighLightColor(2)
        c_disk_p2_RE3.Range(-10.26568,-73.24462,111.695,124.805)
        c_disk_p2_RE3.SetFillColor(0)
        c_disk_p2_RE3.SetBorderMode(0)
        c_disk_p2_RE3.SetBorderSize(2)
        c_disk_p2_RE3.SetLeftMargin(0.084172)
        c_disk_p2_RE3.SetRightMargin(0.05489479)
        c_disk_p2_RE3.SetBottomMargin(0.3698297)
        c_disk_p2_RE3.SetFrameBorderMode(0)
        c_disk_p2_RE3.SetFrameBorderMode(0)

        hDp2RE3_eff.SetMaximum(100)
        hDp2RE3_eff.SetMinimum(-0.1)
        hDp2RE3_eff.SetMarkerColor(1)
        hDp2RE3_eff.SetMarkerStyle(22)
        hDp2RE3_eff.GetXaxis().SetLabelFont(32)
        hDp2RE3_eff.GetXaxis().SetTitleFont(32)
        hDp2RE3_eff.GetYaxis().SetTitle("%")
        hDp2RE3_eff.GetYaxis().SetLabelFont(32)
        hDp2RE3_eff.GetYaxis().SetTitleFont(32)

        hDp2RE3_eff.Draw()

        hDp2RE3_eff_STA.SetMarkerColor(ROOT.kBlue) ##
        hDp2RE3_eff_STA.SetMarkerStyle(22) ##
        hDp2RE3_eff_STA.Draw("same") ##
        hDp2RE3_masked.Draw("same")
        c_disk_p2_RE3.Update()

        hDp2RE3_bx.SetMarkerColor(ROOT.kRed)
        hDp2RE3_bx.SetMarkerStyle(23)
        scale = 110./21.
        hDp2RE3_bx.SetLineColor(ROOT.kRed)
        hDp2RE3_bx.Scale(scale)
        hDp2RE3_bx.Draw("same")

        htemp = hDp2RE3_eff.Clone()
        for k in range(htemp.GetNbinsX()+1):
            if k <=108: htemp.SetBinContent(k,scale*10)
        hDp2RE3_bx.Add(htemp)

        htemp_STA = hDp2RE3_eff_STA.Clone()
        for k in range(htemp_STA.GetNbinsX()+1):
            if k <=108: htemp_STA.SetBinContent(k,scale*10)        

        axis = TGaxis(ROOT.gPad.GetUxmax(),ROOT.gPad.GetUymin(),ROOT.gPad.GetUxmax(), ROOT.gPad.GetUymax(),-10.,10,510,"+L")
        axis.SetLineColor(ROOT.kRed)
        axis.SetLabelColor(ROOT.kRed)
        axis.SetLabelOffset(0.005)
        axis.SetLabelSize(0.04)
        axis.SetTickSize(0.03)
        axis.SetGridLength(0)
        axis.SetTitleOffset(1)
        axis.SetTitleSize(0.04)
        axis.SetTitleColor(1)
        axis.SetTitleFont(62)

        axis.Draw();
        c_disk_p2_RE3.Write()
        c_disk_p2_RE3.SaveAs(path+"run"+run+"_c_disk_p2_RE3.gif")

##      c_disk_p2_RE2 = TCanvas("c_disk_p2_RE2", "Disk +2 RE2",4,25,1445,490)
        c_disk_p2_RE2 = TCanvas("c_disk_p2_RE2", "Disk +2 RE2",23,91,1247,400)
        c_disk_p2_RE2.SetHighLightColor(2)
        c_disk_p2_RE2.Range(-10.26568,-73.24462,111.695,124.805)
        c_disk_p2_RE2.SetFillColor(0)
        c_disk_p2_RE2.SetBorderMode(0)
        c_disk_p2_RE2.SetBorderSize(2)
        c_disk_p2_RE2.SetLeftMargin(0.084172)
        c_disk_p2_RE2.SetRightMargin(0.05489479)
        c_disk_p2_RE2.SetBottomMargin(0.3698297)
        c_disk_p2_RE2.SetFrameBorderMode(0)
        c_disk_p2_RE2.SetFrameBorderMode(0)

        hDp2RE2_eff.SetMaximum(100)
        hDp2RE2_eff.SetMinimum(-0.1)
        hDp2RE2_eff.SetMarkerColor(1)
        hDp2RE2_eff.SetMarkerStyle(22)
        hDp2RE2_eff.GetXaxis().SetLabelFont(32)
        hDp2RE2_eff.GetXaxis().SetTitleFont(32)
        hDp2RE2_eff.GetYaxis().SetTitle("%")
        hDp2RE2_eff.GetYaxis().SetLabelFont(32)
        hDp2RE2_eff.GetYaxis().SetTitleFont(32)

        hDp2RE2_eff.Draw()

        hDp2RE2_eff_STA.SetMarkerColor(ROOT.kBlue) ##
        hDp2RE2_eff_STA.SetMarkerStyle(22) ##
        hDp2RE2_eff_STA.Draw("same") ##
        hDp2RE2_masked.Draw("same")
        c_disk_p2_RE2.Update()

        hDp2RE2_bx.SetMarkerColor(ROOT.kRed)
        hDp2RE2_bx.SetMarkerStyle(23)
        scale = 110./21.
        hDp2RE2_bx.SetLineColor(ROOT.kRed)
        hDp2RE2_bx.Scale(scale)
        hDp2RE2_bx.Draw("same")
        htemp = hDp2RE2_eff.Clone()
        for k in range(htemp.GetNbinsX()+1):
            if k <=108: htemp.SetBinContent(k,scale*10)
        hDp2RE2_bx.Add(htemp)

        htemp_STA = hDp2RE2_eff_STA.Clone()
        for k in range(htemp_STA.GetNbinsX()+1):
            if k <=108: htemp_STA.SetBinContent(k,scale*10)
        
        axis = TGaxis(ROOT.gPad.GetUxmax(),ROOT.gPad.GetUymin(),ROOT.gPad.GetUxmax(), ROOT.gPad.GetUymax(),-10.,10,510,"+L")
        axis.SetLineColor(ROOT.kRed)
        axis.SetLabelColor(ROOT.kRed)
        axis.SetLabelOffset(0.005)
        axis.SetLabelSize(0.04)
        axis.SetTickSize(0.03)
        axis.SetGridLength(0)
        axis.SetTitleOffset(1)
        axis.SetTitleSize(0.04)
        axis.SetTitleColor(1)
        axis.SetTitleFont(62)

        axis.Draw();
        c_disk_p2_RE2.Write()
        c_disk_p2_RE2.SaveAs(path+"run"+run+"_c_disk_p2_RE2.gif")
        
##      c_disk_p2_RE1 = TCanvas("c_disk_p2_RE1", "Disk +2 RE1",4,25,1445,490)
        c_disk_p2_RE1 = TCanvas("c_disk_p2_RE1", "Disk +2 RE1",23,91,1247,400)
        c_disk_p2_RE1.SetHighLightColor(2)
        c_disk_p2_RE1.Range(-10.26568,-73.24462,111.695,124.805)
        c_disk_p2_RE1.SetFillColor(0)
        c_disk_p2_RE1.SetBorderMode(0)
        c_disk_p2_RE1.SetBorderSize(2)
        c_disk_p2_RE1.SetLeftMargin(0.084172)
        c_disk_p2_RE1.SetRightMargin(0.05489479)
        c_disk_p2_RE1.SetBottomMargin(0.3698297)
        c_disk_p2_RE1.SetFrameBorderMode(0)
        c_disk_p2_RE1.SetFrameBorderMode(0)

        hDp2RE1_eff.SetMaximum(100)
        hDp2RE1_eff.SetMinimum(-0.1)
        hDp2RE1_eff.SetMarkerColor(1)
        hDp2RE1_eff.SetMarkerStyle(22)
        hDp2RE1_eff.GetXaxis().SetLabelFont(32)
        hDp2RE1_eff.GetXaxis().SetTitleFont(32)
        hDp2RE1_eff.GetYaxis().SetTitle("%")
        hDp2RE1_eff.GetYaxis().SetLabelFont(32)
        hDp2RE1_eff.GetYaxis().SetTitleFont(32)

        hDp2RE1_eff.Draw()

        hDp2RE1_eff_STA.SetMarkerColor(ROOT.kBlue) ##
        hDp2RE1_eff_STA.SetMarkerStyle(22) ##
        hDp2RE1_eff_STA.Draw("same") ##
        hDp2RE1_masked.Draw("same")
        c_disk_p2_RE1.Update()

        hDp2RE1_bx.SetMarkerColor(ROOT.kRed)
        hDp2RE1_bx.SetMarkerStyle(23)
        scale = 110./21.
        hDp2RE1_bx.SetLineColor(ROOT.kRed)
        hDp2RE1_bx.Scale(scale)
        hDp2RE1_bx.Draw("same")

        htemp = hDp2RE1_eff.Clone()
        for k in range(htemp.GetNbinsX()+1):
            if k <=108: htemp.SetBinContent(k,scale*10)
        hDp2RE1_bx.Add(htemp)

        htemp_STA = hDp2RE1_eff_STA.Clone()
        for k in range(htemp_STA.GetNbinsX()+1):
            if k <=108: htemp_STA.SetBinContent(k,scale*10)
        
        axis = TGaxis(ROOT.gPad.GetUxmax(),ROOT.gPad.GetUymin(),ROOT.gPad.GetUxmax(), ROOT.gPad.GetUymax(),-10.,10,510,"+L")
        axis.SetLineColor(ROOT.kRed)
        axis.SetLabelColor(ROOT.kRed)
        axis.SetLabelOffset(0.005)
        axis.SetLabelSize(0.04)
        axis.SetTickSize(0.03)
        axis.SetGridLength(0)
        axis.SetTitleOffset(1)
        axis.SetTitleSize(0.04)
        axis.SetTitleColor(1)
        axis.SetTitleFont(62)

        axis.Draw();
        c_disk_p2_RE1.Write()
        c_disk_p2_RE1.SaveAs(path+"run"+run+"_c_disk_p2_RE1.gif")
        
##------------------------------------ RE +1 ----------------------------------------------------------
        
##      c_disk_p1_RE3 = TCanvas("c_disk_p1_RE3", "Disk +1 RE3",4,25,1445,490)
        c_disk_p1_RE3 = TCanvas("c_disk_p1_RE3", "Disk +1 RE3",23,91,1247,400)
        c_disk_p1_RE3.SetHighLightColor(2)
        c_disk_p1_RE3.Range(-10.26568,-73.24462,111.695,124.805)
        c_disk_p1_RE3.SetFillColor(0)
        c_disk_p1_RE3.SetBorderMode(0)
        c_disk_p1_RE3.SetBorderSize(2)
        c_disk_p1_RE3.SetLeftMargin(0.084172)
        c_disk_p1_RE3.SetRightMargin(0.05489479)
        c_disk_p1_RE3.SetBottomMargin(0.3698297)
        c_disk_p1_RE3.SetFrameBorderMode(0)
        c_disk_p1_RE3.SetFrameBorderMode(0)

        hDp1RE3_eff.SetMaximum(100)
        hDp1RE3_eff.SetMinimum(-0.1)
        hDp1RE3_eff.SetMarkerColor(1)
        hDp1RE3_eff.SetMarkerStyle(22)
        hDp1RE3_eff.GetXaxis().SetLabelFont(32)
        hDp1RE3_eff.GetXaxis().SetTitleFont(32)
        hDp1RE3_eff.GetYaxis().SetTitle("%")
        hDp1RE3_eff.GetYaxis().SetLabelFont(32)
        hDp1RE3_eff.GetYaxis().SetTitleFont(32)

        hDp1RE3_eff.Draw()

        hDp1RE3_eff_STA.SetMarkerColor(ROOT.kBlue) ##
        hDp1RE3_eff_STA.SetMarkerStyle(22) ##
        hDp1RE3_eff_STA.Draw("same") ##
        hDp1RE3_masked.Draw("same")
        c_disk_p1_RE3.Update()

        hDp1RE3_bx.SetMarkerColor(ROOT.kRed)
        hDp1RE3_bx.SetMarkerStyle(23)
        scale = 110./21.
        hDp1RE3_bx.SetLineColor(ROOT.kRed)
        hDp1RE3_bx.Scale(scale)
        hDp1RE3_bx.Draw("same")

        htemp = hDp1RE3_eff.Clone()
        for k in range(htemp.GetNbinsX()+1):
            if k <=108: htemp.SetBinContent(k,scale*10)
        hDp1RE3_bx.Add(htemp)

        htemp_STA = hDp1RE3_eff_STA.Clone()
        for k in range(htemp_STA.GetNbinsX()+1):
            if k <=108: htemp_STA.SetBinContent(k,scale*10)
 
        axis = TGaxis(ROOT.gPad.GetUxmax(),ROOT.gPad.GetUymin(),ROOT.gPad.GetUxmax(), ROOT.gPad.GetUymax(),-10.,10,510,"+L")
        axis.SetLineColor(ROOT.kRed)
        axis.SetLabelColor(ROOT.kRed)
        axis.SetLabelOffset(0.005)
        axis.SetLabelSize(0.04)
        axis.SetTickSize(0.03)
        axis.SetGridLength(0)
        axis.SetTitleOffset(1)
        axis.SetTitleSize(0.04)
        axis.SetTitleColor(1)
        axis.SetTitleFont(62)

        axis.Draw();
        c_disk_p1_RE3.Write()
        c_disk_p1_RE3.SaveAs(path+"run"+run+"_c_disk_p1_RE3.gif")
        
##      c_disk_p1_RE2 = TCanvas("c_disk_p1_RE2", "Disk +1 RE2",4,25,1445,490)
        c_disk_p1_RE2 = TCanvas("c_disk_p1_RE2", "Disk +1 RE2",23,91,1247,400)
        c_disk_p1_RE2.SetHighLightColor(2)
        c_disk_p1_RE2.Range(-10.26568,-73.24462,111.695,124.805)
        c_disk_p1_RE2.SetFillColor(0)
        c_disk_p1_RE2.SetBorderMode(0)
        c_disk_p1_RE2.SetBorderSize(2)
        c_disk_p1_RE2.SetLeftMargin(0.084172)
        c_disk_p1_RE2.SetRightMargin(0.05489479)
        c_disk_p1_RE2.SetBottomMargin(0.3698297)
        c_disk_p1_RE2.SetFrameBorderMode(0)
        c_disk_p1_RE2.SetFrameBorderMode(0)

        hDp1RE2_eff.SetMaximum(100)
        hDp1RE2_eff.SetMinimum(-0.1)
        hDp1RE2_eff.SetMarkerColor(1)
        hDp1RE2_eff.SetMarkerStyle(22)
        hDp1RE2_eff.GetXaxis().SetLabelFont(32)
        hDp1RE2_eff.GetXaxis().SetTitleFont(32)
        hDp1RE2_eff.GetYaxis().SetTitle("%")
        hDp1RE2_eff.GetYaxis().SetLabelFont(32)
        hDp1RE2_eff.GetYaxis().SetTitleFont(32)

        hDp1RE2_eff.Draw()
        hDp1RE2_eff_STA.SetMarkerColor(ROOT.kBlue) ##
        hDp1RE2_eff_STA.SetMarkerStyle(22) ##
        hDp1RE2_eff_STA.Draw("same") ##
        hDp1RE2_masked.Draw("same")
        c_disk_p1_RE2.Update()

        hDp1RE2_bx.SetMarkerColor(ROOT.kRed)
        hDp1RE2_bx.SetMarkerStyle(23)
        scale = 110./21.
        hDp1RE2_bx.SetLineColor(ROOT.kRed)
        hDp1RE2_bx.Scale(scale)
        hDp1RE2_bx.Draw("same")

        htemp = hDp1RE2_eff.Clone()
        for k in range(htemp.GetNbinsX()+1):
            if k <=108: htemp.SetBinContent(k,scale*10)
        hDp1RE2_bx.Add(htemp)

        htemp_STA = hDp1RE2_eff_STA.Clone()
        for k in range(htemp_STA.GetNbinsX()+1):
            if k <=108: htemp_STA.SetBinContent(k,scale*10)
        
        axis = TGaxis(ROOT.gPad.GetUxmax(),ROOT.gPad.GetUymin(),ROOT.gPad.GetUxmax(), ROOT.gPad.GetUymax(),-10.,10,510,"+L")
        axis.SetLineColor(ROOT.kRed)
        axis.SetLabelColor(ROOT.kRed)
        axis.SetLabelOffset(0.005)
        axis.SetLabelSize(0.04)
        axis.SetTickSize(0.03)
        axis.SetGridLength(0)
        axis.SetTitleOffset(1)
        axis.SetTitleSize(0.04)
        axis.SetTitleColor(1)
        axis.SetTitleFont(62)

        axis.Draw();
        c_disk_p1_RE2.Write()
        c_disk_p1_RE2.SaveAs(path+"run"+run+"_c_disk_p1_RE2.gif")
        
##      c_disk_p1_RE1 = TCanvas("c_disk_p1_RE1", "Disk +1 RE1",4,25,1445,490)
        c_disk_p1_RE1 = TCanvas("c_disk_p1_RE1", "Disk +1 RE1",23,91,1247,400)
        c_disk_p1_RE1.SetHighLightColor(2)
        c_disk_p1_RE1.Range(-10.26568,-73.24462,111.695,124.805)
        c_disk_p1_RE1.SetFillColor(0)
        c_disk_p1_RE1.SetBorderMode(0)
        c_disk_p1_RE1.SetBorderSize(2)
        c_disk_p1_RE1.SetLeftMargin(0.084172)
        c_disk_p1_RE1.SetRightMargin(0.05489479)
        c_disk_p1_RE1.SetBottomMargin(0.3698297)
        c_disk_p1_RE1.SetFrameBorderMode(0)
        c_disk_p1_RE1.SetFrameBorderMode(0)

        hDp1RE1_eff.SetMaximum(100)
        hDp1RE1_eff.SetMinimum(-0.1)
        hDp1RE1_eff.SetMarkerColor(1)
        hDp1RE1_eff.SetMarkerStyle(22)
        hDp1RE1_eff.GetXaxis().SetLabelFont(32)
        hDp1RE1_eff.GetXaxis().SetTitleFont(32)
        hDp1RE1_eff.GetYaxis().SetTitle("%")
        hDp1RE1_eff.GetYaxis().SetLabelFont(32)
        hDp1RE1_eff.GetYaxis().SetTitleFont(32)

        hDp1RE1_eff.Draw()

        hDp1RE1_eff_STA.SetMarkerColor(ROOT.kBlue) ##
        hDp1RE1_eff_STA.SetMarkerStyle(22) ##
        hDp1RE1_eff_STA.Draw("same") ##
        hDp1RE1_masked.Draw("same")
        c_disk_p1_RE1.Update()

        hDp1RE1_bx.SetMarkerColor(ROOT.kRed)
        hDp1RE1_bx.SetMarkerStyle(23)
        scale = 110./21.
        hDp1RE1_bx.SetLineColor(ROOT.kRed)
        hDp1RE1_bx.Scale(scale)
        hDp1RE1_bx.Draw("same")
        htemp = hDp1RE1_eff.Clone()
        for k in range(htemp.GetNbinsX()+1):
            if k <=108: htemp.SetBinContent(k,scale*10)
        hDp1RE1_bx.Add(htemp)
       
        htemp_STA = hDp1RE1_eff_STA.Clone()
        for k in range(htemp_STA.GetNbinsX()+1):
            if k <=108: htemp_STA.SetBinContent(k,scale*10)
 
        axis = TGaxis(ROOT.gPad.GetUxmax(),ROOT.gPad.GetUymin(),ROOT.gPad.GetUxmax(), ROOT.gPad.GetUymax(),-10.,10,510,"+L")
        axis.SetLineColor(ROOT.kRed)
        axis.SetLabelColor(ROOT.kRed)
        axis.SetLabelOffset(0.005)
        axis.SetLabelSize(0.04)
        axis.SetTickSize(0.03)
        axis.SetGridLength(0)
        axis.SetTitleOffset(1)
        axis.SetTitleSize(0.04)
        axis.SetTitleColor(1)
        axis.SetTitleFont(62)

        axis.Draw();
        c_disk_p1_RE1.Write()
        c_disk_p1_RE1.SaveAs(path+"run"+run+"_c_disk_p1_RE1.gif")

##--------------------------------------------------------------------------------------------
        
        ch1 = TCanvas("hBarrel_bx","hBarrel_bx",1)
        ch1.cd()
        hBarrel_bx.Draw()
        ch1.SaveAs(path+"run"+run+"_hBarrel_bx.gif")

        ch2 = TCanvas("hBarrel_masked","hBarrel_masked",1)
        ch2.cd()
        hBarrel_masked.Draw()
        ch2.SaveAs(path+"run"+run+"_hBarrel_masked.gif")

        ch3 = TCanvas("hBarrel_eff","hBarrel_eff",1)
        ch3.cd()
        hBarrel_eff.SetLineColor(1) 
        hBarrel_eff_STA.SetLineColor(ROOT.kBlue)
        hBarrel_eff.Draw()
        hBarrel_eff_STA.Draw("same")
        ch3.SaveAs(path+"run"+run+"_hBarrel_eff.gif")

        ch4 = TCanvas("hEndcap_bx","hEndcap_bx",1)
        ch4.cd()
        hEndcap_bx.Draw()
        ch4.SaveAs(path+"run"+run+"_hEndcap_bx.gif")

        ch5 = TCanvas("hEndcap_masked","hEndcap_masked",1)
        ch5.cd()
        hEndcap_masked.Draw()
        ch5.SaveAs(path+"run"+run+"_hEndcap_masked.gif")

        ch6 = TCanvas("hEndcap_eff","hEndcap_eff",1)
        ch6.cd()
        hEndcap_eff.SetLineColor(1)
        hEndcap_eff_STA.SetLineColor(ROOT.kBlue)
        hEndcap_eff.Draw()
        hEndcap_eff_STA.Draw("same")
        ch6.SaveAs(path+"run"+run+"_hEndcap_eff.gif")

##---------------------------------------------------------------------------

        ch7 = TCanvas("hWm2_eff","hWm2_eff",1)
        ch7.cd()
        hWm2_eff.SetLineColor(1)
        hWm2_eff_STA.SetLineColor(ROOT.kBlue)
        hWm2_eff.Draw()
        hWm2_eff_STA.Draw("same")
        ch7.SaveAs(path+"run"+run+"_hWm2_eff.gif")

        ch8 = TCanvas("hWm2_masked","hWm2_masked",1)
        ch8.cd()
        hWm2_masked.Draw()
        ch8.SaveAs(path+"run"+run+"_hWm2_masked.gif")

        ch9 = TCanvas("hWm1_eff","hWm1_eff",1)
        ch9.cd()
        hWm1_eff.SetLineColor(1)
        hWm1_eff_STA.SetLineColor(ROOT.kBlue)
        hWm1_eff.Draw()
        hWm1_eff_STA.Draw("same")
        ch9.SaveAs(path+"run"+run+"_hWm1_eff.gif")

        ch10 = TCanvas("hWm1_masked","hWm1_masked",1)
        ch10.cd()
        hWm1_masked.Draw()
        ch10.SaveAs(path+"run"+run+"_hWm1_masked.gif")

        ch11 = TCanvas("hW0_eff","hW0_eff",1)
        ch11.cd()
        hW0_eff.SetLineColor(1)
        hW0_eff_STA.SetLineColor(ROOT.kBlue)
        hW0_eff.Draw()
        hW0_eff_STA.Draw("same")
        ch11.SaveAs(path+"run"+run+"_hW0_eff.gif")

        ch12 = TCanvas("hW0_masked","hW0_masked",1)
        ch12.cd()
        hW0_masked.Draw()
        ch12.SaveAs(path+"run"+run+"_hW0_masked.gif")

        ch13 = TCanvas("hWp1_eff","hWp1_eff",1)
        ch13.cd()
        hWp1_eff.SetLineColor(1)
        hWp1_eff_STA.SetLineColor(ROOT.kBlue)
        hWp1_eff.Draw()
        hWp1_eff_STA.Draw("same")
        ch13.SaveAs(path+"run"+run+"_hWp1_eff.gif")

        ch14 = TCanvas("hWp1_masked","hWp1_masked",1)
        ch14.cd()
        hWp1_masked.Draw()
        ch14.SaveAs(path+"run"+run+"_hWp1_masked.gif")

        ch15 = TCanvas("hWp2_eff","hWp2_eff",1)
        ch15.cd()
        hWp2_eff.SetLineColor(1)
        hWp2_eff_STA.SetLineColor(ROOT.kBlue)
        hWp2_eff.Draw()
        hWp2_eff_STA.Draw("same")
        ch15.SaveAs(path+"run"+run+"_hWp2_eff.gif")

        ch15 = TCanvas("hWp2_masked","hWp2_masked",1)
        ch15.cd()
        hWp2_masked.Draw()
        ch15.SaveAs(path+"run"+run+"_hWp2_masked.gif")

        ch16 = TCanvas("hDm1_eff","hDm1_eff",1)
        ch16.cd()
        hDm1_eff.SetLineColor(1)
        hDm1_eff_STA.SetLineColor(ROOT.kBlue)
        hDm1_eff.Draw()
        hDm1_eff_STA.Draw("same")
        ch16.SaveAs(path+"run"+run+"_hDm1_eff.gif")

        ch17 = TCanvas("hDm1_masked","hDm1_masked",1)
        ch17.cd()
        hDm1_masked.Draw()
        ch17.SaveAs(path+"run"+run+"_hDm1_masked.gif")

        ch18 = TCanvas("hDm2_eff","hDm2_eff",1)
        ch18.cd()
        hDm2_eff.SetLineColor(1)
        hDm2_eff_STA.SetLineColor(ROOT.kBlue)
        hDm2_eff.Draw()
        hDm2_eff_STA.Draw("same")
        ch18.SaveAs(path+"run"+run+"_hDm2_eff.gif")

        ch19 = TCanvas("hDm2_masked","hDm2_masked",1)
        ch19.cd()
        hDm2_masked.Draw()
        ch19.SaveAs(path+"run"+run+"_hDm2_masked.gif")

        ch20 = TCanvas("hDm3_eff","hDm3_eff",1)
        ch20.cd()
        hDm3_eff.SetLineColor(1)
        hDm3_eff_STA.SetLineColor(ROOT.kBlue)
        hDm3_eff.Draw()
        hDm3_eff_STA.Draw("same")
        ch20.SaveAs(path+"run"+run+"_hDm3_eff.gif")

        ch21 = TCanvas("hDm3_masked","hDm3_masked",1)
        ch21.cd()
        hDm3_masked.Draw()
        ch21.SaveAs(path+"run"+run+"_hDm3_masked.gif")

        ch22 = TCanvas("hDp1_eff","hDp1_eff",1)
        ch22.cd()
        hDp1_eff.SetLineColor(1)
        hDp1_eff_STA.SetLineColor(ROOT.kBlue)
        hDp1_eff.Draw()
        hDp1_eff_STA.Draw("same")
        ch22.SaveAs(path+"run"+run+"_hDp1_eff.gif")

        ch23 = TCanvas("hDp1_masked","hDp1_masked",1)
        ch23.cd()
        hDp1_masked.Draw()
        ch23.SaveAs(path+"run"+run+"_hDp1_masked.gif")
        
        ch24 = TCanvas("hDp2_eff","hDp2_eff",1)
        ch24.cd()
        hDp2_eff.SetLineColor(1)
        hDp2_eff_STA.SetLineColor(ROOT.kBlue)
        hDp2_eff.Draw()
        hDp2_eff_STA.Draw("same")
        ch24.SaveAs(path+"run"+run+"_hDp2_eff.gif")

        ch25 = TCanvas("hDp2_masked","hDp2_masked",1)
        ch25.cd()
        hDp2_masked.Draw()
        ch25.SaveAs(path+"run"+run+"_hDp2_masked.gif")

        ch26 = TCanvas("hDp3_eff","hDp3_eff",1)
        ch26.cd()
        hDp3_eff.SetLineColor(1)
        hDp3_eff_STA.SetLineColor(ROOT.kBlue)
        hDp3_eff.Draw()
        hDp3_eff_STA.Draw("same")
        ch26.SaveAs(path+"run"+run+"_hDp3_eff.gif")

        ch27 = TCanvas("hDp3_masked","hDp3_masked",1)
        ch27.cd()
        hDp3_masked.Draw()
        ch27.SaveAs(path+"run"+run+"_hDp3_masked.gif")

        ch28 = TCanvas("BxDistribution_Wheel_m2","BxDistribution_Wheel_m2",1)
        ch28.cd()
        try:
            TH1F.BxDistribution_Wheel_m2.Draw()
            ch28.SaveAs(path+"run"+run+"_BxDistribution_Wheel_m2.gif")
        except AttributeError:
            print "Bx Wheel m2 missing"

        ch29 = TCanvas("ClusterSize_Wheel_m2","ClusterSize_Wheel_m2",1)
        ch29.cd()
        try:
            TH1F.ClusterSize_Wheel_m2.Draw()
            ch29.SaveAs(path+"run"+run+"_ClusterSize_Wheel_m2.gif")
        except AttributeError:
            print "ClusterSize Wheel m2 missing"

        ch30 = TCanvas("BxDistribution_Wheel_m1","BxDistribution_Wheel_m1",1)
        ch30.cd()
        try:
            TH1F.BxDistribution_Wheel_m1.Draw()
            ch30.SaveAs(path+"run"+run+"_BxDistribution_Wheel_m1.gif")
        except AttributeError:
            print "Bx Wheel m1 missing"

        ch31 = TCanvas("ClusterSize_Wheel_m1","ClusterSize_Wheel_m1",1)
        ch31.cd()
        try:
            TH1F.ClusterSize_Wheel_m1.Draw()
            ch31.SaveAs(path+"run"+run+"_ClusterSize_Wheel_m1.gif")
        except AttributeError:
            print "ClusterSize Wheel m1 missing"

        ch32 = TCanvas("BxDistribution_Wheel_0","BxDistribution_Wheel_0",1)
        ch32.cd()
        try:
            TH1F.BxDistribution_Wheel_0.Draw()
            ch32.SaveAs(path+"run"+run+"_BxDistribution_Wheel_0.gif")
        except AttributeError:
            print "Bx Wheel 0 missing"

        ch33 = TCanvas("ClusterSize_Wheel_0","ClusterSize_Wheel_0",1)
        ch33.cd()
        try:
            TH1F.ClusterSize_Wheel_0.Draw()
            ch33.SaveAs(path+"run"+run+"_ClusterSize_Wheel_0.gif")
        except AttributeError:
            print "ClusterSize Wheel 0 missing"

        ch34 = TCanvas("BxDistribution_Wheel_p1","BxDistribution_Wheel_p1",1)
        ch34.cd()
        try:
            TH1F.BxDistribution_Wheel_p1.Draw()
            ch34.SaveAs(path+"run"+run+"_BxDistribution_Wheel_p1.gif")
        except AttributeError:
            print "Bx Wheel p1 missing"

        ch35 = TCanvas("ClusterSize_Wheel_p1","ClusterSize_Wheel_p1",1)
        ch35.cd()
        try:
            TH1F.ClusterSize_Wheel_p1.Draw()
            ch35.SaveAs(path+"run"+run+"_ClusterSize_Wheel_p1.gif")
        except AttributeError:
            print "ClusterSize Wheel p1 missing"

        ch36 = TCanvas("BxDistribution_Wheel_p2","BxDistribution_Wheel_p2",1)
        ch36.cd()
        try:
            TH1F.BxDistribution_Wheel_p2.Draw()
            ch36.SaveAs(path+"run"+run+"_BxDistribution_Wheel_p2.gif")
        except AttributeError:
            print "Bx Wheel m2 missing"

        ch37 = TCanvas("ClusterSize_Wheel_p2","ClusterSize_Wheel_p2",1)
        ch37.cd()
        try:
            TH1F.ClusterSize_Wheel_p2.Draw()
            ch37.SaveAs(path+"run"+run+"_ClusterSize_Wheel_p2.gif")
        except AttributeError:
            print "ClusterSize Wheel p2 missing"

        ch38 = TCanvas("BxDistribution_Disk_p1","BxDistribution_Disk_p1",1)
        ch38.cd()
        try:
            TH1F.BxDistribution_Disk_p1.Draw()
            ch38.SaveAs(path+"run"+run+"_BxDistribution_Disk_p1.gif")
        except AttributeError:
            print "Bx Disk p1 missing"

        ch39 = TCanvas("ClusterSize_Disk_p1","ClusterSize_Disk_p1",1)
        ch39.cd()
        try:
            TH1F.ClusterSize_Disk_p1.Draw()
            ch39.SaveAs(path+"run"+run+"_ClusterSize_Disk_p1.gif")
        except AttributeError:
            print "ClusterSize Disk p1 missing"

        ch40 = TCanvas("BxDistribution_Disk_p2","BxDistribution_Disk_p2",1)
        ch40.cd()
        try:
            TH1F.BxDistribution_Disk_p2.Draw()
            ch40.SaveAs(path+"run"+run+"_BxDistribution_Disk_p2.gif")
        except AttributeError:
            print "Bx Disk p2 missing"

        ch41 = TCanvas("ClusterSize_Disk_p2","ClusterSize_Disk_p2",1)
        ch41.cd()
        try:
            TH1F.ClusterSize_Disk_p2.Draw()
            ch41.SaveAs(path+"run"+run+"_ClusterSize_Disk_p2.gif")
        except AttributeError:
            print "ClusterSize Disk p2 missing"

        ch42 = TCanvas("BxDistribution_Disk_p3","BxDistribution_Disk_p3",1)
        ch42.cd()
        try:
            TH1F.BxDistribution_Disk_p3.Draw()
            ch42.SaveAs(path+"run"+run+"_BxDistribution_Disk_p3.gif")
        except AttributeError:
            print "Bx Disk p3 missing"

        ch43 = TCanvas("ClusterSize_Disk_p3","ClusterSize_Disk_p3",1)
        ch43.cd()
        try:
            TH1F.ClusterSize_Disk_p3.Draw()
            ch43.SaveAs(path+"run"+run+"_ClusterSize_Disk_p3.gif")
        except AttributeError:
            print "ClusterSize Disk p3 missing"

##-----------------------------------------------------------------------------------------------------------------------------

        ch44 = TCanvas("ClusterSize_for_Barrel","ClusterSize_for_Barrel",1)
        ch44.cd()
        try:
            TH1F.ClusterSize_for_Barrel.Draw()
            ch44.SaveAs(path+"run"+run+"_ClusterSize_for_Barrel.gif")
        except AttributeError:
            print "ClusterSize Barrel missing"

        ch45 = TCanvas("ClusterSize_for_Endcap_P","ClusterSize_for_Endcap_P",1)
        ch45.cd()
        try:
            TH1F.ClusterSize_for_Endcap_P.Draw()
            ch45.SaveAs(path+"run"+run+"_ClusterSize_for_Endcap_P.gif")
        except AttributeError:
            print "ClusterSize Positive Endcap missing"


        ch46 = TCanvas("ClusterSize_for_Endcap_N","ClusterSize_for_Endcap_N",1)
        ch46.cd()
        try:
            TH1F.ClusterSize_for_Endcap_N.Draw()
            ch46.SaveAs(path+"run"+run+"_ClusterSize_for_Endcap_N.gif")
        except AttributeError:
            print "ClusterSize Positive Endcap missing"

##-----------------------------------------------------------------------------------------------------------------------------

        self.NewRootFile.Write()
        self.NewRootFile.Close()

    def findNear(self,name):
        coord = name.rstrip().split("_")
        near = False
        sec = ["S01","S02","S03","S04","S05","S06","S07","S08","S09","S10","S11","S12"]
        counter = 0
        for i in sec:
            if str(i) == str(coord[2]) and (counter < 3 or counter > 8):
                near = True
                break
            else:
                near = False
            counter+=1
        return near

    def fillDetListBarrel(self):

        cmd = "pwd"
        homedir = [item[:-1] for item in os.popen(cmd)]
        f=open(str(homedir[0])+'/wheel_coord.txt', 'r')
        
        detList = []
        for line in f:
            coord = line.rstrip().split("  ")
            detList.append(str(coord[0]))

        f.close()
        return detList

    def fillDetListEndcap(self):

        cmd = "pwd"
        homedir = [item[:-1] for item in os.popen(cmd)]
        f=open(str(homedir[0])+'/disk_coord.txt', 'r')
        
        detList = []
        for line in f:
            coord = line.rstrip().split("  ")
            detList.append(str(coord[0]))

        f.close()
        return detList

    def getMeanValue(self,histoname):
        inputname = histoname.rstrip().split("_")

        histo_back = histoname + '_Backward'
        histo_for = histoname + '_Forward'
        rolls_in_chamber = [histo_for,histo_back]

        if (cmp(inputname[1],'W+2') == 0 or cmp(inputname[1],'W-2') == 0) and cmp(inputname[2],'RB2out') == 0:
            histo_middle = histoname + '_Middle'
            rolls_in_chamber.append(histo_middle)
        elif (cmp(inputname[1],'W-1')==0 or cmp(inputname[1],'W+0')==0 or cmp(inputname[1],'W+1')==0) and cmp(inputname[2],'RB2in')==0:
            histo_middle = histoname + '_Middle'
            rolls_in_chamber.append(histo_middle)

        meanvalue = []
        for roll in rolls_in_chamber:
            try:
                histo = gDirectory.FindObjectAny(roll)
                meanvalue.append(histo.GetMean())
                meanvalue.append(histo.GetRMS())
            except AttributeError:
                meanvalue.append(-100)
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
        elif (cmp(inputname[1],'W-1')==0 or cmp(inputname[1],'W+0')==0 or cmp(inputname[1],'W+1')==0) and cmp(inputname[2],'RB2in')==0:
            histo_middle = histoname + '_Middle'
            rolls_in_chamber.append(histo_middle)

        meanvalue = []
        for roll in rolls_in_chamber:
            try:
                histo = gDirectory.FindObjectAny(roll)
                sumeff = 0
                sumefferr = 0
                stripcount = 0
                aveeff = 0
                aveerr = 0

                for i in range(histo.GetNbinsX()):
                    
                    sumeff += histo.GetBinContent(i)
                    sumefferr += (histo.GetBinError(i))*(histo.GetBinError(i))
                    if histo.GetBinContent(i):
                        stripcount +=1

                if stripcount:
                    aveeff = sumeff/stripcount
                    aveerr = sqrt(sumefferr)/stripcount
                    if aveeff + aveerr > 100:
                        aveerr = 100-aveeff
                    meanvalue.append(aveeff)
                    meanvalue.append(aveerr)
                else:
                    meanvalue.append(-100)
                    meanvalue.append(-100) 
                    
            except AttributeError:
                meanvalue.append(-100)
                meanvalue.append(-100)

        return meanvalue
                    
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
        elif (cmp(inputname[1],'W-1')==0 or cmp(inputname[1],'W+0')==0 or cmp(inputname[1],'W+1')==0) and cmp(inputname[2],'RB2in')==0:
            histo_middle = histoname + '_Middle'
            rolls_in_chamber.append(histo_middle)

        meanvalue = []
        for roll in rolls_in_chamber:
            try:
                histo = gDirectory.FindObjectAny(roll)
                counter = 0
                for j in range(histo.GetNbinsX()):
                    if histo.GetBinContent(j+1) == 0: counter += 1
                meanvalue.append(float(counter)/float(histo.GetNbinsX())*100.)
            except AttributeError:
                meanvalue.append(-100)
        return meanvalue

    def getCountWheel(self):

        WheelNameList = ['Wheel_-2', 'Wheel_-1', 'Wheel_0', 'Wheel_1', 'Wheel_2']
        countBx_Barrel = 0

        for Wheel in WheelNameList:
            BxLabel = 'BxDistribution_' + Wheel
            try:
                if(gDirectory.FindObjectAny(BxLabel)):
                    countBx_Barrel += 1
            except AttributeError:
                pass
        print "countBx_Barrel : ", countBx_Barrel    
        return countBx_Barrel

#----------------------------------- Bx of Barrel  -----------------------------------------------------
   

    def getBinEntry(self,Num):

        Bx = []        
         
        if Num == "-2":
            try:  
                TH1F.BxDistribution_Wheel_m2 = gDirectory.FindObjectAny("BxDistribution_Wheel_-2") 
                for i in range(12):
                    Bx.append(TH1F.BxDistribution_Wheel_m2.GetBinContent(i))

            except AttributeError:
                for j in range(12):
                    Bx.append(0)

            return Bx
 
        if Num == "-1":
            try:
                TH1F.BxDistribution_Wheel_m1 = gDirectory.FindObjectAny("BxDistribution_Wheel_-1")
                for i in range(12):
                    Bx.append(TH1F.BxDistribution_Wheel_m1.GetBinContent(i))

            except AttributeError:
                for j in range(12):
                    Bx.append(0)

            return Bx 

        if Num == "0":
            try:
                TH1F.BxDistribution_Wheel_0 = gDirectory.FindObjectAny("BxDistribution_Wheel_0")
                for i in range(12):
                    Bx.append(TH1F.BxDistribution_Wheel_0.GetBinContent(i))

            except AttributeError:
                for j in range(12):
                    Bx.append(0)

            return Bx

        if Num == "1":
            try:
                TH1F.BxDistribution_Wheel_p1 = gDirectory.FindObjectAny("BxDistribution_Wheel_1")
                for i in range(12):
                    Bx.append(TH1F.BxDistribution_Wheel_p1.GetBinContent(i))

            except AttributeError:
                for j in range(12):
                    Bx.append(0)

            return Bx 

        if Num == "2":
            try:
                TH1F.BxDistribution_Wheel_p2 = gDirectory.FindObjectAny("BxDistribution_Wheel_2")
                for i in range(12):
                    Bx.append(TH1F.BxDistribution_Wheel_p2.GetBinContent(i))

            except AttributeError:
                for j in range(12):
                    Bx.append(0)

            return Bx

#-------------------------------------------------------------------------------------------------------

    def getMeanValueDisk(self,histoname):
        inputname = histoname.rstrip().split("_")

        histo_A = histoname + '_A'
        histo_B = histoname + '_B'
        histo_C = histoname + '_C'
        rolls_in_chamber = [histo_A,histo_B,histo_C]

        meanvalue = []
        for roll in rolls_in_chamber:
            try:
                histo = gDirectory.FindObjectAny(roll)
                meanvalue.append(histo.GetMean())
                meanvalue.append(histo.GetRMS())
            except AttributeError:
                meanvalue.append(-100)
                meanvalue.append(-100)
        return meanvalue

    def getMediaDisk(self,histoname):
        inputname = histoname.rstrip().split("_")
        histo_A = histoname + '_A'
        histo_B = histoname + '_B'
        histo_C = histoname + '_C'

        rolls_in_chamber = [histo_A,histo_B,histo_C]

        meanvalue = []
        for roll in rolls_in_chamber:
            try:
                histo = gDirectory.FindObjectAny(roll)
                sumeff = 0
                sumefferr = 0
                stripcount = 0
                aveeff = 0
                aveerr = 0

                for i in range(histo.GetNbinsX()):
                    
                    sumeff += histo.GetBinContent(i)
                    sumefferr += (histo.GetBinError(i))*(histo.GetBinError(i))
                    if histo.GetBinContent(i):
                        stripcount +=1

                if stripcount:
                    aveeff = sumeff/stripcount
                    aveerr = sqrt(sumefferr)/stripcount
                    if aveeff + aveerr > 100:
                        aveerr = 100-aveeff
                    meanvalue.append(aveeff)
                    meanvalue.append(aveerr)
                else:
                    meanvalue.append(-100)
                    meanvalue.append(-100) 
                    
            except AttributeError:
                meanvalue.append(-100)
                meanvalue.append(-100)

        return meanvalue

    def getMaskedStripDisk(self,histoname):
        inputname = histoname.rstrip().split("_")

        histo_A = histoname + '_A'
        histo_B = histoname + '_B'
        histo_C = histoname + '_C'
        rolls_in_chamber = [histo_A,histo_B,histo_C]

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

    def getCountDisk(self):
        DiskList = ['Disk_-1', 'Disk_-2', 'Disk_-3', 'Disk_1', 'Disk_2', 'Disk_3']
        countBx_Endcap = 0

        for Disk in DiskList:
            BxLabel = 'BxDistribution_' + Disk
            try:
                if(gDirectory.FindObjectAny(BxLabel)):
                    countBx_Endcap += 1
            except AttributeError:
                pass
        print "countBx_Endcap : ", countBx_Endcap
        return countBx_Endcap

#----------------------------------- Bx of Endcap -----------------------------------------------------


    def getBinEntryDisk(self,Num):

        Bx = []

        if Num == "-1":
            try:
                TH1F.BxDistribution_Disk_m1 = gDirectory.FindObjectAny("BxDistribution_Disk_-1")
                for i in range(12):
                    Bx.append(TH1F.BxDistribution_Disk_m1.GetBinContent(i))

            except AttributeError:
                for j in range(12):
                    Bx.append(0)

            return Bx

        if Num == "-2":
            try:
                TH1F.BxDistribution_Disk_m2 = gDirectory.FindObjectAny("BxDistribution_Disk_-2")
                for i in range(12):
                    Bx.append(TH1F.BxDistribution_Disk_m2.GetBinContent(i))

            except AttributeError:
                for j in range(12):
                    Bx.append(0)

            return Bx

        if Num == "-3":
            try:
                TH1F.BxDistribution_Disk_m3 = gDirectory.FindObjectAny("BxDistribution_Disk_-3")
                for i in range(12):
                    Bx.append(TH1F.BxDistribution_Disk_m3.GetBinContent(i))

            except AttributeError:
                for j in range(12):
                    Bx.append(0)

            return Bx

        if Num == "1":
            try:
                TH1F.BxDistribution_Disk_p1 = gDirectory.FindObjectAny("BxDistribution_Disk_1")
                for i in range(12):
                    Bx.append(TH1F.BxDistribution_Disk_p1.GetBinContent(i))

            except AttributeError:
                for j in range(12):
                    Bx.append(0)

            return Bx

        if Num == "2":
            try:
                TH1F.BxDistribution_Disk_p2 = gDirectory.FindObjectAny("BxDistribution_Disk_2")
                for i in range(12):
                    Bx.append(TH1F.BxDistribution_Disk_p2.GetBinContent(i))

            except AttributeError:
                for j in range(12):
                    Bx.append(0)

            return Bx


        if Num == "3":
            try:
                TH1F.BxDistribution_Disk_p3 = gDirectory.FindObjectAny("BxDistribution_Disk_3")
                for i in range(12):
                    Bx.append(TH1F.BxDistribution_Disk_p3.GetBinContent(i))

            except AttributeError:
                for j in range(12):
                    Bx.append(0)

            return Bx

#-------------------------------------------------------------------------------------------------------
    

##if __name__ == "__main__": GlobalPlotsProduction("rfio:/castor/cern.ch/cms/store/caf/user/ccmuon/RPC/GlobalRuns/CosmicsCommissioning09-PromptReco-v1RECO/83063/root/Merge_tot_new.root","/tmp/seungen/","83063")

##if __name__ == "__main__": GlobalPlotsProduction("rfio:/castor/cern.ch/cms/store/caf/user/ccmuon/RPC/GlobalRuns/CosmicsCommissioning09-PromptReco-v1RECO/83063/root/Merge_tot_new.root","83073","/tmp/seungen/")
if __name__ == "__main__": GlobalPlotsProduction(sys.argv[1],sys.argv[2],sys.argv[3])

