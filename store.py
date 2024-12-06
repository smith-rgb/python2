# import pandas as pd
# import matplotlib.pyplot  as plt 
# import seaborn as sns
# import numpy as np 

# df = pd.read_csv("superstore.csv", encoding= "unicode_escape")

# df. info()

# df["Order Date"]= pd.to_datetime(df["Order Date"],format='%m/%d/%Y')
# df["Ship Date"]= pd.to_datetime(df["Ship Date"],format='%m/%d/%Y')
# df["dt_month"] = df["Order Date"].dt.month
# df["dt_year"] = df["Order Date"].dt.year
# df["dt_dia"] = df["Order Date"].dt.day

# plt.figure(figsize=(12,6))
# sns.barplot(x="dt_month", y= "Sales", data=df)
# plt.show()


import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
df = pd.read_csv("Superstore.csv",encoding="unicode_escape")
print(
df.info()
)
df["Order Date"]= pd.to_datetime(df["Order Date"],format='%m/%d/%Y')
df["Ship Date"]= pd.to_datetime(df["Ship Date"],format='%m/%d/%Y')
df["dt_month"] = df["Order Date"].dt.month
df["dt_year"] = df["Order Date"].dt.year
df["dt_dia"] = df["Order Date"].dt.day
plt.figure(figsize=(12,6))
sns.barplot(x='dt_month',y='Sales',data=df)
plt.show()

plt. figure(figsize=(12,6))
sns. kdeplot(x="Ship Date", data=df)
plt. show()

