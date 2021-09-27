'''
Plotting the various different types of data on the API
'''

import matplotlib.pyplot as plt
from matplotlib.gridspec import GridSpec
from matplotlib.widgets import CheckButtons
from data_get import data_get
from title_formatter import title_formatter
from highlighting import vaccine_groups
from highlighting import lockdowns
import numpy as np

from rolling_average import rolling_average


def plotting_all():
    # data = data_get(AREA_TYPE',AREA_NAME='portsmouth')
    data = data_get()
    metrics = (data.columns)[4:]
    nrows = 4  
    ncols = int(len(metrics) / nrows)
    fig, axes = plt.subplots(nrows, ncols, figsize = (15,10))
    axes = axes.flatten()
    vc_all = []
    ld_all = []

    for i in range(len(axes)):
        column = metrics[i]
        metric = data[column]
        
        ra = rolling_average(data[['date', column]],7)
        axes[i].plot(ra.iloc[:,0], ra.iloc[:,2], color = "purple", zorder=3)

        latest_ra = ra.iloc[0][ra.columns[-1]]

        if latest_ra > 0:
            color = 'r'
            ra_label = f'7 Day Avg: {latest_ra:.0f} $\\uparrow$'

        elif latest_ra < 0:
            color = 'g'
            ra_label = f'7 Day Avg: {latest_ra:.0f} $\\downarrow$'

        axes[i].plot(data['date'], metric, color="black", alpha=0.7, label=ra_label, zorder=2)
        legend = axes[i].legend(facecolor=color, framealpha=0.1)
        for text in legend.get_texts():
            text.set_color(color)

            

        title = title_formatter(column)
        axes[i].set_title(title)
        if 'Vaccines' in title:
            vc_patches = vaccine_groups(axes[i])
            vc_all.append(vc_patches)
        elif 'Vaccinated' in title:
            vc_patches = vaccine_groups(axes[i])
            vc_all.append(vc_patches)
        
        ld_patches =  lockdowns(axes[i])
        ld_all.append(ld_patches)

    # Adding Tick Boxes for patches
    ld_all = np.array(ld_all).flatten()
    vc_all = np.array(vc_all).flatten()

    labels = ['Lockdowns', 'Vaccines']
    activated = [True, True]
    axCheckButton = plt.axes([0.053, 0.91, 0.1, 0.05])
    check = CheckButtons(axCheckButton, labels, activated)
    check_colors = ['yellow', 'cornflowerblue']
    [rectangle.set_facecolor(check_colors[i]) for i, rectangle in enumerate(check.rectangles)]
    def func(label):
        index = labels.index(label)
        
        if index == 0:
                for patch in ld_all:
                    patch.set_visible(not patch.get_visible())
                 
        elif index == 1:
            for patch in vc_all:
                patch.set_visible(not patch.get_visible())
        
        plt.draw()
            
    check.on_clicked(func)
    
    plt.tight_layout()
    plt.show()


plotting_all()
