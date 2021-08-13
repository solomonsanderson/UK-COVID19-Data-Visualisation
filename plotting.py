'''
Plotting the various different types of data on the API
'''

import matplotlib.pyplot as plt
from matplotlib.gridspec import GridSpec
from data_processing import data_processing

fig = plt.figure()
gs = GridSpec(2, 2)
ax = fig.add_subplot(gs[0])
ax1 = fig.add_subplot(gs[1])
ax2 = fig.add_subplot(gs[2])



def vaccines(data, new_ax=ax, cum_ax=ax1):
    date = data['date']
    new_one = data['newPeopleVaccinatedFirstDoseByPublishDate']
    new_sec = data['newPeopleVaccinatedSecondDoseByPublishDate']
    new_tot = data['newVaccinesGivenByPublishDate']
    cum_one = data['cumPeopleVaccinatedFirstDoseByPublishDate']
    cum_sec = data['cumPeopleVaccinatedSecondDoseByPublishDate']
    cum_tot = data['cumVaccinesGivenByPublishDate']
    new_lines = [ax.plot(date, new_one), ax.plot(date, new_sec)]
    cum_lines = [ax1.plot(date, cum_one), ax1.plot(date, cum_sec)]
    return cum_lines


data = data_processing()
vaccines(data)



plt.show()