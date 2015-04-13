#! /usr/bin/env python
import commands
import sys, os, string, fileinput
from ROOT import *
from math import *

def numfiles(dataset,runnum):
    total =[item[:-1] for item in os.popen('./aSearchCLI --dbsInst=cms_dbs_prod_global --limit=-1 --input \"find file where dataset like ' + dataset + ' and run = ' + runnum + '\" | grep -v root | awk \'{print $2}\'')]
#    print 'numfiles! ' + str(total[0])+ ' ' +  str(total[1])
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

    print 'Reading DBS please be patient, do not rush!!!!'
    detString = DetectFiles()

    me = [item[:-1] for item in os.popen('whoami')]
    casa = [item[:-1] for item in os.popen('echo $HOME')]

    ds = str(sys.argv[1]).replace('/','')  
    tmpath = '/tmp/' + me[0] + '/' +  str(sys.argv[2]) + '/'
    tmpath1 = casa[0] + '/scratch0/' + str(sys.argv[2]) + '/job/'
    
    os.system('mkdir ' + casa[0] + '/scratch0/' + str(sys.argv[2]))
    os.system('mkdir ' + tmpath1)
    
    path = '/store/caf/user/ccmuon/RPC/GlobalRuns/' + ds + '/' + str(sys.argv[2]) + '/' + str(sys.argv[4])
    path1 = '/castor/cern.ch/cms/store/caf/user/ccmuon/RPC/GlobalRuns/' + ds + '/' + str(sys.argv[2]) + '/out'


#    print str(numfiles(str(sys.argv[1]),str(sys.argv[2])))
    if (numfiles(str(sys.argv[1]),str(sys.argv[2])) != 1 ):

        numjob = sqrt(float(numfiles(str(sys.argv[1]),str(sys.argv[2])))-1)
        
    else:
        numjob = 1
#    numjob = 1
    numjob = int(numjob)
    numtemp = int(numfiles(str(sys.argv[1]),str(sys.argv[2])))/numjob+1
#    numtemp = 1

    
    a = []
    b = []

    j=0
    for i in range(int(numfiles(str(sys.argv[1]),str(sys.argv[2])))):
    #for i in range(int(1)):
        a.append(str(sys.argv[3])+str(i)+'.root')
        j=j+1
        if (j==int(numtemp)):
            b.append(a)
            a = []
            j = 0

    if (a != []):
        b.append(a)

    for i in range(numjob):
        job = tmpath1 + 'MergeJobTemplate_' + str(sys.argv[2]) + '_' + str(sys.argv[3]) + str(i) +'.job'
        ver = [item[:-1] for item in os.popen('rfdir /castor/cern.ch/cms' + path + '/' +  str(sys.argv[3]) + str(sys.argv[2]) + '_' + str(i) + '.root')]
        print ver
        if (ver == []):
            
            os.system('cp MergeJobTemplate.job ' + job )
            
            detString.replacesingle(job ,['----RUN-NUMBER----',str(sys.argv[2])])
            
            fh = open(job,'a')
            #        fh.writelines('\n rm -f ' + tmpath + str(sys.argv[3]) + '*.root \n')
        
            for item in b[i]:
                if (item == b[i][0]):
                    cmd3 = 'cmsStageIn ' + path + '/' + item + ' ' + tmpath + item #'aux_' + str(sys.argv[3]) + '.root'
                    fh.writelines(cmd3 + '\n')
                    fh.writelines('mv ' + tmpath + item + ' ' + 'aux_' + str(sys.argv[3]) + '.root \n')
                else:    
                    cmd3 = 'cmsStageIn ' + path + '/' + item + ' ' + tmpath + item
                    fh.writelines(cmd3 + '\n')
                    cmd3 = 'hadd ' + tmpath + 'out_' + str(sys.argv[3]) + '.root ' + tmpath + item + ' ' + tmpath + 'aux_' + str(sys.argv[3]) + '.root'
                    fh.writelines(cmd3 + '\n')
                    cmd3 = 'rm ' + tmpath + 'aux_' + str(sys.argv[3]) + '.root'
                    fh.writelines(cmd3 + '\n')
                    cmd3 = 'mv ' + tmpath + 'out_' + str(sys.argv[3]) + '.root ' + tmpath + 'aux_' + str(sys.argv[3]) + '.root'
                    fh.writelines(cmd3 + '\n')
            fh.writelines('mv ' + tmpath + 'aux_' + str(sys.argv[3]) + '.root ' + tmpath + '' + str(sys.argv[3]) +  str(sys.argv[2]) + '_' + str(i) + '.root\n')         
            fh.writelines('cmsStageOut '+ tmpath + '' + str(sys.argv[3]) + str(sys.argv[2]) + '_' + str(i) + '.root ' + path + '/ \n')
            fh.writelines('rfchmod +777 /castor/cern.ch/cms' + path + '/' + str(sys.argv[3]) + str(sys.argv[2]) + '_' + str(i) + '.root \n')
            fh.writelines('exit 0')
            fh.close()
            os.system('chmod a+x ' + job)
            joberr = job + 'err'
            jobout = job + 'out'
            os.system('bsub -q cmscaf1nh ' + ' -e ' +  tmpath1 + joberr + ' -o ' +  tmpath1 + jobout + ' ' + job)
            #        os.system('bsub -q 1nh ' + ' -e ' +  tmpath1 + joberr + ' -o ' +  tmpath1 + jobout + ' ' + job)        
    print 'Small Jobs Are Being submmitted'
