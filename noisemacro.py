#! /usr/bin/env python
import commands
from Tkinter import *
import sys, os, string, fileinput
from ROOT import TCanvas,TH1F,TH2F,gROOT,TFile,gDirectory,TTree,gStyle,TStyle
from time import ctime


def SetStyle():
    global defa
    defa = TStyle("defa1","defa2")
    defa.SetPalette(1)
    defa.SetOptStat(0)
    gROOT.SetStyle("defa")
    return 


#
#main
#


if __name__ == "__main__":

    ds = str(sys.argv[1]).replace('/','')
    Root = Tk()
    
    RootFile=TFile.Open('rfio:/castor/cern.ch/cms/store/caf/user/ccmuon/RPC/GlobalRuns/' + ds + '/' + sys.argv[2] + '/noise/merge_NoiseTrig.root' )
#    RootFile=TFile(sys.argv[1])
    T=RootFile.Get('RPCTriggerNoiseMonitoring')


    SetStyle()
    gStyle.SetOptStat(0)
    
    nen = T.GetEntries()
    print 'eventos ' + str(nen)
    imin = T.GetMinimum('tempo')
    imax = T.GetMaximum('tempo')
    binnum = imax-imin + 1


############.....................Trigger study ...........................####

    ##------------------------- TRIGGER STUDY -------------------------------------------------------

    ntrigmuon =  TH1F('NTrigMuon', 'Number of muon trig. candidate per event ',int(binnum), 0, int(binnum));
    ntrigrpc =  TH1F('NTrigRPC', 'Number of RPC trig. candidate per event ',int(binnum), 0, int(binnum));
    ntrigdt =  TH1F('NTrigDT', 'Number of DT trig. candidate per event ',int(binnum), 0, int(binnum));
    ntrigcsc =  TH1F('NTrigCSC', 'Number of CSC trig. candidate per event ',int(binnum), 0, int(binnum));
    ntrigecal =  TH1F('NTrigECAL', 'Number of ECAL trig. candidate per event ',int(binnum), 0, int(binnum));

    ndigirpc =  TH1F('NDigiRPC', 'Number of RPC digis per event ',int(binnum), 0, int(binnum));
    ndigidt =  TH1F('NDigiDT', 'Number of DT digis per event ',int(binnum), 0, int(binnum));
    ndigicsc =  TH1F('NDigiCSC', 'Number of CSC digis per event ',int(binnum), 0, int(binnum));
    nrechitecal =  TH1F('NRecHitECAL', 'Number of ECAL RecHits per event ',int(binnum), 0, int(binnum));
    nrechithcal =  TH1F('NRecHitHCAL', 'Number of HCAL RecHits per event ',int(binnum), 0, int(binnum));
    ndigipixel =  TH1F('NDigiPixel', 'Number of Pixel digis per event ',int(binnum), 0, int(binnum));
    ndigitracker = TH1F('NDigiTracker', 'Number of Tracker digis per event ',int(binnum), 0, int(binnum));

    ndigirpc_rpc =  TH1F('NDigiRPC_TRPC', 'Number of RPC digis per event with RPC trigger',int(binnum), 0, int(binnum));
    ndigidt_rpc =  TH1F('NDigiDT_TRPC', 'Number of DT digis per event with RPC trigger',int(binnum), 0, int(binnum));
    ndigicsc_rpc =  TH1F('NDigiCSC_TRPC', 'Number of CSC digis per event with RPC trigger',int(binnum), 0, int(binnum));
    nrechitecal_rpc =  TH1F('NRecHitECAL_TRPC', 'Number of ECAL RecHits per event with RPC trigger',int(binnum), 0, int(binnum));
    nrechithcal_rpc =  TH1F('NRecHitHCAL_TRPC', 'Number of HCAL RecHits per event with RPC trigger',int(binnum), 0, int(binnum));
    ndigipixel_rpc =  TH1F('NDigiPixel_TRPC', 'Number of Pixel digis per event with RPC trigger',int(binnum), 0, int(binnum));
    ndigitracker_rpc = TH1F('NDigiTracker_TRPC', 'Number of Tracker digis per event with RPC trigger',int(binnum), 0, int(binnum));

    ndigirpc_dt_csc = TH1F('NDigiRPC_TDT_CSC', 'Number of RPC digis per event with DT-CSC trigger',int(binnum), 0, int(binnum));
    ndigidt_dt_csc = TH1F('NDigiDT_TDT_CSC', 'Number of DT digis per event with DT-CSC trigger',int(binnum), 0, int(binnum));
    ndigicsc_dt_csc = TH1F('NDigiCSC_TDT_CSC', 'Number of CSC digis per event with DT-CSC trigger',int(binnum), 0, int(binnum));
    nrechitecal_dt_csc = TH1F('NRecHitECAL_TDT_CSC', 'Number of ECAL RecHits per event with DT-CSC trigger',int(binnum), 0, int(binnum));
    nrechithcal_dt_csc =  TH1F('NRecHitHCAL_TDT_CSC', 'Number of HCAL RecHits per event with DT-CSC trigger',int(binnum), 0, int(binnum));
    ndigipixel_dt_csc = TH1F('NDigiPixel_TDT_CSC', 'Number of Pixel digis per event with DT-CSC trigger',int(binnum), 0, int(binnum));
    ndigitracker_dt_csc = TH1F('NDigiTracker_TDT_CSC', 'Number of Tracker digis per event with DT-CSC trigger',int(binnum), 0, int(binnum));

    ##----------------------------------------------------------------------------------------------


    wheels = ['W-2','W-1','W+0','W+1','W+2']
    sec = ['S01','S02','S03','S04','S05','S06','S07','S08','S09','S10','S11','S12']
    rbs = ['RB1in','RB1out','RB2in','RB2out','RB3+','RB3-','RB4+','RB4-','RB4++','RB4+-','RB4--','RB4-+']
    dir = ['Forward','Backward','Middle']
    #disks = ['D-3','D-2','D-1','D+1','D+2','D+3']
    disks = ['D+1','D+2','D+3']
    RES = ['RE2','RE3']
    secd = ['S01','S02','S03','S04','S05','S06']
    secdis = ['S01','S02','S03','S04','S05','S06','S07','S08','S09','S10','S11','S12','S13','S14','S15','S16','S17','S18','S19','S20','S21','S22','S23','S24','S25','S26','S27','S28','S29','S30','S31','S32','S33','S34','S35','S36']
    dirdis = ['A','B','C']

    occtot = TH1F('Occtot', 'Occupancy for all RPCs',int(binnum), 0, int(binnum));
    occbarrel =TH1F('Occbarrel','Occupancy for Barrel',int(binnum),0,int(binnum));
    occEnd =TH1F('OccEndcapForward','Occupancy for Endcap',int(binnum),0,int(binnum));    
    occwheelbarrel =TH2F('occwheelbarrel','Global Barrel Plot',int(binnum),0,int(binnum),5,0,5)
    occdiskendcap =TH2F('occdiskendcap','Global Endcap Plot',int(binnum),0,int(binnum),6,0,6)
    occbrlend =TH2F('occbarlend','Global Endcap and Barrel',int(binnum),0,int(binnum),3,0,3)

    wheelhis = []
    diskhis = []
    chamwheelhis = []
    chamdiskhis = []

    for d in disks:
        for r in RES:
            for s in secd:
                histochamdisk = TH2F(d + '_' + r + '_' + s, 'Disk '+ d + ' ' + r + ' ' + s + ' noise',int(binnum),0,int(binnum),18,0,18)
                count = 1
                for se in secdis:
                    for di in dirdis:
                        if((cmp(s,'S01')==0) and
                           (cmp(se,'S02')==0 or cmp(se,'S03')==0 or cmp(se,'S04')==0 or cmp(se,'S05')==0 or cmp(se,'S06')==0 or cmp(se,'S07')==0)):
                            histochamdisk.GetYaxis().SetBinLabel(count,d + '_' + r + '_' + se + '_' + di)
                            count = count + 1
                        elif((cmp(s,'S02')==0) and
                             (cmp(se,'S08')==0 or cmp(se,'S09')==0 or cmp(se,'S10')==0 or cmp(se,'S11')==0 or cmp(se,'S12')==0 or cmp(se,'S13')==0)):
                            histochamdisk.GetYaxis().SetBinLabel(count,d + '_' + r + '_' + se + '_' + di)
                            count = count + 1
                        elif((cmp(s,'S03')==0) and
                             (cmp(se,'S14')==0 or cmp(se,'S15')==0 or cmp(se,'S16')==0 or cmp(se,'S17')==0 or cmp(se,'S18')==0 or cmp(se,'S19')==0)):
                            histochamdisk.GetYaxis().SetBinLabel(count,d + '_' + r + '_' + se + '_' + di)
                            count = count + 1
                        elif((cmp(s,'S04')==0) and
                             (cmp(se,'S20')==0 or cmp(se,'S21')==0 or cmp(se,'S22')==0 or cmp(se,'S23')==0 or cmp(se,'S24')==0 or cmp(se,'S25')==0)):
                            histochamdisk.GetYaxis().SetBinLabel(count,d + '_' + r + '_' + se + '_' + di)
                            count = count + 1
                        elif((cmp(s,'S05')==0) and
                             (cmp(se,'S26')==0 or cmp(se,'S27')==0 or cmp(se,'S28')==0 or cmp(se,'S29')==0 or cmp(se,'S30')==0 or cmp(se,'S31')==0)):
                            histochamdisk.GetYaxis().SetBinLabel(count,d + '_' + r + '_' + se + '_' + di)
                            count = count + 1
                        elif((cmp(s,'S06')==0) and
                             (cmp(se,'S01')==0 or cmp(se,'S32')==0 or cmp(se,'S33')==0 or cmp(se,'S34')==0 or cmp(se,'S35')==0 or cmp(se,'S36')==0)):
                            histochamdisk.GetYaxis().SetBinLabel(count,d + '_' + r + '_' + se + '_' + di)
                            count = count + 1
                chamdiskhis.append(histochamdisk)
                           
    
    for w in wheels:
        histowheel = TH2F( w,'Barrel ' + w + ' Noise',int(binnum),0,int(binnum),12,0,12)
        cont =1
        for s in sec:
            histowheel.GetYaxis().SetBinLabel(cont,w + '_' + s)
            cont = cont + 1
        wheelhis.append(histowheel)

    for w in wheels:
        for s in sec:
            if (cmp(s,'S04') == 0):
                chamwheel = TH2F(w + '_' + s ,w + ' ' + s + ' Noise',int(binnum),0,int(binnum),21,0,21)
            else:
                chamwheel = TH2F(w + '_' + s ,w + ' ' + s + ' Noise',int(binnum),0,int(binnum),17,0,17)
            cont = 1    
            for r in rbs:
                for j in dir:
                    if((cmp(r,'RB4++')==0 or cmp(r,'RB4+-')==0 or cmp(r,'RB4--')==0 or cmp(r,'RB4-+')==0) and cmp(s,'S04')!=0):
                        break
                    elif(cmp(s,'S04')==0 and (cmp(r,'RB4+')==0 or cmp(r,'RB4-')==0)):
                        break
                    elif((cmp(r,'RB2in')==0 and (cmp(w,'W+2')==0 or cmp(w,'W-2')==0)) and cmp(j,'Middle')==0):
                        break
                    elif((cmp(r,'RB2out')==0 and (cmp(w,'W+0')==0 or cmp(w,'W+1')==0 or cmp(w,'W-1')==0)) and cmp(j,'Middle')==0):
                        break
                    elif((cmp(r,'RB1in')==0 or cmp(r,'RB1out')==0 or cmp(r,'RB3+')==0 or cmp(r,'RB3-')==0 or cmp(r,'RB4+')==0 or cmp(r,'RB4-')==0 or
                        cmp(r,'RB4++')==0 or cmp(r,'RB4+-')==0 or cmp(r,'RB4--')==0 or cmp(r,'RB4-+')==0) and cmp(j,'Middle')==0):
                        break
                    else:
                        chamwheel.GetYaxis().SetBinLabel(cont,w + '_' + r + '_' + s + '_' + j )
                        cont = cont + 1
            chamwheelhis.append(chamwheel)                
                
            

    for d in disks:
        histodisk = TH2F(d,'Disk ' + d + ' Noise',int(binnum),0,int(binnum),12,0,12)
        cont = 1
        for r in RES:
            for s in secd:
                histodisk.GetYaxis().SetBinLabel(cont,d + '_' + r + '_' + s)
                cont = cont + 1
        diskhis.append(histodisk)        

    occwheelbarrel.GetYaxis().SetBinLabel(1,'W-2')
    occwheelbarrel.GetYaxis().SetBinLabel(2,'W-1')
    occwheelbarrel.GetYaxis().SetBinLabel(3,'W+0')
    occwheelbarrel.GetYaxis().SetBinLabel(4,'W+1')
    occwheelbarrel.GetYaxis().SetBinLabel(5,'W+2')

    occdiskendcap.GetYaxis().SetBinLabel(1,'D-3')
    occdiskendcap.GetYaxis().SetBinLabel(2,'D-2')
    occdiskendcap.GetYaxis().SetBinLabel(3,'D-1')
    occdiskendcap.GetYaxis().SetBinLabel(4,'D+1')
    occdiskendcap.GetYaxis().SetBinLabel(5,'D+2')
    occdiskendcap.GetYaxis().SetBinLabel(6,'D+3')

    occbrlend.GetYaxis().SetBinLabel(1,'E+')
    occbrlend.GetYaxis().SetBinLabel(2,'Barrel')
    occbrlend.GetYaxis().SetBinLabel(3,'E-')

    ir = 0
    for i in xrange(nen):

        print str(ir)
        ir = ir + 1
        
        z = T.GetEntry(i)
        
        ##---------------------- TRIGGER STUDY --------------------------------------

        ntrigmuon.Fill(T.tempo-imin,T.irpcb+T.irpcf+T.idt+T.icsc+T.ihalo)
        ntrigrpc.Fill(int(T.tempo-imin),(T.irpcb+T.irpcf))
        ntrigdt.Fill(int(T.tempo-imin),(T.idt))
        ntrigcsc.Fill(int(T.tempo-imin),(T.icsc))
        ntrigecal.Fill(int(T.tempo-imin),(T.iecalo))
        
        ndigirpc.Fill(int(T.tempo-imin),(T.nrpcdigi))
        ndigidt.Fill(int(T.tempo-imin),(T.ndtdigi))
        ndigicsc.Fill(int(T.tempo-imin),(T.ncscdigi))
##        nrechitecal.Fill(int(T.tempo-imin),(T.necalorechit))
        nrechithcal.Fill(int(T.tempo-imin),(T.nhcalorechit))
        ndigipixel.Fill(int(T.tempo-imin),(T.npixeldigi))
        ndigitracker.Fill(int(T.tempo-imin),(T.ntrackerdigi))

        if ((T.rpcb_l1a or T.rpcf_l1a) and (not (T.dt_l1a) and not (T.csc_l1a))) :
            ndigirpc_rpc.Fill(int(T.tempo-imin),(T.nrpcdigi))
            ndigidt_rpc.Fill(int(T.tempo-imin),(T.ndtdigi))
            ndigicsc_rpc.Fill(int(T.tempo-imin),(T.ncscdigi))
##            nrechitecal_rpc.Fill(int(T.tempo-imin),(T.necalorechit))
            nrechithcal_rpc.Fill(int(T.tempo-imin),(T.nhcalorechit))
            ndigipixel_rpc.Fill(int(T.tempo-imin),(T.npixeldigi))
            ndigitracker_rpc.Fill(int(T.tempo-imin),(T.ntrackerdigi))

        if (T.dt_l1a or T.csc_l1a or T.halo_l1a) and (not T.rpcb_l1a and not T.rpcf_l1a):
            ndigirpc_dt_csc.Fill(int(T.tempo-imin),(T.nrpcdigi))
            ndigidt_dt_csc.Fill(int(T.tempo-imin),(T.ndtdigi))
            ndigicsc_dt_csc.Fill(int(T.tempo-imin),(T.ncscdigi))
##            nrechitecal_dt_csc.Fill(int(T.tempo-imin),(T.necalorechit))
            nrechithcal_dt_csc.Fill(int(T.tempo-imin),(T.nhcalorechit))
            ndigipixel_dt_csc.Fill(int(T.tempo-imin),(T.npixeldigi))
            ndigitracker_dt_csc.Fill(int(T.tempo-imin),(T.ntrackerdigi))

        ##--------------------------------------------------------------------------------

    TN=RootFile.Get('RPCNoiseMonitoring')
    
    nen = TN.GetEntries()
    print 'eventos ' + str(nen)
    imin = TN.GetMinimum('tempo')
    imax = TN.GetMaximum('tempo')
    binnum = imax-imin + 1

    for i in xrange(nen):
        print str(i+1)
        z = TN.GetEntry(i)
                                
        occtot.Fill(int(TN.tempo-imin),TN.nrpcdigiroll)
        nompart = TN.nomchamb.split('_')
        for w in wheelhis:
            for k in range(12):
                nom = w.GetYaxis().GetBinLabel(k+1)
                nom1 = nom.split('_')
                if (cmp(nom1[0],nompart[0])==0 and cmp(nompart[2],nom1[1])==0):
                    w.Fill(int(TN.tempo-imin),k,TN.nrpcdigiroll)

        for d in chamdiskhis:
            for k in range(18):
                if (cmp(nompart[0],'D+1')==0 or cmp(nompart[0],'D+2')==0 or cmp(nompart[0],'D+3')==0):
                    nom = d.GetYaxis().GetBinLabel(k+1)
                    nom1 = nom.split('_')
                    nompart1 = nompart[2].split('S')
                    if (cmp(nom1[0],nompart[0])==0 and cmp(nom1[1],nompart[1])==0 and cmp(nom1[2],'S' + nompart1[1])==0 and cmp(nom1[3],nompart[3])==0):
                        d.Fill(int(TN.tempo-imin),k,TN.nrpcdigiroll)
                else:        
                    break
                
        for w in chamwheelhis:
            for k in range(w.GetYaxis().GetNbins()):
                nom = w.GetYaxis().GetBinLabel(k+1)
                nom1 = nom.split('_')
                if (cmp(nom1[0],nompart[0])==0 and cmp(nom1[2],nompart[2])==0 and cmp(nom1[1],nompart[1])==0 and cmp(nompart[3],nom1[3])==0):
                    w.Fill(int(TN.tempo-imin),k,TN.nrpcdigiroll)
                                                                        
                    
        for d in diskhis:
            for k in range(12):
                nom = d.GetYaxis().GetBinLabel(k+1)
                nom1= nom.split('_')
                if (cmp(nom1[0],nompart[0])==0 and cmp(nompart[1],nom1[1])==0):
                    nompart1 = nompart[2].split('S')
                    if(0<=k<=5):
                        l=k
                    else:
                        l=k-6
                    mink = 2 + 6*l
                    maxk = mink + 5                    
                    if(mink<=int(nompart1[1])<=maxk):
                        d.Fill(int(TN.tempo-imin),k,TN.nrpcdigiroll)
                    elif (int(nompart1[1])==1):
                        d.Fill(int(TN.tempo-imin),5,TN.nrpcdigiroll)
                
        
        
        if(cmp(nompart[0],'W+1')==0 or cmp(nompart[0],'W+2')==0 or cmp(nompart[0],'W+0')==0 or cmp(nompart[0],'W-1')==0 or cmp(nompart[0],'W-2')==0):
            occbarrel.Fill(int(TN.tempo-imin),TN.nrpcdigiroll)
            if(cmp(nompart[0],'W+1')==0):
                occbrlend.Fill(int(TN.tempo-imin),1,TN.nrpcdigiroll)
                occwheelbarrel.Fill(int(TN.tempo-imin),3,TN.nrpcdigiroll)
            elif (cmp(nompart[0],'W+2')==0):
                occbrlend.Fill(int(TN.tempo-imin),1,TN.nrpcdigiroll)
                occwheelbarrel.Fill(int(TN.tempo-imin),4,TN.nrpcdigiroll)
            elif (cmp(nompart[0],'W+0')==0):
                occbrlend.Fill(int(TN.tempo-imin),1,TN.nrpcdigiroll)
                occwheelbarrel.Fill(int(TN.tempo-imin),2,TN.nrpcdigiroll)
            elif (cmp(nompart[0],'W-1')==0):    
                occbrlend.Fill(int(TN.tempo-imin),1,TN.nrpcdigiroll)
                occwheelbarrel.Fill(int(TN.tempo-imin),1,TN.nrpcdigiroll)
            elif (cmp(nompart[0],'W-2')==0):        
                occbrlend.Fill(int(TN.tempo-imin),1,TN.nrpcdigiroll)
                occwheelbarrel.Fill(int(TN.tempo-imin),0,TN.nrpcdigiroll)
                
        elif(cmp(nompart[0],'D+1')==0 or cmp(nompart[0],'D+2')==0 or cmp(nompart[0],'D+3')==0 or
             cmp(nompart[0],'D-1')==0 or cmp(nompart[0],'D-2')==0 or cmp(nompart[0],'D-3')==0):
            occEnd.Fill(int(TN.tempo-imin)+1,TN.nrpcdigiroll)
            if(cmp(nompart[0],'D+3')==0):
                occbrlend.Fill(int(TN.tempo-imin),0,TN.nrpcdigiroll)
                occdiskendcap.Fill(int(TN.tempo-imin),5,TN.nrpcdigiroll)
            elif (cmp(nompart[0],'D+2')==0):
                occbrlend.Fill(int(TN.tempo-imin),0,TN.nrpcdigiroll)
                occdiskendcap.Fill(int(TN.tempo-imin),4,TN.nrpcdigiroll)
            elif(cmp(nompart[0],'D+1')==0):
                occbrlend.Fill(int(TN.tempo-imin),0,TN.nrpcdigiroll)
                occdiskendcap.Fill(int(TN.tempo-imin),3,TN.nrpcdigiroll)
            elif(cmp(nompart[0],'D-1')==0):
                occbrlend.Fill(int(TN.tempo-imin),2,TN.nrpcdigiroll)
                occdiskendcap.Fill(int(TN.tempo-imin),2,TN.nrpcdigiroll)
            elif(cmp(nompart[0],'D-2')==0):
                occbrlend.Fill(int(TN.tempo-imin),2,TN.nrpcdigiroll)
                occdiskendcap.Fill(int(TN.tempo-imin),1,TN.nrpcdigiroll)
            elif(cmp(nompart[0],'D-3')==0):
                occbrlend.Fill(int(TN.tempo-imin),2,TN.nrpcdigiroll)
                occdiskendcap.Fill(int(TN.tempo-imin),0,TN.nrpcdigiroll)
                                                                                            
            
    for i in range(0,int(binnum)):
        if(i%10==0):
            t=ctime(imin+i)
            print t

            ##------------------- TRIGGER STUDY ----------------------------

            ntrigmuon.GetXaxis().SetBinLabel(i+1,t)
            ntrigrpc.GetXaxis().SetBinLabel(i+1,t)
            ntrigdt.GetXaxis().SetBinLabel(i+1,t)
            ntrigcsc.GetXaxis().SetBinLabel(i+1,t)
            ntrigecal.GetXaxis().SetBinLabel(i+1,t)
            
            ndigirpc.GetXaxis().SetBinLabel(i+1,t)
            ndigidt.GetXaxis().SetBinLabel(i+1,t)
            ndigicsc.GetXaxis().SetBinLabel(i+1,t)
            nrechitecal.GetXaxis().SetBinLabel(i+1,t)
            nrechithcal.GetXaxis().SetBinLabel(i+1,t)
            ndigipixel.GetXaxis().SetBinLabel(i+1,t)
            ndigitracker.GetXaxis().SetBinLabel(i+1,t)

            ndigirpc_rpc.GetXaxis().SetBinLabel(i+1,t)
            ndigidt_rpc.GetXaxis().SetBinLabel(i+1,t)
            ndigicsc_rpc.GetXaxis().SetBinLabel(i+1,t)
            nrechitecal_rpc.GetXaxis().SetBinLabel(i+1,t)
            nrechithcal_rpc.GetXaxis().SetBinLabel(i+1,t)
            ndigipixel_rpc.GetXaxis().SetBinLabel(i+1,t)
            ndigitracker_rpc.GetXaxis().SetBinLabel(i+1,t)

            ndigirpc_dt_csc.GetXaxis().SetBinLabel(i+1,t)
            ndigidt_dt_csc.GetXaxis().SetBinLabel(i+1,t)
            ndigicsc_dt_csc.GetXaxis().SetBinLabel(i+1,t)
            nrechitecal_dt_csc.GetXaxis().SetBinLabel(i+1,t)
            nrechithcal_dt_csc.GetXaxis().SetBinLabel(i+1,t)
            ndigipixel_dt_csc.GetXaxis().SetBinLabel(i+1,t)
            ndigitracker_dt_csc.GetXaxis().SetBinLabel(i+1,t)

            ##-------------------------------------------------------------            

            
            occtot.GetXaxis().SetBinLabel(i+1,t)
            occbarrel.GetXaxis().SetBinLabel(i+1,t)
            occEnd.GetXaxis().SetBinLabel(i+1,t)
            occbrlend.GetXaxis().SetBinLabel(i+1,t)
            occdiskendcap.GetXaxis().SetBinLabel(i+1,t)
            occwheelbarrel.GetXaxis().SetBinLabel(i+1,t)
            for j in wheelhis:
                j.GetXaxis().SetBinLabel(i+1,t)
            for j in diskhis:
                j.GetXaxis().SetBinLabel(i+1,t)
            for j in chamwheelhis:
                j.GetXaxis().SetBinLabel(i+1,t)
            for j in chamdiskhis:
                j.GetXaxis().SetBinLabel(i+1,t)

    occbrlend.SetOption('COLZ')
    occbrlend.GetXaxis().LabelsOption('v')
    occdiskendcap.SetOption('COLZ')
    occdiskendcap.GetXaxis().LabelsOption('v')
    occwheelbarrel.SetOption('COLZ')
    occwheelbarrel.GetXaxis().LabelsOption('v')

#    canvas = TCanvas('c1','prueba',1)
 #   occwheelbarrel.Draw('COLZ')
  #  canvas.SaveAs('prueba.root')
    Noisefile = TFile('RPCTriggerNoiseMonitoringOut_' + str(sys.argv[2]) +'.root','RECREATE')
#    Noisefile = TFile('RPCTriggerNoiseMonitoringOut_' + '.root','RECREATE')

    ntrigmuon.Write()
    ntrigrpc.Write()
    ntrigdt.Write()
    ntrigcsc.Write()
    ntrigecal.Write()
    
    ndigirpc.Write()
    ndigidt.Write()
    ndigicsc.Write()
    nrechitecal.Write()
    nrechithcal.Write()
    ndigipixel.Write()
    ndigitracker.Write()

    ndigirpc_rpc.Write()
    ndigidt_rpc.Write()
    ndigicsc_rpc.Write()
    nrechitecal_rpc.Write()
    nrechithcal_rpc.Write()
    ndigipixel_rpc.Write()
    ndigitracker_rpc.Write()

    ndigirpc_dt_csc.Write()
    ndigidt_dt_csc.Write()
    ndigicsc_dt_csc.Write()
    nrechitecal_dt_csc.Write()
    nrechithcal_dt_csc.Write()
    ndigipixel_dt_csc.Write()
    ndigitracker_dt_csc.Write()
    
    
    occtot.Write()
    occbarrel.Write()
    occEnd.Write()
    occbrlend.Write()
    occdiskendcap.Write()
    occwheelbarrel.Write()

    for i in wheelhis:
        i.SetOption('COLZ')
        i.GetXaxis().LabelsOption('v')
        i.Write()

    for j in diskhis:
        j.SetOption('COLZ')
        j.GetXaxis().LabelsOption('v')
        j.Write()

    for i in chamwheelhis:
        i.SetOption('COLZ')
        i.GetXaxis().LabelsOption('v')
        i.Write()

    for i in chamdiskhis:
        i.SetOption('COLZ')
        i.GetXaxis().LabelsOption('v')
        i.Write()

                                
    Noisefile.Close()
    os.system('rfcp ' + 'RPCTriggerNoiseMonitoringOut_' + str(sys.argv[2]) +'.root /castor/cern.ch/cms/store/caf/user/ccmuon/RPC/GlobalRuns/' + ds + '/' + str(sys.argv[2]) + '/noise/')
    print 'Done!!!!!!!!!!!'
    mainloop()
