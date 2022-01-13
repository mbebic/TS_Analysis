# Timesheet Analysis.

This Repository will contain functions designed for analysis and plotting of timesheet information. This type of tangible information is incredibly useful to any project manager or team leader that would like to have plotted data of hours worked on particular projects by certain employees. This type of code was developed out of a need for this type of data plotting, but without paying extra premiums on timesheet applications on the web. We wanted to be able to fully customize what we wanted to see, and have oversight on the development.

Within Timesheet_Plotting_Code_v2.py, the first plotting function exists, titled 'projects_by_employee_daterange'. This function allows us to use the datetime library from pandas. This allow us to create calendar formatted dates (2022-01-01) instead of using integer values (Day 1, Day 2, etc.). Using calendar dates is more realistic to every day life, as well as minimizes confusion and error when analyzing and inputting timesheets.

We also wanted to be able to stack the bar chart values for each day that people worked on various projects. This creates an easier way to visualize the amount of time each employee spends on any given project.

The x1 variable will read the current date, and x2 will read the date from 10 weeks prior. This value can be changed, and the increment can be changed to days, months, etc. Then, it filters for each employee within your data frame and puts them into the variable employees. 

To create the ability to stack the plots, we had to use a pandas series function to increment where the previous employees cumulative hours stopped, so the next employees cumulative hours that are graphed are not starting from y=0 position, but rather the position of the first employees cumulative hours. The code block is as follows:

```python
# CODE BLOCK 1
mindate, maxdate = df1['Day'].agg(['min','max'])
ix1 = pd.date_range(mindate,maxdate,freq='1D')
yz = np.zeros(ix1.shape)
ds9 = pd.Series(yz, index=ix1)
```

In line 1, we create the mindate and maxdate to be the first and last date of the csv file we have imported. Next, we create a date range between those two dates and assign it to the ix1 variable. We create yz to be filled with zeros and the same shape as ix1. Finally, we create a pandas series with yz and the index set to ix1. This is essentially a 1D array that can hold data of any type. This will help us with incrementing the positions of the hours worked by employee 1, and stack the hours worked by employee 2 on the last known hour position of employee 1, instead of overlapping.

```python
# CODE BLOCK 2
x = df1d.index.values
y = df1d['Duration'].values 
yz = ds9.loc[x]

ax0.bar(x, y, bottom = yz, alpha=0.5)
ds9.loc[x] += y
```

In line 1 and 2, we are pulling the value of the datetime and the duration of hours worked respectively. We set yz to ds9.loc[x] to create a placeholder series where we know what days employee 1 worked. Then, the bar chart is plotted with the bottom position being yz. For employee 1, the yz position will be 0. Then, the crucial line of code is the last line. This increments each position (ds9.loc[x]) in the ds9 panda series with the last known hour position of employee 1 [y]. By doing this, the yz values change to the values of duration from employee 1. Then, once the for loop begins again with employee 2, the same process will repeat and their respective hours will be added to the ds9 pandas series. This avoids overlapping of hours worked by each employee. I will provide an example of the methodology of this.

``` python
CODE BLOCK 3
# employee 1 hours: 1
# employee 2 hours: 3 
# both worked on the same day, 2022-01-07

# employee 1's x and y values: (2022-01-07, 1)
# employee 2's x and y values: (2022-01-07, 3)

yz = ds9.loc[x]
# this starts out as zeros, as described in code block 1.

# for employee 1, the plotting will read
ax0.bar(2022-01-07, 1, bottom = yz) # yz is 0 to start
ds9.loc[x] += y 

# in this case, ds9.loc[x] += 1
# ds9.loc[x], or yz, has now turned into 1 for the corresponding date of 2022-01-07.
# when the for loop begins again for employee 2, this is how the plot will read

ax0.bar(2022-01-07, 3, bottom = yz) # yz is 1
ds9.loc[x] += y 

# in this case, ds9.loc[x] += 3
# ds9.loc[x], or yz, has now turned into 4 (1+3) for the corresponding date of 2022-01-07.
```

By incrementing the position argument like this, the bar chart stacks the values of duration without overlap.
