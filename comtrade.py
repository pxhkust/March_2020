import holoviews as holoviews
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import seaborn as sns
import itertools
from chord import Chord

data = pd.read_csv("comtrade.csv")
# data.head()
print(data)
names = ["HongKong_export", "HongKong_re-export", "HongKong_import", "Bangladesh", "China", "Other_Asia_nes", "Nigeria", "Philippines", "Thailand", "China_Macao", "USA"]
# data = list(itertools.chain.from_iterable((i, i[::-1])for i in data.values))
# matrix = pd.pivot(pd.DataFrame(data), index=0, columns=1, fill_value=0).values.tolist()
#
# pd.DataFrame(matrix)
matrix = data.corr()
matrix = matrix.values.tolist()
# Chord(matrix, names)

plot = Chord(matrix, names, colors="d3.schemeSet2").show()







