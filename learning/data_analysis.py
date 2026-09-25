import  pandas  as pd
import numpy as np
from data_preparation import df
import  matplotlib.pyplot as plt
import seaborn as sns

# for col in df.columns:
#     print(col)
#     print(df[col].unique()[:5])
#     print(df[col].nunique())

#     print("*************")
# %%
sns.histplot(df.msrp)
plt.show()

