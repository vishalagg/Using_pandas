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

Calling pandas.Series.dt.month returns a Series containing the integer values for each month (e.g. 1 for January, 2 for February, etc.). 
'''
'''
****coloring: in order to show two line graphs in one graph of different colors,we can provide different colors also, by passing c = 'color_name' in plot method.


eg:
fig = plt.figure(figsize=(6,3))
plt.plot(x_value1,y_value1, c='red')
plt.plot(x_value2,y_value2, c='blue')
plt.show()


In case of multi lines in single graph,To help remind us which value each line corresponds to, we can add a legend that links each color to the value the line is representing.for this we can pass lable = "line1"(say) in lpot method.

We can create the legend using pyplot.legend and specify its location using the loc parameter:
    plt.legend(loc='upper left')
'''
'''
title:plt.title('title of chart')
xlabel: plt.xlabel('x title')
ylabel: plt.ylabel('y title')

'''