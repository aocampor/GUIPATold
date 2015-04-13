#! /usr/bin/env python
from Tkinter import *
import commands
import sys, os, string, fileinput
from sys import argv
from ROOT import *

if __name__ == '__main__':

    RootFile=sys.argv[1]
    wheel = sys.argv[2]
    layers = ['RB1in','RB1out','RB2in','RB2out','RB3','RB3+','RB3-','RB4','RB4+','RB4-','RB4++','RB4+-','RB4--','RB4-+']
    for item in layers:
#        print str(item)
        os.system('./plot_producer.py ' + str(RootFile) + ' ' + str(wheel) + ' ' + str(item))
    os.system('hadd ' + str(RootFile) + '_media.root ' + str(RootFile) + '_RB*.root')
    os.system('rm ' + str(RootFile) + '_RB*.root')
