#! /usr/bin/env python

import commands
import sys, os, string, fileinput

#
#main
#
if __name__=="__main__":

    release = str(sys.argv[1])
    ds = str(sys.argv[2]).replace('/','')
    dataset = str(sys.argv[2])
    runnum = str(sys.argv[3])

    search = []
    place = []
    
    if int(sys.argv[4]) == 1 or int(sys.argv[5]) == 1 or int(sys.argv[6]) == 1 or int(sys.argv[10]) == 1: place.append("root")
    if int(sys.argv[7]) == 1 or int(sys.argv[8])== 1 or int(sys.argv[9]): place.append("noise")

    if int(sys.argv[4]) == 1: search.append("GRPC")
    if int(sys.argv[5]) == 1: search.append("SRPC")
    if int(sys.argv[6]) == 1: search.append("DQM")
    if int(sys.argv[7]) == 1: search.append("Noise")
    if int(sys.argv[8]) == 1: search.append("Trig")
    if int(sys.argv[9]) == 1: search.append("Strips_00")
    if int(sys.argv[9]) == 1: search.append("Strips_01")
    if int(sys.argv[9]) == 1: search.append("Strips_02")
    if int(sys.argv[9]) == 1: search.append("Strips_0m1")
    if int(sys.argv[9]) == 1: search.append("Strips_0m2")
    if int(sys.argv[9]) == 1: search.append("Strips_11")
    if int(sys.argv[9]) == 1: search.append("Strips_12")
    if int(sys.argv[9]) == 1: search.append("Strips_13")
    if int(sys.argv[9]) == 1: search.append("Strips_m11")
    if int(sys.argv[9]) == 1: search.append("Strips_m12")
    if int(sys.argv[9]) == 1: search.append("Strips_m13")
    if int(sys.argv[10]) == 1: search.append("Trigger_eff")    

    print release, dataset, runnum, sys.argv[4], sys.argv[5], sys.argv[6], sys.argv[7], sys.argv[8], sys.argv[9], sys.argv[10]
    total =[item[:-1] for item in os.popen('./aSearchCLI --dbsInst=cms_dbs_prod_global --limit=-1 --input \"find file where dataset like ' + dataset + ' and run = ' + runnum + '\" | grep -v root | awk \'{print $2}\'')]
    print total[1]

    for ei in place:

        directory = '/castor/cern.ch/cms/store/caf/user/ccmuon/RPC/GlobalRuns/' + ds + '/' + runnum + '/' + ei + '/'
    
        for el in search:
            if ((el == "GRPC" or el == "SRPC" or el == "DQM" or el == "Trigger_eff" ) and ei == "noise") or ((el == "Noise" or el == "Trig" or el == "Strip_00" or el == "Strip_01" or el == "Strip_02" or el == "Strip_0m1" or el == "Strip_0m2" or el == "Strip_11" or el == "Strip_12" or el == "Strip_13" or el == "Strip_m11" or el == "Strip_m12" or el == "Strip_m13" ) and ei == "root"): continue
            
            missing = 0.

            ausent = []
            for i in range(int(total[1])):
                file =[item[:-1] for item in os.popen('rfdir ' + directory + ' | grep \"_' + str(i) + '.root\" ' + '| awk \'{print $9}\' | grep \"' + el + '\"' )]
                if (file == []):
                    missing = missing + 1
                    ausent.append(i)

            print "For: " + str(el)
            print "Missing numbers are:", ausent
            print 'Succesful ' + str((float(total[1])-missing)/float(total[1])*100.) + ' %'
            print "Failed " + str(missing/float(total[1])*100.) +' %'

            if el == "GRPC":
                for item in ausent:
                    os.system('./RunJobForAGivenRunNumberNew.py '+ release + ' ' + dataset + ' ' + runnum  + ' 1 ' + str(item) +' 1 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 &')

            if el == "SRPC":
                for item in ausent:
                    os.system('./RunJobForAGivenRunNumberNew.py '+ release + ' ' + dataset + ' ' + runnum  + ' 1 ' + str(item) +' 0 1 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 &')

            if el == "DQM":
                for item in ausent:
                    os.system('./RunJobForAGivenRunNumberNew.py '+ release + ' ' + dataset + ' ' + runnum  + ' 1 ' + str(item) +' 0 0 1 0 0 0 0 0 0 0 0 0 0 0 0 0 0 &')
                    
            if el == "Noise":
                for item in ausent:
                    os.system('./RunJobForAGivenRunNumberNew.py '+ release + ' ' + dataset + ' ' + runnum  + ' 1 ' + str(item) +' 0 0 0 1 0 0 0 0 0 0 0 0 0 0 0 0 0 &')

            if el == "Trig":
                for item in ausent:
                    os.system('./RunJobForAGivenRunNumberNew.py '+ release + ' ' + dataset + ' ' + runnum  + ' 1 ' + str(item) +' 0 0 0 0 1 0 0 0 0 0 0 0 0 0 0 0 0 &')
                    

            if el == "Strips_m11":
                for item in ausent:
                    os.system('./RunJobForAGivenRunNumberNew.py '+ release + ' ' + dataset + ' ' + runnum  + ' 1 ' + str(item) +' 0 0 0 0 0 1 0 0 0 0 0 0 0 0 0 0 0 &')


            if el == "Strips_m12":
                for item in ausent:
                    os.system('./RunJobForAGivenRunNumberNew.py '+ release + ' ' + dataset + ' ' + runnum  + ' 1 ' + str(item) +' 0 0 0 0 0 0 0 1 0 0 0 0 0 0 0 0 0 &')


            if el == "Strips_m13":
                for item in ausent:
                    os.system('./RunJobForAGivenRunNumberNew.py '+ release + ' ' + dataset + ' ' + runnum  + ' 1 ' + str(item) +' 0 0 0 0 0 0 0 0 1 0 0 0 0 0 0 0 0 &')                                        

            if el == "Strips_11":
                for item in ausent:
                    os.system('./RunJobForAGivenRunNumberNew.py '+ release + ' ' + dataset + ' ' + runnum  + ' 1 ' + str(item) +' 0 0 0 0 0 0 0 0 0 1 0 0 0 0 0 0 0 &')                    

            if el == "Strips_12":
                for item in ausent:
                    os.system('./RunJobForAGivenRunNumberNew.py '+ release + ' ' + dataset + ' ' + runnum  + ' 1 ' + str(item) +' 0 0 0 0 0 0 0 0 0 0 1 0 0 0 0 0 0 &')

            if el == "Strips_13":
                for item in ausent:
                    os.system('./RunJobForAGivenRunNumberNew.py '+ release + ' ' + dataset + ' ' + runnum  + ' 1 ' + str(item) +' 0 0 0 0 0 0 0 0 0 0 0 1 0 0 0 0 0 &')

            if el == "Strips_01":
                for item in ausent:
                    os.system('./RunJobForAGivenRunNumberNew.py '+ release + ' ' + dataset + ' ' + runnum  + ' 1 ' + str(item) +' 0 0 0 0 0 0 0 0 0 0 0 0 1 0 0 0 0 &')                                        

            if el == "Strips_02":
                for item in ausent:
                    os.system('./RunJobForAGivenRunNumberNew.py '+ release + ' ' + dataset + ' ' + runnum  + ' 1 ' + str(item) +' 0 0 0 0 0 0 0 0 0 0 0 0 0 1 0 0 0 &')

            if el == "Strips_00":
                for item in ausent:
                    os.system('./RunJobForAGivenRunNumberNew.py '+ release + ' ' + dataset + ' ' + runnum  + ' 1 ' + str(item) +' 0 0 0 0 0 0 0 0 0 0 0 0 0 0 1 0 0 &')                    

            if el == "Strips_0m1":
                for item in ausent:
                    os.system('./RunJobForAGivenRunNumberNew.py '+ release + ' ' + dataset + ' ' + runnum  + ' 1 ' + str(item) +' 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 1 0 &')

            if el == "Strips_0m2":
                for item in ausent:
                    os.system('./RunJobForAGivenRunNumberNew.py '+ release + ' ' + dataset + ' ' + runnum  + ' 1 ' + str(item) +' 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 1 &')                                        
                    
            if el == "Trigger_eff":
                for item in ausent:
                    os.system('./RunJobForAGivenRunNumberNew.py '+ release + ' ' + dataset + ' ' + runnum  + ' 1 ' + str(item) +' 0 0 0 0 0 0 1 0 0 0 0 0 0 0 0 0 0 &')
