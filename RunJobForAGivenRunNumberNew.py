#! /usr/bin/env python
import commands
import sys, os, string, fileinput

class ShellCommandTranslation:
    def __init__(self):
        self.data = []
        
    def rfdir_py(self,string_file):
        cmd = 'rfdir' + ' ' + string_file + ' | ' + ' awk \'{print $9}\' '
        the_files = [item[:-1] for item in os.popen(cmd)]
        return the_files    

    def rfmkdir_py(self,string_path):
        newdir = ''
        for i in range(len(string_path)):
            newdir = newdir + '/'+ string_path[i]
            
        #cmd = 'rfmkdir ' + ' -m 777  ' + newdir
        cmd = 'rfmkdir ' + newdir
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
        cmd = './aSearchCLI --dbsInst=cms_dbs_prod_global --limit=-1 --input \"find file where dataset = ' + dataset + ' and ' + 'run = ' + runNumber + ' \" | egrep \"[a-Z]\" | grep -v \"Found\" '
        the_files = [item[:-1] for item in os.popen(cmd)]
##        print the_files
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


########### Create path for Castor ###############################################

    ds = str(sys.argv[2]).replace('/','')          # search for position
    
    path1 = ['/castor/cern.ch/cms/store/caf/user/ccmuon/RPC/GlobalRuns',ds,str(sys.argv[3]),'root']
    path1_aux = '/store/caf/user/ccmuon/RPC/GlobalRuns/'+ds+'/'+str(sys.argv[3])+'/root/'
    path2 = ['/castor/cern.ch/cms/store/caf/user/ccmuon/RPC/GlobalRuns',ds,str(sys.argv[3]),'out']
    path3 = ['/castor/cern.ch/cms/store/caf/user/ccmuon/RPC/GlobalRuns',ds,str(sys.argv[3]),'noise']
    path4 = ['/castor/cern.ch/cms/store/caf/user/ccmuon/RPC/GlobalRuns',ds,str(sys.argv[3]),'gif']
    
    shellComm = ShellCommandTranslation()
    shellComm.rfmkdir_py(path1)
    shellComm.rfmkdir_py(path2)
    shellComm.rfmkdir_py(path3)             
    shellComm.rfmkdir_py(path4) 

#################################################################################    
######## CREATE DIRECTORY FOR FILE .py and .job FOR SUBMISSION ##################   

    cmd = "echo $HOME"
    homedir = [item[:-1] for item in os.popen(cmd)]
    py_finalpath = str(homedir[0]) + '/scratch0/'+ str(sys.argv[3]) + '/python'
    job_finalpath = str(homedir[0]) + '/scratch0/'+ str(sys.argv[3]) + '/job'

    try:
	os.makedirs(py_finalpath)
        os.makedirs(job_finalpath)
    except OSError:
        pass

#################################################################################
############### SEARCH ON DBS THE DATASET AND CREATION OF FILES #################    

    detString = DetectFiles()
    the_files = detString.findPath(sys.argv[2],sys.argv[3])
    end = 0
    
    if int(sys.argv[4]) == -1:
        end = 10000000
    else:
        end = int(sys.argv[4])
        
    cont = 0
    job_info = job_finalpath + '/job_info.txt'
    cmdtou = 'touch ' + job_info
    os.system(cmdtou)
    countnoise1 = 0
    countnoise2 = 0

    me = [item[:-1] for item in os.popen('whoami')]

    dqm_true = 0

    dqm_fil = [item[:-1] for item in os.popen('rfdir /castor/cern.ch/cms' + path1_aux + 'Merge_DQM.root')]
    if (dqm_fil == []):
        cmd_dqm = '/afs/cern.ch/cms/CAF/CMSCOMM/COMM_DQM/data/PromptReco/' + str(sys.argv[3])[0] + str(sys.argv[3])[1] + str(sys.argv[3])[2] + '/' + str(sys.argv[3])[3] + str(sys.argv[3])[4] + str(sys.argv[3])[5] + '/DQM_V0001_R000' + str(sys.argv[3]) + '__Cosmics__CRAFT09-PromptReco-v1__RECO.root '
        dqname = [item[:-1] for item in os.popen('ls '+ cmd_dqm)]
        if(dqname != []):
            os.system('cp '+ cmd_dqm + ' Merge_DQM.root ' )
            os.system('cmsStageOut Merge_DQM.root ' + path1_aux)
            os.system('rm Merge_DQM.root')
            dqm_true = 1
    else:
        dqm_true = 1
    for i in range(len(the_files)):
        if i >= int(sys.argv[5]):
            if cont < end :
                cont = cont + 1                                  
                filename = 'trackEff_' + str(i) + '.py'
                filename1 = 'segmentEff_' + str(i) + '.py'
                filename2 = 'DQM_' + str(i) + '.py'
                filename3 = 'Noise_' + str(i) + '.py'
                filename4 = 'Trigger_' + str(i) + '.py'
                filename5_m11 = 'Strips_m11_' + str(i) + '.py'
                filename5_m12 = 'Strips_m12_' + str(i) + '.py'
                filename5_m13 = 'Strips_m13_' + str(i) + '.py'
                filename5_11 = 'Strips_11_' + str(i) + '.py'
                filename5_12 = 'Strips_12_' + str(i) + '.py'
                filename5_13 = 'Strips_13_' + str(i) + '.py'
                filename5_01 = 'Strips_01_' + str(i) + '.py'
                filename5_02 = 'Strips_02_' + str(i) + '.py'
                filename5_00 = 'Strips_00_' + str(i) + '.py'
                filename5_0m1 = 'Strips_0m1_' + str(i) + '.py'
                filename5_0m2 = 'Strips_0m2_' + str(i) + '.py'
                filename6 = 'Trigger_eff_' + str(i) + '.py'
                
                py_nameout = py_finalpath + '/' + filename
                py_nameout1 = py_finalpath + '/' + filename1
                py_nameout2 = py_finalpath + '/' + filename2
                py_nameout3 = py_finalpath + '/' + filename3
                py_nameout4 = py_finalpath + '/' + filename4
                py_nameout5_m11 = py_finalpath + '/' + filename5_m11
                py_nameout5_m12 = py_finalpath + '/' + filename5_m12
                py_nameout5_m13 = py_finalpath + '/' + filename5_m13
                py_nameout5_11 = py_finalpath + '/' + filename5_11
                py_nameout5_12 = py_finalpath + '/' + filename5_12
                py_nameout5_13 = py_finalpath + '/' + filename5_13
                py_nameout5_01 = py_finalpath + '/' + filename5_01
                py_nameout5_02 = py_finalpath + '/' + filename5_02
                py_nameout5_00 = py_finalpath + '/' + filename5_00
                py_nameout5_0m1 = py_finalpath + '/' + filename5_0m1
                py_nameout5_0m2 = py_finalpath + '/' + filename5_0m2
                py_nameout6 = py_finalpath + '/' + filename6
                
                                                                                                                                                
                
                job_nameout = job_finalpath + '/' + filename + '.job'
                job_nameout1 = job_finalpath + '/' + filename1 + '.job'
                job_nameout2 = job_finalpath + '/' + filename2 + '.job'
                job_nameout3 = job_finalpath + '/' + filename3 + '.job'
                job_nameout4 = job_finalpath + '/' + filename4 + '.job'
                job_nameout5_m11 = job_finalpath + '/' + filename5_m11 + '.job'
                job_nameout5_m12 = job_finalpath + '/' + filename5_m12 + '.job'
                job_nameout5_m13 = job_finalpath + '/' + filename5_m13 + '.job'
                job_nameout5_11 = job_finalpath + '/' + filename5_11 + '.job'
                job_nameout5_12 = job_finalpath + '/' + filename5_12 + '.job'
                job_nameout5_13 = job_finalpath + '/' + filename5_13 + '.job'
                job_nameout5_01 = job_finalpath + '/' + filename5_01 + '.job'
                job_nameout5_02 = job_finalpath + '/' + filename5_02 + '.job'
                job_nameout5_00 = job_finalpath + '/' + filename5_00 + '.job'
                job_nameout5_0m1 = job_finalpath + '/' + filename5_0m1 + '.job'
                job_nameout5_0m2 = job_finalpath + '/' + filename5_0m2 + '.job'
                job_nameout6 = job_finalpath + '/' + filename6 + '.job'
                                                                                                                                                                                
                
                job_cerr = job_finalpath + '/' + filename + '.cerr'
                job_cerr1 = job_finalpath + '/' + filename1 + '.cerr'
                job_cerr2 = job_finalpath + '/' + filename2 + '.cerr'
                job_cerr3 = job_finalpath + '/' + filename3 + '.cerr'
                job_cerr4 = job_finalpath + '/' + filename4 + '.cerr'
                job_cerr5_m11 = job_finalpath + '/' + filename5_m11 + '.cerr'
                job_cerr5_m12 = job_finalpath + '/' + filename5_m12 + '.cerr'
                job_cerr5_m13 = job_finalpath + '/' + filename5_m13 + '.cerr'
                job_cerr5_11 = job_finalpath + '/' + filename5_11 + '.cerr'
                job_cerr5_12 = job_finalpath + '/' + filename5_12 + '.cerr'
                job_cerr5_13 = job_finalpath + '/' + filename5_13 + '.cerr'
                job_cerr5_01 = job_finalpath + '/' + filename5_01 + '.cerr'
                job_cerr5_02 = job_finalpath + '/' + filename5_02 + '.cerr'
                job_cerr5_00 = job_finalpath + '/' + filename5_00 + '.cerr'
                job_cerr5_0m1 = job_finalpath + '/' + filename5_0m1 + '.cerr'
                job_cerr5_0m2 = job_finalpath + '/' + filename5_0m2 + '.cerr'
                job_cerr6 = job_finalpath + '/' + filename6 + '.cerr'
                
                
                job_cout = job_finalpath + '/' + filename + '.cout'
                job_cout1 = job_finalpath + '/' + filename1 + '.cout'
                job_cout2 = job_finalpath + '/' + filename2 + '.cout'
                job_cout3 = job_finalpath + '/' + filename3 + '.cout'
                job_cout4 = job_finalpath + '/' + filename4 + '.cout'
                job_cout5_m11 = job_finalpath + '/' + filename5_m11 + '.cout'
                job_cout5_m12 = job_finalpath + '/' + filename5_m12 + '.cout'
                job_cout5_m13 = job_finalpath + '/' + filename5_m13 + '.cout'
                job_cout5_11 = job_finalpath + '/' + filename5_11 + '.cout'
                job_cout5_12 = job_finalpath + '/' + filename5_12 + '.cout'
                job_cout5_13 = job_finalpath + '/' + filename5_13 + '.cout'
                job_cout5_01 = job_finalpath + '/' + filename5_01 + '.cout'
                job_cout5_02 = job_finalpath + '/' + filename5_02 + '.cout'
                job_cout5_00 = job_finalpath + '/' + filename5_00 + '.cout'
                job_cout5_0m1 = job_finalpath + '/' + filename5_0m1 + '.cout'
                job_cout5_0m2 = job_finalpath + '/' + filename5_0m2 + '.cout'
                job_cout6 = job_finalpath + '/' + filename6 + '.cout'
                
                strreplace1 = 'GRPC_'+str(i)+'.root'
                strreplace3 = 'SRPC_'+str(i)+'.root'
                strreplace4 = 'DQM_'+str(i)+'.root'
                strreplace5 = 'Noise_'+str(i)+'.root'
                strreplace7 = 'Trig_'+str(i)+'.root'
                strreplace8_m11 = 'Strips_m11_'+str(i)+'.root'
                strreplace8_m12 = 'Strips_m12_'+str(i)+'.root'
                strreplace8_m13 = 'Strips_m13_'+str(i)+'.root'
                strreplace8_11 = 'Strips_11_'+str(i)+'.root'
                strreplace8_12 = 'Strips_12_'+str(i)+'.root'
                strreplace8_13 = 'Strips_13_'+str(i)+'.root'
                strreplace8_01 = 'Strips_01_'+str(i)+'.root'
                strreplace8_02 = 'Strips_02_'+str(i)+'.root'
                strreplace8_00 = 'Strips_00_'+str(i)+'.root'
                strreplace8_0m1 = 'Strips_0m1_'+str(i)+'.root'
                strreplace8_0m2 = 'Strips_0m2_'+str(i)+'.root'
                strreplace9 = 'Trigger_eff_'+str(i)+'.root'
                

                lista3 = ["----input_file----",the_files[i],"----output_file----",strreplace5]
                listaj3 = ["----input_file----",filename3,"----output_file----",strreplace5,"----RUN-NUMBER----",
                               sys.argv[3],"----DATASET----",ds,"----RELEASE----",sys.argv[1]]
                lista = ["----input_file----",the_files[i],"---GRPC---",strreplace1]
                lista1 = ["----input_file----",the_files[i],"----SRPC----",strreplace3]
                lista2 = ["----input_file----",the_files[i],"----output_file----",strreplace4]
                listaj = ["----input_file----",filename,"----output_file1----",strreplace1,
                          "----RUN-NUMBER----",sys.argv[3],"----DATASET----",ds,"----RELEASE----",sys.argv[1]]
                listaj1 = ["----input_file----",filename1,"----output_file----",strreplace3,"----RUN-NUMBER----",
                           sys.argv[3],"----DATASET----",ds,"----RELEASE----",sys.argv[1]]
                listaj2 = ["----input_file----",filename2,"----output_file----",strreplace4,"----RUN-NUMBER----",
                           sys.argv[3],"----DATASET----",ds,"----RELEASE----",sys.argv[1]]
                listaj4 = ["----input_file----",filename4,"----output_file----",strreplace7,"----RUN-NUMBER----",
                           sys.argv[3],"----DATASET----",ds,"----RELEASE----",sys.argv[1]]
                lista4 = ["----input_file----",the_files[i],"----Trig----",strreplace7]
                listaj5_m11 = ["----input_file----",filename5_m11,"----output_file----",strreplace8_m11,"----RUN-NUMBER----",
                               sys.argv[3],"----DATASET----",ds,"----RELEASE----",sys.argv[1]]
                lista5_m11 = ["----input_file----",the_files[i],"----strip----",strreplace8_m11,"---wheel---",'1',"---region---",'-1']
                listaj5_m12 = ["----input_file----",filename5_m12,"----output_file----",strreplace8_m12,"----RUN-NUMBER----",
                               sys.argv[3],"----DATASET----",ds,"----RELEASE----",sys.argv[1]]
                lista5_m12 = ["----input_file----",the_files[i],"----strip----",strreplace8_m12,"---wheel---",'2',"---region---",'-1']
                listaj5_m13 = ["----input_file----",filename5_m13,"----output_file----",strreplace8_m13,"----RUN-NUMBER----",
                               sys.argv[3],"----DATASET----",ds,"----RELEASE----",sys.argv[1]]
                lista5_m13 = ["----input_file----",the_files[i],"----strip----",strreplace8_m13,"---wheel---",'3',"---region---",'-1']
                listaj5_11 = ["----input_file----",filename5_11,"----output_file----",strreplace8_11,"----RUN-NUMBER----",
                              sys.argv[3],"----DATASET----",ds,"----RELEASE----",sys.argv[1]]
                lista5_11 = ["----input_file----",the_files[i],"----strip----",strreplace8_11,"---wheel---",'1',"---region---",'1']
                listaj5_12 = ["----input_file----",filename5_12,"----output_file----",strreplace8_12,"----RUN-NUMBER----",
                              sys.argv[3],"----DATASET----",ds,"----RELEASE----",sys.argv[1]]
                lista5_12 = ["----input_file----",the_files[i],"----strip----",strreplace8_12,"---wheel---",'2',"---region---",'1']
                listaj5_13 = ["----input_file----",filename5_13,"----output_file----",strreplace8_13,"----RUN-NUMBER----",
                              sys.argv[3],"----DATASET----",ds,"----RELEASE----",sys.argv[1]]
                lista5_13 = ["----input_file----",the_files[i],"----strip----",strreplace8_13,"---wheel---",'3',"---region---",'1']
                listaj5_01 = ["----input_file----",filename5_01,"----output_file----",strreplace8_01,"----RUN-NUMBER----",
                              sys.argv[3],"----DATASET----",ds,"----RELEASE----",sys.argv[1]]
                lista5_01 = ["----input_file----",the_files[i],"----strip----",strreplace8_01,"---wheel---",'1',"---region---",'0']
                listaj5_02 = ["----input_file----",filename5_02,"----output_file----",strreplace8_02,"----RUN-NUMBER----",
                              sys.argv[3],"----DATASET----",ds,"----RELEASE----",sys.argv[1]]
                lista5_02 = ["----input_file----",the_files[i],"----strip----",strreplace8_02,"---wheel---",'2',"---region---",'0']
                listaj5_00 = ["----input_file----",filename5_00,"----output_file----",strreplace8_00,"----RUN-NUMBER----",
                              sys.argv[3],"----DATASET----",ds,"----RELEASE----",sys.argv[1]]
                lista5_00 = ["----input_file----",the_files[i],"----strip----",strreplace8_00,"---wheel---",'0',"---region---",'0']
                listaj5_0m1 = ["----input_file----",filename5_0m1,"----output_file----",strreplace8_0m1,"----RUN-NUMBER----",
                               sys.argv[3],"----DATASET----",ds,"----RELEASE----",sys.argv[1]]
                lista5_0m1 = ["----input_file----",the_files[i],"----strip----",strreplace8_0m1,"---wheel---",'-1',"---region---",'0']
                listaj5_0m2 = ["----input_file----",filename5_0m2,"----output_file----",strreplace8_0m2,"----RUN-NUMBER----",
                               sys.argv[3],"----DATASET----",ds,"----RELEASE----",sys.argv[1]]
                lista5_0m2 = ["----input_file----",the_files[i],"----strip----",strreplace8_0m2,"---wheel---",'-2',"---region---",'0']
                lista6 = ["----input_file----",the_files[i],"----output----",strreplace9]
                listaj6 = ["----input_file----",filename6,"----output_file----",strreplace9,"----RUN-NUMBER----",
                           sys.argv[3],"----DATASET----",ds,"----RELEASE----",sys.argv[1]]
                                
                if int(sys.argv[6]) == 1: detString.replaceStringInFile("TrackEff.py",py_nameout,lista)
                if int(sys.argv[6]) == 1: detString.replaceStringInFile("jobtemplate0",job_nameout,listaj)
                if int(sys.argv[7]) == 1: detString.replaceStringInFile("segment.py",py_nameout1,lista1)
                if int(sys.argv[7]) == 1: detString.replaceStringInFile("jobtemplate1",job_nameout1,listaj1)
                if int(sys.argv[8]) == 1: detString.replaceStringInFile("dqm_digi.py",py_nameout2,lista2)
                if int(sys.argv[8]) == 1: detString.replaceStringInFile("jobtemplate2",job_nameout2,listaj2)
                if int(sys.argv[9]) == 1: detString.replaceStringInFile("noisebas.py",py_nameout3,lista3)
                if int(sys.argv[9]) == 1: detString.replaceStringInFile("jobtemplate3",job_nameout3,listaj3)            
                if int(sys.argv[10]) == 1: detString.replaceStringInFile("trig.py",py_nameout4,lista4)
                if int(sys.argv[10]) == 1: detString.replaceStringInFile("jobtemplate4",job_nameout4,listaj4)
                if int(sys.argv[11]) == 1: detString.replaceStringInFile("strip.py",py_nameout5_m11,lista5_m11)
                if int(sys.argv[11]) == 1: detString.replaceStringInFile("jobtemplate5",job_nameout5_m11,listaj5_m11)
                if int(sys.argv[13]) == 1: detString.replaceStringInFile("strip.py",py_nameout5_m12,lista5_m12)
                if int(sys.argv[13]) == 1: detString.replaceStringInFile("jobtemplate5",job_nameout5_m12,listaj5_m12)
                if int(sys.argv[14]) == 1: detString.replaceStringInFile("strip.py",py_nameout5_m13,lista5_m13)
                if int(sys.argv[14]) == 1: detString.replaceStringInFile("jobtemplate5",job_nameout5_m13,listaj5_m13)
                if int(sys.argv[15]) == 1: detString.replaceStringInFile("strip.py",py_nameout5_11,lista5_11)
                if int(sys.argv[15]) == 1: detString.replaceStringInFile("jobtemplate5",job_nameout5_11,listaj5_11)
                if int(sys.argv[16]) == 1: detString.replaceStringInFile("strip.py",py_nameout5_12,lista5_12)
                if int(sys.argv[16]) == 1: detString.replaceStringInFile("jobtemplate5",job_nameout5_12,listaj5_12)
                if int(sys.argv[17]) == 1: detString.replaceStringInFile("strip.py",py_nameout5_13,lista5_13)
                if int(sys.argv[17]) == 1: detString.replaceStringInFile("jobtemplate5",job_nameout5_13,listaj5_13)
                if int(sys.argv[18]) == 1: detString.replaceStringInFile("strip.py",py_nameout5_01,lista5_01)
                if int(sys.argv[18]) == 1: detString.replaceStringInFile("jobtemplate5",job_nameout5_01,listaj5_01)
                if int(sys.argv[19]) == 1: detString.replaceStringInFile("strip.py",py_nameout5_02,lista5_02)
                if int(sys.argv[19]) == 1: detString.replaceStringInFile("jobtemplate5",job_nameout5_02,listaj5_02)
                if int(sys.argv[20]) == 1: detString.replaceStringInFile("strip.py",py_nameout5_00,lista5_00)
                if int(sys.argv[20]) == 1: detString.replaceStringInFile("jobtemplate5",job_nameout5_00,listaj5_00)
                if int(sys.argv[21]) == 1: detString.replaceStringInFile("strip.py",py_nameout5_0m1,lista5_0m1)
                if int(sys.argv[21]) == 1: detString.replaceStringInFile("jobtemplate5",job_nameout5_0m1,listaj5_0m1)
                if int(sys.argv[22]) == 1: detString.replaceStringInFile("strip.py",py_nameout5_0m2,lista5_0m2)
                if int(sys.argv[22]) == 1: detString.replaceStringInFile("jobtemplate5",job_nameout5_0m2,listaj5_0m2)
                if int(sys.argv[12]) == 1: detString.replaceStringInFile("triggereff.py",py_nameout6,lista6)
                if int(sys.argv[12]) == 1: detString.replaceStringInFile("jobtemplate6",job_nameout6,listaj6)
                
                
                cmdchmode = 'chmod a+x ' + job_nameout
                cmdchmode1 = 'chmod a+x ' + job_nameout1
                cmdchmode2 = 'chmod a+x ' + job_nameout2
                cmdchmode3 = 'chmod a+x ' + job_nameout3
                cmdchmode4 = 'chmod a+x ' + job_nameout4
                cmdchmode5_m11 = 'chmod a+x ' + job_nameout5_m11
                cmdchmode5_m12 = 'chmod a+x ' + job_nameout5_m12
                cmdchmode5_m13 = 'chmod a+x ' + job_nameout5_m13
                cmdchmode5_11 = 'chmod a+x ' + job_nameout5_11
                cmdchmode5_12 = 'chmod a+x ' + job_nameout5_12
                cmdchmode5_13 = 'chmod a+x ' + job_nameout5_13
                cmdchmode5_01 = 'chmod a+x ' + job_nameout5_01
                cmdchmode5_02 = 'chmod a+x ' + job_nameout5_02
                cmdchmode5_00 = 'chmod a+x ' + job_nameout5_00
                cmdchmode5_0m1 = 'chmod a+x ' + job_nameout5_0m1
                cmdchmode5_0m2 = 'chmod a+x ' + job_nameout5_0m2
                cmdchmode6 = 'chmod a+x ' + job_nameout6
                                
                
                if int(sys.argv[6]) == 1: os.system(cmdchmode)
                if int(sys.argv[7]) == 1: os.system(cmdchmode1)
                if int(sys.argv[8]) == 1: os.system(cmdchmode2)
                if int(sys.argv[9]) == 1: os.system(cmdchmode3)
                if int(sys.argv[10]) == 1: os.system(cmdchmode4)
                if int(sys.argv[11]) == 1: os.system(cmdchmode5_m11)
                if int(sys.argv[13]) == 1: os.system(cmdchmode5_m12)
                if int(sys.argv[14]) == 1: os.system(cmdchmode5_m13)
                if int(sys.argv[15]) == 1: os.system(cmdchmode5_11)
                if int(sys.argv[16]) == 1: os.system(cmdchmode5_12)
                if int(sys.argv[17]) == 1: os.system(cmdchmode5_13)
                if int(sys.argv[18]) == 1: os.system(cmdchmode5_00)
                if int(sys.argv[19]) == 1: os.system(cmdchmode5_01)
                if int(sys.argv[20]) == 1: os.system(cmdchmode5_02)
                if int(sys.argv[21]) == 1: os.system(cmdchmode5_0m1)
                if int(sys.argv[22]) == 1: os.system(cmdchmode5_0m2)
                if int(sys.argv[12]) == 1: os.system(cmdchmode6)
                
                cmdsub = 'bsub -q cmscaf1nd' + ' -e ' + job_cerr + ' -o ' + job_cout + ' ' + job_nameout
                cmdsub1 = 'bsub -q cmscaf1nh' + ' -e ' + job_cerr1 + ' -o ' + job_cout1 + ' ' + job_nameout1
                cmdsub2 = 'bsub -q cmscaf1nh' + ' -e ' + job_cerr2 + ' -o ' + job_cout2 + ' ' + job_nameout2
                cmdsub3 = 'bsub -q cmscaf1nh' + ' -e ' + job_cerr3 + ' -o ' + job_cout3 + ' ' + job_nameout3
                cmdsub4 = 'bsub -q cmscaf1nh' + ' -e ' + job_cerr4 + ' -o ' + job_cout4 + ' ' + job_nameout4
                cmdsub5_m11 = 'bsub -q cmscaf1nh' + ' -e ' + job_cerr5_m11 + ' -o ' + job_cout5_m11 + ' ' + job_nameout5_m11
                cmdsub5_m12 = 'bsub -q cmscaf1nh' + ' -e ' + job_cerr5_m12 + ' -o ' + job_cout5_m12 + ' ' + job_nameout5_m12
                cmdsub5_m13 = 'bsub -q cmscaf1nh' + ' -e ' + job_cerr5_m13 + ' -o ' + job_cout5_m13 + ' ' + job_nameout5_m13
                cmdsub5_11 = 'bsub -q cmscaf1nh' + ' -e ' + job_cerr5_11 + ' -o ' + job_cout5_11 + ' ' + job_nameout5_11
                cmdsub5_12 = 'bsub -q cmscaf1nh' + ' -e ' + job_cerr5_12 + ' -o ' + job_cout5_12 + ' ' + job_nameout5_12
                cmdsub5_13 = 'bsub -q cmscaf1nh' + ' -e ' + job_cerr5_13 + ' -o ' + job_cout5_13 + ' ' + job_nameout5_13
                cmdsub5_01 = 'bsub -q cmscaf1nh' + ' -e ' + job_cerr5_01 + ' -o ' + job_cout5_01 + ' ' + job_nameout5_01
                cmdsub5_02 = 'bsub -q cmscaf1nh' + ' -e ' + job_cerr5_02 + ' -o ' + job_cout5_02 + ' ' + job_nameout5_02
                cmdsub5_00 = 'bsub -q cmscaf1nh' + ' -e ' + job_cerr5_00 + ' -o ' + job_cout5_00 + ' ' + job_nameout5_00
                cmdsub5_0m1 = 'bsub -q cmscaf1nh' + ' -e ' + job_cerr5_0m1 + ' -o ' + job_cout5_0m1 + ' ' + job_nameout5_0m1
                cmdsub5_0m2 = 'bsub -q cmscaf1nh' + ' -e ' + job_cerr5_0m2 + ' -o ' + job_cout5_0m2 + ' ' + job_nameout5_0m2
                cmdsub6 = 'bsub -q cmscaf1nd' + ' -e ' + job_cerr6 + ' -o ' + job_cout6 + ' ' + job_nameout6


                if int(sys.argv[6]) == 1: os.system(cmdsub)
                if int(sys.argv[7]) == 1: os.system(cmdsub1)
                if(dqm_true == 0):
                    if int(sys.argv[8]) == 1: os.system(cmdsub2)
                if int(sys.argv[9]) == 1: os.system(cmdsub3)
                if int(sys.argv[10]) == 1: os.system(cmdsub4)
                if int(sys.argv[11]) == 1: os.system(cmdsub5_m11)
                if int(sys.argv[13]) == 1: os.system(cmdsub5_m12)
                if int(sys.argv[14]) == 1: os.system(cmdsub5_m13)
                if int(sys.argv[15]) == 1: os.system(cmdsub5_11)
                if int(sys.argv[16]) == 1: os.system(cmdsub5_12)
                if int(sys.argv[17]) == 1: os.system(cmdsub5_13)
                if int(sys.argv[18]) == 1: os.system(cmdsub5_01)
                if int(sys.argv[19]) == 1: os.system(cmdsub5_02)
                if int(sys.argv[20]) == 1: os.system(cmdsub5_00)
                if int(sys.argv[21]) == 1: os.system(cmdsub5_0m1)
                if int(sys.argv[22]) == 1: os.system(cmdsub5_0m2)
                if int(sys.argv[12]) == 1: os.system(cmdsub6)
                
                                                                                                                                                                                
        
    cmdcat = 'cat ' + job_info
    os.system(cmdcat)
   

            

            


