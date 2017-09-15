import pandas as pd
import matplotlib.pyplot as plt

'''
lets first look at how to calculate frquency of each item in an iterable and count them and then ill see how to sort them:

    f_c = Series.value_counts() => returns series object and resulting Series object                                   will be sorted by frequency in descending order.
    
    to get ascending order:
    sort_index = f_c.sort_index()
'''
'''
****
bins:
 To construct a histogram, the first step is to "bin" the range of values—that is, divide the entire range of values into a series of intervals—and then count how many values fall into each interval. The bins are usually specified as consecutive, non-overlapping intervals of a variable.
'''
'''
    We can create histogram using=> Axes.hist() => This method has only 1 required parameter, an iterable object containing the values we want a histogram for.
    
By default, matplotlib will:

1.calculate the minimum and maximum value from the sequence of values we passed in
2.create 10 bins of equal length that span the range from the minimum to the maximum     value.
3.group unique values into the bins
4.sum up the associated unique values
5.generate a bar for the frequency sum for each bin
'''
'''
 We can use the range parameter to specify the range we want matplotlib to use as a tuple:
            fig, ax = plt.subplots()
            ax.hist(ls, range=(0, 5),bins=20)
            plt.show()
'''