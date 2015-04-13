#!/usr/bin/env python

import os,sys, DLFCN, time, math


sys.setdlopenflags(DLFCN.RTLD_GLOBAL+DLFCN.RTLD_LAZY)

from pluginCondDBPyInterface import *
from CondCore.Utilities import iovInspector as inspect

class CurrentMonitoring:
    def __init__(self,startTime,endTime):
        start = time.time()
        a = FWIncantation()
        rdbms = RDBMS("/afs/cern.ch/cms/DB/conddb/prep/")
        dbName =  "oracle://cms_orcoff_prep/CMS_COND_30X_RPC"

        self.db = rdbms.getDB(dbName)

        self.detMapName = {}
        self.detMap = {}
        self.detMapResults = {}

        self.detMapNameTemp = {}
        self.detMapTemp = {}
        self.detMapResultsTemp = {}
        
####--------------------------------- Correnti -----------------------------------------------------------

        self.createResultsMap('Imon_test1','current',0,startTime,endTime)

###--------------------------------- Temperature ---------------------------------------------------------
        
        self.createResultsMap('Temp_test1','temp',4,startTime,endTime)


    def createResultsMap(self,tag,valuetype,subtype,startTime,endTime):

        try:
            if valuetype == 'current': threshold = 1.
            elif valuetype == 'temp': threshold = 3.

            tagPVSS = 'Test_70195_map'
            
            detMapName = {}
            iov = inspect.Iov(self.db,tagPVSS)
            iovlist=iov.list()
            for p in iovlist:
                payload=inspect.PayLoad(self.db,p[0])
                info = payload.summary().split(" ")

                for i in xrange(0,len(info),8):
                    if i+7 < len(info):
                        if int(info[i+7]) != int(subtype) and int(info[i+1]) != 0: continue
                        listForName = [info[i+1],info[i+2],info[i+3],info[i+4],info[i+5],info[i+6]]

                        detMapName[int(info[i])] = self.getDetName(listForName)

            if int(subtype) == 0:
                self.detMapName = detMapName
            elif int(subtype) == 4:
                self.detMapNameTemp = detMapName


            detMap = {}
            detMapResults = {}

            iov = inspect.Iov(self.db,tag)

            ans = {'how': valuetype,'which' : [0]}
            curr =  iov.trendinrange(ans,startTime,endTime)
            
            ans = {'how': 'detid','which' : [0]}
            detid =  iov.trendinrange(ans,startTime,endTime)

            ans = {'how': 'day','which' : [0]}
            day = iov.trendinrange(ans,startTime,endTime)
            
            ans = {'how': 'time','which' : [0]}
            t = iov.trendinrange(ans,startTime,endTime)

            counterPayLoad = 0
            for c in detid:
                counterEl = 0
                for d in c[2]:
                    if detMapName.has_key(int(d)):
                        if detMapName[int(d)].count("W") == 0: continue
                        if detMap.has_key(detMapName[int(d)]):
                            cvalue = (curr[counterPayLoad])[2][counterEl]
                            tvalue = self.getSecond( str(int((day[counterPayLoad])[2][counterEl])),str(int((t[counterPayLoad])[2][counterEl])))
                            detMap[detMapName[int(d)]][0].append(int(tvalue))
                            detMap[detMapName[int(d)]][1].append(float(cvalue))
                        else:
                            cvalue = (curr[counterPayLoad])[2][counterEl]
                            tvalue = self.getSecond( str(int((day[counterPayLoad])[2][counterEl])),str(int((t[counterPayLoad])[2][counterEl])))
                            detMap[detMapName[int(d)]] = [[int(tvalue)],[float(cvalue)]]
                            
                    counterEl += 1
                counterPayLoad += 1

            for (k,v) in detMap.items():
                average = 0
                summ = 0
                count = 0
                for s in v[1]:
                    if s > 0:
                        summ += s
                        count += 1
                if count != 0: average = summ/count
                
                sigma = 0
                highCurrent = False
        
                for c in v[1]:
                    if c > 0:
                        sigma += math.pow((average-c), 2)
                        if math.fabs(average-c) > threshold: highCurrent = True
                        if count != 0: sigma = math.sqrt(sigma/count)

                detMapResults[k] = [len(v[0]),average,sigma,highCurrent]

            if valuetype == 'current':
                self.detMap = detMap
                self.detMapResults = detMapResults
            elif valuetype == 'temp':
                self.detMapTemp = detMap
                self.detMapResultsTemp = detMapResults

        except Exception, er :
            print er

    def getMapResultsTemp(self):
        return self.detMapResultsTemp

    def getDetMapTemp(self):
        return self.detMapTemp

    def getValuesTemp(self,element):
        if self.detMapResultsTemp.has_key(element):
            return self.detMapResultsTemp[element]
        else:
            return 0

    def getMapElementTemp(self,element):
        if self.detMapTemp.has_key(element):
            return self.detMapTemp[element]
        else:
            return [0,0]

    def getMapResults(self):
        return self.detMapResults
    
    def getDetMap(self):
        return self.detMap    

    def getValues(self,element):
        if self.detMapResults.has_key(element):
            return self.detMapResults[element]
        else:
            return 0

    def getMapElement(self,element):
        if self.detMap.has_key(element):
            return self.detMap[element]
        else:
            return 0
        
    def getSecond(self,day,t):
        if len(day) == 5:
            data = time.mktime((int(day[3]+day[4]),int(day[1]+day[2]),int(day[0]),0,0,0,0,0,0))
        if len(day) == 6:
            data = time.mktime((int(day[4]+day[5]),int(day[2]+day[3]),int(day[0]+day[1]),0,0,0,0,0,0))

        sec = 0
        if len(t) < 3:
            sec = 3600 + int(t)
        elif len(t) == 3:
            sec = 3600 + int(t[0])*60 + int(t[1]+t[2])
        elif len(t) == 4:
            sec = 3600 + int(t[0]+t[1])*60 + int(t[2]+t[3])
        elif len(t) == 5:
            sec = 3600 + int(t[0])*3600+int(t[1]+t[2])*60 + int(t[3]+t[4])
        elif len(t) == 6:
            sec = 3600 + int(t[0]+t[1])*3600+int(t[2]+t[3])*60 + int(t[4]+t[5])

        return data+sec

    def getDetName(self,listForName):
        detName = ''
        if int(listForName[0]) == 0:
            detName += "W"+str(listForName[1])+"_RB"+str(listForName[3])
            if int(listForName[3]) < 3:
                if int(listForName[4]) == 1: detName += 'in'
                if int(listForName[4]) == 2: detName += 'out'
            else:
                if int(listForName[2]) != 4 and int(listForName[2]) != 9 and int(listForName[2]) != 11:
                    if int(listForName[5]) == 1: detName += '-'
                    if int(listForName[5]) == 2: detName += '+'    
                elif int(listForName[2]) == 4 and int(listForName[3]) == 4:
                    if int(listForName[5]) == 1: detName += '--'
                    if int(listForName[5]) == 2: detName += '-+'
                    if int(listForName[5]) == 3: detName += '+-'
                    if int(listForName[5]) == 4: detName += '++'
                elif int(listForName[2]) == 4 and int(listForName[3]) == 3:
                    if int(listForName[5]) == 1: detName += '-'
                    if int(listForName[5]) == 2: detName += '+'
                    
            if int(listForName[2]) < 10: detName += '_S0'+str(listForName[2])
            if int(listForName[2]) >= 10: detName += '_S'+str(listForName[2])
            
        else:
            detName = "RE"+str(listForName[1])+"_R"+str(listForName[4])+"_CH"+str(listForName[2])
        return detName


if __name__ == '__main__':

    timeStart = time.mktime((2009, 06, 9, 4, 10, 0,0,0,0))
    timeEnd = time.mktime((2009, 06, 10, 4, 10, 0,0,0,0))

    root=CurrentMonitoring(timeStart,timeEnd)

    print root.getValuesTemp("W2_RB1in_S06")
    
##    print root.getMapElement("W2_RB1in_S06")
##    print "GET AVLUES:  ",root.getValues("W2_RB1in_S06")

##    for i,j in root.getMapResults().items():
##        if i=="W2_RB1in_S06": print i,j 
