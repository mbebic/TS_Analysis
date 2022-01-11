# -*- coding: utf-8 -*-
"""
Created on Sat Dec 18 15:39:16 2021

@author: MarijaBebic
"""

import numpy as np
import matplotlib.pyplot as plt
import logging
import pandas as pd #multidimensional data analysis
import random
import csv
import matplotlib.backends.backend_pdf as dpdf
import matplotlib.dates as mdates
import datetime as datetime


# If changing basicConfig, make sure to close the dedicated console; it will not take otherwise
logging.basicConfig(filename='timesheet.log', filemode='w', 
                    format='%(levelname)s: %(message)s',
                    level=logging.DEBUG)

# Read the input data. Use pandas dataframes to hold data 
# because they are very flexible
df1 = pd.read_csv('Clockify_Time_Report_Detailed_2021-01-01-2021-12-31.csv', # Clockify_Time_Report_Detailed_2021-01-01-2021-12-31.csv
                   usecols=(0,4,8,13),
                  names=['Project', 'Employee',  'Day', 'Duration'], header=0,
                  comment='#',
                  parse_dates=['Day']
                  # dtype = {'Project': str, 'Employee': np.str, 'Day': np.datetime64, 'Duration': float}
                  )

projects = df1['Project'].unique()
employees = df1['Employee'].unique()

p = len(projects)
e = len(employees)

print('There are '+str(len(employees))+' unique employees and '+str(len(projects))+' unique projects')

