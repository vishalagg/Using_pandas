import matplotlib.pyplot as plt

'''
In line charts, we simply pass the the x_values,y_values to plt.plot() and rest of wprk is done by the function itself. In case of bar graph, we have to take care of three things:
    1.position of bars(ie. starting position of each bar)
    2.position of axis labels. 
    3.width of the bars.
'''
'''
 We can generate a vertical bar plot using either pyplot.bar() or Axes.bar(). prefebly, use Axes.bar() so we can extensively customize the bar plot more easily. We can use pyplot.subplots() to first generate a single subplot and return both the Figure and Axes object.
 eg:******
    fig, ax = plt.subplots()
    
    ^above eqn is equivalent to:
    fig = plt.figure(1,1,1)
    ax = fig.add_subplot()
'''
'''
To pass all three parameters mentioned in 1st paragraph, we can pass like:
    ax.bar(bar_positions, bar_heights, width)
    
here:   
    bar_positions(left) and bar_heights = Both are lists.
    width = specifys the width of each bar,generally float o int.
'''
'''
Ticks,labels,rotation:

By default, matplotlib sets the x-axis tick labels to the integer values the bars spanned on the x-axis (from 0 to 6). We only need tick labels on the x-axis where the bars are positioned. We can use Axes.set_xticks() to change the positions of the ticks to [1, 2, 3, 4, 5]:

    tick_positions = range(1,6)
    ax.set_xticks(tick_positions)

Then, we can use Axes.set_xticklabels() to specify the tick labels:
    
    col = ['bar1','bar2','bar3','bar4','bar5']
    ax.set_xticklabels(num_cols,rotation=90)
'''
'''
***similarly we can create HORIZONTAL BAR using:

ax.barh(bar_positions(bottom), bar_widths,width) instead of ax.bar()

 We use Axes.set_yticks() to set the y-axis tick positions to [1, 2, 3, 4, 5] and Axes.set_yticklabels() to set the tick labels to the column names

'''