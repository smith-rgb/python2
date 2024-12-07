import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv("datos.csv")


print(df)

df["Month"]= pd.to_datetime(df["Month"],format='%m/%d/%Y')
# df["dt_month"] = df["Order Date"].dt.month
# df["dt_year"] = df["Order Date"].dt.year
# df["dt_dia"] = df["Order Date"].dt.day
print(df.info())

# plt.figure(figsize=(12,6))
# sns.barplot(x="Month", y= "Sales", data=df)
# plt.show()


plt.figure(figsize=(12,6))
sns.barplot(x="State", y= "Sales", data=df)
plt.show()




