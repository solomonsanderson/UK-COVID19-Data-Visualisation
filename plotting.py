'''
Plotting the various different types of data on the API
'''

import matplotlib.pyplot as plt
from matplotlib.gridspec import GridSpec
from data_get import data_get
from title_formatter import title_formatter
from highlighting import vaccine_groups
from highlighting import lockdowns

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
        axes[i].plot(data['date'], metric, color='black')
        title = title_formatter(column)
        axes[i].set_title(title)
        if 'Vaccines' in title:
            vaccine_groups(axes[i])
        elif 'Vaccinated' in title:
            vaccine_groups(axes[i])

        lockdowns(axes[i])

    plt.tight_layout()
    plt.show()


plotting_all()
