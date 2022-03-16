import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import seaborn as sns
from scipy import stats

fig = plt.figure(figsize=(10, 5))
df = pd.read_csv("point1228.csv")

# plt.figure(figsize=(8,8), dpi=80)
# plt.figure(1)
#
# ax1 = plt.subplot(311)
sns.scatterplot(x="Price", y="Quantity", data=df, color="black")

# # ax1 = plt.subplot(221)
# sns.scatterplot(x="Price_470710", y="Quantity_470710", data=df, color="black")
#
# ax1 = plt.subplot(322)
# sns.scatterplot(x="Price_470720", y="Quantity_470720", data=df, color="black")
#
# ax1 = plt.subplot(331)
# sns.scatterplot(x="Price_470730", y="Quantity_470730", data=df, color="black")
#
# ax1 = plt.subplot(332)
# sns.scatterplot(x="Price_470790", y="Quantity_470790", data=df, color="black")
plt.xlabel("Price(U.S.$/t)")
plt.ylabel("Quantity(thousand tonnes)")
plt.show()
