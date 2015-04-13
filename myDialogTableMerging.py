from Tkinter import *
from tkSimpleDialog import askfloat

module5 = __import__('MergeFrame_new')
module6 = __import__('MergeFrameForSeveralJobs')

demos3 = {
    'Merge Frame':  lambda: module5.Demo(),
    'Merge Frame for several runs': lambda: module6.Demo()
}

