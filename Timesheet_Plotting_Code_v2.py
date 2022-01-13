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
import os


# this function allows us to use matplotlib library of datetime. This is able to 
# create actual formatted dates instead of integers, which is more realistic to 
# everyday life, where employees clock in on calendar days, not integer days

def projects_by_employee_daterange(pltPdf1, df1a, axis_title=None, plot_size=(6.5,4.8)):
    fig, (ax0) = plt.subplots(nrows=1, ncols=1, figsize=plot_size, sharex=True)
    

    # this reads todays date
    x1 = datetime.datetime.now()
    # this reads the date 10 weeks prior to todays date
    x2 = x1 + datetime.timedelta(weeks = -10)
    employees = df1a['Employee'].unique()
    
    mindate, maxdate = df1['Day'].agg(['min','max'])
    ix1 = pd.date_range(mindate,maxdate,freq='1D')
    yz = np.zeros(ix1.shape)
    ds9 = pd.Series(yz, index=ix1)
    
    
    for e in employees:
        df1b = df1a[df1a['Employee'] == e]
        df1c = df1b[(df1b['Day'] >= x2) & (df1b['Day'] <= x1)]
        df1d = df1c.groupby(by=['Day']).sum() #cumulative sum of the hours worked on project per day
        
        x = df1d.index.values
        y = df1d['Duration'].values #duration of values per day
        yz = ds9.loc[x]
        
        ax0.bar(x, y, bottom = yz, alpha=0.5)
        ds9.loc[x] += y
            
    if axis_title is not None:
        ax0.set_title(axis_title)

    ax0.grid(True)
    ax0.legend(employees, loc = 'upper left')
    
    ax0.set_xlim([x2,x1])
    ax0.set_xlabel('Day')
    dtFmt = mdates.DateFormatter('%m'+'/'+'%d') # define the formatting
    ax0.xaxis.set_major_formatter(dtFmt) # apply the format to the desired axis
    
    pltPdf1.savefig()
    plt.close()

    return

def employees_by_project_daterange(pltPdf1, df1a, axis_title=None, plot_size=(6.5,4.8)):
    fig, (ax0) = plt.subplots(nrows=1, ncols=1, figsize=plot_size, sharex=True)
    
    # this reads todays date
    x1 = datetime.datetime.now()
    # this reads the date 10 weeks prior to todays date
    x2 = x1 + datetime.timedelta(weeks = -10)
    projects = df1a['Project'].unique()
    
    mindate, maxdate = df1['Day'].agg(['min','max'])
    ix1 = pd.date_range(mindate,maxdate,freq='1D')
    yz = np.zeros(ix1.shape)
    ds9 = pd.Series(yz, index=ix1)
    
    for p in projects:

        df1b = df1a[df1a['Project'] == p]
        df1c = df1b[(df1b['Day'] >= x2) & (df1b['Day'] <= x1)]
        df1d = df1c.groupby(by=['Day']).sum() #cumulative sum of the hours worked on project alpha per day
        
        x = df1d.index.values
        y = df1d['Duration'].values #duration of values per day
        yz = ds9.loc[x]
        
        ax0.bar(x, y, bottom = yz, alpha=0.5)
        ds9.loc[x] += y
            
    if axis_title is not None:
        ax0.set_title(axis_title)

    ax0.grid(True)
    ax0.legend(projects, loc = 'upper left')
    
    ax0.set_xlim([x2,x1])
    ax0.set_xlabel('Day')
    dtFmt = mdates.DateFormatter('%m'+'/'+'%d') # define the formatting
    ax0.xaxis.set_major_formatter(dtFmt) # apply the format to the desired axis
    
    pltPdf1.savefig()
    plt.close()

    return

if __name__ == "__main__":

    # If changing basicConfig, make sure to close the dedicated console; it will not take otherwise
    logging.basicConfig(filename='timesheet.log', filemode='w', 
                        format='%(levelname)s: %(message)s',
                        level=logging.DEBUG)
    
    # Reading the input data. Use pandas dataframes to hold data 
    # because they are very flexible
    datadir = 'Data'
    fname = 'Clockify_Time_Report_Detailed_2021-01-01-2021-12-31.csv'
    df1 = pd.read_csv(os.path.join(datadir, fname), # Clockify_Time_Report_Detailed_2021-01-01-2021-12-31.csv
                       usecols=(0,4,8,13),
                      names=['Project', 'Employee',  'Day', 'Duration'], header=0,
                      comment='#',
                      parse_dates=['Day']
                      # dtype = {'Project': str, 'Employee': np.str, 'Day': np.datetime64, 'Duration': float}
                      )
    
    # Open a pdf file to save the plots
    pltPdf1  = dpdf.PdfPages('Timesheet_BarChart.pdf')
    
    projects = df1['Project'].unique()
    employees = df1['Employee'].unique()

    p = len(projects)
    e = len(employees)

    print('There are '+str(len(employees))+' unique employees and '+str(len(projects))+' unique projects')
            
    if False:
        
        for p in projects:
            df1a = df1[df1['Project'] == p]
            
            projects_by_employee_daterange(pltPdf1, df1a, axis_title=p)
            
    if False:
        
        for e in employees:
            df1a = df1[df1['Employee'] == e]
            
            employees_by_project_daterange(pltPdf1, df1a, axis_title=e)
            
    if True:
        
        for e in employees:
            df1a = df1[df1['Employee'] == e]
            
            employees_by_project_daterange_cumsum(pltPdf1, df1a, axis_title=e)
            

    print('Closing pdf file')
    
    pltPdf1.close()
    
    logging.shutdown()
    