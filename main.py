import pandas
import webbrowser
import os
import numpy as np

data_table = pandas.read_csv("nflx_trades.csv")

del data_table["id"]
del data_table["dt"]

#m = data_table.values()

html = data_table[0:100].to_html()

with open("data.html","w") as f:
    f.write(html)

full_filename = os.path.abspath("data.html")
webbrowser.open("file://{}".format(full_filename))
