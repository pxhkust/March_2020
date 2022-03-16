import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import seaborn as sns
from scipy import stats

fig = plt.figure(figsize=(10,5))
sns.set(style="darkgrid", context="notebook", palette="muted")
plt.style.use('ggplot')
df = pd.read_csv("summarylate.csv")
slope, intercept, r_value, p_value, std_err = stats.linregress(df["Price"], df["Quantity"])
sns.regplot(x="Price", y="Quantity", data=df,
             color="black",
             marker="o",
line_kws={'label':"y={0:.1f}x+{1:.1f}".format(slope, intercept)})


plt.title("Mainland paper recycling index and HK waste paper export price")
plt.xlabel("local_price(HKD/t)")
plt.ylabel("export_price(HKD/t)")
plt.legend()
plt.show()
# plt.savefig("figure1.png")
print(r_value**2)
print(p_value)
# pccs = np.corrcoef(local_price, export_price)
# print(pccs)
