'''
gives a rolling average for whichever data is input over  the specified time period
'''


import pandas as pd


def rolling_average(data, window):
    df = pd.DataFrame(data)
    for i in range(0, df.shape[0]-2):
        df['7dayavg'] = df.rolling(window).mean()

    df = df.dropna()
    print(df)
    return df