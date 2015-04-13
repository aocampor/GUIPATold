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
    stopc = 0
    while joder == 0:
        cont = 0
        for z in range(numjob):
            strip01 = [item[:-1] for item in os.popen('rfdir /castor/cern.ch/cms' + path1 + '/' + 'Strips_01_' + str(sys.argv[2]) + '_' + str(z) + '.root' )]
            if (strip01 == []):
                cont = cont + 1
            strip02 = [item[:-1] for item in os.popen('rfdir /castor/cern.ch/cms' + path1 + '/' + 'Strips_02_' + str(sys.argv[2]) + '_' + str(z) + '.root' )]
            if (strip02 == []):
                cont = cont + 1
            strip00 = [item[:-1] for item in os.popen('rfdir /castor/cern.ch/cms' + path1 + '/' + 'Strips_00_' + str(sys.argv[2]) + '_' + str(z) + '.root' )]
            if (strip00 == []):
                cont = cont + 1
            strip0m1 = [item[:-1] for item in os.popen('rfdir /castor/cern.ch/cms' + path1 + '/' + 'Strips_0m1_' + str(sys.argv[2]) + '_' + str(z) + '.root' )]
            if (strip0m1 == []):
                cont = cont + 1
            strip0m2 = [item[:-1] for item in os.popen('rfdir /castor/cern.ch/cms' + path1 + '/' + 'Strips_0m2_' + str(sys.argv[2]) + '_' + str(z) + '.root' )]
            if (strip0m2 == []):
                cont = cont + 1
            strip11 = [item[:-1] for item in os.popen('rfdir /castor/cern.ch/cms' + path1 + '/' + 'Strips_11_' + str(sys.argv[2]) + '_' + str(z) + '.root' )]
            if (strip11 == []):
                cont = cont + 1
            strip12 = [item[:-1] for item in os.popen('rfdir /castor/cern.ch/cms' + path1 + '/' + 'Strips_12_' + str(sys.argv[2]) + '_' + str(z) + '.root' )]
            if (strip12 == []):
                cont = cont + 1                                
            strip13 = [item[:-1] for item in os.popen('rfdir /castor/cern.ch/cms' + path1 + '/' + 'Strips_13_' + str(sys.argv[2]) + '_' + str(z) + '.root' )]
            if (strip13 == []):
                cont = cont + 1
            stripm11 = [item[:-1] for item in os.popen('rfdir /castor/cern.ch/cms' + path1 + '/' + 'Strips_m11_' + str(sys.argv[2]) + '_' + str(z) + '.root' )]
            if (stripm11 == []):
                cont = cont + 1
            stripm12 = [item[:-1] for item in os.popen('rfdir /castor/cern.ch/cms' + path1 + '/' + 'Strips_m12_' + str(sys.argv[2]) + '_' + str(z) + '.root' )]
            if (stripm12 == []):
                cont = cont + 1
            stripm13 = [item[:-1] for item in os.popen('rfdir /castor/cern.ch/cms' + path1 + '/' + 'Strips_m13_' + str(sys.argv[2]) + '_' + str(z) + '.root' )]
            if (stripm13 == []):
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
                stopc = 1
        if (joder == 0):        
            time.sleep(60)


        
    os.system('rm MergeJobTemplate_*.job')
    os.system('cp MergeJobTemplate.job ' +tmpath1+'MergeJobTemplate_noise_' + str(sys.argv[2]) + '.job' )
    os.system('cmsenv')
    detString.replacesingle(tmpath1 +'MergeJobTemplate_noise_' + str(sys.argv[2]) + '.job' ,['----RUN-NUMBER----',str(sys.argv[2])])
    fh = open(tmpath1 + 'MergeJobTemplate_noise_' + str(sys.argv[2]) + '.job','a')
    fh.writelines('\n rm -f ' + tmpath0 + 'Strips*.root \n')
    fh.writelines('rm -f ' + tmpath0 + 'Merge*.root \n')
    fh.writelines('cp '+pwd[0]+'/noise_run_analyzer.py ' + tmpath0 +'\n')
    fh.writelines('chmod a+x ' + tmpath0 + 'noise_run_analyzer.py\n')
    fh.writelines('cp '+pwd[0]+'/wheel_noise_producer.py ' + tmpath0 +'\n')
    fh.writelines('chmod a+x ' + tmpath0 + 'wheel_noise_producer.py\n')
    fh.writelines('cp '+pwd[0]+'/plot_producer1.py ' + tmpath0 +'\n')
    fh.writelines('chmod a+x ' + tmpath0 + 'plot_producer1.py\n')
    fh.writelines('cp '+pwd[0]+'/plot_davide.py ' + tmpath0 +'\n')
    fh.writelines('chmod a+x ' + tmpath0 + 'plot_davide.py\n')    
    fh.writelines('cp '+pwd[0]+'/plot_producer.py ' + tmpath0 +'\n')
    fh.writelines('chmod a+x ' + tmpath0 + 'plot_producer.py\n')
    fh.writelines('cp '+pwd[0]+'/end_noise_producer.py ' + tmpath0 +'\n')
    fh.writelines('chmod a+x ' + tmpath0 + 'end_noise_producer.py\n')
    fh.writelines('cp '+pwd[0]+'/summary_plot_producer.py ' + tmpath0 +'\n')
    fh.writelines('chmod a+x ' + tmpath0 + 'summary_plot_producer.py\n')
    fh.writelines('cp '+pwd[0]+'/summary_plot_producer_end.py ' + tmpath0 +'\n')
    fh.writelines('chmod a+x ' + tmpath0 + 'summary_plot_producer_end.py\n')    
    fh.writelines('cp '+pwd[0]+'/plot_producer1_end.py ' + tmpath0 +'\n')
    fh.writelines('chmod a+x ' + tmpath0 + 'plot_producer1_end.py\n')
    fh.writelines('cp '+pwd[0]+'/plot_producer_end.py ' + tmpath0 +'\n')
    fh.writelines('chmod a+x ' + tmpath0 + 'plot_producer_end.py\n')
    fh.writelines('cp '+pwd[0]+'/noise_summary_plot_producer.py ' + tmpath0 +'\n')
    fh.writelines('chmod a+x ' + tmpath0 + 'noise_summary_plot_producer.py\n')
    
    for z in range(numjob):
        fh.writelines('cmsStageIn '+ path1 + '/' + 'Strips_01_' + str(sys.argv[2]) + '_' + str(z) + '.root .\n')
        fh.writelines('cmsStageIn '+ path1 + '/' + 'Strips_02_' + str(sys.argv[2]) + '_' + str(z) + '.root .\n')
        fh.writelines('cmsStageIn '+ path1 + '/' + 'Strips_0m1_' + str(sys.argv[2]) + '_' + str(z) + '.root .\n')
        fh.writelines('cmsStageIn '+ path1 + '/' + 'Strips_0m2_' + str(sys.argv[2]) + '_' + str(z) + '.root .\n')
        fh.writelines('cmsStageIn '+ path1 + '/' + 'Strips_00_' + str(sys.argv[2]) + '_' + str(z) + '.root .\n')
        fh.writelines('cmsStageIn '+ path1 + '/' + 'Strips_11_' + str(sys.argv[2]) + '_' + str(z) + '.root .\n')
        fh.writelines('cmsStageIn '+ path1 + '/' + 'Strips_12_' + str(sys.argv[2]) + '_' + str(z) + '.root .\n')
        fh.writelines('cmsStageIn '+ path1 + '/' + 'Strips_13_' + str(sys.argv[2]) + '_' + str(z) + '.root .\n')
        fh.writelines('cmsStageIn '+ path1 + '/' + 'Strips_m11_' + str(sys.argv[2]) + '_' + str(z) + '.root .\n')
        fh.writelines('cmsStageIn '+ path1 + '/' + 'Strips_m12_' + str(sys.argv[2]) + '_' + str(z) + '.root .\n')
        fh.writelines('cmsStageIn '+ path1 + '/' + 'Strips_m13_' + str(sys.argv[2]) + '_' + str(z) + '.root .\n')


        if (int(z)==0 ): 
            fh.writelines('hadd out_01.root '+ 'Strips_01_' + str(sys.argv[2]) + '_' + str(z) + '.root \n')
            fh.writelines('mv out_01.root aux_01.root \n')
            fh.writelines('hadd out_02.root '+ 'Strips_02_' + str(sys.argv[2]) + '_' + str(z) + '.root \n')
            fh.writelines('mv out_02.root aux_02.root \n')
            fh.writelines('hadd out_00.root '+ 'Strips_00_' + str(sys.argv[2]) + '_' + str(z) + '.root \n')
            fh.writelines('mv out_00.root aux_00.root \n')
            fh.writelines('hadd out_0m1.root '+ 'Strips_0m1_' + str(sys.argv[2]) + '_' + str(z) + '.root \n')
            fh.writelines('mv out_0m1.root aux_0m1.root \n')
            fh.writelines('hadd out_0m2.root '+ 'Strips_0m2_' + str(sys.argv[2]) + '_' + str(z) + '.root \n')
            fh.writelines('mv out_0m2.root aux_0m2.root \n')
            fh.writelines('hadd out_11.root '+ 'Strips_11_' + str(sys.argv[2]) + '_' + str(z) + '.root \n')
            fh.writelines('mv out_11.root aux_11.root \n')
            fh.writelines('hadd out_12.root '+ 'Strips_12_' + str(sys.argv[2]) + '_' + str(z) + '.root \n')
            fh.writelines('mv out_12.root aux_12.root \n')
            fh.writelines('hadd out_13.root '+ 'Strips_13_' + str(sys.argv[2]) + '_' + str(z) + '.root \n')
            fh.writelines('mv out_13.root aux_13.root \n')
            fh.writelines('hadd out_m11.root '+ 'Strips_m11_' + str(sys.argv[2]) + '_' + str(z) + '.root \n')
            fh.writelines('mv out_m11.root aux_m11.root \n')
            fh.writelines('hadd out_m12.root '+ 'Strips_m12_' + str(sys.argv[2]) + '_' + str(z) + '.root \n')
            fh.writelines('mv out_m12.root aux_m12.root \n')
            fh.writelines('hadd out_m13.root '+ 'Strips_m13_' + str(sys.argv[2]) + '_' + str(z) + '.root \n')
            fh.writelines('mv out_m13.root aux_m13.root \n')
        else:
            fh.writelines('hadd out_01.root '+ 'Strips_01_' + str(sys.argv[2]) + '_' + str(z) + '.root  aux_01.root\n')
            fh.writelines('rm aux_01.root \n')
            fh.writelines('mv out_01.root aux_01.root \n')
            fh.writelines('hadd out_02.root '+ 'Strips_02_' + str(sys.argv[2]) + '_' + str(z) + '.root  aux_02.root\n')
            fh.writelines('rm aux_02.root \n')
            fh.writelines('mv out_02.root aux_02.root \n')
            fh.writelines('hadd out_00.root '+ 'Strips_00_' + str(sys.argv[2]) + '_' + str(z) + '.root  aux_00.root\n')
            fh.writelines('rm aux_00.root \n')
            fh.writelines('mv out_00.root aux_00.root \n')
            fh.writelines('hadd out_0m1.root '+ 'Strips_0m1_' + str(sys.argv[2]) + '_' + str(z) + '.root  aux_0m1.root\n')
            fh.writelines('rm aux_0m1.root \n')
            fh.writelines('mv out_0m1.root aux_0m1.root \n')
            fh.writelines('hadd out_0m2.root '+ 'Strips_0m2_' + str(sys.argv[2]) + '_' + str(z) + '.root  aux_0m2.root\n')
            fh.writelines('rm aux_0m2.root \n')
            fh.writelines('mv out_0m2.root aux_0m2.root \n')
            fh.writelines('hadd out_11.root '+ 'Strips_11_' + str(sys.argv[2]) + '_' + str(z) + '.root  aux_11.root\n')
            fh.writelines('rm aux_11.root \n')
            fh.writelines('mv out_11.root aux_11.root \n')
            fh.writelines('hadd out_12.root '+ 'Strips_12_' + str(sys.argv[2]) + '_' + str(z) + '.root  aux_12.root\n')
            fh.writelines('rm aux_12.root \n')
            fh.writelines('mv out_12.root aux_12.root \n')
            fh.writelines('hadd out_13.root '+ 'Strips_13_' + str(sys.argv[2]) + '_' + str(z) + '.root  aux_13.root\n')
            fh.writelines('rm aux_13.root \n')
            fh.writelines('mv out_13.root aux_13.root \n')
            fh.writelines('hadd out_m11.root '+ 'Strips_m11_' + str(sys.argv[2]) + '_' + str(z) + '.root  aux_m11.root\n')
            fh.writelines('rm aux_m11.root \n')
            fh.writelines('mv out_m11.root aux_m11.root \n')
            fh.writelines('hadd out_m12.root '+ 'Strips_m12_' + str(sys.argv[2]) + '_' + str(z) + '.root  aux_m12.root\n')
            fh.writelines('rm aux_m12.root \n')
            fh.writelines('mv out_m12.root aux_m12.root \n')
            fh.writelines('hadd out_m13.root '+ 'Strips_m13_' + str(sys.argv[2]) + '_' + str(z) + '.root  aux_m13.root\n')
            fh.writelines('rm aux_m13.root \n')
            fh.writelines('mv out_m13.root aux_m13.root \n')
            
    fh.writelines('mv aux_01.root ' + str(sys.argv[2])+'_01.root \n')        
    fh.writelines('cmsStageOut '+ str(sys.argv[2])+'_01.root ' + path1 +'/'+str(sys.argv[2])+'_01.root \n')
    fh.writelines('rfchmod +777 ' + path1 +'/'+str(sys.argv[2])+'_01.root \n')
    fh.writelines('mv aux_02.root ' + str(sys.argv[2])+'_02.root \n')
    fh.writelines('cmsStageOut ' +str(sys.argv[2])+'_02.root ' + path1 +'/'+str(sys.argv[2])+'_02.root \n')
    fh.writelines('rfchmod +777 ' + path1 +'/'+str(sys.argv[2])+'_02.root \n')
    fh.writelines('mv aux_00.root ' + str(sys.argv[2])+'_00.root \n')    
    fh.writelines('cmsStageOut '+str(sys.argv[2])+'_00.root ' + path1 +'/'+str(sys.argv[2])+'_00.root \n')
    fh.writelines('rfchmod +777 ' + path1 +'/'+str(sys.argv[2])+'_00.root \n')
    fh.writelines('mv aux_0m1.root ' + str(sys.argv[2])+'_0m1.root \n')    
    fh.writelines('cmsStageOut '+ str(sys.argv[2])+'_0m1.root ' + path1 +'/'+str(sys.argv[2])+'_0m1.root \n')
    fh.writelines('rfchmod +777 ' + path1 +'/'+str(sys.argv[2])+'_0m1.root \n')
    fh.writelines('mv aux_0m2.root ' + str(sys.argv[2])+'_0m2.root \n')    
    fh.writelines('cmsStageOut ' + str(sys.argv[2])+'_0m2.root ' + path1 +'/'+str(sys.argv[2])+'_0m2.root \n')
    fh.writelines('rfchmod +777 ' + path1 +'/'+str(sys.argv[2])+'_0m2.root \n')
    fh.writelines('mv aux_11.root ' + str(sys.argv[2])+'_11.root \n')
    fh.writelines('cmsStageOut ' +str(sys.argv[2])+'_11.root ' + path1 +'/'+str(sys.argv[2])+'_11.root \n')
    fh.writelines('rfchmod +777 ' + path1 +'/'+str(sys.argv[2])+'_11.root \n')
    fh.writelines('mv aux_12.root ' + str(sys.argv[2])+'_12.root \n')    
    fh.writelines('cmsStageOut '+str(sys.argv[2])+'_12.root ' + path1 +'/'+str(sys.argv[2])+'_12.root \n')
    fh.writelines('rfchmod +777 ' + path1 +'/'+str(sys.argv[2])+'_12.root \n')
    fh.writelines('mv aux_13.root ' + str(sys.argv[2])+'_13.root \n')    
    fh.writelines('cmsStageOut '+str(sys.argv[2])+'_13.root ' + path1 +'/'+str(sys.argv[2])+'_13.root \n')
    fh.writelines('rfchmod +777 ' + path1 +'/'+str(sys.argv[2])+'_13.root \n')
    fh.writelines('mv aux_m11.root ' + str(sys.argv[2])+'_m11.root \n')    
    fh.writelines('cmsStageOut ' +str(sys.argv[2])+'_m11.root ' + path1 +'/'+str(sys.argv[2])+'_m11.root \n')
    fh.writelines('rfchmod +777 ' + path1 +'/'+str(sys.argv[2])+'_m11.root \n')
    fh.writelines('mv aux_m12.root ' + str(sys.argv[2])+'_m12.root \n')    
    fh.writelines('cmsStageOut '+str(sys.argv[2])+'_m12.root ' + path1 +'/'+str(sys.argv[2])+'_m12.root \n')
    fh.writelines('rfchmod +777 ' + path1 +'/'+str(sys.argv[2])+'_m12.root \n')
    fh.writelines('mv aux_m13.root ' + str(sys.argv[2])+'_m13.root \n')    
    fh.writelines('cmsStageOut '+str(sys.argv[2])+'_m13.root ' + path1 +'/'+str(sys.argv[2])+'_m13.root \n')
    fh.writelines('rfchmod +777 ' + path1 +'/'+str(sys.argv[2])+'_m13.root \n')
    
    fh.writelines('./noise_run_analyzer.py ' + str(sys.argv[2]) + '\n')
    fh.writelines('cmsStageOut '+str(sys.argv[2])+'_final.root ' + path1 +'/ \n')
    fh.writelines('rfchmod +777 ' + path1 +'/'+str(sys.argv[2])+'_final.root \n')
    fh.close()
    tmpath1 = casa[0] + '/scratch0/' + str(sys.argv[2]) + '/job/'
    job = 'MergeJobTemplate_noise_' + str(sys.argv[2]) + '.job'
    joberr = job + 'cerr'
    jobout = job + 'cout'
    os.system('chmod a+x '+tmpath1+'MergeJobTemplate_noise_' + str(sys.argv[2]) + '.job')
    if(stopc == 0):
     os.system('bsub -q cmscaf1nd ' + ' -e ' +  tmpath1 + joberr + ' -o ' +  tmpath1 + jobout + ' ' + tmpath1 + job)
    print 'Done Final Noise merge!!!'
    
