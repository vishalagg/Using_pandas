import matplotlib.pyplot as plt

'''
fig = plt.figure() : used to create figure manually
fig = plt.figure(figsize=(width, height)) => we can also give size of figure so that there is no problem regarding reading of ticks label. Width & height must be in "inches".
'''
'''
axes_obj = fig.add_subplot(nrows, ncols, plot_number) :
            To add a new subplot to an existing figure, use Figure.add_subplot.This will return a new Axes object, which needs to be assigned to a variable

eg:  ax1 = fig.add_subplot(2,1,1)
     ax2 = fig.add_subplot(2,1,2)
     we can display everything using: plt.show()
      here the x-axis and y-axis values ranging from 0.0 to 1.0 (unlike previous one, -0.6 to 0.6 using plot function)
'''
'''
To generate a line chart within an Axes object, we need to call Axes.plot() and pass in the data you want plotted.
eg: x_values = [0.0, 0.5, 1.0]
    y_values = [10, 20, 40]
    ax1.plot(x_values, y_values)
'''

'''
**To extract Month(let say) from date dataset,we can use the pandas.Series.dt accessor:
e.g:
    month_col['MONTH'] = month_col['DATE'].dt.month
'''