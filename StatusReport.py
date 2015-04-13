#! /usr/bin/env python
import os
import sys
#from sys import argv
from QualityPerformance import Diagnostic

class StatusReport(object):

    def __init__(self,root_file_name,values):
        self.RootFileName = root_file_name
        self.values = values

        print values
        
        name = root_file_name.rstrip().split("/")
        self.diagn = Diagnostic(self.RootFileName)

        numsta = self.diagn.getStatistics('Statistics')

        cmd = "pwd"
        homedir = [item[:-1] for item in os.popen(cmd)]
        f=open(str(homedir[0])+'/wheel_coord.txt', 'r')
        f1=open(str(homedir[0])+'/disk_coord.txt', 'r')

        fout=open("StatusReport.txt",'w')

        listWheel = ['W-2','W-1','W+0','W+1','W+2']
        listDisk = ['RE-3','RE-2','RE-1','RE+1','RE+2','RE+2']

#        print name[9],numsta
        fout.write("Dataset: "+values[0]+"\n")
        fout.write("Run number: "+values[1]+"\n")
        fout.write("Number of events: "+str(numsta)+"\n")
        
        for line in f:
            for el in listWheel:
                coord = line.rstrip().split("  ")
                histoname_bx = 'BXN_'+el+'_' + coord[0]
                histoname_cls = 'ClusterSize_'+el+'_'+coord[0]
                histoname_occ = 'Occupancy_'+el+'_'+coord[0]
                histoname_Eff = 'LocalEfficiencyFromSegments_'+el+'_' + coord[0]

                bx_for = self.diagn.getMeanValue(histoname_bx)[1]
                cls_for = self.diagn.getMeanValue(histoname_cls)[1]
                eff_for = self.diagn.getMedia(histoname_Eff)[1]
                mask_for = self.diagn.getMaskedStrip(histoname_occ)[1]

                bx_back = self.diagn.getMeanValue(histoname_bx)[0]
                cls_back = self.diagn.getMeanValue(histoname_cls)[0]
                eff_back = self.diagn.getMedia(histoname_Eff)[0]
                mask_back = self.diagn.getMaskedStrip(histoname_occ)[0]

                if len(self.diagn.getMeanValue(histoname_bx)) == 3:

                    bx_middle = self.diagn.getMeanValue(histoname_bx)[2]
                    cls_middle = self.diagn.getMeanValue(histoname_cls)[2]
                    eff_middle = self.diagn.getMedia(histoname_Eff)[2]
                    mask_middle = self.diagn.getMaskedStrip(histoname_occ)[2]
 
                if values[2]<= bx_for <= values[3] and values[4]<= cls_for <= values[5] and values[6]<= eff_for <= values[7] and values[8]<= mask_for <= values[9]:

                    fout.write("Wheel: "+el+"   "+"Ch: "+coord[0]+"   "+"Bx Forw: "+("%.2f" % (bx_for))+"   "+"Cls Forw :"+("%.2f" % (cls_for))+"   "+"Eff Forw: "+("%.2f" % (eff_for))+"   "+"Mask Forw: "+("%.2f" % (mask_for))+"\n")

                if values[2]<= bx_back <= values[3] and values[4]<= cls_back <= values[5] and values[6]<= eff_back <= values[7] and values[8]<= mask_back <= values[9]:

                    fout.write("Wheel: "+el+"   "+"Ch: "+coord[0]+"   "+"Bx Back: "+("%.2f" % (bx_back))+"   "+"Cls Back :"+("%.2f" % (cls_back))+"   "+"Eff Back: "+("%.2f" % (eff_back))+"   "+"Mask Back: "+("%.2f" % (mask_back))+"\n")


                if len(self.diagn.getMeanValue(histoname_bx)) == 3:
                    if values[2]<= bx_middle <= values[3] and values[4]<= cls_middle <= values[5] and values[6]<= eff_middle <= values[7] and values[8]<= mask_middle <= values[9]:
                        fout.write("Wheel: "+el+"   "+"Ch: "+coord[0]+"   "+"Bx Middle: "+("%.2f" % (bx_middle))+"   "+"Cls Middle :"+("%.2f" % (cls_middle))+"   "+"Eff Middle: "+("%.2f" % (eff_middle))+"   "+"Mask Middle: "+("%.2f" % (mask_middle))+"\n")

                    
        for line in f1:
            for el in listDisk:
                coord = line.rstrip().split("  ")
                histoname_bx = 'BXN_'+el+'_' + coord[0]
                histoname_cls = 'ClusterSize_'+el+'_'+coord[0]
                histoname_occ = 'Occupancy_'+el+'_'+coord[0]
                histoname_Eff = 'LocalEfficiencyFromSegments_'+el+'_' + coord[0]

                bx_1 = self.diagn.getMeanValue(histoname_bx)[0]
                cls_1 = self.diagn.getMeanValue(histoname_cls)[0]
                eff_1 = self.diagn.getMedia(histoname_Eff)[0]
                mask_1 = self.diagn.getMaskedStrip(histoname_occ)[0]

                bx_2 = self.diagn.getMeanValue(histoname_bx)[1]
                cls_2 = self.diagn.getMeanValue(histoname_cls)[1]
                eff_2 = self.diagn.getMedia(histoname_Eff)[1]
                mask_2 = self.diagn.getMaskedStrip(histoname_occ)[1]

                if len(self.diagn.getMeanValue(histoname_bx)) == 3:

                    bx_3 = self.diagn.getMeanValue(histoname_bx)[2]
                    cls_3 = self.diagn.getMeanValue(histoname_cls)[2]
                    eff_3 = self.diagn.getMedia(histoname_Eff)[2]
                    mask_3 = self.diagn.getMaskedStrip(histoname_occ)[2]

                
                if values[2]<= bx_1 <= values[3] and values[4]<= cls_1 <= values[5] and values[6]<= eff_1 <= values[7] and values[8]<= mask_1 <= values[9]:
                    fout.write("Disk: "+el+"   "+"Ch: "+coord[0]+"   "+"Bx 1: "+("%.2f" % (bx_1))+"   "+"Cls 1 :"+("%.2f" % (cls_1))+"   "+"Eff 1: "+("%.2f" % (eff_1))+"   "+"Mask 1: "+("%.2f" % (mask_1))+"\n")

                if values[2]<= bx_2 <= values[3] and values[4]<= cls_2 <= values[5] and values[6]<= eff_2 <= values[7] and values[8]<= mask_2 <= values[9]: 
                    fout.write("Disk: "+el+"   "+"Ch: "+coord[0]+"   "+"Bx 2: "+("%.2f" % (bx_2))+"   "+"Cls 2 :"+("%.2f" % (cls_2))+"   "+"Eff 2: "+("%.2f" % (eff_2))+"   "+"Mask 2: "+("%.2f" % (mask_2))+"\n")

                if len(self.diagn.getMeanValue(histoname_bx)) == 3:

                    if values[2]<= bx_3 <= values[3] and values[4]<= cls_3 <= values[5] and values[6]<= eff_3 <= values[7] and values[8]<= mask_3 <= values[9]: 
                        fout.write("Disk: "+el+"   "+"Ch: "+coord[0]+"   "+"Bx 3: "+("%.2f" % (bx_3))+"   "+"Cls 3 :"+("%.2f" % (cls_3))+"   "+"Eff 3: "+("%.2f" % (eff_3))+"   "+"Mask 3: "+("%.2f" % (mask_3))+"\n")


        print "Done!"

