#! /usr/bin/env python
from Tkinter import *
import commands
import sys, os, string, fileinput
from sys import argv
from ROOT import *

if __name__ == '__main__':

    RootFile=sys.argv[1]
    wheel = sys.argv[2]
    layers = ['S01','S02','S03','S04','S05','S06']
    item = 'out1'
#    for item in layers:
#        print str(item)
    os.system('./plot_producer_end.py ' + str(RootFile) + ' ' + str(wheel) + ' ' + str(item))
#    os.system('hadd ' + str(RootFile) + '_out1.root ' + str(RootFile) + '_S0*.root')
 #   os.system('rm ' + str(RootFile) + '_S0*.root')
