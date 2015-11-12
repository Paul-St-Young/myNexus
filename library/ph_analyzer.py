##################################################################
##  (c) Copyright 2015-  by Jaron T. Krogel                     ##
##################################################################


#====================================================================#
#  ph_analyzer.py                                                 #
#    Supports data analysis for Phonon output.  Can handle log file   #
#    and XML output.                                                 #
#                                                                    #
#  Content summary:                                                  #
#    PhAnalyzer                                                   #
#      SimulationAnalyzer class for Phonon.                           #
#      Reads log output and converts data to numeric form.           #
#      Can also read data-file.xml.  See ph_data_reader.py.       #
#                                                                    #
#====================================================================#


import os
from numpy import array,fromstring,sqrt
from generic import obj
from unit_converter import convert
from periodic_table import PeriodicTable
from simulation import SimulationAnalyzer,Simulation
from ph_input import PhInput
from ph_data_reader import read_qexml
from debug import *
import code

pt = PeriodicTable()
elements = set(pt.elements.keys())

def is_number(s):
    try:
        float(s)
        return True
    except ValueError:
        return False
#end def is_number


def ph_time(tsin):
    ts = tsin
    h,m,s='','',''
    if ts!='' and ts.find('h')!=-1:
        sp = ts.split('h')
        h = sp[0]
        ts = sp[1]
    #end if
    if ts!='' and ts.find('m')!=-1:
        sp = ts.split('m')
        m = sp[0]
        ts = sp[1]
    #end if
    if ts!='' and ts.find('s')!=-1:
        sp = ts.split('s')
        s = sp[0]
        ts = sp[1]
    #end if

    times = [h,m,s]
    time = 0.
    for n in range(3):
        t = times[n]
        if is_number(t):
            t=float(t)
        else:
            t=0
        #end if
        time += t/(60.)**n
    #end for
    
    return time
#end def ph_time


class PhAnalyzer(SimulationAnalyzer):
    def __init__(self,arg0=None,infile_name=None,outfile_name=None,pw2c_outfile_name=None,analyze=False,xml=False,warn=False):
        if isinstance(arg0,Simulation):
            sim = arg0
            path = sim.locdir
            self.infile_name = sim.infile
            self.outfile_name= sim.outfile
        elif arg0!=None:
            path = arg0
            self.infile_name = infile_name
            self.outfile_name = outfile_name
        else:
            return
        #end if
        self.path = path
        self.abspath = os.path.abspath(path)

        self.info = obj(xml=xml,warn=warn)

        self.input = PhInput(os.path.join(self.path,self.infile_name))

        if analyze:
            self.analyze()
        #end if
    #end def __init__

    
    def analyze(self):
        path = self.path
        infile_name = self.infile_name
        outfile_name = self.outfile_name

        #end if
    #end def analyze

#end class PhAnalyzer
        
