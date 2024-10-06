import pandas as pd
import os

f=0
df = pd.read_excel(r'D:\sjwlab\meixuewen\all_data\our_data\dbt\org\val\excel.xlsx')
for index, row in df.iterrows():
    name = row['PatientID']
    view=row['View']
    Class=row['Class']
    if f==0:
        flag1,flag2=name,Class

