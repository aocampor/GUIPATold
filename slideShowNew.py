########################################################################
# SlideShow: a simple photo image slideshow in Python/Tkinter;
# the base feature set coded here can be extended in subclasses;
########################################################################
from tkMessageBox import *
from Tkinter import *
from glob import glob
from tkFileDialog import askopenfilename
import random

from PlotDisplayGlobal  import DisplayPlotsGlobal 
import os

sys.argv.append('-b-') 
import ROOT
from ROOT import TCanvas,TH1F,gROOT,TFile,gDirectory

Width, Height = 450, 450

imageTypes = [('Gif files', '.gif'),    # for file open dialog
              ('Ppm files', '.ppm'),    # plus jpg with a Tk patch,
              ('Pgm files', '.pgm'),    # plus bitmaps with BitmapImage
              ('All files', '*')]

class SlideShow(Frame):
    def __init__(self, ds,run,parent=None, picdir='.', msecs=3000):
        my_window = Toplevel()
        Frame.__init__(self, my_window)
        self.makeWidgets()
        self.pack(expand=YES, fill=BOTH)
        self.opens = picdir
        files = []
        for label, ext in imageTypes[:-1]:
            files = files + glob('%s/*%s' % (picdir, ext))
        self.images = map(lambda x: (x, PhotoImage(file=x)), files)
        self.msecs  = msecs
        self.beep   = 1
        self.drawn  = None
        print ds,run

        cmd0 = 'whoami'
        user = [item[:-1] for item in os.popen(cmd0)]

        print user
        os.system('./set_caf.csh')

        self.tmppath = '/tmp/' + user[0] + '/' + run + '/'
        os.system("mkdir "+self.tmppath)
        self.run = run
        self.ds = ds

## ----------------------------------------------------------------------------------------------------------------------------------------------------

    def histoBarrelEff(self):
        file1 = self.tmppath+'run'+self.run+'_hBarrel_eff.gif'
        if not os.path.exists(self.tmppath+'run'+self.run+'_hBarrel_eff.gif'):
            os.system("cmsStageIn /store/caf/user/ccmuon/RPC/GlobalRuns/"+self.ds+"/"+self.run+"/gif/run"+self.run+"_hBarrel_eff.gif "+file1)
            os.system('mv '+'run'+self.run+'_hBarrel_eff.gif ' + self.tmppath)
        self.onPicture(file1)

    def histoBarrelBx(self):
        file1 = self.tmppath+'run'+self.run+'_hBarrel_bx.gif'
        if not os.path.exists(self.tmppath+'run'+self.run+'_hBarrel_bx.gif'):
            os.system("cmsStageIn /store/caf/user/ccmuon/RPC/GlobalRuns/"+self.ds+"/"+self.run+"/gif/run"+self.run+"_hBarrel_bx.gif "+file1)
            os.system('mv '+'run'+self.run+'_hBarrel_bx.gif ' + self.tmppath)
        self.onPicture(file1)

    def histoBarrelCS(self):
        file1 = self.tmppath+'run'+self.run+'_ClusterSize_for_Barrel.gif'
        if not os.path.exists(self.tmppath+'run'+self.run+'_ClusterSize_for_Barrel.gif'):
            os.system("cmsStageIn /store/caf/user/ccmuon/RPC/GlobalRuns/"+self.ds+"/"+self.run+"/gif/run"+self.run+"_ClusterSize_for_Barrel.gif "+file1)
            os.system('mv '+'run'+self.run+'_ClusterSize_for_Barrel.gif ' + self.tmppath)
        self.onPicture(file1)

    def histoBarrelMasked(self):
        file1 = self.tmppath+'run'+self.run+'_hBarrel_masked.gif'
        if not os.path.exists(self.tmppath+'run'+self.run+'_hBarrel_masked.gif'):
            os.system("cmsStageIn /store/caf/user/ccmuon/RPC/GlobalRuns/"+self.ds+"/"+self.run+"/gif/run"+self.run+"_hBarrel_masked.gif "+file1)
            os.system('mv '+ 'run'+self.run+'_hBarrel_masked.gif ' + self.tmppath)
        self.onPicture(file1)

##-------------------------------------------------------------------------------------------------------------------------------------------------------

    def histoEndcapEff(self):
        file1 = self.tmppath+'run'+self.run+'_hEndcap_eff.gif'
        if not os.path.exists(self.tmppath+'run'+self.run+'_hEndcap_eff.gif'):
            os.system("cmsStageIn /store/caf/user/ccmuon/RPC/GlobalRuns/"+self.ds+"/"+self.run+"/gif/run"+self.run+"_hEndcap_eff.gif "+file1)
            os.system('mv '+ 'run'+self.run+'_hEndcap_eff.gif ' + self.tmppath)
        self.onPicture(file1)

    def histoEndcapBx(self):
        file1 = self.tmppath+'run'+self.run+'_hEndcap_bx.gif'
        if not os.path.exists(self.tmppath+'run'+self.run+'_hEndcap_bx.gif'):
            os.system("cmsStageIn /store/caf/user/ccmuon/RPC/GlobalRuns/"+self.ds+"/"+self.run+"/gif/run"+self.run+"_hEndcap_bx.gif "+file1)
            os.system('mv '+ 'run'+self.run+'_hEndcap_bx.gif ' + self.tmppath)
        self.onPicture(file1)

    def histoEndcapCSP(self):
        file1 = self.tmppath+'run'+self.run+'_ClusterSize_for_Endcap_P.gif'
        if not os.path.exists(self.tmppath+'run'+self.run+'_ClusterSize_for_Endcap_P.gif'):
            os.system("cmsStageIn /store/caf/user/ccmuon/RPC/GlobalRuns/"+self.ds+"/"+self.run+"/gif/run"+self.run+"_ClusterSize_for_Endcap_P.gif "+file1)
            os.system('mv '+ 'run'+self.run+'_ClusterSize_for_Endcap_P.gif ' + self.tmppath)
        self.onPicture(file1)

    def histoEndcapCSN(self):
        file1 = self.tmppath+'run'+self.run+'_ClusterSize_for_Endcap_N.gif'
        if not os.path.exists(self.tmppath+'run'+self.run+'_ClusterSize_for_Endcap_N.gif'):
            os.system("cmsStageIn /store/caf/user/ccmuon/RPC/GlobalRuns/"+self.ds+"/"+self.run+"/gif/run"+self.run+"_ClusterSize_for_Endcap_N.gif "+file1)
            os.system('mv '+ 'run'+self.run+'_ClusterSize_for_Endcap_N.gif ' + self.tmppath)
        self.onPicture(file1)

    def histoEndcapMasked(self):
        file1 = self.tmppath+'run'+self.run+'_hEndcap_masked.gif'
        if not os.path.exists(self.tmppath+'run'+self.run+'_hEndcap_masked.gif'):
            os.system("cmsStageIn /store/caf/user/ccmuon/RPC/GlobalRuns/"+self.ds+"/"+self.run+"/gif/run"+self.run+"_hEndcap_masked.gif "+file1)
            os.system('mv '+ 'run'+self.run+'_hEndcap_masked.gif ' + self.tmppath)
        self.onPicture(file1)


##-------------------------------------------------------------------------------------------------------------------------------------------------------

    def histoWm2Bx(self):
        file1 = self.tmppath+'run'+self.run+'_BxDistribution_Wheel_m2.gif'
        if not os.path.exists(self.tmppath+'run'+self.run+'_BxDistribution_Wheel_m2.gif'):
            os.system("cmsStageIn /store/caf/user/ccmuon/RPC/GlobalRuns/"+self.ds+"/"+self.run+"/gif/run"+self.run+"_BxDistribution_Wheel_m2.gif "+file1)
            os.system('mv '+ 'run'+self.run+'_BxDistribution_Wheel_m2.gif ' + self.tmppath)
        self.onPicture(file1)

    def histoWm1Bx(self):
        file1 = self.tmppath+'run'+self.run+'_BxDistribution_Wheel_m1.gif'
        if not os.path.exists(self.tmppath+'run'+self.run+'_BxDistribution_Wheel_m1.gif'):
            os.system("cmsStageIn /store/caf/user/ccmuon/RPC/GlobalRuns/"+self.ds+"/"+self.run+"/gif/run"+self.run+"_BxDistribution_Wheel_m1.gif "+file1)
            os.system('mv '+ 'run'+self.run+'_BxDistribution_Wheel_m1.gif ' + self.tmppath)
        self.onPicture(file1)

    def histoW0Bx(self):
        file1 = self.tmppath+'run'+self.run+'_BxDistribution_Wheel_0.gif'
        if not os.path.exists(self.tmppath+'run'+self.run+'_BxDistribution_Wheel_0.gif'):
            os.system("cmsStageIn /store/caf/user/ccmuon/RPC/GlobalRuns/"+self.ds+"/"+self.run+"/gif/run"+self.run+"_BxDistribution_Wheel_0.gif "+file1)
            os.system('mv '+ 'run'+self.run+'_BxDistribution_Wheel_0.gif ' + self.tmppath)
        self.onPicture(file1)

    def histoWp1Bx(self):
        file1 = self.tmppath+'run'+self.run+'_BxDistribution_Wheel_p1.gif'
        if not os.path.exists(self.tmppath+'run'+self.run+'_BxDistribution_Wheel_p1.gif'):
            os.system("cmsStageIn /store/caf/user/ccmuon/RPC/GlobalRuns/"+self.ds+"/"+self.run+"/gif/run"+self.run+"_BxDistribution_Wheel_p1.gif "+file1)
            os.system('mv '+ 'run'+self.run+'_BxDistribution_Wheel_p1.gif ' + self.tmppath)
        self.onPicture(file1)
        
    def histoWp2Bx(self):
        file1 = self.tmppath+'run'+self.run+'_BxDistribution_Wheel_p2.gif'
        if not os.path.exists(self.tmppath+'run'+self.run+'_BxDistribution_Wheel_p2.gif'):
            os.system("cmsStageIn /store/caf/user/ccmuon/RPC/GlobalRuns/"+self.ds+"/"+self.run+"/gif/run"+self.run+"_BxDistribution_Wheel_p2.gif "+file1)
            os.system('mv '+ 'run'+self.run+'_BxDistribution_Wheel_p2.gif ' + self.tmppath)
        self.onPicture(file1)

    def histoDm1Bx(self):
        file1 = self.tmppath+'run'+self.run+'_BxDistribution_Disk_m1.gif'
        if not os.path.exists(self.tmppath+'run'+self.run+'_BxDistribution_Disk_m1.gif'):
            os.system("cmsStageIn /store/caf/user/ccmuon/RPC/GlobalRuns/"+self.ds+"/"+self.run+"/gif/run"+self.run+"_BxDistribution_Disk_m1.gif "+file1)
            os.system('mv '+ 'run'+self.run+'_BxDistribution_Disk_m1.gif ' + self.tmppath)
        self.onPicture(file1)

    def histoDm2Bx(self):
        file1 = self.tmppath+'run'+self.run+'_BxDistribution_Disk_m2.gif'
        if not os.path.exists(self.tmppath+'run'+self.run+'_BxDistribution_Disk_m2.gif'):
            os.system("cmsStageIn /store/caf/user/ccmuon/RPC/GlobalRuns/"+self.ds+"/"+self.run+"/gif/run"+self.run+"_BxDistribution_Disk_m2.gif "+file1)
            os.system('mv '+ 'run'+self.run+'_BxDistribution_Disk_m2.gif ' + self.tmppath)
        self.onPicture(file1)

    def histoDm3Bx(self):
        file1 = self.tmppath+'run'+self.run+'_BxDistribution_Disk_m3.gif'
        if not os.path.exists(self.tmppath+'run'+self.run+'_BxDistribution_Disk_m3.gif'):
            os.system("cmsStageIn /store/caf/user/ccmuon/RPC/GlobalRuns/"+self.ds+"/"+self.run+"/gif/run"+self.run+"_BxDistribution_Disk_m3.gif "+file1)
            os.system('mv '+ 'run'+self.run+'_BxDistribution_Disk_m3.gif ' + self.tmppath)
        self.onPicture(file1)

    def histoDp1Bx(self):
        file1 = self.tmppath+'run'+self.run+'_BxDistribution_Disk_p1.gif'
        if not os.path.exists(self.tmppath+'run'+self.run+'_BxDistribution_Disk_p1.gif'):
            os.system("cmsStageIn /store/caf/user/ccmuon/RPC/GlobalRuns/"+self.ds+"/"+self.run+"/gif/run"+self.run+"_BxDistribution_Disk_p1.gif "+file1)
            os.system('mv '+ 'run'+self.run+'_BxDistribution_Disk_p1.gif ' + self.tmppath)
        self.onPicture(file1)

    def histoDp2Bx(self):
        file1 = self.tmppath+'run'+self.run+'_BxDistribution_Disk_p2.gif'
        if not os.path.exists(self.tmppath+'run'+self.run+'_BxDistribution_Disk_p2.gif'):
            os.system("cmsStageIn /store/caf/user/ccmuon/RPC/GlobalRuns/"+self.ds+"/"+self.run+"/gif/run"+self.run+"_BxDistribution_Disk_p2.gif "+file1)
            os.system('mv '+ 'run'+self.run+'_BxDistribution_Disk_p2.gif ' + self.tmppath)
        self.onPicture(file1)

    def histoDp3Bx(self):
        file1 = self.tmppath+'run'+self.run+'_BxDistribution_Disk_p3.gif'
        if not os.path.exists(self.tmppath+'run'+self.run+'_BxDistribution_Disk_p3.gif'):
            os.system("cmsStageIn /store/caf/user/ccmuon/RPC/GlobalRuns/"+self.ds+"/"+self.run+"/gif/run"+self.run+"_BxDistribution_Disk_p3.gif "+file1)
            os.system('mv '+ 'run'+self.run+'_BxDistribution_Disk_p3.gif ' + self.tmppath)
        self.onPicture(file1)

##------------------------------------------- Cluster size -------------------------

    def histoWm2ClusterSize(self):
        file1 = self.tmppath+'run'+self.run+'_ClusterSize_Wheel_m2.gif'
        if not os.path.exists(self.tmppath+'run'+self.run+'_ClusterSize_Wheel_m2.gif'):
            os.system("cmsStageIn /store/caf/user/ccmuon/RPC/GlobalRuns/"+self.ds+"/"+self.run+"/gif/run"+self.run+"_ClusterSize_Wheel_m2.gif "+file1)
            os.system('mv '+ 'run'+self.run+'_ClusterSize_Wheel_m2.gif ' + self.tmppath)
        self.onPicture(file1)

    def histoWm1ClusterSize(self):
        file1 = self.tmppath+'run'+self.run+'_ClusterSize_Wheel_m1.gif'
        if not os.path.exists(self.tmppath+'run'+self.run+'_ClusterSize_Wheel_m1.gif'):
            os.system("cmsStageIn /store/caf/user/ccmuon/RPC/GlobalRuns/"+self.ds+"/"+self.run+"/gif/run"+self.run+"_ClusterSize_Wheel_m1.gif "+file1)
            os.system('mv '+ 'run'+self.run+'_ClusterSize_Wheel_m1.gif ' + self.tmppath)
        self.onPicture(file1)

    def histoW0ClusterSize(self):
        file1 = self.tmppath+'run'+self.run+'_ClusterSize_Wheel_0.gif'
        if not os.path.exists(self.tmppath+'run'+self.run+'_ClusterSize_Wheel_0.gif'):
            os.system("cmsStageIn /store/caf/user/ccmuon/RPC/GlobalRuns/"+self.ds+"/"+self.run+"/gif/run"+self.run+"_ClusterSize_Wheel_0.gif "+file1)
            os.system('mv '+ 'run'+self.run+'_ClusterSize_Wheel_0.gif ' + self.tmppath)
        self.onPicture(file1)

    def histoWp1ClusterSize(self):
        file1 = self.tmppath+'run'+self.run+'_ClusterSize_Wheel_p1.gif'
        if not os.path.exists(self.tmppath+'run'+self.run+'_ClusterSize_Wheel_p1.gif'):
            os.system("cmsStageIn /store/caf/user/ccmuon/RPC/GlobalRuns/"+self.ds+"/"+self.run+"/gif/run"+self.run+"_ClusterSize_Wheel_p1.gif "+file1)
            os.system('mv '+ 'run'+self.run+'_ClusterSize_Wheel_p1.gif ' + self.tmppath)
        self.onPicture(file1)
        
    def histoWp2ClusterSize(self):
        file1 = self.tmppath+'run'+self.run+'_ClusterSize_Wheel_p2.gif'
        if not os.path.exists(self.tmppath+'run'+self.run+'_ClusterSize_Wheel_p2.gif'):
            os.system("cmsStageIn /store/caf/user/ccmuon/RPC/GlobalRuns/"+self.ds+"/"+self.run+"/gif/run"+self.run+"_ClusterSize_Wheel_p2.gif "+file1)
            os.system('mv '+ 'run'+self.run+'_ClusterSize_Wheel_p2.gif ' + self.tmppath)
        self.onPicture(file1)

    def histoDm1ClusterSize(self):
        file1 = self.tmppath+'run'+self.run+'_ClusterSize_Disk_m1.gif'
        if not os.path.exists(self.tmppath+'run'+self.run+'_ClusterSize_Disk_m1.gif'):
            os.system("cmsStageIn /store/caf/user/ccmuon/RPC/GlobalRuns/"+self.ds+"/"+self.run+"/gif/run"+self.run+"_ClusterSize_Disk_m1.gif "+file1)
            os.system('mv '+ 'run'+self.run+'_ClusterSize_Disk_m1.gif ' + self.tmppath)
        self.onPicture(file1)

    def histoDm2ClusterSize(self):
        file1 = self.tmppath+'run'+self.run+'_ClusterSize_Disk_m2.gif'
        if not os.path.exists(self.tmppath+'run'+self.run+'_ClusterSize_Disk_m2.gif'):
            os.system("cmsStageIn /store/caf/user/ccmuon/RPC/GlobalRuns/"+self.ds+"/"+self.run+"/gif/run"+self.run+"_ClusterSize_Disk_m2.gif "+file1)
            os.system('mv '+ 'run'+self.run+'_ClusterSize_Disk_m2.gif ' + self.tmppath)
        self.onPicture(file1)

    def histoDm3ClusterSize(self):
        file1 = self.tmppath+'run'+self.run+'_ClusterSize_Disk_m3.gif'
        if not os.path.exists(self.tmppath+'run'+self.run+'_ClusterSize_Disk_m3.gif'):
            os.system("cmsStageIn /store/caf/user/ccmuon/RPC/GlobalRuns/"+self.ds+"/"+self.run+"/gif/run"+self.run+"_ClusterSize_Disk_m3.gif "+file1)
            os.system('mv '+ 'run'+self.run+'_ClusterSize_Disk_m3.gif ' + self.tmppath)
        self.onPicture(file1)

    def histoDp1ClusterSize(self):
        file1 = self.tmppath+'run'+self.run+'_ClusterSize_Disk_p1.gif'
        if not os.path.exists(self.tmppath+'run'+self.run+'_ClusterSize_Disk_p1.gif'):
            os.system("cmsStageIn /store/caf/user/ccmuon/RPC/GlobalRuns/"+self.ds+"/"+self.run+"/gif/run"+self.run+"_ClusterSize_Disk_p1.gif "+file1)
            os.system('mv '+ 'run'+self.run+'_ClusterSize_Disk_p1.gif ' + self.tmppath)
        self.onPicture(file1)

    def histoDp2ClusterSize(self):
        file1 = self.tmppath+'run'+self.run+'_ClusterSize_Disk_p2.gif'
        if not os.path.exists(self.tmppath+'run'+self.run+'_ClusterSize_Disk_p2.gif'):
            os.system("cmsStageIn /store/caf/user/ccmuon/RPC/GlobalRuns/"+self.ds+"/"+self.run+"/gif/run"+self.run+"_ClusterSize_Disk_p2.gif "+file1)
            os.system('mv '+ 'run'+self.run+'_ClusterSize_Disk_p2.gif ' + self.tmppath)
        self.onPicture(file1)

    def histoDp3ClusterSize(self):
        file1 = self.tmppath+'run'+self.run+'_ClusterSize_Disk_p3.gif'
        if not os.path.exists(self.tmppath+'run'+self.run+'_ClusterSize_Disk_p3.gif'):
            os.system("cmsStageIn /store/caf/user/ccmuon/RPC/GlobalRuns/"+self.ds+"/"+self.run+"/gif/run"+self.run+"_ClusterSize_Disk_p3.gif "+file1)
            os.system('mv '+ 'run'+self.run+'_ClusterSize_Disk_p3.gif ' + self.tmppath)
        self.onPicture(file1)       

        
##------------------------------------------- Barrel Effi Global Distribution Function ---------------------------------------------------------------

    def histoWm2NearEff(self):
        file1 = self.tmppath+'run'+self.run+'_c_wheel_m2_near.gif'
        if not os.path.exists(self.tmppath+'run'+self.run+'_c_wheel_m2_near.gif'):
            os.system("cmsStageIn /store/caf/user/ccmuon/RPC/GlobalRuns/"+self.ds+"/"+self.run+"/gif/run"+self.run+"_c_wheel_m2_near.gif "+file1)
            os.system('mv '+ 'run'+self.run+'_c_wheel_m2_near.gif ' + self.tmppath)
        self.onPicture(file1)

    def histoWm2FarEff(self):
        file1 = self.tmppath+'run'+self.run+'_c_wheel_m2_Far.gif'
        if not os.path.exists(self.tmppath+'run'+self.run+'_c_wheel_m2_Far.gif'):
            os.system("cmsStageIn /store/caf/user/ccmuon/RPC/GlobalRuns/"+self.ds+"/"+self.run+"/gif/run"+self.run+"_c_wheel_m2_Far.gif "+file1)
            os.system('mv '+ 'run'+self.run+'_c_wheel_m2_Far.gif ' + self.tmppath)
        self.onPicture(file1)

    def histoWm1NearEff(self):
        file1 = self.tmppath+'run'+self.run+'_c_wheel_m1_near.gif'
        if not os.path.exists(self.tmppath+'run'+self.run+'_c_wheel_m1_near.gif'):
            os.system("cmsStageIn /store/caf/user/ccmuon/RPC/GlobalRuns/"+self.ds+"/"+self.run+"/gif/run"+self.run+"_c_wheel_m1_near.gif "+file1)
            os.system('mv '+ 'run'+self.run+'_c_wheel_m1_near.gif ' + self.tmppath)
        self.onPicture(file1)

    def histoWm1FarEff(self):
        file1 = self.tmppath+'run'+self.run+'_c_wheel_m1_Far.gif'
        if not os.path.exists(self.tmppath+'run'+self.run+'_c_wheel_m1_Far.gif'):
            os.system("cmsStageIn /store/caf/user/ccmuon/RPC/GlobalRuns/"+self.ds+"/"+self.run+"/gif/run"+self.run+"_c_wheel_m1_Far.gif "+file1)
            os.system('mv '+ 'run'+self.run+'_c_wheel_m1_Far.gif ' + self.tmppath)
        self.onPicture(file1)

    def histoW0NearEff(self):
        file1 = self.tmppath+'run'+self.run+'_c_wheel_0_near.gif'
        if not os.path.exists(self.tmppath+'run'+self.run+'_c_wheel_0_near.gif'):
            os.system("cmsStageIn /store/caf/user/ccmuon/RPC/GlobalRuns/"+self.ds+"/"+self.run+"/gif/run"+self.run+"_c_wheel_0_near.gif "+file1)
            os.system('mv '+ 'run'+self.run+'_c_wheel_0_near.gif ' + self.tmppath)
        self.onPicture(file1)

    def histoW0FarEff(self):
        file1 = self.tmppath+'run'+self.run+'_c_wheel_0_Far.gif'
        if not os.path.exists(self.tmppath+'run'+self.run+'_c_wheel_0_Far.gif'):
            os.system("cmsStageIn /store/caf/user/ccmuon/RPC/GlobalRuns/"+self.ds+"/"+self.run+"/gif/run"+self.run+"_c_wheel_0_Far.gif "+file1)
            os.system('mv '+ 'run'+self.run+'_c_wheel_0_Far.gif ' + self.tmppath)
        self.onPicture(file1)

    def histoWp1NearEff(self):
        file1 = self.tmppath+'run'+self.run+'_c_wheel_p1_near.gif'
        if not os.path.exists(self.tmppath+'run'+self.run+'_c_wheel_p1_near.gif'):
            os.system("cmsStageIn /store/caf/user/ccmuon/RPC/GlobalRuns/"+self.ds+"/"+self.run+"/gif/run"+self.run+"_c_wheel_p1_near.gif "+file1)
            os.system('mv '+ 'run'+self.run+'_c_wheel_p1_near.gif ' + self.tmppath)
        self.onPicture(file1)

    def histoWp1FarEff(self):
        file1 = self.tmppath+'run'+self.run+'_c_wheel_p1_Far.gif'
        if not os.path.exists(self.tmppath+'run'+self.run+'_c_wheel_p2_Far.gif'):
            os.system("cmsStageIn /store/caf/user/ccmuon/RPC/GlobalRuns/"+self.ds+"/"+self.run+"/gif/run"+self.run+"_c_wheel_p1_Far.gif "+file1)
            os.system('mv '+ 'run'+self.run+'_c_wheel_p1_Far.gif ' + self.tmppath)
        self.onPicture(file1)

    def histoWp2NearEff(self):
        file1 = self.tmppath+'run'+self.run+'_c_wheel_p2_near.gif'
        if not os.path.exists(self.tmppath+'run'+self.run+'_c_wheel_p2_near.gif'):
            os.system("cmsStageIn /store/caf/user/ccmuon/RPC/GlobalRuns/"+self.ds+"/"+self.run+"/gif/run"+self.run+"_c_wheel_p2_near.gif "+file1)
            os.system('mv '+ 'run'+self.run+'_c_wheel_p2_near.gif ' + self.tmppath)
        self.onPicture(file1)

    def histoWp2FarEff(self):
        file1 = self.tmppath+'run'+self.run+'_c_wheel_p2_Far.gif'
        if not os.path.exists(self.tmppath+'run'+self.run+'_c_wheel_p2_Far.gif'):
            os.system("cmsStageIn /store/caf/user/ccmuon/RPC/GlobalRuns/"+self.ds+"/"+self.run+"/gif/run"+self.run+"_c_wheel_p2_Far.gif "+file1)
            os.system('mv '+ 'run'+self.run+'_c_wheel_p2_Far.gif ' + self.tmppath)
        self.onPicture(file1)

##----------------------------------- Endcap Effi Global Distribution Function -------------------------------------------------------------------------

    def histoDm1RE1GloEff(self):
        file1 = self.tmppath+'run'+self.run+'_c_disk_m1_RE1.gif'
        if not os.path.exists(self.tmppath+'run'+self.run+'_c_disk_m1_RE1.gif'):
            os.system("cmsStageIn /store/caf/user/ccmuon/RPC/GlobalRuns/"+self.ds+"/"+self.run+"/gif/run"+self.run+"_c_disk_m1_RE1.gif "+file1)
            os.system('mv '+ 'run'+self.run+'_c_disk_m1_RE1.gif ' + self.tmppath)
        self.onPicture(file1)

    def histoDm1RE2GloEff(self):
        file1 = self.tmppath+'run'+self.run+'_c_disk_m1_RE2.gif'
        if not os.path.exists(self.tmppath+'run'+self.run+'_c_disk_m1_RE2.gif'):
            os.system("cmsStageIn /store/caf/user/ccmuon/RPC/GlobalRuns/"+self.ds+"/"+self.run+"/gif/run"+self.run+"_c_disk_m1_RE2.gif "+file1)
            os.system('mv '+ 'run'+self.run+'_c_disk_m1_RE2.gif ' + self.tmppath)
        self.onPicture(file1)

    def histoDm1RE3GloEff(self):
        file1 = self.tmppath+'run'+self.run+'_c_disk_m1_RE3.gif'
        if not os.path.exists(self.tmppath+'run'+self.run+'_c_disk_m1_RE3.gif'):
            os.system("cmsStageIn /store/caf/user/ccmuon/RPC/GlobalRuns/"+self.ds+"/"+self.run+"/gif/run"+self.run+"_c_disk_m1_RE3.gif "+file1)
            os.system('mv '+ 'run'+self.run+'_c_disk_m1_RE3.gif ' + self.tmppath)
        self.onPicture(file1)

    def histoDm2RE1GloEff(self):
        file1 = self.tmppath+'run'+self.run+'_c_disk_m2_RE1.gif'
        if not os.path.exists(self.tmppath+'run'+self.run+'_c_disk_m2_RE1.gif'):
            os.system("cmsStageIn /store/caf/user/ccmuon/RPC/GlobalRuns/"+self.ds+"/"+self.run+"/gif/run"+self.run+"_c_disk_m2_RE1.gif "+file1)
            os.system('mv '+ 'run'+self.run+'_c_disk_m2_RE1.gif ' + self.tmppath)
        self.onPicture(file1)

    def histoDm2RE2GloEff(self):
        file1 = self.tmppath+'run'+self.run+'_c_disk_m2_RE2.gif'
        if not os.path.exists(self.tmppath+'run'+self.run+'_c_disk_m2_RE2.gif'):
            os.system("cmsStageIn /store/caf/user/ccmuon/RPC/GlobalRuns/"+self.ds+"/"+self.run+"/gif/run"+self.run+"_c_disk_m2_RE2.gif "+file1)
            os.system('mv '+ 'run'+self.run+'_c_disk_m2_RE2.gif ' + self.tmppath)
        self.onPicture(file1)

    def histoDm2RE3GloEff(self):
        file1 = self.tmppath+'run'+self.run+'_c_disk_m2_RE3.gif'
        if not os.path.exists(self.tmppath+'run'+self.run+'_c_disk_m2_RE3.gif'):
            os.system("cmsStageIn /store/caf/user/ccmuon/RPC/GlobalRuns/"+self.ds+"/"+self.run+"/gif/run"+self.run+"_c_disk_m2_RE3.gif "+file1)
            os.system('mv '+ 'run'+self.run+'_c_disk_m2_RE3.gif ' + self.tmppath)
        self.onPicture(file1)

    def histoDm3RE1GloEff(self):
        file1 = self.tmppath+'run'+self.run+'_c_disk_m3_RE1.gif'
        if not os.path.exists(self.tmppath+'run'+self.run+'_c_disk_m3_RE1.gif'):
            os.system("cmsStageIn /store/caf/user/ccmuon/RPC/GlobalRuns/"+self.ds+"/"+self.run+"/gif/run"+self.run+"_c_disk_m3_RE1.gif "+file1)
            os.system('mv '+ 'run'+self.run+'_c_disk_m3_RE1.gif ' + self.tmppath)
        self.onPicture(file1)

    def histoDm3RE2GloEff(self):
        file1 = self.tmppath+'run'+self.run+'_c_disk_m3_RE2.gif'
        if not os.path.exists(self.tmppath+'run'+self.run+'_c_disk_m3_RE2.gif'):
            os.system("cmsStageIn /store/caf/user/ccmuon/RPC/GlobalRuns/"+self.ds+"/"+self.run+"/gif/run"+self.run+"_c_disk_m3_RE2.gif "+file1)
            os.system('mv '+ 'run'+self.run+'_c_disk_m3_RE2.gif ' + self.tmppath)
        self.onPicture(file1)

    def histoDm3RE3GloEff(self):
        file1 = self.tmppath+'run'+self.run+'_c_disk_m3_RE3.gif'
        if not os.path.exists(self.tmppath+'run'+self.run+'_c_disk_m3_RE3.gif'):
            os.system("cmsStageIn /store/caf/user/ccmuon/RPC/GlobalRuns/"+self.ds+"/"+self.run+"/gif/run"+self.run+"_c_disk_m3_RE3.gif "+file1)
            os.system('mv '+ 'run'+self.run+'_c_disk_m3_RE3.gif ' + self.tmppath)
        self.onPicture(file1)

    def histoDp1RE1GloEff(self):
        file1 = self.tmppath+'run'+self.run+'_c_disk_p1_RE1.gif'
        if not os.path.exists(self.tmppath+'run'+self.run+'_c_disk_p1_RE1.gif'):
            os.system("cmsStageIn /store/caf/user/ccmuon/RPC/GlobalRuns/"+self.ds+"/"+self.run+"/gif/run"+self.run+"_c_disk_p1_RE1.gif "+file1)
            os.system('mv '+ 'run'+self.run+'_c_disk_p1_RE1.gif ' + self.tmppath)
        self.onPicture(file1)

    def histoDp1RE2GloEff(self):
        file1 = self.tmppath+'run'+self.run+'_c_disk_p1_RE2.gif'
        if not os.path.exists(self.tmppath+'run'+self.run+'_c_disk_p1_RE2.gif'):
            os.system("cmsStageIn /store/caf/user/ccmuon/RPC/GlobalRuns/"+self.ds+"/"+self.run+"/gif/run"+self.run+"_c_disk_p1_RE2.gif "+file1)
            os.system('mv '+ 'run'+self.run+'_c_disk_p1_RE2.gif ' + self.tmppath)
        self.onPicture(file1)

    def histoDp1RE3GloEff(self):
        file1 = self.tmppath+'run'+self.run+'_c_disk_p1_RE3.gif'
        if not os.path.exists(self.tmppath+'run'+self.run+'_c_disk_p1_RE3.gif'):
            os.system("cmsStageIn /store/caf/user/ccmuon/RPC/GlobalRuns/"+self.ds+"/"+self.run+"/gif/run"+self.run+"_c_disk_p1_RE3.gif "+file1)
            os.system('mv '+ 'run'+self.run+'_c_disk_p1_RE3.gif ' + self.tmppath)
        self.onPicture(file1)

    def histoDp2RE1GloEff(self):
        file1 = self.tmppath+'run'+self.run+'_c_disk_p2_RE1.gif'
        if not os.path.exists(self.tmppath+'run'+self.run+'_c_disk_p2_RE1.gif'):
            os.system("cmsStageIn /store/caf/user/ccmuon/RPC/GlobalRuns/"+self.ds+"/"+self.run+"/gif/run"+self.run+"_c_disk_p2_RE1.gif "+file1)
            os.system('mv '+ 'run'+self.run+'_c_disk_p2_RE1.gif ' + self.tmppath)
        self.onPicture(file1)

    def histoDp2RE2GloEff(self):
        file1 = self.tmppath+'run'+self.run+'_c_disk_p2_RE2.gif'
        if not os.path.exists(self.tmppath+'run'+self.run+'_c_disk_p2_RE2.gif'):
            os.system("cmsStageIn /store/caf/user/ccmuon/RPC/GlobalRuns/"+self.ds+"/"+self.run+"/gif/run"+self.run+"_c_disk_p2_RE2.gif "+file1)
            os.system('mv '+ 'run'+self.run+'_c_disk_p2_RE2.gif ' + self.tmppath)
        self.onPicture(file1)

    def histoDp2RE3GloEff(self):
        file1 = self.tmppath+'run'+self.run+'_c_disk_p2_RE3.gif'
        if not os.path.exists(self.tmppath+'run'+self.run+'_c_disk_p2_RE3.gif'):
            os.system("cmsStageIn /store/caf/user/ccmuon/RPC/GlobalRuns/"+self.ds+"/"+self.run+"/gif/run"+self.run+"_c_disk_p2_RE3.gif "+file1)
            os.system('mv '+ 'run'+self.run+'_c_disk_p2_RE3.gif ' + self.tmppath)
        self.onPicture(file1)

    def histoDp3RE1GloEff(self):
        file1 = self.tmppath+'run'+self.run+'_c_disk_p3_RE1.gif'
        if not os.path.exists(self.tmppath+'run'+self.run+'_c_disk_p3_RE1.gif'):
            os.system("cmsStageIn /store/caf/user/ccmuon/RPC/GlobalRuns/"+self.ds+"/"+self.run+"/gif/run"+self.run+"_c_disk_p3_RE1.gif "+file1)
            os.system('mv '+ 'run'+self.run+'_c_disk_p3_RE1.gif ' + self.tmppath)
        self.onPicture(file1)

    def histoDp3RE2GloEff(self):
        file1 = self.tmppath+'run'+self.run+'_c_disk_p3_RE2.gif'
        if not os.path.exists(self.tmppath+'run'+self.run+'_c_disk_p3_RE2.gif'):
            os.system("cmsStageIn /store/caf/user/ccmuon/RPC/GlobalRuns/"+self.ds+"/"+self.run+"/gif/run"+self.run+"_c_disk_p3_RE2.gif "+file1)
            os.system('mv '+ 'run'+self.run+'_c_disk_p3_RE2.gif ' + self.tmppath)
        self.onPicture(file1)

    def histoDp3RE3GloEff(self):
        file1 = self.tmppath+'run'+self.run+'_c_disk_p3_RE3.gif'
        if not os.path.exists(self.tmppath+'run'+self.run+'_c_disk_p3_RE3.gif'):
            os.system("cmsStageIn /store/caf/user/ccmuon/RPC/GlobalRuns/"+self.ds+"/"+self.run+"/gif/run"+self.run+"_c_disk_p3_RE3.gif "+file1)
            os.system('mv '+ 'run'+self.run+'_c_disk_p3_RE3.gif ' + self.tmppath)
        self.onPicture(file1)


##--------------------------------------------------- Effi Profile Function  -----------------------------------------------------------------------------

    def histoWm2Eff(self):
        file1 = self.tmppath+'run'+self.run+'_hWm2_eff.gif'
        if not os.path.exists(self.tmppath+'run'+self.run+'_hWm2_eff.gif'):
            os.system("cmsStageIn /store/caf/user/ccmuon/RPC/GlobalRuns/"+self.ds+"/"+self.run+"/gif/run"+self.run+"_hWm2_eff.gif "+file1)
            os.system('mv '+ 'run'+self.run+'_hWm2_eff.gif ' + self.tmppath)
        self.onPicture(file1)

    def histoWm1Eff(self):
        file1 = self.tmppath+'run'+self.run+'_hWm1_eff.gif'
        if not os.path.exists(self.tmppath+'run'+self.run+'_hWm1_eff.gif'):
            os.system("cmsStageIn /store/caf/user/ccmuon/RPC/GlobalRuns/"+self.ds+"/"+self.run+"/gif/run"+self.run+"_hWm1_eff.gif "+file1)
            os.system('mv '+ 'run'+self.run+'_hWm1_eff.gif ' + self.tmppath)
        self.onPicture(file1)

    def histoW0Eff(self):
        file1 = self.tmppath+'run'+self.run+'_hW0_eff.gif'
        if not os.path.exists(self.tmppath+'run'+self.run+'_hW0_eff.gif'):
            os.system("cmsStageIn /store/caf/user/ccmuon/RPC/GlobalRuns/"+self.ds+"/"+self.run+"/gif/run"+self.run+"_hW0_eff.gif "+file1)
            os.system('mv '+ 'run'+self.run+'_hWm0_eff.gif ' + self.tmppath)
        self.onPicture(file1)

    def histoWp1Eff(self):
        file1 = self.tmppath+'run'+self.run+'_hWp1_eff.gif'
        if not os.path.exists(self.tmppath+'run'+self.run+'_hWp1_eff.gif'):
            os.system("cmsStageIn /store/caf/user/ccmuon/RPC/GlobalRuns/"+self.ds+"/"+self.run+"/gif/run"+self.run+"_hWp1_eff.gif "+file1)
            os.system('mv '+ 'run'+self.run+'_hWp_eff.gif ' + self.tmppath)
        self.onPicture(file1)

    def histoWp2Eff(self):
        file1 = self.tmppath+'run'+self.run+'_hWp2_eff.gif'
        if not os.path.exists(self.tmppath+'run'+self.run+'_hWp2_eff.gif'):
            os.system("cmsStageIn /store/caf/user/ccmuon/RPC/GlobalRuns/"+self.ds+"/"+self.run+"/gif/run"+self.run+"_hWp2_eff.gif "+file1)
            os.system('mv '+ 'run'+self.run+'_hWp2_eff.gif ' + self.tmppath)
        self.onPicture(file1)

    def histoDm1Eff(self):
        file1 = self.tmppath+'run'+self.run+'_hDm1_eff.gif'
        if not os.path.exists(self.tmppath+'run'+self.run+'_hDm1_eff.gif'):
            os.system("cmsStageIn /store/caf/user/ccmuon/RPC/GlobalRuns/"+self.ds+"/"+self.run+"/gif/run"+self.run+"_hDm1_eff.gif "+file1)
            os.system('mv '+ 'run'+self.run+'_hDm1_eff.gif ' + self.tmppath)
        self.onPicture(file1)

    def histoDm2Eff(self):
        file1 = self.tmppath+'run'+self.run+'_hDm2_eff.gif'
        if not os.path.exists(self.tmppath+'run'+self.run+'_hDm2_eff.gif'):
            os.system("cmsStageIn /store/caf/user/ccmuon/RPC/GlobalRuns/"+self.ds+"/"+self.run+"/gif/run"+self.run+"_hDm2_eff.gif "+file1)
            os.system('mv '+ 'run'+self.run+'_hDm2_eff.gif ' + self.tmppath)
        self.onPicture(file1)

    def histoDm3Eff(self):
        file1 = self.tmppath+'run'+self.run+'_hDm3_eff.gif'
        if not os.path.exists(self.tmppath+'run'+self.run+'_hDm3_eff.gif'):
            os.system("cmsStageIn /store/caf/user/ccmuon/RPC/GlobalRuns/"+self.ds+"/"+self.run+"/gif/run"+self.run+"_hDm3_eff.gif "+file1)
            os.system('mv '+ 'run'+self.run+'_hDm3_eff.gif ' + self.tmppath)
        self.onPicture(file1)

    def histoDp1Eff(self):
        file1 = self.tmppath+'run'+self.run+'_hDp1_eff.gif'
        if not os.path.exists(self.tmppath+'run'+self.run+'_hDp1_eff.gif'):
            os.system("cmsStageIn /store/caf/user/ccmuon/RPC/GlobalRuns/"+self.ds+"/"+self.run+"/gif/run"+self.run+"_hDp1_eff.gif "+file1)
            os.system('mv '+ 'run'+self.run+'_hDp1_eff.gif ' + self.tmppath)
        self.onPicture(file1)        
        
    def histoDp2Eff(self):
        file1 = self.tmppath+'run'+self.run+'_hDp2_eff.gif'
        if not os.path.exists(self.tmppath+'run'+self.run+'_hDp2_eff.gif'):
            os.system("cmsStageIn /store/caf/user/ccmuon/RPC/GlobalRuns/"+self.ds+"/"+self.run+"/gif/run"+self.run+"_hDp2_eff.gif "+file1)
            os.system('mv '+ 'run'+self.run+'_hDp2_eff.gif ' + self.tmppath)
        self.onPicture(file1)

    def histoDp3Eff(self):
        file1 = self.tmppath+'run'+self.run+'_hDp3_eff.gif'
        if not os.path.exists(self.tmppath+'run'+self.run+'_hDp3_eff.gif'):
            os.system("cmsStageIn /store/caf/user/ccmuon/RPC/GlobalRuns/"+self.ds+"/"+self.run+"/gif/run"+self.run+"_hDp3_eff.gif "+file1)
            os.system('mv '+ 'run'+self.run+'_hDp3_eff.gif ' + self.tmppath)
        self.onPicture(file1) 
        
##---------------------------------------- Masked function -----------------------------------------------------------------------------------

    def histoWm2Masked(self):
        file1 = self.tmppath+'run'+self.run+'_hWm2_masked.gif'
        if not os.path.exists(self.tmppath+'run'+self.run+'_hWm2_masked.gif'):
            os.system("cmsStageIn /store/caf/user/ccmuon/RPC/GlobalRuns/"+self.ds+"/"+self.run+"/gif/run"+self.run+"_hWm2_masked.gif "+file1)
            os.system('mv '+ 'run'+self.run+'_hWm2_masked.gif ' + self.tmppath)
        self.onPicture(file1)

    def histoWm1Masked(self):
        file1 = self.tmppath+'run'+self.run+'_hWm1_masked.gif'
        if not os.path.exists(self.tmppath+'run'+self.run+'_hWm1_masked.gif'):
            os.system("cmsStageIn /store/caf/user/ccmuon/RPC/GlobalRuns/"+self.ds+"/"+self.run+"/gif/run"+self.run+"_hWm1_masked.gif "+file1)
            os.system('mv '+ 'run'+self.run+'_hWm1_masked.gif ' + self.tmppath)
        self.onPicture(file1)

    def histoW0Masked(self):
        file1 = self.tmppath+'run'+self.run+'_hW0_masked.gif'
        if not os.path.exists(self.tmppath+'run'+self.run+'_hW0_masked.gif'):
            os.system("cmsStageIn /store/caf/user/ccmuon/RPC/GlobalRuns/"+self.ds+"/"+self.run+"/gif/run"+self.run+"_hW0_masked.gif "+file1)
            os.system('mv '+ 'run'+self.run+'_hW0_masked.gif ' + self.tmppath)
        self.onPicture(file1)

    def histoWp1Masked(self):
        file1 = self.tmppath+'run'+self.run+'_hWp1_masked.gif'
        if not os.path.exists(self.tmppath+'run'+self.run+'_hWp1_masked.gif'):
            os.system("cmsStageIn /store/caf/user/ccmuon/RPC/GlobalRuns/"+self.ds+"/"+self.run+"/gif/run"+self.run+"_hWp1_masked.gif "+file1)
            os.system('mv '+ 'run'+self.run+'_hWp1_masked.gif ' + self.tmppath)
        self.onPicture(file1)

    def histoWp2Masked(self):
        file1 = self.tmppath+'run'+self.run+'_hWp2_masked.gif'
        if not os.path.exists(self.tmppath+'run'+self.run+'_hWp2_masked.gif'):
            os.system("cmsStageIn /store/caf/user/ccmuon/RPC/GlobalRuns/"+self.ds+"/"+self.run+"/gif/run"+self.run+"_hWp2_masked.gif "+file1)
            os.system('mv '+ 'run'+self.run+'_hWp2_masked.gif ' + self.tmppath)
        self.onPicture(file1)

    def histoDm1Masked(self):
        file1 = self.tmppath+'run'+self.run+'_hDm1_masked.gif'
        if not os.path.exists(self.tmppath+'run'+self.run+'_hDm1_masked.gif'):
            os.system("cmsStageIn /store/caf/user/ccmuon/RPC/GlobalRuns/"+self.ds+"/"+self.run+"/gif/run"+self.run+"_hDm1_masked.gif "+file1)
            os.system('mv '+ 'run'+self.run+'_hDm1_masked.gif ' + self.tmppath)
        self.onPicture(file1)

    def histoDm2Masked(self):
        file1 = self.tmppath+'run'+self.run+'_hDm2_masked.gif'
        if not os.path.exists(self.tmppath+'run'+self.run+'_hDm2_masked.gif'):
            os.system("cmsStageIn /store/caf/user/ccmuon/RPC/GlobalRuns/"+self.ds+"/"+self.run+"/gif/run"+self.run+"_hDm2_masked.gif "+file1)
            os.system('mv '+ 'run'+self.run+'_hDm2_masked.gif ' + self.tmppath)
        self.onPicture(file1)

    def histoDm3Masked(self):
        file1 = self.tmppath+'run'+self.run+'_hDm3_masked.gif'
        if not os.path.exists(self.tmppath+'run'+self.run+'_hDm3_masked.gif'):
            os.system("cmsStageIn /store/caf/user/ccmuon/RPC/GlobalRuns/"+self.ds+"/"+self.run+"/gif/run"+self.run+"_hDm3_masked.gif "+file1)
            os.system('mv '+ 'run'+self.run+'_hDm3_masked.gif ' + self.tmppath)
        self.onPicture(file1)

    def histoDp1Masked(self):
        file1 = self.tmppath+'run'+self.run+'_hDp1_masked.gif'
        if not os.path.exists(self.tmppath+'run'+self.run+'_hDp1_masked.gif'):
            os.system("cmsStageIn /store/caf/user/ccmuon/RPC/GlobalRuns/"+self.ds+"/"+self.run+"/gif/run"+self.run+"_hDp1_masked.gif "+file1)
            os.system('mv '+ 'run'+self.run+'_hDp1_masked.gif ' + self.tmppath)
        self.onPicture(file1)        
        
    def histoDp2Masked(self):
        file1 = self.tmppath+'run'+self.run+'_hDp2_masked.gif'
        if not os.path.exists(self.tmppath+'run'+self.run+'_hDp2_masked.gif'):
            os.system("cmsStageIn /store/caf/user/ccmuon/RPC/GlobalRuns/"+self.ds+"/"+self.run+"/gif/run"+self.run+"_hDp2_masked.gif "+file1)
            os.system('mv '+ 'run'+self.run+'_hDp2_masked.gif ' + self.tmppath)
        self.onPicture(file1)

    def histoDp3Masked(self):
        file1 = self.tmppath+'run'+self.run+'_hDp3_masked.gif'
        if not os.path.exists(self.tmppath+'run'+self.run+'_hDp3_masked.gif'):
            os.system("cmsStageIn /store/caf/user/ccmuon/RPC/GlobalRuns/"+self.ds+"/"+self.run+"/gif/run"+self.run+"_hDp3_masked.gif "+file1)
            os.system('mv '+ 'run'+self.run+'_hDp3_masked.gif ' + self.tmppath)
        self.onPicture(file1)         

#-------------------------------------------------------------------------------------------------------------------------------------------------

    def makeWidgets(self):
        self.canvas = Canvas(self, bg='white', height=Height, width=Width)
        self.canvas.pack(side=LEFT, fill=BOTH, expand=YES)

        Button(self, text='Open',  command=self.onOpen).pack(fill=X)
        Button(self, text='Quit',  command=self.onQuit).pack(fill=X)
        self.makeMenuBar()

    def makeMenuBar(self):
        self.menubar = Frame(self, relief=RAISED, bd=2)
        self.menubar.pack(side=TOP, fill=X)

        self.BarrelMenu()
        self.Wm2Menu()
        self.Wm1Menu()
        self.W0Menu()
        self.Wp1Menu()
        self.Wp2Menu()

        self.EndcapMenu()
        self.Dm1Menu()
        self.Dm2Menu()
        self.Dm3Menu()
        self.Dp1Menu()
        self.Dp2Menu()
        self.Dp3Menu()
        
    def BarrelMenu(self):
        mbutton = Menubutton(self.menubar, text='Barrel  ', underline=0)
        mbutton.pack(side=TOP)
        mbutton.config(bg='white',bd=4,relief=RAISED)
        menu = Menu(mbutton)
        menu.add_command(label='Bunch Crossing', command=self.histoBarrelBx)
        menu.add_command(label='Cluster Size', command=self.histoBarrelCS) ## ?
        menu.add_command(label='Efficiency', command=self.histoBarrelEff) ## ?
        menu.add_command(label='Msked Strips', command=self.histoBarrelMasked) ## ?
        mbutton['menu'] = menu
        return mbutton

    def EndcapMenu(self):
        mbutton = Menubutton(self.menubar, text='Endcap  ', underline=0)
        mbutton.pack(side=TOP)
        mbutton.config(bg='white',bd=4,relief=RAISED)
        menu = Menu(mbutton)
        menu.add_command(label='Bunch Crossing',command=self.histoEndcapBx)
        menu.add_command(label='Cluster Size of Positive', command=self.histoEndcapCSP) ## ?
        menu.add_command(label='Cluster Size of Negative', command=self.histoEndcapCSN) ## ?
        menu.add_command(label='Efficiency', command=self.histoEndcapEff) ## ?
        menu.add_command(label='Masked Strips', command=self.histoEndcapMasked) ## ?
        mbutton['menu'] = menu
        return mbutton

    def Wm2Menu(self):
        mbutton = Menubutton(self.menubar, text='Wheel -2  ', underline=0)
        mbutton.pack(side=TOP)
        mbutton.config(bg='white',bd=4,relief=RAISED)
        menu = Menu(mbutton)
        menu.add_command(label='Bunch Crossing', command=self.histoWm2Bx)
        menu.add_command(label='Cluster Size', command=self.histoWm2ClusterSize)
        menu.add_command(label='Wheel -2 Efficiency', command=self.histoWm2Eff) ##
        menu.add_command(label='Nearside Efficiency', command=self.histoWm2NearEff) ##
        menu.add_command(label='Farside Efficiency', command=self.histoWm2FarEff) ##
        menu.add_command(label='Masked Strips', command=self.histoWm2Masked)
        mbutton['menu'] = menu
        return mbutton

    def Wm1Menu(self):
        mbutton = Menubutton(self.menubar, text='Wheel -1  ', underline=0)
        mbutton.pack(side=TOP)
        mbutton.config(bg='white',bd=4,relief=RAISED)
        menu = Menu(mbutton)
        menu.add_command(label='Bunch Crossing', command=self.histoWm1Bx)
        menu.add_command(label='Cluster Size', command=self.histoWm1ClusterSize)
        menu.add_command(label='Wheel -1 Efficiency', command=self.histoWm1Eff) ##
        menu.add_command(label='Nearside Efficiency', command=self.histoWm1NearEff) ##
        menu.add_command(label='Farside Efficiency', command=self.histoWm1FarEff) ##
        menu.add_command(label='Masked Strips', command=self.histoWm1Masked)
        mbutton['menu'] = menu
        return mbutton

    def W0Menu(self):
        mbutton = Menubutton(self.menubar, text='Wheel 0  ', underline=0)
        mbutton.pack(side=TOP)
        mbutton.config(bg='white',bd=4,relief=RAISED)
        menu = Menu(mbutton)
        menu.add_command(label='Bunch Crossing', command=self.histoW0Bx)
        menu.add_command(label='Cluster Size', command=self.histoW0ClusterSize)
        menu.add_command(label='Wheel 0 Efficiency', command=self.histoW0Eff)
        menu.add_command(label='Nearside Efficiency', command=self.histoW0NearEff) ##
        menu.add_command(label='Farside Efficiency', command=self.histoW0FarEff) ##
        menu.add_command(label='Masked Strips', command=self.histoW0Masked)
        mbutton['menu'] = menu
        return mbutton

    def Wp1Menu(self):
        mbutton = Menubutton(self.menubar, text='Wheel +1  ', underline=0)
        mbutton.pack(side=TOP)
        mbutton.config(bg='white',bd=4,relief=RAISED)
        menu = Menu(mbutton)
        menu.add_command(label='Bunch Crossing', command=self.histoWp1Bx)
        menu.add_command(label='Cluster Size', command=self.histoWp1ClusterSize)
        menu.add_command(label='Wheel +1 Efficiency', command=self.histoWp1Eff)
        menu.add_command(label='Nearside Efficiency', command=self.histoWp1NearEff) ##
        menu.add_command(label='Farside Efficiency', command=self.histoWp1FarEff) ##
        menu.add_command(label='Masked Strips', command=self.histoWp1Masked)
        mbutton['menu'] = menu
        return mbutton

    def Wp2Menu(self):
        mbutton = Menubutton(self.menubar, text='Wheel +2  ', underline=0)
        mbutton.pack(side=TOP)
        mbutton.config(bg='white',bd=4,relief=RAISED)
        menu = Menu(mbutton)
        menu.add_command(label='Bunch Crossing', command=self.histoWp2Bx)
        menu.add_command(label='Cluster Size', command=self.histoWp2ClusterSize)
        menu.add_command(label='Wheel +2 Efficiency', command=self.histoWp2Eff)
        menu.add_command(label='Nearside Efficiency', command=self.histoWp2NearEff) ##
        menu.add_command(label='Farside Efficiency', command=self.histoWp2FarEff) ##
        menu.add_command(label='Masked Strips', command=self.histoWp2Masked)
        mbutton['menu'] = menu
        return mbutton

    def Dm1Menu(self):
        mbutton = Menubutton(self.menubar, text='Disk -1  ', underline=0)
        mbutton.pack(side=TOP)
        mbutton.config(bg='white',bd=4,relief=RAISED)
        menu = Menu(mbutton)
        menu.add_command(label='Bunch Crossing', command=self.histoDm1Bx)
        menu.add_command(label='Cluster Size', command=self.histoDm1ClusterSize)
        menu.add_command(label='Disk -1 Efficiency', command=self.histoDm1Eff)
        menu.add_command(label='RE1 Global Efficiency', command=self.histoDm1RE1GloEff)
        menu.add_command(label='RE2 Global Efficiency', command=self.histoDm1RE2GloEff)
        menu.add_command(label='RE3 Global Efficiency', command=self.histoDm1RE3GloEff)
        menu.add_command(label='Masked Strips', command=self.histoDm1Masked)
        mbutton['menu'] = menu
        return mbutton

    def Dm2Menu(self):
        mbutton = Menubutton(self.menubar, text='Disk -2  ', underline=0)
        mbutton.pack(side=TOP)
        mbutton.config(bg='white',bd=4,relief=RAISED)
        menu = Menu(mbutton)
        menu.add_command(label='Bunch Crossing', command=self.histoDm2Bx)
        menu.add_command(label='Cluster Size', command=self.histoDm2ClusterSize)
        menu.add_command(label='Disk -2 Efficiency', command=self.histoDm2Eff)
        menu.add_command(label='RE1 Global Efficiency', command=self.histoDm2RE1GloEff)
        menu.add_command(label='RE2 Global Efficiency', command=self.histoDm2RE2GloEff)
        menu.add_command(label='RE3 Global Efficiency', command=self.histoDm2RE3GloEff)
        menu.add_command(label='Masked Strips', command=self.histoDm2Masked)
        mbutton['menu'] = menu
        return mbutton

    def Dm3Menu(self):
        mbutton = Menubutton(self.menubar, text='Disk -3  ', underline=0)
        mbutton.pack(side=TOP)
        mbutton.config(bg='white',bd=4,relief=RAISED)
        menu = Menu(mbutton)
        menu.add_command(label='Bunch Crossing', command=self.histoDm3Bx)
        menu.add_command(label='Cluster Size', command=self.histoDm3ClusterSize)
        menu.add_command(label='Disk -3 Efficiency', command=self.histoDm3Eff)
        menu.add_command(label='RE1 Global Efficiency', command=self.histoDm3RE1GloEff)
        menu.add_command(label='RE2 Global Efficiency', command=self.histoDm3RE2GloEff)
        menu.add_command(label='RE3 Global Efficiency', command=self.histoDm3RE3GloEff)
        menu.add_command(label='Masked Strips', command=self.histoDm3Masked)
        mbutton['menu'] = menu
        return mbutton

    def Dp1Menu(self):
        mbutton = Menubutton(self.menubar, text='Disk +1  ', underline=0)
        mbutton.pack(side=TOP)
        mbutton.config(bg='white',bd=4,relief=RAISED)
        menu = Menu(mbutton)
        menu.add_command(label='Bunch Crossing', command=self.histoDp1Bx)
        menu.add_command(label='Cluster Size', command=self.histoDp1ClusterSize)
        menu.add_command(label='Disk +1 Efficiency', command=self.histoDp1Eff)
        menu.add_command(label='RE1 Global Efficiency', command=self.histoDp1RE1GloEff)
        menu.add_command(label='RE2 Global Efficiency', command=self.histoDp1RE2GloEff)
        menu.add_command(label='RE3 Global Efficiency', command=self.histoDp1RE3GloEff)
        menu.add_command(label='Masked Strips', command=self.histoDp1Masked)
        mbutton['menu'] = menu
        return mbutton

    def Dp2Menu(self):
        mbutton = Menubutton(self.menubar, text='Disk +2  ', underline=0)
        mbutton.pack(side=TOP)
        mbutton.config(bg='white',bd=4,relief=RAISED)
        menu = Menu(mbutton)
        menu.add_command(label='Bunch Crossing', command=self.histoDp2Bx)
        menu.add_command(label='Cluster Size', command=self.histoDp2ClusterSize)
        menu.add_command(label='Disk +2 Efficiency', command=self.histoDp2Eff)
        menu.add_command(label='RE1 Global Efficiency', command=self.histoDp2RE1GloEff)
        menu.add_command(label='RE2 Global Efficiency', command=self.histoDp2RE2GloEff)
        menu.add_command(label='RE3 Global Efficiency', command=self.histoDp2RE3GloEff)
        menu.add_command(label='Masked Strips', command=self.histoDp2Masked)
        mbutton['menu'] = menu
        return mbutton

    def Dp3Menu(self):
        mbutton = Menubutton(self.menubar, text='Disk +3  ', underline=0)
        mbutton.pack(side=TOP)
        mbutton.config(bg='white',bd=4,relief=RAISED)
        menu = Menu(mbutton)
        menu.add_command(label='Bunch Crossing', command=self.histoDp3Bx)
        menu.add_command(label='Cluster Size', command=self.histoDp3ClusterSize)
        menu.add_command(label='Disk +3 Efficiency', command=self.histoDp3Eff)
        menu.add_command(label='RE1 Global Efficiency', command=self.histoDp3RE1GloEff)
        menu.add_command(label='RE2 Global Efficiency', command=self.histoDp3RE2GloEff)
        menu.add_command(label='RE3 Global Efficiency', command=self.histoDp3RE3GloEff)
        menu.add_command(label='Masked Strips', command=self.histoDp3Masked)
        mbutton['menu'] = menu
        return mbutton

#-------------------------------------------------------------------------------------------------

    def greeting(self):
        showinfo('greeting', 'Greetings')

    def notdone(self):
        showerror('Missing plot', 'Plot not available')

    def quit(self):
        if askyesno('Verify quit', 'Are you sure you want to quit?'):
            Frame.quit(self)

    def onPicture(self,name):
        try:
            os.path.exists(name)
            img = PhotoImage(file=name)
            self.canvas.config(height=img.height(), width=img.width())
            self.drawn = self.canvas.create_image(2, 2, image=img, anchor=NW)
            self.image = name, img

            self.canvas.update()
        except:
            self.notdone()
        
    def onOpen(self):
        self.onStop()
        name = askopenfilename(initialdir=self.opens, filetypes=imageTypes)
        if name:
            if self.drawn: self.canvas.delete(self.drawn)
            img = PhotoImage(file=name)
            self.canvas.config(height=img.height(), width=img.width())
            self.drawn = self.canvas.create_image(2, 2, image=img, anchor=NW)
            self.image = name, img

    def onQuit(self):
        self.onStop()
        self.update()
        if askyesno('PyView', 'Really quit now?'):
            self.quit()

##if __name__ == '__main__':
##    import sys
##    if len(sys.argv) == 2:
##        picdir = sys.argv[1]
##    else:
##        picdir = '../gifs'
##    root = Tk()
##    root.title('PyView 1.0')
##    root.iconname('PyView')
##    Label(root, text="Python Slide Show Viewer").pack()
##    SlideShow(root, picdir=picdir, bd=3, relief=SUNKEN)
##    root.mainloop()
