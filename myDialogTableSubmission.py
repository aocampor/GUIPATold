from Tkinter import *
from tkSimpleDialog import askfloat

module4 = __import__('SubmissionFrame')
module10 = __import__('SubmissionFrameForMissingJobs')

demos2 = {
    'Submission Frame':  lambda: module4.Demo(),
    'Submission Frame for missing jobs': lambda: module10.Demo()
}

