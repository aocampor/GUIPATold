from Tkinter import *
from tkSimpleDialog import askfloat

module1 = __import__('SearchDataSet')
module2 = __import__('SearchRun')
module3 = __import__('SearchDSFromRun')
module9 = __import__('StatusFrame')

demos1 = {

    'Search Dataset': lambda: module1.Demo(),
    'Search Run': lambda: module2.Demo(),
    'Search Dataset from Run': lambda: module3.Demo(),
    'Status Frame': lambda: module9.Demo()
}

