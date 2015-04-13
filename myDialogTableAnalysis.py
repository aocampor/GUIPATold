from Tkinter import *
from tkSimpleDialog import askfloat

module8 = __import__('KeyBoardForDetectorNew')
module9 = __import__('HVScanFrame')
module10 = __import__('CurrentMonitoringFrame')

demos4 = {
    'Analysis Frame': lambda: module8.Demo(),
    'HV or Threshold scan Frame': lambda: module9.Demo(),
    'Current Monitoring Frame': lambda: module10.Demo()
}

