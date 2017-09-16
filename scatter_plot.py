'''
 A plot containing just the markers is known as a scatter plot.
'''
import matplotlib.pyplot as plt

fig,ax = plt.subplots()

'''
we can create scatter plot using: ax.scatter(x_values,y_values)

x_values,y_values:iterable objects of matching lengths (lists, NumPy arrays, or pandas series)
'''
'''
set x and ylabels:
ax.set_xlabel('Xlabel')
ax.set_ylabel('Ylabel')
'''

'''
When generating multiple scatter plots for the purpose of comparison, it's important that all plots share the same ranges in the x-axis and y-axis. We can use Axes.set_xlim() and Axes.set_ylim() to set the data limits for both axes:

    ax.set_xlim(0, 5)
    ax.set_ylim(0, 5)
'''

'''
    Most of the plotting functionality in pandas is contained within the DataFrame.plot() method. When we call this method, we specify the data we want plotted as well as the type of plot. We use the kind parameter to specify the type of plot we want. We use x and y to specify the data we want on each axis.
    
    eg:
        DataFrame.plot(x='x_size', y='y_value', kind='scatter')
        
    also, we can pass figure size and title too:
        DataFrame.plot(x='x_size', y='y_value', kind='scatter',title='title',figsize=(5,10))
'''
