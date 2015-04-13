#! /usr/bin/env python
import commands, time
import sys, os, string, fileinput
from ROOT import *


def numfiles(dataset,runnum):
    total = [item[:-1] for item in os.popen('./aSearchCLI --dbsInst=cms_dbs_prod_global --limit=-1 --input \"find file where dataset like ' + dataset + ' and run = ' + runnum + '\" | grep -v root | awk \'{print $2}\'')]
    return total[1]

class DetectFiles:
    def f(self):
        return 'Detecting string!'

    def __init__(self):
        self.data = []

    def findPath(self,dataset,runNumber):
        cmd = './aSearchCLI --dbsInst=cms_dbs_prod_global --limit=10000 --input \" find file where dataset = ' + dataset + ' and ' + 'run = ' + runNumber +' \" | egrep \"[a-Z]\" | grep -v \"Found\" '
        the_files = [item[:-1] for item in os.popen(cmd)]
        print the_files
        return the_files

    def replaceStringInFile(self,namein,nameout,list):
        fin=open(namein, 'r')
        fout=open(nameout, 'w')
        for line in fin:
            for ilist in range(len(list)):
                if ilist%2 == 0:
                    lineno1 = 0
                    lineno1 = string.find(line, list[ilist])
                    if lineno1 > 0:
                        line =line.replace(list[ilist], list[ilist+1])
            fout.write(line)
                        
    def replacesingle(self,file,list):
        for line in fileinput.FileInput(file,inplace=1):
            line = line.replace(list[0],list[1])
            if line != '':
                print line
if __name__ == "__main__":

    detString = DetectFiles()

    me = [item[:-1] for item in os.popen('whoami')]
    casa = [item[:-1] for item in os.popen('echo $HOME')]
    pwd = [item[:-1] for item in os.popen('pwd')]

    ds = str(sys.argv[1]).replace('/','')

    tmpath = '/tmp/' + me[0] +'/'
    tmpath0 = '/tmp/' + me[0] +'/'+str(sys.argv[2])+ '/' 
    tmpath1 = casa[0] + '/scratch0/' + str(sys.argv[2]) + '/job/'


    os.system('mkdir ' + tmpath)
    os.system('mkdir ' + tmpath0)
    os.system('mkdir ' + tmpath1)
    os.system('mkdir ' + casa[0] + '/scratch0/' + str(sys.argv[2]))

    path = '/store/caf/user/ccmuon/RPC/GlobalRuns/' + ds + '/' + str(sys.argv[2]) + '/root'
    path1 = '/store/caf/user/ccmuon/RPC/GlobalRuns/' + ds + '/' + str(sys.argv[2]) + '/noise'


    if(numfiles(str(sys.argv[1]),str(sys.argv[2])) != 1 ):
        numjob = sqrt(float(numfiles(str(sys.argv[1]),str(sys.argv[2])))-1)
    else:
        numjob = 1
   # numjob = 1
    numjob = int(numjob)
    print str(numjob)
    joder = 0
    stopc = 0
    while joder == 0:
        cont = 0
        for z in range(numjob):
            dqm = [item[:-1] for item in os.popen('rfdir /castor/cern.ch/cms' + path + '/' + 'DQM_' + str(sys.argv[2]) + '_' + str(z) + '.root' )]
            if (dqm == []):
                cont = cont + 1
            srpc = [item[:-1] for item in os.popen('rfdir /castor/cern.ch/cms' + path + '/' + 'SRPC_' + str(sys.argv[2]) + '_' + str(z) + '.root' )]
            if (srpc == []):
                cont = cont + 1
            grpc = [item[:-1] for item in os.popen('rfdir /castor/cern.ch/cms' + path + '/' + 'GRPC_' + str(sys.argv[2]) + '_' + str(z) + '.root' )]
            if (grpc == []):
                cont = cont + 1
            terpc = [item[:-1] for item in os.popen('rfdir /castor/cern.ch/cms' + path + '/' + 'Trigger_eff_' + str(sys.argv[2]) + '_' + str(z) + '.root' )]
            if (terpc == []):
                cont = cont + 1
            noi = [item[:-1] for item in os.popen('rfdir /castor/cern.ch/cms' + path1 + '/' + 'Noise_' + str(sys.argv[2]) + '_' + str(z) + '.root' )]
            if (dqm == []):
                cont = cont + 1
            trig = [item[:-1] for item in os.popen('rfdir /castor/cern.ch/cms' + path1 + '/' + 'Trig_' + str(sys.argv[2]) + '_' + str(z) + '.root' )]
            if (noi == []):
                cont = cont + 1

            print 'count  =========== ' + str(cont)    

        if(cont == 0):
            joder = 1
        else:
            cor = [item[:-1] for item in os.popen('bjobs | wc | awk \'{print $1}\'') ]
            print 'running jobs =============== ' + str(cor[0])
            if ( int(cor[0]) < int(cont) ):
                print 'There were some failed jobs in the first step of merging, it maybe do to missing jobs or a crash in a small job in merging , check and resubmit!!!!!!!!!'
                joder = 1
                stopc =1
        if (joder == 0):        
            time.sleep(60)                

    os.system('rm MergeJobTemplate_*.job')

    os.system('cp MergeJobTemplate.job '+ tmpath1 + 'MergeJobTemplate_DQM_' + str(sys.argv[2]) + '.job' )
    os.system('cp MergeJobTemplate.job '+ tmpath1 + 'MergeJobTemplate_SRPC_' + str(sys.argv[2]) + '.job' )
    os.system('cp MergeJobTemplate.job '+ tmpath1 + 'MergeJobTemplate_GRPC_' + str(sys.argv[2]) + '.job' )
    os.system('cp MergeJobTemplate.job '+ tmpath1 + 'MergeJobTemplate_Trigger_eff_' + str(sys.argv[2]) + '.job' )
    os.system('cp MergeJobTemplate.job '+ tmpath1 + 'MergeJobTemplate_Noise_' + str(sys.argv[2]) + '.job' )
    os.system('cp MergeJobTemplate.job '+ tmpath1 + 'MergeJobTemplate_Trig_' + str(sys.argv[2]) + '.job' )
    
    os.system('cmsenv')
    
    detString.replacesingle( tmpath1 + 'MergeJobTemplate_DQM_' + str(sys.argv[2]) + '.job' ,['----RUN-NUMBER----',str(sys.argv[2])])
    detString.replacesingle( tmpath1 + 'MergeJobTemplate_SRPC_' + str(sys.argv[2]) + '.job' ,['----RUN-NUMBER----',str(sys.argv[2])])
    detString.replacesingle( tmpath1 + 'MergeJobTemplate_GRPC_' + str(sys.argv[2]) + '.job' ,['----RUN-NUMBER----',str(sys.argv[2])])
    detString.replacesingle( tmpath1 + 'MergeJobTemplate_Trigger_eff_' + str(sys.argv[2]) + '.job' ,['----RUN-NUMBER----',str(sys.argv[2])])
    detString.replacesingle( tmpath1 + 'MergeJobTemplate_Noise_' + str(sys.argv[2]) + '.job' ,['----RUN-NUMBER----',str(sys.argv[2])])
    detString.replacesingle( tmpath1 + 'MergeJobTemplate_Trig_' + str(sys.argv[2]) + '.job' ,['----RUN-NUMBER----',str(sys.argv[2])])
    
    fh1 = open( tmpath1 +'MergeJobTemplate_DQM_' + str(sys.argv[2]) + '.job','a')
    fh2 = open( tmpath1 +'MergeJobTemplate_SRPC_' + str(sys.argv[2]) + '.job','a')
    fh3 = open( tmpath1 +'MergeJobTemplate_GRPC_' + str(sys.argv[2]) + '.job','a')
    fh4 = open( tmpath1 +'MergeJobTemplate_Trigger_eff_' + str(sys.argv[2]) + '.job','a')
    fh5 = open( tmpath1 +'MergeJobTemplate_Noise_' + str(sys.argv[2]) + '.job','a')
    fh6 = open( tmpath1 +'MergeJobTemplate_Trig_' + str(sys.argv[2]) + '.job','a')
    
    fh1.writelines('\n rm -f ' + tmpath + 'DQM*.root \n')
    fh2.writelines('rm -f ' + tmpath + 'SRPC*.root \n')
    fh3.writelines('rm -f ' + tmpath + 'GRPC*.root \n')
    fh4.writelines('rm -f ' + tmpath + 'Trigger_eff_*.root \n')
    fh5.writelines('rm -f ' + tmpath + 'Noise*.root \n')
    fh6.writelines('rm -f ' + tmpath + 'Trig*.root \n')
    
    fh1.writelines('rm -f ' + tmpath + 'W*.root \n')
    fh1.writelines('rm -f ' + tmpath + 'Merge*.root \n')
    fh2.writelines('rm -f ' + tmpath + 'W*.root \n')
    fh2.writelines('rm -f ' + tmpath + 'Merge*.root \n')
    fh3.writelines('rm -f ' + tmpath + 'W*.root \n')
    fh3.writelines('rm -f ' + tmpath + 'Merge*.root \n')
    fh4.writelines('rm -f ' + tmpath + 'W*.root \n')
    fh4.writelines('rm -f ' + tmpath + 'Merge*.root \n')
    fh5.writelines('rm -f ' + tmpath + 'W*.root \n')
    fh5.writelines('rm -f ' + tmpath + 'Merge*.root \n')
    fh6.writelines('rm -f ' + tmpath + 'W*.root \n')
    fh6.writelines('rm -f ' + tmpath + 'Merge*.root \n')
    
    for z in range(numjob):
         fh1.writelines('cmsStageIn '+ path + '/' + 'DQM_' + str(sys.argv[2]) + '_' + str(z) + '.root .\n')
         fh2.writelines('cmsStageIn '+ path + '/' + 'SRPC_' + str(sys.argv[2]) + '_' + str(z) + '.root .\n' )
         fh3.writelines('cmsStageIn '+ path + '/' + 'GRPC_' + str(sys.argv[2]) + '_' + str(z) + '.root .\n' )
         fh4.writelines('cmsStageIn '+ path + '/' + 'Trigger_eff_' + str(sys.argv[2]) + '_' + str(z) + '.root .\n' )
         
         if (int(z)==0 ): 
            fh1.writelines('hadd out.root '+ 'DQM_' + str(sys.argv[2]) + '_' + str(z) + '.root \n')
            fh2.writelines('hadd out.root '+ 'SRPC_' + str(sys.argv[2]) + '_' + str(z) + '.root \n')
            fh3.writelines('hadd out.root '+ 'GRPC_' + str(sys.argv[2]) + '_' + str(z) + '.root \n')
            fh4.writelines('hadd out.root '+ 'Trigger_eff_' + str(sys.argv[2]) + '_' + str(z) + '.root \n')
            
            fh1.writelines('mv out.root aux.root \n')
            fh2.writelines('mv out.root aux.root \n')
            fh3.writelines('mv out.root aux.root \n')
            fh4.writelines('mv out.root aux.root \n')
            
         else:
            fh1.writelines('hadd out.root '+ 'DQM_' + str(sys.argv[2]) + '_' + str(z) + '.root aux.root\n')
            fh2.writelines('hadd out.root '+ 'SRPC_' + str(sys.argv[2]) + '_' + str(z) + '.root aux.root\n')
            fh3.writelines('hadd out.root '+ 'GRPC_' + str(sys.argv[2]) + '_' + str(z) + '.root aux.root\n')
            fh4.writelines('hadd out.root '+ 'Trigger_eff_' + str(sys.argv[2]) + '_' + str(z) + '.root aux.root\n')
            
            fh1.writelines('rm aux.root \n')
            fh1.writelines('mv out.root aux.root \n')
            fh2.writelines('rm aux.root \n')
            fh2.writelines('mv out.root aux.root \n')
            fh3.writelines('rm aux.root \n')
            fh3.writelines('mv out.root aux.root \n')
            fh4.writelines('rm aux.root \n')
            fh4.writelines('mv out.root aux.root \n')            

            
         fh5.writelines('cmsStageIn '+ path1 + '/' + 'Noise_' + str(sys.argv[2]) + '_' + str(z) + '.root .\n')
         fh6.writelines('cmsStageIn '+ path1 + '/' + 'Trig_' + str(sys.argv[2]) + '_' + str(z) + '.root .\n')
        
         if (int(z)==0 ):
            fh5.writelines('mv Noise_' + str(sys.argv[2]) + '_' + str(z) + '.root aux1.root\n')
            fh6.writelines('mv Trig_' + str(sys.argv[2]) + '_' + str(z) + '.root aux3.root\n')
         else:    
            fh5.writelines('hadd out1.root '+ 'Noise_' + str(sys.argv[2]) + '_' + str(z) + '.root ' + 'aux1.root\n')
            fh6.writelines('hadd out3.root '+ 'Trig_' + str(sys.argv[2]) + '_' + str(z) + '.root ' + 'aux3.root\n')
            fh5.writelines('rm aux1.root \n')
            fh5.writelines('mv out1.root aux1.root \n')
            fh6.writelines('rm aux3.root \n')
            fh6.writelines('mv out3.root aux3.root \n')


    fh1.writelines('cmsStageOut aux.root ' + path +'/Merge_DQM.root \n')
    fh1.writelines('rfchmod +777 ' + path +'/Merge_DQM.root \n' )
    fh2.writelines('cmsStageOut aux.root ' + path +'/Merge_SRPC.root \n')
    fh2.writelines('rfchmod +777 ' + path +'/Merge_SRPC.root \n' )
    fh3.writelines('cmsStageOut aux.root ' + path +'/Merge_GRPC.root \n')
    fh3.writelines('rfchmod +777 ' + path +'/Merge_GRPC.root \n' )
    fh4.writelines('cmsStageOut aux.root ' + path +'/Trigger_eff_tot.root \n')
    fh4.writelines('rfchmod +777 ' + path +'/Trigger_eff_tot.root \n' )    
    fh5.writelines('cmsStageOut aux1.root ' + path1 +'/Merge_Noise_tot.root \n')
    fh5.writelines('rfchmod +777 ' + path1 +'/Merge_Noise_tot.root \n' )
    fh6.writelines('cmsStageOut aux3.root ' + path1 +'/Merge_Trig_tot.root \n')
    fh6.writelines('rfchmod +777 ' + path1 +'/Merge_Trig_tot.root \n' )
    
    fh1.close()
    fh2.close()
    fh3.close()
    fh4.close()
    fh5.close()
    fh6.close()
    
    job1 = 'MergeJobTemplate_DQM_' + str(sys.argv[2]) + '.job'
    job2 = 'MergeJobTemplate_SRPC_' + str(sys.argv[2]) + '.job'
    job3 = 'MergeJobTemplate_GRPC_' + str(sys.argv[2]) + '.job'
    job4 = 'MergeJobTemplate_Trigger_eff_' + str(sys.argv[2]) + '.job'
    job5 = 'MergeJobTemplate_Noise_' + str(sys.argv[2]) + '.job'
    job6 = 'MergeJobTemplate_Trig_' + str(sys.argv[2]) + '.job'
    
    joberr1 = job1 + 'cerr'
    jobout1 = job1 + 'cout'
    joberr2 = job2 + 'cerr'
    jobout2 = job2 + 'cout'
    joberr3 = job3 + 'cerr'
    jobout3 = job3 + 'cout'
    joberr4 = job4 + 'cerr'
    jobout4 = job4 + 'cout'
    joberr5 = job5 + 'cerr'
    jobout5 = job5 + 'cout'
    joberr6 = job6 + 'cerr'
    jobout6 = job6 + 'cout'
     
    os.system('chmod a+x ' + tmpath1 + 'MergeJobTemplate_DQM_' + str(sys.argv[2]) + '.job')
    dqm = [item[:-1] for item in os.popen('rfdir /castor/cern.ch/cms' + path + '/' + 'Merge_DQM.root' )]
    if (dqm == [] and stopc == 0):
        os.system('bsub -q cmscaf1nh ' + ' -e ' +  tmpath1 + joberr1 + ' -o ' +  tmpath1 + jobout1 + ' ' + tmpath1 + job1)
    os.system('chmod a+x ' + tmpath1 + 'MergeJobTemplate_SRPC_' + str(sys.argv[2]) + '.job')
    srpc = [item[:-1] for item in os.popen('rfdir /castor/cern.ch/cms' + path + '/' + 'Merge_SRPC.root' )]
    if (srpc == [] and stopc == 0):
        os.system('bsub -q cmscaf1nh ' + ' -e ' +  tmpath1 + joberr2 + ' -o ' +  tmpath1 + jobout2 + ' ' + tmpath1 + job2)
    os.system('chmod a+x ' + tmpath1 + 'MergeJobTemplate_GRPC_' + str(sys.argv[2]) + '.job')
    grpc = [item[:-1] for item in os.popen('rfdir /castor/cern.ch/cms' + path + '/' + 'Merge_GRPC.root' )]
    if (grpc == [] and stopc == 0):
        os.system('bsub -q cmscaf1nh ' + ' -e ' +  tmpath1 + joberr3 + ' -o ' +  tmpath1 + jobout3 + ' ' + tmpath1 + job3)
    os.system('chmod a+x ' + tmpath1 + 'MergeJobTemplate_Trigger_eff_' + str(sys.argv[2]) + '.job')
    tef = [item[:-1] for item in os.popen('rfdir /castor/cern.ch/cms' + path + '/' + 'Trigger_eff_tot.root' )]
    if (tef == [] and stopc == 0):
        os.system('bsub -q cmscaf1nh ' + ' -e ' +  tmpath1 + joberr4 + ' -o ' +  tmpath1 + jobout4 + ' ' + tmpath1 + job4)
    os.system('chmod a+x ' + tmpath1 + 'MergeJobTemplate_Noise_' + str(sys.argv[2]) + '.job')
    nois = [item[:-1] for item in os.popen('rfdir /castor/cern.ch/cms' + path1 + '/' + 'Merge_Noise_tot.root' )]
    if (nois == [] and stopc == 0):
        os.system('bsub -q cmscaf1nh ' + ' -e ' +  tmpath1 + joberr5 + ' -o ' +  tmpath1 + jobout5 + ' ' + tmpath1 + job5)
    os.system('chmod a+x ' + tmpath1 + 'MergeJobTemplate_Trig_' + str(sys.argv[2]) + '.job')
    tri = [item[:-1] for item in os.popen('rfdir /castor/cern.ch/cms' + path1 + '/' + 'Merge_Trig_tot.root' )]
    if (tri == [] and stopc == 0):
        os.system('bsub -q cmscaf1nh ' + ' -e ' +  tmpath1 + joberr6 + ' -o ' +  tmpath1 + jobout6 + ' ' + tmpath1 + job6)

    joder = 0
    stopc = 0

    while joder == 0:
        cont = 0
        dqm = [item[:-1] for item in os.popen('rfdir /castor/cern.ch/cms' + path + '/' + 'Merge_DQM.root' )]
        if (dqm == []):
            cont = cont + 1
        srpc = [item[:-1] for item in os.popen('rfdir /castor/cern.ch/cms' + path + '/' + 'Merge_SRPC.root' )]
        if (srpc == []):
            cont = cont + 1
        grpc = [item[:-1] for item in os.popen('rfdir /castor/cern.ch/cms' + path + '/' + 'Merge_GRPC.root' )]
        if (grpc == []):
            cont = cont + 1

        print 'Second step count  =========== ' + str(cont)    

        if(cont == 0):
            joder = 1
        else:
            cor = [item[:-1] for item in os.popen('bjobs | wc | awk \'{print $1}\'') ]
            print 'running jobs =============== ' + str(cor[0])
            if ( int(cor[0]) < int(cont) ):
                print 'There were some failed jobs merging the efficiencies or the DQM, check and resubmit!!!!!!!!!'
                joder = 1
                stopc = 1
        if (joder == 0):        
            time.sleep(60)


    
    job = 'MergeJobTemplate_tot_' + str(sys.argv[2]) + '.job'
    os.system('cp MergeJobTemplate.job '+ tmpath1 + job )
    
    detString.replacesingle( tmpath1 + job ,['----RUN-NUMBER----',str(sys.argv[2])])
    
    fh = open( tmpath1 + job,'a')
    
    fh.writelines('cmsStageIn '+ path + '/' + 'Merge_DQM.root .\n')
    fh.writelines('cmsStageIn '+ path + '/' + 'Merge_SRPC.root .\n' )
    fh.writelines('cmsStageIn '+ path + '/' + 'Merge_GRPC.root .\n' )
    
    fh.writelines('hadd Merge_DQM_SRPC_GRPC.root Merge_DQM.root Merge_SRPC.root Merge_GRPC.root \n')
    
    fh.writelines('cmsStageOut Merge_DQM_SRPC_GRPC.root ' + path +'/Merge_DQM_SRPC_GRPC.root \n')
    fh.writelines('rfchmod +777 ' + path +'/Merge_DQM_SRPC_GRPC.root \n' )
    
    fh.writelines('cp '+pwd[0]+'/LastPlotStep.py ' + tmpath + str(sys.argv[2])+'\n')
    fh.writelines('chmod a+x ' + tmpath + str(sys.argv[2]) + '/LastPlotStep.py\n')
    fh.writelines('cp '+pwd[0]+'/GlobalPlotsProduction.py ' + tmpath + str(sys.argv[2])+'\n')
    fh.writelines('chmod a+x ' + tmpath + str(sys.argv[2]) + '/GlobalPlotsProduction.py\n')
    fh.writelines('cp '+pwd[0]+'/QualityPerformance.py ' + tmpath + str(sys.argv[2])+'\n')
    fh.writelines('chmod a+x ' + tmpath + str(sys.argv[2]) + '/QualityPerformance.py\n')
    fh.writelines('cp '+pwd[0]+'/EfficiencyPlotProductionDisk.py ' + tmpath + str(sys.argv[2])+'\n')
    fh.writelines('chmod a+x ' + tmpath + str(sys.argv[2]) + '/EfficiencyPlotProductionDisk.py\n')
    fh.writelines('cp '+pwd[0]+'/EfficiencyPlotProduction.py ' + tmpath + str(sys.argv[2])+'\n')
    fh.writelines('chmod a+x ' + tmpath + str(sys.argv[2]) + '/EfficiencyPlotProduction.py\n')
    fh.writelines('cp '+pwd[0]+'/disk_coord.txt ' + tmpath + str(sys.argv[2])+'\n')
    fh.writelines('cp '+pwd[0]+'/wheel_coord.txt ' + tmpath + str(sys.argv[2])+'\n')
    
    fh.writelines('./LastPlotStep.py ' + str(sys.argv[1]) +  ' '  + str(sys.argv[2]) + '\n')    
    fh.close()
    
    joberr = job + 'cerr'
    jobout = job + 'cout'
    os.system('chmod a+x '+tmpath1+ job)
    if (stopc == 0):
        os.system('bsub -q cmscaf1nd ' + ' -e ' +  tmpath1 + joberr + ' -o ' +  tmpath1 + jobout + ' ' + tmpath1 + job)
    print 'Done Final merge!!!'            
