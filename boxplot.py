import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import seaborn as sns
from scipy import stats


sns.set(style="white", context="notebook", palette="muted")

tips = pd.read_csv("boxplot.csv")
tips.head()

sns.boxplot(x="Company", y="Local_Weight", data=tips)

plt.title("Local Transation Weight")
plt.legend(labels=["Local_Weight"])
plt.show()
