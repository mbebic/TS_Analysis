# Timesheet Analysis.

This Repository will contain functions designed for analysis and plotting of timesheet information. This type of tangible information is incredibly useful to any project manager or team leader that would like to have plotted data of hours worked on particular projects by certain employees. This type of code was developed out of a need for this type of data plotting, but without paying extra premiums on timesheet applications on the web. We wanted to be able to fully customize what we wanted to see, and have oversight on the development.

Within Timesheet_Plotting_Code_v2.py, the first plotting function exists, titled 'projects_by_employee_daterange'. This function allows us to use the datetime library from pandas. This allow us to create calendar formatted dates (2022-01-01) instead of using integer values (Day 1, Day 2, etc.). Using calendar dates is more realistic to every day life, as well as minimizes confusion and error when analyzing and inputting timesheets.

We also wanted to be able to stack the bar chart values for each day that people worked on various projects. This creates an easier way to visualize the amount of time each employee spends on any given project.

The x1 variable will read the current date, and x2 will read the date from 10 weeks prior. This value can be changed, and the increment can be changed to days, months, etc. Then, it filters for each employee within your data frame and puts them into the variable employees. 

To create the ability to stack the plots, we had to use a pandas series function to increment where the previous employees cumulative hours stopped, so the next employees cumulative hours that are graphed are not starting from y=0 position, but rather the position of the first employees cumulative hours. The code block is as follows:

```python
mindate, maxdate = df1['Day'].agg(['min','max'])
ix1 = pd.date_range(mindate,maxdate,freq='1D')
yz = np.zeros(ix1.shape)
ds9 = pd.Series(yz, index=ix1)
```

In 
