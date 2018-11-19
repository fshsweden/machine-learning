import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.dates as dates

ts = pd.Series(np.random.randn(1000), index=pd.date_range('1/1/2000', periods=1000))

ts = ts.cumsum()

ts.plot()

plt.figure()

ts.plot(style='k--', label='Series')

plt.legend()

plt.show()
