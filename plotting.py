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


def plotting_all():
    data = data_get()
    # print(list(data.columns)[4:])
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
        axes[i].plot(data['date'], metric, color='black')
        title = title_formatter(column)
        axes[i].set_title(title)
        if 'Vaccines' in title:
            vc_patches = vaccine_groups(axes[i])
            vc_all.append(vc_patches)
        elif 'Vaccinated' in title:
            vc_patches = vaccine_groups(axes[i])
            vc_all.append(vc_patches)
        
        # # Adding Tick Boxes for patches
        # vc_patches = vaccine_groups(axes[i])
        ld_patches =  lockdowns(axes[i])
        ld_all.append(ld_patches)
    
    ld_all = np.array(ld_all).flatten()
    vc_all = np.array(vc_all).flatten()
    
    labels = ['Lockdowns', 'Vaccines']
    activated = [True, True]
    axCheckButton = plt.axes([0.03, 0.4, 0.10, 0.15])
    check = CheckButtons(axCheckButton, labels, activated)

    def func(label):
        index = labels.index(label)
        
        if index == 0:
                for patch in ld_all:
                    # print(patch.get_visible())
                    patch.set_visible(not patch.get_visible())
                    # print(patch.get_visible())
                    # for patch in ld_patches:
                    #     patch.remove()
        elif index == 1:
            for patch in vc_all:
                patch.set_visible(not patch.get_visible())
                # for patch in vc_patches:
                #     patch.remove()

        # def set_visible(label):
        #     index = labels.index(label)
        #     if index == 1:
        #         ld_patches[index].set_visible(not patches[index].get_visible())

        #     elif index == 2:
        axes[0].set_title('yeet')
        plt.draw()
                

    
    check.on_clicked(func)


    plt.tight_layout()
    plt.show()


plotting_all()
