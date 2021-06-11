# -*- coding: utf-8 -*-
"""
Created on Thu Jun 10 11:27:24 2021

@author: james
"""

# runs teetime getter
# set to specific time using task scheduler

# imprt module
from bookings.funcs import TeeTime
import os
from config import *

# timeit
from time import time


# set working directory
os.chdir(TEETIME_DIRECTORY) # may not be necessary

# establish class
a = TeeTime()

# runit
a.signin()

starttime = time()

a.choose_tee_time()

endtime = time()

a.add_others()

a.submit()

print('it took {} seconds to execute the script'.format(endtime - starttime))