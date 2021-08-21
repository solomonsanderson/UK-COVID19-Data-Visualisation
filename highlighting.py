'''
Holds data on vaccine groups and key restriction dates and plots them
'''


from datetime import datetime, date
import numpy as np


def vaccine_groups(axis):
    vaccine_groups = ['80+, Care Homes', 'Healthcare Workers', '70+, extremely vulnerable', '65+, underlying health condtions ']
    vaccine_dates = ['2020-12-8', '2021-01-18', '2021-02-15', '2021-03-01', '2021-03-06', '2021-03-17', '2021-04-13','2021-04-26', '2021-04-27', '2021-04-30', '2021-05-13', '2021-05-18', '2021-05-20', '2021-05-22', '2021-05-26', '2021-06-08', '2021-06-15', '2021-06-16', '2021-06-18']
    vaccine_dates = [datetime.strptime(date, '%Y-%m-%d') for date in vaccine_dates]
    vaccine_dates.append(date.today())

    rgbs = np.linspace(0.2, 1, len(vaccine_dates) - 1)
    rgbs = np.flip(rgbs)
    for i in range(0, len(vaccine_dates) - 1):
	    axis.axvspan(vaccine_dates[i], vaccine_dates[i+1], color = (rgbs[i], rgbs[i], 1), alpha = 0.7)


def lockdowns(axis):
    lockdown_dates = [("2020-03-26","2020-05-10"), ('2020-11-02', '2020-12-02'), ('2021-01-06', '2021-04-12')]
    for dates in lockdown_dates:
        start = datetime.strptime(dates[0], "%Y-%m-%d")
        end = datetime.strptime(dates[1], "%Y-%m-%d")
        print(start, end)
        axis.axvspan(start, end, color="r", alpha=0.2)

