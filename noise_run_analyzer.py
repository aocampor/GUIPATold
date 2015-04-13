#! /usr/bin/env python
from Tkinter import *
import commands
import sys, os, string, fileinput
from sys import argv
from ROOT import *

if __name__ == '__main__':

    run = sys.argv[1]
    wh = ['0m2','0m1','00','01','02']
    wh1 = ['W-2','W-1','W+0','W+1','W+2']
    en = ['m11','m12','m13','11','12','13']
    en1 = ['RE-1','RE-2','RE-3','RE+1','RE+2','RE+3']
    for item in wh:
        if ( item == '0m2'):
            fn = 'W-2'
        else:
            if( item == '0m1'):
                fn = 'W-1'
            else:
                if (item == '00'):
                    fn = 'W+0'
                else:
                    if (item == '01'):
                        fn = 'W+1'
                    else:
                        if( item == '02'):
                            fn = 'W+2'
        os.system('./wheel_noise_producer.py ' + str(run) + '_' + str(item) + '.root ' + str(fn))
        os.system('./plot_producer1.py ' + str(run) + '_' + str(item) + '.root_media.root ' + str(fn))
    for item in en:
        if ( item == 'm11'):
            fn = 'RE-1'
        else:
            if( item == 'm12'):
                fn = 'RE-2'
            else:
                if (item == 'm13'):
                    fn = 'RE-3'
                else:
                    if (item == '11'):
                        fn = 'RE+1'
                    else:
                        if( item == '12'):
                            fn = 'RE+2'
                        else:
                            if ( item == '13'):
                                fn = 'RE+3'
        #       os.system('./end_noise_producer.py ' + str(run) + '_' + str(item) + '.root ' + str(fn))
        os.system('./plot_producer_end.py ' + str(run) + '_' + str(item) + '.root ' + ' ' + str(fn) )
        os.system('./plot_producer1_end.py ' + str(run) + '_' + str(item) + '.root_media.root ' + str(fn))
    os.system('hadd ' + str(run) + '_media.root ' + str(run) + '_*.root_media.root' )
#    os.system('rm ' + str(run) + '_*.root_media.root')
    os.system('hadd ' + str(run) + '_splots.root ' +  str(run) + '_*.root_media.root_plots.root')
 #   os.system('rm ' + str(run) + '_*.root_media.root_plots.root')
    for item in wh1:
        os.system('./summary_plot_producer.py ' + str(run) + '_media.root '+ str(item))
    for item in en1:
        os.system('./summary_plot_producer_end.py ' + str(run) + '_media.root '+ str(item))        
    os.system('hadd ' + str(run) + '_summary_out.root '  + str(run) + '_media.root_*_summary_out.root' )
  #  os.system('rm ' + str(run) + '_media.root_*_summary_out.root')
    os.system('./plot_davide.py ' + str(run) + '_summary_out.root ' + str(run))
    os.system('hadd ' + str(run) + '_final.root ' + str(run) + '_summary_out.root '  + str(run) + '_summary_out.root_davide.root ' +  str(run) + '_splots.root')
#    os.system('hadd ' + str(run) + '_final.root ' + str(run) + '_media.root ' + str(run) + '_summary_out.root '  + str(run) + '_summary_out.root_davide.root ' +  str(run) + '_splots.root')
   # os.system('rm ' + str(run) + '.root_out2.root '  + str(run) + '_summary_out.root_davide.root ' +   str(run) + '_summary_out.root')
