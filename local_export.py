import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import seaborn as sns
from scipy import stats

# sns.set(style="darkgrid", context="notebook", palette="muted")
# 双y轴图
plt.style.use('ggplot')
df = pd.read_csv("summary.csv")
x = np.arange(df.shape[0])

# fig, ax1 = plt.subplots()
fig = plt.figure(figsize=(40,20))
ax1 = fig.add_subplot(111)


line1, = ax1.plot(x, df['Price'], color="black", linestyle='-', label='Price')
p1 = ax1.scatter(x, df['Price'], color="black", marker='v', s=30)

ax2 = ax1.twinx()
line2, = ax2.plot(x, df['Quantity'], color="black", linestyle='--', label='Quantity')
p2 = ax2.scatter(x, df['Quantity'], color="black", marker='o', s=30)

plt.title("HK waste paper export price and quantity", fontsize=12)

plt.xticks(x, df.Month, fontsize=0.001, rotation=90)
ax1.legend(loc=2)

ax1.set_xlabel("Month")
ax1.set_ylabel("Price(HKD/t)")
ax2.set_ylabel("Quantity(t)")
ax2.legend(loc=1)
fig.autofmt_xdate()
plt.show()
# plt.savefig("HK waste paper export price and quantity.png")