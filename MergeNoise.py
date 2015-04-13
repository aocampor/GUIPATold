#! /usr/bin/env python
import commands
import sys, os, string, fileinput
from ROOT import *

def numfiles(dataset,runnum):
    total =[item[:-1] for item in os.popen('./aSearchCLI --dbsInst=cms_dbs_prod_global --limit=-1 --input \"find file where dataset like ' + dataset + ' and run = ' + runnum + '\" | grep -v root | awk \'{print $2}\'')]
    return total[1]


class DetectFiles:
    def f(self):
        return 'Detecting string!'

    def __init__(self):
        self.data = []
        
    def findPath(self,dataset,runNumber):
        cmd = './aSearchCLI --dbsInst=cms_dbs_prod_global --limit=10000 --input \" find file where dataset = ' + dataset + ' and ' + 'run = ' + runNumber + ' \" | egrep \"[a-Z]\" | grep -v \"Found\" '
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

    ds = str(sys.argv[1]).replace('/','')
    tmpath = '/tmp/' + me[0] + '/'
    tmpath1 = casa[0] + '/scratch0/' + str(sys.argv[2]) + '/job/'
    
    os.system('mkdir ' + casa[0] + '/scratch0/' + str(sys.argv[2]))
    os.system('mkdir ' + tmpath1)
    
    path = '/castor/cern.ch/cms/store/caf/user/ccmuon/RPC/GlobalRuns/' + ds + '/' + str(sys.argv[2]) + '/noise'
    path1 = '/castor/cern.ch/cms/store/caf/user/ccmuon/RPC/GlobalRuns/' + ds + '/' + str(sys.argv[2]) + '/out'


    numjob = sqrt(float(numfiles(str(sys.argv[1]),str(sys.argv[2])))-1)
    numjob = int(numjob)
    numtemp = int(numfiles(str(sys.argv[1]),str(sys.argv[2])))/numjob+1
    a = []
    b = []
    
    j=0
    for i in range(int(numfiles(str(sys.argv[1]),str(sys.argv[2])))):
        a.append(str(sys.argv[3])+str(i)+'.root')
        j=j+1
        if (j==int(numtemp)):
            b.append(a)
            a = []
            j = 0
            
    if (a != []):
        b.append(a)
        
    for i in range(numjob):
        
        job = tmpath1 + 'MergeNoiseTemplate_' + str(sys.argv[2]) + '_' + str(sys.argv[3]) + str(i) +'.job'
        print str(i) + ' ' + job
        os.system('cp MergeNoiseTemplate.job ' + job )
        detString.replacesingle(job ,['----RUN-NUMBER----',str(sys.argv[2])])
        
        fh = open(job,'a')

        for item in b[i]:
            fh.writelines('   ch.Add(\"rfio:' + path + '/' + item + '\");\n')
            fh.writelines('   ch1.Add(\"rfio:' + path + '/' + item + '\");\n')

        fh.writelines('   ch.Merge(\"'+tmpath + 'mergeTrig'+str(sys.argv[2])+ '_' +str(i) +'.root\");\n')
        fh.writelines('   ch1.Merge(\"'+tmpath + 'mergeNoise'+str(sys.argv[2])+ '_' +str(i) +'.root\");\n')
        fh.writelines('   .! hadd '+tmpath + 'MergeTrigNoise'+str(sys.argv[2])+'_' +str(i) +'.root '+tmpath + 'mergeNoise'+str(sys.argv[2])+ '_' +str(i) +'.root '+tmpath + 'mergeTrig'+str(sys.argv[2])+ '_' +str(i) +'.root \n')
        fh.writelines('   .! cmsStageOut '+ tmpath + 'MergeTrigNoise'+str(sys.argv[2])+ '_' +str(i) +'.root ' + path + '/ \n')
        fh.writelines('EOF \n')
        fh.close()
        
        os.system('chmod a+x ' + job)
        joberr = job + 'err'
        jobout = job + 'out'
        os.system('bsub -q cmscaf ' + ' -e ' +  tmpath1 + joberr + ' -o ' +  tmpath1 + jobout + ' ' + job)

        
