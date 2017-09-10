import pandas as pd

dataframe = pd.read_file("file.csv")

'''
    let say file.csv have header like: DATE   AVG
then to convert DATE from string to date datatype use: pd.to_datetime()
'''

dataframe['DATE'] = pd.to_datetime(dataframe['DATE'])

'''
To create the line chart, we'll use the matplotlib library,The pyplot module provides a high-level interface for matplotlib that allows us to quickly create common data plots and perform common tweaks to them.
'''
import matplotlib.pyplot as plt
    
plt.plot()# plot() function would generate an empty plot with just the axes and ticks
plt.show()# show() function would display that plot

'''
By default, Matplotlib displayed a coordinate grid with:
1.the x-axis and y-axis values ranging from -0.06 to 0.06
2.no grid lines
3.no data
'''

'''
plt.plot(x_values, y_values) => x=_vlaues and y_values can be iterable objects or Series.
'''

'''
Sometimes labels on x or y axis are to close to read, we can rotate them by 90 using:
    plt.xticks(rotation=90) #for x-axis
    plt.yticks(rotation=90) #for y-axis
'''

'''
set x-lable: plt.xlabel('LABEL ON X_AXIS')
set y-lable: plt.ylabel('LABEL ON y_AXIS')
set title on chart: plt.title('LABEL ON chart')
'''