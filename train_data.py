import pandas as pd
import webbrowser
import os
import numpy as np
import matplotlib.pyplot as plt

# Make the graphs a bit prettier, and bigger
# pd.set_option('display.mpl_style', 'default')

# This is necessary to show lots of columns in pandas 0.12.
# Not necessary in pandas 0.13.
pd.set_option('display.width', 5000)
pd.set_option('display.max_columns', 60)

plt.rcParams['figure.figsize'] = (15, 5)

def present_as_html(dt):
    html = dt[0:100].to_html()
    with open("data.html", "w") as f:
        f.write(html)
    full_filename = os.path.abspath("data.html")
    webbrowser.open("file://{}".format(full_filename))


dt = pd.read_csv("nflx_trades.csv")

del dt["id"]
#del dt["dt"]

dt["prev-price"] = dt["price"].shift(1)
dt["diff"] = dt["price"] - dt["prev-price"]

dt["mean50"] = dt["price"].rolling(window=50).mean()
dt["mean200"] = dt["price"].rolling(window=200).mean()

dt["mean200"].tail(3000).plot()
dt["mean50"].tail(3000).plot()

plt.show()

present_as_html(dt)

