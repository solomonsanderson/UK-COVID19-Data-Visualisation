'''
Plotting the various different types of data on the API
'''

import matplotlib.pyplot as plt
from matplotlib.gridspec import GridSpec
import pandas as pd
from data_get import data_get
from title_formatter import title_formatter


def vaccine_

def plotting_all():
    data = data_get()
    # print(list(data.columns)[4:])
    metrics = (data.columns)[4:]
    nrows = 4  
    ncols = int(len(metrics) / nrows)
    fig, axes = plt.subplots(nrows, ncols, figsize = (15,10))
    axes = axes.flatten()
    for i in range(len(axes)):
        column = metrics[i]
        metric = data[column]
        axes[i].plot(data['date'], metric)
        axes[i].set_title(title_formatter(column))
    
    plt.tight_layout()
    plt.show()


plotting_all()
