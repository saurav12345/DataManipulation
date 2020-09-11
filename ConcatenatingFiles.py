#!/usr/bin/env python
# coding: utf-8

# In[9]:


import pandas as pd
import glob
g = map(pd.read_excel, glob.glob("C:\\Users\\saurav.an.kumar\\Desktop\\Q12 Monthly Reporting\\Apr'20 Data Reporting\\Team Details\\*.xlsx"))
df = pd.concat(g, ignore_index=True)
print(df.shape)
print(df.head())
df.to_excel("C:\\Users\\saurav.an.kumar\\Desktop\\Q12 Monthly Reporting\\Apr'20 Data Reporting\\Team Details\\Team Details_v1.xlsx".format(engine), index=False, encoding='utf8', engine='xlsxwriter')


# In[21]:


g = map(pd.read_excel, glob.glob("C:\\Users\\saurav.an.kumar\\Desktop\\Q12 Monthly Reporting\\Apr'20 Data Reporting\\Team Membership\\*.xlsx"))
df = pd.concat(g, ignore_index=True)
print(df.shape)
print(df.head())
df.to_excel("C:\\Users\\saurav.an.kumar\\Desktop\\Q12 Monthly Reporting\\Apr'20 Data Reporting\\Team Membership\\Team Membership_v1.xlsx".format(engine), index=False, encoding='utf8', engine='xlsxwriter')