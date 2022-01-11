# -*- coding: utf-8 -*-
"""
Created on Mon Dec 27 12:27:39 2021

@author: MarijaBebic
"""

import numpy as np
import matplotlib.pyplot as plt
import logging
import pandas as pd #multidimensional data analysis
import random
import csv
from datetime import datetime # time stamps
from datetime import timedelta
import holidays

column_titles = ['Name', 'Project', 'Day', 'Duration']
employees = ['jzb', 'mjb', 'wjs', 'rab', 'ddb']
projects = ['Alpha', 'Beta', 'Gamma', 'Delta']
total_hours = 0

days = []
employees1 = []
projects1 = []
hours = []
start_time = []
end_time = []

start_date1 = input('What is the first day of the work period? Input date in YYYY-MM-DD format.')
end_date1 = input('What is the last day of the work period? Input date in YYYY-MM-DD format.')
d1 = datetime.strptime(start_date1, '%Y-%m-%d')
d2 = datetime.strptime(end_date1, '%Y-%m-%d')

d = d1
holiday_hours = 8

while d <= d2:
    if d.weekday() >= 5:
        print(datetime.strftime(d,'%Y-%m-%d')+' is a weekend, no timesheet needed')
        d += timedelta(days=1)
        continue #goes back to the while loop
    elif d.date() in holidays.US(years=[2021,2022]):
        print(datetime.strftime(d,'%Y-%m-%d')+' is a holiday, timesheet with holiday pay needed')
        for employee in employees:
            dtb = d+timedelta(hours=8)
            dte = dtb+timedelta(hours=holiday_hours)
            employees1.append(employee)
            projects1.append('Holiday Pay')
            hours.append(holiday_hours)
            start_time.append(datetime.strftime(dtb, '%H:%M:%S'))
            end_time.append(datetime.strftime(dte, '%H:%M:%S'))
            days.append(d)
    else:
        for employee in employees:
            total_hours = 0
            dtb = d+timedelta(hours=8)
            while total_hours <= 8:
                temp = round(random.uniform(0.5,8.5), 1)
                hour_generator = round(temp*4)/4
                total_hours += hour_generator
                dte = dtb+timedelta(hours=hour_generator)
                project_generator = random.choice(projects)
                # check for lunch break
                noon = d+timedelta(hours=12)
                if dtb < noon and dte > noon:
                    start_time.append(datetime.strftime(dtb, '%H:%M:%S'))
                    end_time.append(datetime.strftime(noon, '%H:%M:%S'))
                    employees1.append(employee)
                    projects1.append(project_generator)
                    days.append(d)
                    temp = (noon - dtb)/timedelta(hours=1)
                    hours.append(temp)
                    # shifting by 1 to account for lunch break
                    noon += timedelta(hours=1)
                    dte += timedelta(hours=1)
                    start_time.append(datetime.strftime(noon, '%H:%M:%S'))
                    end_time.append(datetime.strftime(dte, '%H:%M:%S'))
                    employees1.append(employee)
                    projects1.append(project_generator)
                    days.append(d)
                    hours.append(hour_generator - temp)
                else:
                    start_time.append(datetime.strftime(dtb, '%H:%M:%S'))
                    end_time.append(datetime.strftime(dte, '%H:%M:%S'))
                    employees1.append(employee)
                    projects1.append(project_generator)
                    days.append(d)
                    hours.append(hour_generator)
                dtb = dte
            if total_hours > 9:
                temp = total_hours - 8 
                hours[-1] -= temp
                dte = dte+timedelta(hours=-temp)
                end_time[-1] = datetime.strftime(dte, '%H:%M:%S')
    d+= timedelta(days=1)
            

z = {'Start Date': days, 'End Date': days, 'User': employees1, 'Project': projects1, 'Duration (decimal)': hours, 'Start Time': start_time, 'End Time': end_time}

df1 = pd.DataFrame(z)
df1['Duration (h)'] = pd.to_datetime(df1['Duration (decimal)'], unit='h').dt.strftime('%H:%M:%S')
df1['Email'] = df1['User'] + '@achillearesearch.com'
# df1['Start Date Format'] = df1['Start Date'].dt.strftime('%Y-%m-%d')
df1.to_csv('Timesheet1.csv', float_format='%.2f', index=False)
           # columns=['Start Date','User','Project','Start Time','Duration','Email'])

