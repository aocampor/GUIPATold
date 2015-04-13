#! /usr/bin/env python
import commands
import sys, os, string, fileinput
from ROOT import *


#
# main
#

if __name__ == "__main__":

    ds = str(sys.argv[1]).replace('/','')  
     
    path = '/castor/cern.ch/cms/store/caf/user/ccmuon/RPC/GlobalRuns/' + ds + '/' + str(sys.argv[2]) + '/root'
    path1 = '/castor/cern.ch/cms/store/caf/user/ccmuon/RPC/GlobalRuns/' + ds + '/' + str(sys.argv[2]) + '/noise'
    path2 = '/castor/cern.ch/cms/store/caf/user/ccmuon/RPC/GlobalRuns/' + ds + '/' + str(sys.argv[2]) + '/gif'
    
    cmd0 = 'whoami'
    user = [item[:-1] for item in os.popen(cmd0)]
    tmppath = '/tmp/' + user[0] + '/' + str(sys.argv[2]) + '/'

#    ver1 = [item[:-1] for item in os.popen('rfdir ' + path + '/Merge_DQM_SRPC_GRPC.root')]
    ver1 = [item[:-1] for item in os.popen('rfdir ' + path + '/Merge_DQM.root')]
    print ver1
    if (ver1 == []):
        os.system('./MergeSeveral.py ' + str(sys.argv[1]) + ' ' + str(sys.argv[2]) + ' DQM_' + ' root')

#    ver2 = [item[:-1] for item in os.popen('rfdir ' + path + '/Merge_DQM_SRPC_GRPC.root')]
    ver2 = [item[:-1] for item in os.popen('rfdir ' + path + '/Merge_SRPC.root')]
    print ver2
    if (ver2 == []):
        os.system('./MergeSeveral.py ' + str(sys.argv[1]) + ' ' + str(sys.argv[2]) + ' SRPC_' + ' root')

#    ver2bis = [item[:-1] for item in os.popen('rfdir ' + path + '/Merge_DQM_SRPC_GRPC.root')]
    ver2bis = [item[:-1] for item in os.popen('rfdir ' + path + '/Merge_GRPC.root')]
    print ver2bis
    if (ver2bis == []):
        os.system('./MergeSeveral.py ' + str(sys.argv[1]) + ' ' + str(sys.argv[2]) + ' GRPC_' + ' root')

    ver3 = [item[:-1] for item in os.popen('rfdir ' + path1 + '/Merge_Noise_tot.root')]
    print ver3
    if (ver3 == []):
        os.system('./MergeSeveral.py ' + str(sys.argv[1]) + ' ' + str(sys.argv[2]) + ' Noise_ noise ')

    ver4 = [item[:-1] for item in os.popen('rfdir ' + path1 + '/'+ str(sys.argv[2]) +'_00.root')]
    if (ver4 == []):
        os.system('./MergeSeveral.py ' + str(sys.argv[1]) + ' ' + str(sys.argv[2]) + ' Strips_00_ noise ')

    ver5 = [item[:-1] for item in os.popen('rfdir ' + path1 + '/' + str(sys.argv[2]) +'_01.root')]
    if (ver5 == []):
        os.system('./MergeSeveral.py ' + str(sys.argv[1]) + ' ' + str(sys.argv[2]) + ' Strips_01_ noise ')        

    ver6 = [item[:-1] for item in os.popen('rfdir ' + path1 + '/Merge_Trig_tot.root')]
    print ver6
    if (ver6 == []):
        os.system('./MergeSeveral.py ' + str(sys.argv[1]) + ' ' + str(sys.argv[2]) + ' Trig_ noise ' )
        
    ver7 = [item[:-1] for item in os.popen('rfdir ' + path1 + '/' + str(sys.argv[2]) +'_02.root')]
    if (ver7 == []):
        os.system('./MergeSeveral.py ' + str(sys.argv[1]) + ' ' + str(sys.argv[2]) + ' Strips_02_ noise ')

    ver8 = [item[:-1] for item in os.popen('rfdir ' + path1 + '/' + str(sys.argv[2]) +'_0m1.root')]
    if (ver8 == []):
        os.system('./MergeSeveral.py ' + str(sys.argv[1]) + ' ' + str(sys.argv[2]) + ' Strips_0m1_ noise ')

    ver9 = [item[:-1] for item in os.popen('rfdir ' + path1 + '/' + str(sys.argv[2]) +'_0m2.root')]
    if (ver9 == []):
        os.system('./MergeSeveral.py ' + str(sys.argv[1]) + ' ' + str(sys.argv[2]) + ' Strips_0m2_ noise ')

    ver10 = [item[:-1] for item in os.popen('rfdir ' + path1 + '/' + str(sys.argv[2]) +'_11.root')]
    if (ver10 == []):
        os.system('./MergeSeveral.py ' + str(sys.argv[1]) + ' ' + str(sys.argv[2]) + ' Strips_11_ noise ')

    ver11 = [item[:-1] for item in os.popen('rfdir ' + path1 + '/' + str(sys.argv[2]) +'_12.root')]
    if (ver11 == []):
        os.system('./MergeSeveral.py ' + str(sys.argv[1]) + ' ' + str(sys.argv[2]) + ' Strips_12_ noise ')

    ver12 = [item[:-1] for item in os.popen('rfdir ' + path1 + '/' + str(sys.argv[2]) +'_13.root')]
    if (ver12 == []):
        os.system('./MergeSeveral.py ' + str(sys.argv[1]) + ' ' + str(sys.argv[2]) + ' Strips_13_ noise ')
        
    ver13 = [item[:-1] for item in os.popen('rfdir ' + path1 + '/' + str(sys.argv[2]) +'_m11.root')]
    if (ver13 == []):
        os.system('./MergeSeveral.py ' + str(sys.argv[1]) + ' ' + str(sys.argv[2]) + ' Strips_m11_ noise ')

    ver14 = [item[:-1] for item in os.popen('rfdir ' + path1 + '/' + str(sys.argv[2]) +'_m12.root')]
    if (ver14 == []):
        os.system('./MergeSeveral.py ' + str(sys.argv[1]) + ' ' + str(sys.argv[2]) + ' Strips_m12_ noise ')        

    ver15 = [item[:-1] for item in os.popen('rfdir ' + path1 + '/' + str(sys.argv[2]) +'_m13.root')]
    if (ver15 == []):
        os.system('./MergeSeveral.py ' + str(sys.argv[1]) + ' ' + str(sys.argv[2]) + ' Strips_m13_ noise ')

    ver16 = [item[:-1] for item in os.popen('rfdir ' + path + '/Trigger_eff_tot.root ' )]
    if (ver16 == []):
        os.system('./MergeSeveral.py ' + str(sys.argv[1]) + ' ' + str(sys.argv[2]) + ' Trigger_eff_ root ')        
        

#    plots = [item[:-1] for item in os.popen('rfdir ' + path2 + ' | grep gif')]
 #   if (plots == []):
    os.system('./FinalMerge_v2.py ' + str(sys.argv[1]) + ' ' + str(sys.argv[2])  )
    #noise_files = [item[:-1] for item in os.popen('rfdir ' + path1 + ' | grep Strips')]
    #if (noise_files != []):
    os.system('./FinalNoiseMerge.py ' + str(sys.argv[1]) + ' ' + str(sys.argv[2]) )
    print 'End Of Merge For a Given Run Number!!!!!'
            


