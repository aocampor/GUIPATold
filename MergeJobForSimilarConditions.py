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


        
#
# main
#
if __name__ == "__main__":

    ds = str(sys.argv[1]).replace('/','')
    runs = str(sys.argv[2]).split('.')
    path = []
    cmd0 = 'whoami'
    user = [item[:-1] for item in os.popen(cmd0)]
    tmppath = '/tmp/' + user[0] + '/' + str(sys.argv[2]) + '/'    
    for i in range(len(runs)):
        path.append('/castor/cern.ch/cms/store/caf/user/ccmuon/RPC/GlobalRuns/' + ds + '/' + runs[i] + '/root')
        print path[i]

    shellComm = ShellCommandTranslation()

    os.system('rm ' + tmppath + 'Merge_DQM_SRPC_*.root') 
    for j in range(len(path)):
        file = shellComm.rfdirgrep_py(path[j],'Merge_DQM_SRPC.root','')
        if len(file) == 0:
            os.system('./MergeJobForAGivenRunNumber.py ' + str(sys.argv[1]) + ' ' + runs[j] + ' -1 0')
        os.system('cmsStageIn ' + path[j] +'/Merge_DQM_SRPC.root '+ tmppath + 'Merge_DQM_SRPC_' + runs[j] + '.root')
        
    os.system('hadd -f ' +tmppath + 'Merge_' + str(sys.argv[2]) + 'DQM_SRPC.root ' + tmppath + 'Merge_DQM_SRPC_*.root')

    wheels = ['W-2','W-1','W+0','W+1','W+2']

    for w in wheels:
        os.system('./EfficiencyPlotProduction.py ' + tmppath + 'Merge_' + str(sys.argv[2]) + 'DQM_SRPC.root ' + w)
        os.system('mv prova.root ' + tmppath + w + '.root')

#   disks = ['RE-3','RE-2','RE-1','RE+1','RE+2','RE+3']
    disks = ['RE+2','RE+3']

    for w in disks:
        os.system('./EfficiencyPlotProductionDisk.py ' + tmppath + 'Merge_' + str(sys.argv[2]) + 'DQM_SRPC.root ' + w)
        os.system('mv prova.root ' + tmppath + w + '.root')
                        
    os.system('hadd -f ' + tmppath + 'Merge_'+str(sys.argv[2])+'tot.root ' +  tmppath + 'Merge_' + str(sys.argv[2]) + 'DQM_SRPC.root ' + tmppath +'W*.root ' + tmppath +'RE*.root')
#    os.system('rfcp ' + tmppath + 'Merge_'+str(sys.argv[2])+'tot.root ' + path + '/Merge_tot.root ' )
    print 'It\'s Over' 

            


            


