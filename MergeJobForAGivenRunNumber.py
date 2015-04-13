#! /usr/bin/env python
import commands
import sys, os, string, fileinput
from ROOT import *

class ShellCommandTranslation:
    def __init__(self):
        self.data = []
        
    def rfdir_py(self,string_file):
        cmd = 'rfdir' + ' ' + string_file + ' | ' + ' awk \'{print $9}\' '
        the_files = [item[:-1] for item in os.popen(cmd)]
        return the_files

    def rfdirgrep_py(self,string_file, key, option):
        cmd = 'rfdir' + ' ' + string_file + ' | ' + 'grep ' + option + ' ' + key + ' | ' + ' awk \'{print $9}\' '
        the_files = [item[:-1] for item in os.popen(cmd)]
        return the_files

    def rfmkdir_py(self,string_path):
        newdir = ''
        for i in range(len(string_path)):
            newdir = newdir + '/'+ string_path[i]
            cmd = 'rfmkdir' + ' -m 777  ' + newdir

            try:
                os.system(cmd)
            except OSError:
                pass

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
    ds = str(sys.argv[1]).replace('/','')  
    
    path = '/castor/cern.ch/cms/store/caf/user/ccmuon/RPC/GlobalRuns/' + ds + '/' + str(sys.argv[2]) + '/root'
    path1 = '/castor/cern.ch/cms/store/caf/user/ccmuon/RPC/GlobalRuns/' + ds + '/' + str(sys.argv[2]) + '/noise'

    cmd0 = 'whoami'
    user = [item[:-1] for item in os.popen(cmd0)]
    tmppath = '/tmp/' + user[0] + '/' + str(sys.argv[2]) + '/'
#    gotocom = 'echo $HOME'
#    gotocom1 =  [item[:-1] for item in os.popen(gotocom)]
#    procom = 'project CMSSW'
#    cmscom = 'scramv1 project CMSSW CMSSW_2_2_4'
#    cdcom = 'CMSSW_2_2_4/src'
#    envcom = 'eval `scramv1 ru -csh`'

    os.system('source /afs/cern.ch/cms/caf/setup.csh')

    shellComm = ShellCommandTranslation()
    listSRPC = shellComm.rfdirgrep_py(path,'SRPC','')
    listDQM = shellComm.rfdirgrep_py(path,'DQM','')
    listNoise = shellComm.rfdirgrep_py(path1,'NoiseTrig','')

    os.system('rm MergeJobTemplate_*.job')
    os.system('cp MergeJobTemplate.job MergeJobTemplate_' + str(sys.argv[2]) + '.job' )
    detString.replacesingle('MergeJobTemplate_' + str(sys.argv[2]) + '.job' ,['----RUN-NUMBER----',str(sys.argv[2])])	
    fh = open('MergeJobTemplate_' + str(sys.argv[2]) + '.job','a')
    fh.writelines('\n rm -f ' + tmppath + 'DQM*.root \n')
    fh.writelines('rm -f ' + tmppath + 'SRPC*.root \n')
    fh.writelines('rm -f ' + tmppath + 'W*.root \n')
    fh.writelines('rm -f ' + tmppath + 'Merge*.root \n')
    
    end = 0

    verify = [item[:-1] for item in os.popen('rfdir ' + path + ' | grep \"Merge_DQM_SRPC.root\"')]

    if (verify == []):
        if int(sys.argv[3]) == -1:
            end =[item[:-1] for item in os.popen('rfdir ' + path + ' | grep DQM | grep -v Merge | wc | awk \'{print $1}\'')]

        else:
            end = int(sys.argv[3])

        j=0                         
        for i in range(len(listDQM)):
            if  i < end:
                if i >= int(sys.argv[4]) :
                    if j==0:
                        cmd3 = 'rfcp ' + path + '/' + listDQM[i] + ' ' + tmppath + 'aux_DQM.root'
                        #cmd3 = 'rfcp ' + path + '/' + listDQM[i] + ' ' + tmppath + 'aux_DQM.root'
                        fh.writelines(cmd3 + '\n')
                        j=1
                    else:
                        #cmd3 = 'rfcp ' + path + '/' + listDQM[i] + ' ' + tmppath + listDQM[i]
                        cmd3 = 'rfcp ' + path + '/' + listDQM[i] + ' ' + tmppath + listDQM[i]
                        fh.writelines(cmd3 + '\n')
                        cmd3 = 'hadd ' + tmppath + 'out_DQM.root ' + path + '/' + listDQM[i] + ' ' + tmppath + 'aux_DQM.root'
                        fh.writelines(cmd3 + '\n')
                        cmd3 = 'rm ' + tmppath + 'aux_DQM.root'
                        fh.writelines(cmd3 + '\n')
                        cmd3 = 'mv ' + tmppath + 'out_DQM.root ' + tmppath + 'aux_DQM.root'
                        fh.writelines(cmd3 + '\n')

        fh.writelines('mv ' +tmppath + 'aux_DQM.root ' + tmppath + 'MergeDQM.root\n')


        if int(sys.argv[3]) == -1:
            end =[item[:-1] for item in os.popen('rfdir ' + path1 + ' | grep NoiseTrig | grep -v Merge | wc | awk \'{print $1}\'')]
            
        else:
            end = int(sys.argv[3])
            
        ch = TChain('RPCTriggerNoiseMonitoring')
        ch1 = TChain('RPCNoiseMonitoring')

        j=0
        for i in range(len(listNoise)):
            if  i < end:
                if i >= int(sys.argv[4]) :
                    ch.Add('rfio:' + path1 + '/' + listNoise[i])
                    ch1.Add('rfio:' + path1 + '/' + listNoise[i])
                    j=j+1
                    print 'I\'m Still working for you ' + str(j)

        ch.Merge(tmppath + 'mergeTrig'+str(sys.argv[2])+'.root')
        ch1.Merge(tmppath + 'mergeNoise'+str(sys.argv[2])+'.root')

        os.system('hadd ' + tmppath + 'mergeNoiseTrig'+str(sys.argv[2])+'.root ' + tmppath + 'mergeTrig'+str(sys.argv[2])+'.root ' + tmppath + 'mergeNoise'+str(sys.argv[2])+'.root')                                                        
#        os.system('rfcp ' + tmppath + 'mergeNoiseTrig'+str(sys.argv[2])+'.root ' + path1 + '/merge_NoiseTrig.root \n')
        os.system('rfcp ' + tmppath + 'mergeNoiseTrig'+str(sys.argv[2])+'.root ' + path1 + '/merge_NoiseTrig.root \n')    
    
        if int(sys.argv[3]) == -1:
            end =[item[:-1] for item in os.popen('rfdir ' + path + ' | grep SRPC | grep -v Merge | wc | awk \'{print $1}\'')]
        else:
            end = int(sys.argv[3])

        j=0    
        for i in range(len(listSRPC)):
            if i < end:
                if i >= int(sys.argv[4]):
                    if j==0:
                        #cmd5 = 'rfcp ' + path + '/' + listSRPC[i] + ' ' + tmppath + 'aux_SRPC.root'
                        cmd5 = 'rfcp ' + path + '/' + listSRPC[i] + ' ' + tmppath + 'aux_SRPC.root'
                        fh.writelines(cmd5 +'\n')
                        j=1
                    else:
                        cmd5 = 'rfcp ' + path + '/' + listSRPC[i] + ' ' + tmppath + listSRPC[i]
                        fh.writelines(cmd5 + '\n')
                        cmd5 = 'hadd ' + tmppath + 'out_SRPC.root ' + path + '/' + listSRPC[i] + ' ' + tmppath + 'aux_SRPC.root'
                        fh.writelines(cmd5 + '\n')
                        cmd5 = 'rm ' + tmppath + 'aux_SRPC.root'
                        fh.writelines(cmd5 + '\n')
                        cmd5 = 'mv ' + tmppath + 'out_SRPC.root ' + tmppath + 'aux_SRPC.root'
                        fh.writelines(cmd5 + '\n')

        fh.writelines('mv ' +tmppath + 'aux_SRPC.root ' + tmppath + 'MergeSRPC.root\n')                    

        fh.writelines('hadd ' + tmppath + 'Merge_1.root ' + tmppath + 'Merge*.root \n')
        fh.writelines('rfcp ' + tmppath + 'Merge_1.root ' + path + '/Merge_DQM_SRPC.root \n')
        cwd = os.getcwd()
        fh.writelines('cd ' + cwd + '\n')
        
    wheels = ['W-2','W-1','W+0','W+1','W+2']
    
    for w in wheels:
        fh.writelines('./EfficiencyPlotProduction.py ' + tmppath + 'Merge_1.root ' + w + ' \n')
        fh.writelines('mv prova.root ' + tmppath + w + '.root \n')

    #   disks = ['RE-3','RE-2','RE-1','RE+1','RE+2','RE+3']
    disks = ['RE+2','RE+3']

    for w in disks:
        fh.writelines('./EfficiencyPlotProductionDisk.py ' + tmppath + 'Merge_1.root ' + w + '\n')
        fh.writelines('mv prova.root ' + tmppath + w + '.root \n')
                        
    fh.writelines('hadd -f ' + tmppath + 'Merge_tot.root ' +  tmppath + 'Merge_1.root ' + tmppath +'W*.root ' + tmppath +'RE*.root \n')
    fh.writelines('rfcp ' + tmppath + 'Merge_tot.root ' + path + '/Merge_tot.root \n' )
    fh.close()
    os.system('chmod a+x MergeJobTemplate_' + str(sys.argv[2]) + '.job')
    os.system('bsub -q cmscaf MergeJobTemplate_' + str(sys.argv[2]) + '.job'  )
    print 'DONE!!!!!'
            


