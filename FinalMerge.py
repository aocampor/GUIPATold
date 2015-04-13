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
                                

#
# main
#

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
                print 'There were some failed jobs in merging, check and resubmit!!!!!!!!!'
                joder = 1
        if (joder == 0):        
            time.sleep(60)

    os.system('rm MergeJobTemplate_*.job')
    os.system('cp MergeJobTemplate.job MergeJobTemplate_' + str(sys.argv[2]) + '.job' )
    os.system('cmsenv')
    detString.replacesingle('MergeJobTemplate_' + str(sys.argv[2]) + '.job' ,['----RUN-NUMBER----',str(sys.argv[2])])
    fh = open('MergeJobTemplate_' + str(sys.argv[2]) + '.job','a')
    fh.writelines('\n rm -f ' + tmpath + 'DQM*.root \n')
    fh.writelines('rm -f ' + tmpath + 'SRPC*.root \n')
    fh.writelines('rm -f ' + tmpath + 'GRPC*.root \n')
    fh.writelines('rm -f ' + tmpath + 'Noise*.root \n')
    fh.writelines('rm -f ' + tmpath + 'Trig*.root \n')    
    fh.writelines('rm -f ' + tmpath + 'W*.root \n')
    fh.writelines('rm -f ' + tmpath + 'Merge*.root \n')
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
    
                    
    for z in range(numjob):
        fh.writelines('cmsStageIn '+ path + '/' + 'DQM_' + str(sys.argv[2]) + '_' + str(z) + '.root .\n')
        fh.writelines('cmsStageIn '+ path + '/' + 'SRPC_' + str(sys.argv[2]) + '_' + str(z) + '.root .\n' )
        fh.writelines('cmsStageIn '+ path + '/' + 'GRPC_' + str(sys.argv[2]) + '_' + str(z) + '.root .\n' )
        fh.writelines('cmsStageIn '+ path + '/' + 'Trigger_eff_' + str(sys.argv[2]) + '_' + str(z) + '.root .\n' )

        if (int(z)==0 ): 
            fh.writelines('hadd out.root '+ 'DQM_' + str(sys.argv[2]) + '_' + str(z) + '.root ' + 'GRPC_' + str(sys.argv[2]) + '_' + str(z) + '.root ' + 'SRPC_' + str(sys.argv[2]) + '_' + str(z) + '.root ' +'Trigger_eff_' + str(sys.argv[2]) + '_' + str(z) + '.root \n')
            fh.writelines('mv out.root aux.root \n')
        else:
            fh.writelines('hadd out.root '+ 'DQM_' + str(sys.argv[2]) + '_' + str(z) + '.root ' + 'GRPC_' + str(sys.argv[2]) + '_' + str(z) + '.root ' + 'SRPC_' + str(sys.argv[2]) + '_' + str(z) + '.root ' +'Trigger_eff_' + str(sys.argv[2]) + '_' + str(z) + '.root aux.root\n')
            fh.writelines('rm aux.root \n')
            fh.writelines('mv out.root aux.root \n')
        fh.writelines('cmsStageIn '+ path1 + '/' + 'Noise_' + str(sys.argv[2]) + '_' + str(z) + '.root .\n')
        fh.writelines('cmsStageIn '+ path1 + '/' + 'Trig_' + str(sys.argv[2]) + '_' + str(z) + '.root .\n')
        if (int(z)==0 ):
            fh.writelines('mv Noise_' + str(sys.argv[2]) + '_' + str(z) + '.root aux1.root\n')
            fh.writelines('mv Trig_' + str(sys.argv[2]) + '_' + str(z) + '.root aux3.root\n')
        else:    
            fh.writelines('hadd out1.root '+ 'Noise_' + str(sys.argv[2]) + '_' + str(z) + '.root ' + 'aux1.root\n')
            fh.writelines('hadd out3.root '+ 'Trig_' + str(sys.argv[2]) + '_' + str(z) + '.root ' + 'aux3.root\n')
            fh.writelines('rm aux1.root \n')
            fh.writelines('mv out1.root aux1.root \n')
            fh.writelines('rm aux3.root \n')
            fh.writelines('mv out3.root aux3.root \n')                
            
        
    fh.writelines('cmsStageOut aux.root ' + path +'/Merge_DQM_SRPC_GRPC.root \n')
    fh.writelines('rfchmod +777 ' + path +'/Merge_DQM_SRPC_GRPC.root \n' )
    fh.writelines('cmsStageOut aux1.root ' + path1 +'/Merge_Noise_tot.root \n')
    fh.writelines('rfchmod +777 ' + path1 +'/Merge_Noise_tot.root \n' )
    fh.writelines('cmsStageOut aux3.root ' + path1 +'/Merge_Trig_tot.root \n')
    fh.writelines('rfchmod +777 ' + path1 +'/Merge_Trig_tot.root \n' )
    fh.writelines('./LastPlotStep.py ' + str(sys.argv[1]) +  ' '  + str(sys.argv[2]) + '\n')    
    fh.close()
    tmpath1 = casa[0] + '/scratch0/' + str(sys.argv[2]) + '/job/'
    job = 'MergeJobTemplate_' + str(sys.argv[2]) + '.job'
    joberr = job + 'cerr'
    jobout = job + 'cout'
    os.system('chmod a+x MergeJobTemplate_' + str(sys.argv[2]) + '.job')
    os.system('bsub -q cmscaf ' + ' -e ' +  tmpath1 + joberr + ' -o ' +  tmpath1 + jobout + ' ' + job)
    print 'Done Final merge!!!'
