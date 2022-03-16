import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import seaborn as sns
from scipy import stats

fig = plt.figure(figsize=(10, 5))
df = pd.read_csv("SP.csv")


sns.scatterplot(x="Price", y="Quantity", hue="Waste Paper",
                data=df,palette='Spectral_r')

plt.xlabel("Export_Price(USD/t)")
plt.ylabel("Export_Quantity(thousand tonnes)")
plt.show()