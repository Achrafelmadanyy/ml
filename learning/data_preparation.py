import  pandas  as pd
import numpy as np
data_path='data.csv'

df=pd.read_csv(data_path)


df.columns=df.columns.str.lower().str.replace(" ", "_")


string=list(df.dtypes[df.dtypes == 'str'].index)
for col in  string:
    df[col]=df[col].str.lower().str.replace(" ", "_")





