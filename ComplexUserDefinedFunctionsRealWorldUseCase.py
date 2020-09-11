#!/usr/bin/env python
# coding: utf-8

# In[500]:


import pandas as pd
import numpy as np
from datetime import date
pd.set_option('mode.chained_assignment', None)


# In[526]:


df = pd.read_excel(r'C:\Users\saurav.an.kumar\Desktop\InputFile.xlsx')
print("Shape: ",df.shape,end=" and ")
print("Index: ",df.index)


# In[585]:


df.head(0)


# In[528]:


df.describe()


# In[586]:


df.dtypes


# In[532]:


df = df.fillna(0)
df['year'] = pd.DatetimeIndex(df['DATE_FINISH']).year
df['month'] = pd.DatetimeIndex(df['DATE_FINISH']).month
df['day'] = pd.DatetimeIndex(df['DATE_FINISH']).day
df['date'] = pd.DatetimeIndex(df['DATE_FINISH']).date
df[['year','month','day','date']].head()
#df.drop('Unnamed: 30',axis=1,inplace=True)


# In[650]:


def saurav(a,b):
    return a*b

def vaibhav(df,a,b):
    return df.loc[df[b]!=0,a]

#print(l)
   
#print(sum(FY18.loc[FY18['Q00. Weighted Score'] != 0,'NUMBER OF RESPONDENTS FOR THE WORKGROUP (N SIZE)']))

#FY19[['NUMBER OF RESPONDENTS FOR THE WORKGROUP (N SIZE)','Q00. Weighted Score']].apply(vaibhav)
#sum(FY19.apply(lambda 'NUMBER OF RESPONDENTS FOR THE WORKGROUP (N SIZE)','Q00. Weighted Score': np.array('NUMBER OF RESPONDENTS FOR THE WORKGROUP (N SIZE)') if np.array('Q00. Weighted Score') != 0 else 0))
#p = lambda x,y: x if y != 0 else 0
#print(sum(FY19.apply(p('NUMBER OF RESPONDENTS FOR THE WORKGROUP (N SIZE)','Q00. Weighted Score'))))
#print(sum(vaibhav(FY19,'NUMBER OF RESPONDENTS FOR THE WORKGROUP (N SIZE)','Q00. Weighted Score')))

def custom_filter(col1,col2,month,year,df):
    alpha = df[(df[col1]==month) & (df[col2]==year)]
    return alpha

def custom_filter_1(col,df,date1,date2):
    beta = df[(df[col] >= pd.Timestamp(date(date1[0],date1[1],date1[2]))) & (df[col] < pd.Timestamp(date(date2[0],date2[1],date2[2])))]
    return beta

#pd.DataFrame.from_dict(pd.DataFrame.from_dict(data_dict['FY17_Jan'])).head()
#for item in data_dict.items():
    #var = pd.DataFrame.from_dict(dict(item))
'''df_new = {}
def create_df(l,v):
    for i in l:
        #print(i)
        for val in v:
            df_new[i] = pd.DataFrame(val)
            return(df_new[i])'''

#var_df = pd.DataFrame()
#for var_new in l:
 #   var_new = pd.DataFrame(create_df(l,v))
#print(FY18_Jan.tail())
def create_df(d,k):
    return pd.DataFrame(d[k])

#print(create_df(z,'FY17_Sep').head())

'''def create_named_df(l,d):
    for a in l:
        a = create_df(d,a)
    return a'''
#print(create_named_df(l,data_dict).head())

def create_named_df(l,d):
    for a in l:
        b = a
        a = create_df(d,a)
        res[b] = a
    return res
#for s,t in z.items():
#    print(z[s].head())

def return_named_df_from_Variable_name(z,var_name):
    if var_name in z.keys():
        return (pd.DataFrame(z[var_name]))
    else:
        return False

#print('FY17_Oct' in z.keys())
#z['FY17_Jan'].head()
#print(return_named_df_from_Variable_name(z,'FY17_Oct'))
#g.head()
#print(g.head())
def single_variable_output(var):
    return return_named_df_from_Variable_name(z,var)
#pd.DataFrame(z['FY17_Sep']).head()
#g = single_variable_output('FY17_Oct')
#print(g.head())


# In[689]:


l=[]
v=[]

year = [2016,2017,2018]
month = ['Sep','Oct','Nov','Dec','Jan','Feb','Mar','Apr','May','Jun','Jul','Aug']

for i in range(1,len(year)+1):
    k = i + 16
    for j in range(len(month)):
        if(j > 3):
            l.append("FY"+str(k)+"_"+str(month[j]))
            v.append(custom_filter('month','year',(j+8)%12+1,year[i-1]+1,df))
        else:
            l.append("FY"+str(k)+"_"+str(month[j]))
            v.append(custom_filter('month','year',(j+8)%12+1,year[i-1],df))
       
data_dict={l[i]:v[i] for i in range(len(l))}
#print(data_dict.keys())
#print(data_dict.values())

z = create_named_df(l,data_dict)

#print(data_dict['FY17_Apr'])
#z.head()
#print(data_dict['FY17_Sep'])
#print(custom_filter('month','year',9,2017,df))
#print(z)
#print(1%3)


# In[598]:


FY16 = custom_filter_1('DATE_FINISH',df,[2016,4,29],[2016,9,1])
FY17 = custom_filter_1('DATE_FINISH',df,[2016,9,1],[2017,9,1])
FY18 = custom_filter_1('DATE_FINISH',df,[2017,9,1],[2018,9,1])
FY19 = custom_filter_1('DATE_FINISH',df,[2018,9,1],[2019,9,1])
FY20 = custom_filter_1('DATE_FINISH',df,[2019,9,1],[2020,4,1])

FY16_Apr = custom_filter('month','year',4,2016,df)
FY16_May = custom_filter('month','year',5,2016,df)
FY16_Jun = custom_filter('month','year',6,2016,df)
FY16_Jul = custom_filter('month','year',7,2016,df)
FY16_Aug = custom_filter('month','year',8,2016,df)

FY20_Sep = custom_filter('month','year',9,2019,df)
FY20_Oct = custom_filter('month','year',10,2019,df)
FY20_Nov = custom_filter('month','year',11,2019,df)
FY20_Dec = custom_filter('month','year',12,2019,df)
FY20_Jan = custom_filter('month','year',1,2020,df)
FY20_Feb = custom_filter('month','year',2,2020,df)
FY20_Mar = custom_filter('month','year',3,2020,df)

#print(FY20_Mar.head())


# In[672]:


FY17_Sep = single_variable_output('FY17_Sep')
FY17_Oct = single_variable_output('FY17_Oct')
FY17_Nov = single_variable_output('FY17_Nov')
FY17_Dec = single_variable_output('FY17_Dec')
FY17_Jan = single_variable_output('FY17_Jan')
FY17_Feb = single_variable_output('FY17_Feb')
FY17_Mar = single_variable_output('FY17_Mar')
FY17_Apr = single_variable_output('FY17_Apr')
FY17_May = single_variable_output('FY17_May')
FY17_Jun = single_variable_output('FY17_Jun')
FY17_Jul = single_variable_output('FY17_Jul')
FY17_Aug = single_variable_output('FY17_Aug')

FY18_Sep = single_variable_output('FY18_Sep')
FY18_Oct = single_variable_output('FY18_Oct')
FY18_Nov = single_variable_output('FY18_Nov')
FY18_Dec = single_variable_output('FY18_Dec')
FY18_Jan = single_variable_output('FY18_Jan')
FY18_Feb = single_variable_output('FY18_Feb')
FY18_Mar = single_variable_output('FY18_Mar')
FY18_Apr = single_variable_output('FY18_Apr')
FY18_May = single_variable_output('FY18_May')
FY18_Jun = single_variable_output('FY18_Jun')
FY18_Jul = single_variable_output('FY18_Jul')
FY18_Aug = single_variable_output('FY18_Aug')

FY19_Sep = single_variable_output('FY19_Sep')
FY19_Oct = single_variable_output('FY19_Oct')
FY19_Nov = single_variable_output('FY19_Nov')
FY19_Dec = single_variable_output('FY19_Dec')
FY19_Jan = single_variable_output('FY19_Jan')
FY19_Feb = single_variable_output('FY19_Feb')
FY19_Mar = single_variable_output('FY19_Mar')
FY19_Apr = single_variable_output('FY19_Apr')
FY19_May = single_variable_output('FY19_May')
FY19_Jun = single_variable_output('FY19_Jun')
FY19_Jul = single_variable_output('FY19_Jul')
FY19_Aug = single_variable_output('FY19_Aug')


# In[673]:


FY16['Q00. Weighted Score'] = saurav(FY16['NUMBER OF RESPONDENTS FOR THE WORKGROUP (N SIZE)'],FY16['Q00.  Overall Satisfaction. (MEAN SCORE)'])
FY16['Q01. Weighted Score'] = saurav(FY16['NUMBER OF RESPONDENTS FOR THE WORKGROUP (N SIZE)'],FY16['Q01.  Know What\'s Expected. (MEAN SCORE)'])
FY16['Q02. Weighted Score'] = saurav(FY16['NUMBER OF RESPONDENTS FOR THE WORKGROUP (N SIZE)'],FY16['Q02.  Materials and Equipment. (MEAN SCORE)'])
FY16['Q03. Weighted Score'] = saurav(FY16['NUMBER OF RESPONDENTS FOR THE WORKGROUP (N SIZE)'],FY16['Q03.  Opportunity to do Best. (MEAN SCORE)'])
FY16['Q04. Weighted Score'] = saurav(FY16['NUMBER OF RESPONDENTS FOR THE WORKGROUP (N SIZE)'],FY16['Q04.  Recognition. (MEAN SCORE)'])
FY16['Q05. Weighted Score'] = saurav(FY16['NUMBER OF RESPONDENTS FOR THE WORKGROUP (N SIZE)'],FY16['Q05.  Cares About Me. (MEAN SCORE)'])
FY16['Q06. Weighted Score'] = saurav(FY16['NUMBER OF RESPONDENTS FOR THE WORKGROUP (N SIZE)'],FY16['Q06.  Development. (MEAN SCORE)'])
FY16['Q07. Weighted Score'] = saurav(FY16['NUMBER OF RESPONDENTS FOR THE WORKGROUP (N SIZE)'],FY16['Q07.  Opinions Count. (MEAN SCORE)'])
FY16['Q08. Weighted Score'] = saurav(FY16['NUMBER OF RESPONDENTS FOR THE WORKGROUP (N SIZE)'],FY16['Q08.  Mission/Purpose. (MEAN SCORE)'])
FY16['Q09. Weighted Score'] = saurav(FY16['NUMBER OF RESPONDENTS FOR THE WORKGROUP (N SIZE)'],FY16['Q09.  Committed to Quality. (MEAN SCORE)'])
FY16['Q10. Weighted Score'] = saurav(FY16['NUMBER OF RESPONDENTS FOR THE WORKGROUP (N SIZE)'],FY16['Q10.  Best Friend. (MEAN SCORE)'])
FY16['Q11. Weighted Score'] = saurav(FY16['NUMBER OF RESPONDENTS FOR THE WORKGROUP (N SIZE)'],FY16['Q11.  Progress. (MEAN SCORE)'])
FY16['Q12. Weighted Score'] = saurav(FY16['NUMBER OF RESPONDENTS FOR THE WORKGROUP (N SIZE)'],FY16['Q12.  Learn and Grow. (MEAN SCORE)'])

FY16_Avg_N_Size_Q00 = sum(vaibhav(FY16,'NUMBER OF RESPONDENTS FOR THE WORKGROUP (N SIZE)','Q00.  Overall Satisfaction. (MEAN SCORE)'))
FY16_Avg_N_Size_Q01 = sum(vaibhav(FY16,'NUMBER OF RESPONDENTS FOR THE WORKGROUP (N SIZE)','Q01.  Know What\'s Expected. (MEAN SCORE)'))
FY16_Avg_N_Size_Q02 = sum(vaibhav(FY16,'NUMBER OF RESPONDENTS FOR THE WORKGROUP (N SIZE)','Q02.  Materials and Equipment. (MEAN SCORE)'))
FY16_Avg_N_Size_Q03 = sum(vaibhav(FY16,'NUMBER OF RESPONDENTS FOR THE WORKGROUP (N SIZE)','Q03.  Opportunity to do Best. (MEAN SCORE)'))
FY16_Avg_N_Size_Q04 = sum(vaibhav(FY16,'NUMBER OF RESPONDENTS FOR THE WORKGROUP (N SIZE)','Q04.  Recognition. (MEAN SCORE)'))
FY16_Avg_N_Size_Q05 = sum(vaibhav(FY16,'NUMBER OF RESPONDENTS FOR THE WORKGROUP (N SIZE)','Q05.  Cares About Me. (MEAN SCORE)'))
FY16_Avg_N_Size_Q06 = sum(vaibhav(FY16,'NUMBER OF RESPONDENTS FOR THE WORKGROUP (N SIZE)','Q06.  Development. (MEAN SCORE)'))
FY16_Avg_N_Size_Q07 = sum(vaibhav(FY16,'NUMBER OF RESPONDENTS FOR THE WORKGROUP (N SIZE)','Q07.  Opinions Count. (MEAN SCORE)'))
FY16_Avg_N_Size_Q08 = sum(vaibhav(FY16,'NUMBER OF RESPONDENTS FOR THE WORKGROUP (N SIZE)','Q08.  Mission/Purpose. (MEAN SCORE)'))
FY16_Avg_N_Size_Q09 = sum(vaibhav(FY16,'NUMBER OF RESPONDENTS FOR THE WORKGROUP (N SIZE)','Q09.  Committed to Quality. (MEAN SCORE)'))
FY16_Avg_N_Size_Q10 = sum(vaibhav(FY16,'NUMBER OF RESPONDENTS FOR THE WORKGROUP (N SIZE)','Q10.  Best Friend. (MEAN SCORE)'))
FY16_Avg_N_Size_Q11 = sum(vaibhav(FY16,'NUMBER OF RESPONDENTS FOR THE WORKGROUP (N SIZE)','Q11.  Progress. (MEAN SCORE)'))
FY16_Avg_N_Size_Q12 = sum(vaibhav(FY16,'NUMBER OF RESPONDENTS FOR THE WORKGROUP (N SIZE)','Q12.  Learn and Grow. (MEAN SCORE)'))

FY16_Q00_Avg_Rating = sum(FY16['Q00. Weighted Score'])/FY16_Avg_N_Size_Q00
FY16_Q01_Avg_Rating = sum(FY16['Q01. Weighted Score'])/FY16_Avg_N_Size_Q01
FY16_Q02_Avg_Rating = sum(FY16['Q02. Weighted Score'])/FY16_Avg_N_Size_Q02
FY16_Q03_Avg_Rating = sum(FY16['Q03. Weighted Score'])/FY16_Avg_N_Size_Q03
FY16_Q04_Avg_Rating = sum(FY16['Q04. Weighted Score'])/FY16_Avg_N_Size_Q04
FY16_Q05_Avg_Rating = sum(FY16['Q05. Weighted Score'])/FY16_Avg_N_Size_Q05
FY16_Q06_Avg_Rating = sum(FY16['Q06. Weighted Score'])/FY16_Avg_N_Size_Q06
FY16_Q07_Avg_Rating = sum(FY16['Q07. Weighted Score'])/FY16_Avg_N_Size_Q07
FY16_Q08_Avg_Rating = sum(FY16['Q08. Weighted Score'])/FY16_Avg_N_Size_Q08
FY16_Q09_Avg_Rating = sum(FY16['Q09. Weighted Score'])/FY16_Avg_N_Size_Q09
FY16_Q10_Avg_Rating = sum(FY16['Q10. Weighted Score'])/FY16_Avg_N_Size_Q10
FY16_Q11_Avg_Rating = sum(FY16['Q11. Weighted Score'])/FY16_Avg_N_Size_Q11
FY16_Q12_Avg_Rating = sum(FY16['Q12. Weighted Score'])/FY16_Avg_N_Size_Q12

###########################################################################################################################

FY16_Apr['Q00. Weighted Score'] = saurav(FY16_Apr['NUMBER OF RESPONDENTS FOR THE WORKGROUP (N SIZE)'],FY16_Apr['Q00.  Overall Satisfaction. (MEAN SCORE)'])
FY16_Apr['Q01. Weighted Score'] = saurav(FY16_Apr['NUMBER OF RESPONDENTS FOR THE WORKGROUP (N SIZE)'],FY16_Apr['Q01.  Know What\'s Expected. (MEAN SCORE)'])
FY16_Apr['Q02. Weighted Score'] = saurav(FY16_Apr['NUMBER OF RESPONDENTS FOR THE WORKGROUP (N SIZE)'],FY16_Apr['Q02.  Materials and Equipment. (MEAN SCORE)'])
FY16_Apr['Q03. Weighted Score'] = saurav(FY16_Apr['NUMBER OF RESPONDENTS FOR THE WORKGROUP (N SIZE)'],FY16_Apr['Q03.  Opportunity to do Best. (MEAN SCORE)'])
FY16_Apr['Q04. Weighted Score'] = saurav(FY16_Apr['NUMBER OF RESPONDENTS FOR THE WORKGROUP (N SIZE)'],FY16_Apr['Q04.  Recognition. (MEAN SCORE)'])
FY16_Apr['Q05. Weighted Score'] = saurav(FY16_Apr['NUMBER OF RESPONDENTS FOR THE WORKGROUP (N SIZE)'],FY16_Apr['Q05.  Cares About Me. (MEAN SCORE)'])
FY16_Apr['Q06. Weighted Score'] = saurav(FY16_Apr['NUMBER OF RESPONDENTS FOR THE WORKGROUP (N SIZE)'],FY16_Apr['Q06.  Development. (MEAN SCORE)'])
FY16_Apr['Q07. Weighted Score'] = saurav(FY16_Apr['NUMBER OF RESPONDENTS FOR THE WORKGROUP (N SIZE)'],FY16_Apr['Q07.  Opinions Count. (MEAN SCORE)'])
FY16_Apr['Q08. Weighted Score'] = saurav(FY16_Apr['NUMBER OF RESPONDENTS FOR THE WORKGROUP (N SIZE)'],FY16_Apr['Q08.  Mission/Purpose. (MEAN SCORE)'])
FY16_Apr['Q09. Weighted Score'] = saurav(FY16_Apr['NUMBER OF RESPONDENTS FOR THE WORKGROUP (N SIZE)'],FY16_Apr['Q09.  Committed to Quality. (MEAN SCORE)'])
FY16_Apr['Q10. Weighted Score'] = saurav(FY16_Apr['NUMBER OF RESPONDENTS FOR THE WORKGROUP (N SIZE)'],FY16_Apr['Q10.  Best Friend. (MEAN SCORE)'])
FY16_Apr['Q11. Weighted Score'] = saurav(FY16_Apr['NUMBER OF RESPONDENTS FOR THE WORKGROUP (N SIZE)'],FY16_Apr['Q11.  Progress. (MEAN SCORE)'])
FY16_Apr['Q12. Weighted Score'] = saurav(FY16_Apr['NUMBER OF RESPONDENTS FOR THE WORKGROUP (N SIZE)'],FY16_Apr['Q12.  Learn and Grow. (MEAN SCORE)'])

FY16_Apr_Avg_N_Size_Q00 = sum(vaibhav(FY16_Apr,'NUMBER OF RESPONDENTS FOR THE WORKGROUP (N SIZE)','Q00.  Overall Satisfaction. (MEAN SCORE)'))
FY16_Apr_Avg_N_Size_Q01 = sum(vaibhav(FY16_Apr,'NUMBER OF RESPONDENTS FOR THE WORKGROUP (N SIZE)','Q01.  Know What\'s Expected. (MEAN SCORE)'))
FY16_Apr_Avg_N_Size_Q02 = sum(vaibhav(FY16_Apr,'NUMBER OF RESPONDENTS FOR THE WORKGROUP (N SIZE)','Q02.  Materials and Equipment. (MEAN SCORE)'))
FY16_Apr_Avg_N_Size_Q03 = sum(vaibhav(FY16_Apr,'NUMBER OF RESPONDENTS FOR THE WORKGROUP (N SIZE)','Q03.  Opportunity to do Best. (MEAN SCORE)'))
FY16_Apr_Avg_N_Size_Q04 = sum(vaibhav(FY16_Apr,'NUMBER OF RESPONDENTS FOR THE WORKGROUP (N SIZE)','Q04.  Recognition. (MEAN SCORE)'))
FY16_Apr_Avg_N_Size_Q05 = sum(vaibhav(FY16_Apr,'NUMBER OF RESPONDENTS FOR THE WORKGROUP (N SIZE)','Q05.  Cares About Me. (MEAN SCORE)'))
FY16_Apr_Avg_N_Size_Q06 = sum(vaibhav(FY16_Apr,'NUMBER OF RESPONDENTS FOR THE WORKGROUP (N SIZE)','Q06.  Development. (MEAN SCORE)'))
FY16_Apr_Avg_N_Size_Q07 = sum(vaibhav(FY16_Apr,'NUMBER OF RESPONDENTS FOR THE WORKGROUP (N SIZE)','Q07.  Opinions Count. (MEAN SCORE)'))
FY16_Apr_Avg_N_Size_Q08 = sum(vaibhav(FY16_Apr,'NUMBER OF RESPONDENTS FOR THE WORKGROUP (N SIZE)','Q08.  Mission/Purpose. (MEAN SCORE)'))
FY16_Apr_Avg_N_Size_Q09 = sum(vaibhav(FY16_Apr,'NUMBER OF RESPONDENTS FOR THE WORKGROUP (N SIZE)','Q09.  Committed to Quality. (MEAN SCORE)'))
FY16_Apr_Avg_N_Size_Q10 = sum(vaibhav(FY16_Apr,'NUMBER OF RESPONDENTS FOR THE WORKGROUP (N SIZE)','Q10.  Best Friend. (MEAN SCORE)'))
FY16_Apr_Avg_N_Size_Q11 = sum(vaibhav(FY16_Apr,'NUMBER OF RESPONDENTS FOR THE WORKGROUP (N SIZE)','Q11.  Progress. (MEAN SCORE)'))
FY16_Apr_Avg_N_Size_Q12 = sum(vaibhav(FY16_Apr,'NUMBER OF RESPONDENTS FOR THE WORKGROUP (N SIZE)','Q12.  Learn and Grow. (MEAN SCORE)'))

FY16_Apr_Q00_Avg_Rating = sum(FY16_Apr['Q00. Weighted Score'])/FY16_Apr_Avg_N_Size_Q00
FY16_Apr_Q01_Avg_Rating = sum(FY16_Apr['Q01. Weighted Score'])/FY16_Apr_Avg_N_Size_Q01
FY16_Apr_Q02_Avg_Rating = sum(FY16_Apr['Q02. Weighted Score'])/FY16_Apr_Avg_N_Size_Q02
FY16_Apr_Q03_Avg_Rating = sum(FY16_Apr['Q03. Weighted Score'])/FY16_Apr_Avg_N_Size_Q03
FY16_Apr_Q04_Avg_Rating = sum(FY16_Apr['Q04. Weighted Score'])/FY16_Apr_Avg_N_Size_Q04
FY16_Apr_Q05_Avg_Rating = sum(FY16_Apr['Q05. Weighted Score'])/FY16_Apr_Avg_N_Size_Q05
FY16_Apr_Q06_Avg_Rating = sum(FY16_Apr['Q06. Weighted Score'])/FY16_Apr_Avg_N_Size_Q06
FY16_Apr_Q07_Avg_Rating = sum(FY16_Apr['Q07. Weighted Score'])/FY16_Apr_Avg_N_Size_Q07
FY16_Apr_Q08_Avg_Rating = sum(FY16_Apr['Q08. Weighted Score'])/FY16_Apr_Avg_N_Size_Q08
FY16_Apr_Q09_Avg_Rating = sum(FY16_Apr['Q09. Weighted Score'])/FY16_Apr_Avg_N_Size_Q09
FY16_Apr_Q10_Avg_Rating = sum(FY16_Apr['Q10. Weighted Score'])/FY16_Apr_Avg_N_Size_Q10
FY16_Apr_Q11_Avg_Rating = sum(FY16_Apr['Q11. Weighted Score'])/FY16_Apr_Avg_N_Size_Q11
FY16_Apr_Q12_Avg_Rating = sum(FY16_Apr['Q12. Weighted Score'])/FY16_Apr_Avg_N_Size_Q12

###########################################################################################################################

FY16_May['Q00. Weighted Score'] = saurav(FY16_May['NUMBER OF RESPONDENTS FOR THE WORKGROUP (N SIZE)'],FY16_May['Q00.  Overall Satisfaction. (MEAN SCORE)'])
FY16_May['Q01. Weighted Score'] = saurav(FY16_May['NUMBER OF RESPONDENTS FOR THE WORKGROUP (N SIZE)'],FY16_May['Q01.  Know What\'s Expected. (MEAN SCORE)'])
FY16_May['Q02. Weighted Score'] = saurav(FY16_May['NUMBER OF RESPONDENTS FOR THE WORKGROUP (N SIZE)'],FY16_May['Q02.  Materials and Equipment. (MEAN SCORE)'])
FY16_May['Q03. Weighted Score'] = saurav(FY16_May['NUMBER OF RESPONDENTS FOR THE WORKGROUP (N SIZE)'],FY16_May['Q03.  Opportunity to do Best. (MEAN SCORE)'])
FY16_May['Q04. Weighted Score'] = saurav(FY16_May['NUMBER OF RESPONDENTS FOR THE WORKGROUP (N SIZE)'],FY16_May['Q04.  Recognition. (MEAN SCORE)'])
FY16_May['Q05. Weighted Score'] = saurav(FY16_May['NUMBER OF RESPONDENTS FOR THE WORKGROUP (N SIZE)'],FY16_May['Q05.  Cares About Me. (MEAN SCORE)'])
FY16_May['Q06. Weighted Score'] = saurav(FY16_May['NUMBER OF RESPONDENTS FOR THE WORKGROUP (N SIZE)'],FY16_May['Q06.  Development. (MEAN SCORE)'])
FY16_May['Q07. Weighted Score'] = saurav(FY16_May['NUMBER OF RESPONDENTS FOR THE WORKGROUP (N SIZE)'],FY16_May['Q07.  Opinions Count. (MEAN SCORE)'])
FY16_May['Q08. Weighted Score'] = saurav(FY16_May['NUMBER OF RESPONDENTS FOR THE WORKGROUP (N SIZE)'],FY16_May['Q08.  Mission/Purpose. (MEAN SCORE)'])
FY16_May['Q09. Weighted Score'] = saurav(FY16_May['NUMBER OF RESPONDENTS FOR THE WORKGROUP (N SIZE)'],FY16_May['Q09.  Committed to Quality. (MEAN SCORE)'])
FY16_May['Q10. Weighted Score'] = saurav(FY16_May['NUMBER OF RESPONDENTS FOR THE WORKGROUP (N SIZE)'],FY16_May['Q10.  Best Friend. (MEAN SCORE)'])
FY16_May['Q11. Weighted Score'] = saurav(FY16_May['NUMBER OF RESPONDENTS FOR THE WORKGROUP (N SIZE)'],FY16_May['Q11.  Progress. (MEAN SCORE)'])
FY16_May['Q12. Weighted Score'] = saurav(FY16_May['NUMBER OF RESPONDENTS FOR THE WORKGROUP (N SIZE)'],FY16_May['Q12.  Learn and Grow. (MEAN SCORE)'])

FY16_May_Avg_N_Size_Q00 = sum(vaibhav(FY16_May,'NUMBER OF RESPONDENTS FOR THE WORKGROUP (N SIZE)','Q00.  Overall Satisfaction. (MEAN SCORE)'))
FY16_May_Avg_N_Size_Q01 = sum(vaibhav(FY16_May,'NUMBER OF RESPONDENTS FOR THE WORKGROUP (N SIZE)','Q01.  Know What\'s Expected. (MEAN SCORE)'))
FY16_May_Avg_N_Size_Q02 = sum(vaibhav(FY16_May,'NUMBER OF RESPONDENTS FOR THE WORKGROUP (N SIZE)','Q02.  Materials and Equipment. (MEAN SCORE)'))
FY16_May_Avg_N_Size_Q03 = sum(vaibhav(FY16_May,'NUMBER OF RESPONDENTS FOR THE WORKGROUP (N SIZE)','Q03.  Opportunity to do Best. (MEAN SCORE)'))
FY16_May_Avg_N_Size_Q04 = sum(vaibhav(FY16_May,'NUMBER OF RESPONDENTS FOR THE WORKGROUP (N SIZE)','Q04.  Recognition. (MEAN SCORE)'))
FY16_May_Avg_N_Size_Q05 = sum(vaibhav(FY16_May,'NUMBER OF RESPONDENTS FOR THE WORKGROUP (N SIZE)','Q05.  Cares About Me. (MEAN SCORE)'))
FY16_May_Avg_N_Size_Q06 = sum(vaibhav(FY16_May,'NUMBER OF RESPONDENTS FOR THE WORKGROUP (N SIZE)','Q06.  Development. (MEAN SCORE)'))
FY16_May_Avg_N_Size_Q07 = sum(vaibhav(FY16_May,'NUMBER OF RESPONDENTS FOR THE WORKGROUP (N SIZE)','Q07.  Opinions Count. (MEAN SCORE)'))
FY16_May_Avg_N_Size_Q08 = sum(vaibhav(FY16_May,'NUMBER OF RESPONDENTS FOR THE WORKGROUP (N SIZE)','Q08.  Mission/Purpose. (MEAN SCORE)'))
FY16_May_Avg_N_Size_Q09 = sum(vaibhav(FY16_May,'NUMBER OF RESPONDENTS FOR THE WORKGROUP (N SIZE)','Q09.  Committed to Quality. (MEAN SCORE)'))
FY16_May_Avg_N_Size_Q10 = sum(vaibhav(FY16_May,'NUMBER OF RESPONDENTS FOR THE WORKGROUP (N SIZE)','Q10.  Best Friend. (MEAN SCORE)'))
FY16_May_Avg_N_Size_Q11 = sum(vaibhav(FY16_May,'NUMBER OF RESPONDENTS FOR THE WORKGROUP (N SIZE)','Q11.  Progress. (MEAN SCORE)'))
FY16_May_Avg_N_Size_Q12 = sum(vaibhav(FY16_May,'NUMBER OF RESPONDENTS FOR THE WORKGROUP (N SIZE)','Q12.  Learn and Grow. (MEAN SCORE)'))

FY16_May_Q00_Avg_Rating = sum(FY16_May['Q00. Weighted Score'])/FY16_May_Avg_N_Size_Q00
FY16_May_Q01_Avg_Rating = sum(FY16_May['Q01. Weighted Score'])/FY16_May_Avg_N_Size_Q01
FY16_May_Q02_Avg_Rating = sum(FY16_May['Q02. Weighted Score'])/FY16_May_Avg_N_Size_Q02
FY16_May_Q03_Avg_Rating = sum(FY16_May['Q03. Weighted Score'])/FY16_May_Avg_N_Size_Q03
FY16_May_Q04_Avg_Rating = sum(FY16_May['Q04. Weighted Score'])/FY16_May_Avg_N_Size_Q04
FY16_May_Q05_Avg_Rating = sum(FY16_May['Q05. Weighted Score'])/FY16_May_Avg_N_Size_Q05
FY16_May_Q06_Avg_Rating = sum(FY16_May['Q06. Weighted Score'])/FY16_May_Avg_N_Size_Q06
FY16_May_Q07_Avg_Rating = sum(FY16_May['Q07. Weighted Score'])/FY16_May_Avg_N_Size_Q07
FY16_May_Q08_Avg_Rating = sum(FY16_May['Q08. Weighted Score'])/FY16_May_Avg_N_Size_Q08
FY16_May_Q09_Avg_Rating = sum(FY16_May['Q09. Weighted Score'])/FY16_May_Avg_N_Size_Q09
FY16_May_Q10_Avg_Rating = sum(FY16_May['Q10. Weighted Score'])/FY16_May_Avg_N_Size_Q10
FY16_May_Q11_Avg_Rating = sum(FY16_May['Q11. Weighted Score'])/FY16_May_Avg_N_Size_Q11
FY16_May_Q12_Avg_Rating = sum(FY16_May['Q12. Weighted Score'])/FY16_May_Avg_N_Size_Q12

###########################################################################################################################

FY16_Jun['Q00. Weighted Score'] = saurav(FY16_Jun['NUMBER OF RESPONDENTS FOR THE WORKGROUP (N SIZE)'],FY16_Jun['Q00.  Overall Satisfaction. (MEAN SCORE)'])
FY16_Jun['Q01. Weighted Score'] = saurav(FY16_Jun['NUMBER OF RESPONDENTS FOR THE WORKGROUP (N SIZE)'],FY16_Jun['Q01.  Know What\'s Expected. (MEAN SCORE)'])
FY16_Jun['Q02. Weighted Score'] = saurav(FY16_Jun['NUMBER OF RESPONDENTS FOR THE WORKGROUP (N SIZE)'],FY16_Jun['Q02.  Materials and Equipment. (MEAN SCORE)'])
FY16_Jun['Q03. Weighted Score'] = saurav(FY16_Jun['NUMBER OF RESPONDENTS FOR THE WORKGROUP (N SIZE)'],FY16_Jun['Q03.  Opportunity to do Best. (MEAN SCORE)'])
FY16_Jun['Q04. Weighted Score'] = saurav(FY16_Jun['NUMBER OF RESPONDENTS FOR THE WORKGROUP (N SIZE)'],FY16_Jun['Q04.  Recognition. (MEAN SCORE)'])
FY16_Jun['Q05. Weighted Score'] = saurav(FY16_Jun['NUMBER OF RESPONDENTS FOR THE WORKGROUP (N SIZE)'],FY16_Jun['Q05.  Cares About Me. (MEAN SCORE)'])
FY16_Jun['Q06. Weighted Score'] = saurav(FY16_Jun['NUMBER OF RESPONDENTS FOR THE WORKGROUP (N SIZE)'],FY16_Jun['Q06.  Development. (MEAN SCORE)'])
FY16_Jun['Q07. Weighted Score'] = saurav(FY16_Jun['NUMBER OF RESPONDENTS FOR THE WORKGROUP (N SIZE)'],FY16_Jun['Q07.  Opinions Count. (MEAN SCORE)'])
FY16_Jun['Q08. Weighted Score'] = saurav(FY16_Jun['NUMBER OF RESPONDENTS FOR THE WORKGROUP (N SIZE)'],FY16_Jun['Q08.  Mission/Purpose. (MEAN SCORE)'])
FY16_Jun['Q09. Weighted Score'] = saurav(FY16_Jun['NUMBER OF RESPONDENTS FOR THE WORKGROUP (N SIZE)'],FY16_Jun['Q09.  Committed to Quality. (MEAN SCORE)'])
FY16_Jun['Q10. Weighted Score'] = saurav(FY16_Jun['NUMBER OF RESPONDENTS FOR THE WORKGROUP (N SIZE)'],FY16_Jun['Q10.  Best Friend. (MEAN SCORE)'])
FY16_Jun['Q11. Weighted Score'] = saurav(FY16_Jun['NUMBER OF RESPONDENTS FOR THE WORKGROUP (N SIZE)'],FY16_Jun['Q11.  Progress. (MEAN SCORE)'])
FY16_Jun['Q12. Weighted Score'] = saurav(FY16_Jun['NUMBER OF RESPONDENTS FOR THE WORKGROUP (N SIZE)'],FY16_Jun['Q12.  Learn and Grow. (MEAN SCORE)'])

FY16_Jun_Avg_N_Size_Q00 = sum(vaibhav(FY16_Jun,'NUMBER OF RESPONDENTS FOR THE WORKGROUP (N SIZE)','Q00.  Overall Satisfaction. (MEAN SCORE)'))
FY16_Jun_Avg_N_Size_Q01 = sum(vaibhav(FY16_Jun,'NUMBER OF RESPONDENTS FOR THE WORKGROUP (N SIZE)','Q01.  Know What\'s Expected. (MEAN SCORE)'))
FY16_Jun_Avg_N_Size_Q02 = sum(vaibhav(FY16_Jun,'NUMBER OF RESPONDENTS FOR THE WORKGROUP (N SIZE)','Q02.  Materials and Equipment. (MEAN SCORE)'))
FY16_Jun_Avg_N_Size_Q03 = sum(vaibhav(FY16_Jun,'NUMBER OF RESPONDENTS FOR THE WORKGROUP (N SIZE)','Q03.  Opportunity to do Best. (MEAN SCORE)'))
FY16_Jun_Avg_N_Size_Q04 = sum(vaibhav(FY16_Jun,'NUMBER OF RESPONDENTS FOR THE WORKGROUP (N SIZE)','Q04.  Recognition. (MEAN SCORE)'))
FY16_Jun_Avg_N_Size_Q05 = sum(vaibhav(FY16_Jun,'NUMBER OF RESPONDENTS FOR THE WORKGROUP (N SIZE)','Q05.  Cares About Me. (MEAN SCORE)'))
FY16_Jun_Avg_N_Size_Q06 = sum(vaibhav(FY16_Jun,'NUMBER OF RESPONDENTS FOR THE WORKGROUP (N SIZE)','Q06.  Development. (MEAN SCORE)'))
FY16_Jun_Avg_N_Size_Q07 = sum(vaibhav(FY16_Jun,'NUMBER OF RESPONDENTS FOR THE WORKGROUP (N SIZE)','Q07.  Opinions Count. (MEAN SCORE)'))
FY16_Jun_Avg_N_Size_Q08 = sum(vaibhav(FY16_Jun,'NUMBER OF RESPONDENTS FOR THE WORKGROUP (N SIZE)','Q08.  Mission/Purpose. (MEAN SCORE)'))
FY16_Jun_Avg_N_Size_Q09 = sum(vaibhav(FY16_Jun,'NUMBER OF RESPONDENTS FOR THE WORKGROUP (N SIZE)','Q09.  Committed to Quality. (MEAN SCORE)'))
FY16_Jun_Avg_N_Size_Q10 = sum(vaibhav(FY16_Jun,'NUMBER OF RESPONDENTS FOR THE WORKGROUP (N SIZE)','Q10.  Best Friend. (MEAN SCORE)'))
FY16_Jun_Avg_N_Size_Q11 = sum(vaibhav(FY16_Jun,'NUMBER OF RESPONDENTS FOR THE WORKGROUP (N SIZE)','Q11.  Progress. (MEAN SCORE)'))
FY16_Jun_Avg_N_Size_Q12 = sum(vaibhav(FY16_Jun,'NUMBER OF RESPONDENTS FOR THE WORKGROUP (N SIZE)','Q12.  Learn and Grow. (MEAN SCORE)'))

FY16_Jun_Q00_Avg_Rating = sum(FY16_Jun['Q00. Weighted Score'])/FY16_Jun_Avg_N_Size_Q00
FY16_Jun_Q01_Avg_Rating = sum(FY16_Jun['Q01. Weighted Score'])/FY16_Jun_Avg_N_Size_Q01
FY16_Jun_Q02_Avg_Rating = sum(FY16_Jun['Q02. Weighted Score'])/FY16_Jun_Avg_N_Size_Q02
FY16_Jun_Q03_Avg_Rating = sum(FY16_Jun['Q03. Weighted Score'])/FY16_Jun_Avg_N_Size_Q03
FY16_Jun_Q04_Avg_Rating = sum(FY16_Jun['Q04. Weighted Score'])/FY16_Jun_Avg_N_Size_Q04
FY16_Jun_Q05_Avg_Rating = sum(FY16_Jun['Q05. Weighted Score'])/FY16_Jun_Avg_N_Size_Q05
FY16_Jun_Q06_Avg_Rating = sum(FY16_Jun['Q06. Weighted Score'])/FY16_Jun_Avg_N_Size_Q06
FY16_Jun_Q07_Avg_Rating = sum(FY16_Jun['Q07. Weighted Score'])/FY16_Jun_Avg_N_Size_Q07
FY16_Jun_Q08_Avg_Rating = sum(FY16_Jun['Q08. Weighted Score'])/FY16_Jun_Avg_N_Size_Q08
FY16_Jun_Q09_Avg_Rating = sum(FY16_Jun['Q09. Weighted Score'])/FY16_Jun_Avg_N_Size_Q09
FY16_Jun_Q10_Avg_Rating = sum(FY16_Jun['Q10. Weighted Score'])/FY16_Jun_Avg_N_Size_Q10
FY16_Jun_Q11_Avg_Rating = sum(FY16_Jun['Q11. Weighted Score'])/FY16_Jun_Avg_N_Size_Q11
FY16_Jun_Q12_Avg_Rating = sum(FY16_Jun['Q12. Weighted Score'])/FY16_Jun_Avg_N_Size_Q12

###########################################################################################################################

FY16_Jul['Q00. Weighted Score'] = saurav(FY16_Jul['NUMBER OF RESPONDENTS FOR THE WORKGROUP (N SIZE)'],FY16_Jul['Q00.  Overall Satisfaction. (MEAN SCORE)'])
FY16_Jul['Q01. Weighted Score'] = saurav(FY16_Jul['NUMBER OF RESPONDENTS FOR THE WORKGROUP (N SIZE)'],FY16_Jul['Q01.  Know What\'s Expected. (MEAN SCORE)'])
FY16_Jul['Q02. Weighted Score'] = saurav(FY16_Jul['NUMBER OF RESPONDENTS FOR THE WORKGROUP (N SIZE)'],FY16_Jul['Q02.  Materials and Equipment. (MEAN SCORE)'])
FY16_Jul['Q03. Weighted Score'] = saurav(FY16_Jul['NUMBER OF RESPONDENTS FOR THE WORKGROUP (N SIZE)'],FY16_Jul['Q03.  Opportunity to do Best. (MEAN SCORE)'])
FY16_Jul['Q04. Weighted Score'] = saurav(FY16_Jul['NUMBER OF RESPONDENTS FOR THE WORKGROUP (N SIZE)'],FY16_Jul['Q04.  Recognition. (MEAN SCORE)'])
FY16_Jul['Q05. Weighted Score'] = saurav(FY16_Jul['NUMBER OF RESPONDENTS FOR THE WORKGROUP (N SIZE)'],FY16_Jul['Q05.  Cares About Me. (MEAN SCORE)'])
FY16_Jul['Q06. Weighted Score'] = saurav(FY16_Jul['NUMBER OF RESPONDENTS FOR THE WORKGROUP (N SIZE)'],FY16_Jul['Q06.  Development. (MEAN SCORE)'])
FY16_Jul['Q07. Weighted Score'] = saurav(FY16_Jul['NUMBER OF RESPONDENTS FOR THE WORKGROUP (N SIZE)'],FY16_Jul['Q07.  Opinions Count. (MEAN SCORE)'])
FY16_Jul['Q08. Weighted Score'] = saurav(FY16_Jul['NUMBER OF RESPONDENTS FOR THE WORKGROUP (N SIZE)'],FY16_Jul['Q08.  Mission/Purpose. (MEAN SCORE)'])
FY16_Jul['Q09. Weighted Score'] = saurav(FY16_Jul['NUMBER OF RESPONDENTS FOR THE WORKGROUP (N SIZE)'],FY16_Jul['Q09.  Committed to Quality. (MEAN SCORE)'])
FY16_Jul['Q10. Weighted Score'] = saurav(FY16_Jul['NUMBER OF RESPONDENTS FOR THE WORKGROUP (N SIZE)'],FY16_Jul['Q10.  Best Friend. (MEAN SCORE)'])
FY16_Jul['Q11. Weighted Score'] = saurav(FY16_Jul['NUMBER OF RESPONDENTS FOR THE WORKGROUP (N SIZE)'],FY16_Jul['Q11.  Progress. (MEAN SCORE)'])
FY16_Jul['Q12. Weighted Score'] = saurav(FY16_Jul['NUMBER OF RESPONDENTS FOR THE WORKGROUP (N SIZE)'],FY16_Jul['Q12.  Learn and Grow. (MEAN SCORE)'])

FY16_Jul_Avg_N_Size_Q00 = sum(vaibhav(FY16_Jul,'NUMBER OF RESPONDENTS FOR THE WORKGROUP (N SIZE)','Q00.  Overall Satisfaction. (MEAN SCORE)'))
FY16_Jul_Avg_N_Size_Q01 = sum(vaibhav(FY16_Jul,'NUMBER OF RESPONDENTS FOR THE WORKGROUP (N SIZE)','Q01.  Know What\'s Expected. (MEAN SCORE)'))
FY16_Jul_Avg_N_Size_Q02 = sum(vaibhav(FY16_Jul,'NUMBER OF RESPONDENTS FOR THE WORKGROUP (N SIZE)','Q02.  Materials and Equipment. (MEAN SCORE)'))
FY16_Jul_Avg_N_Size_Q03 = sum(vaibhav(FY16_Jul,'NUMBER OF RESPONDENTS FOR THE WORKGROUP (N SIZE)','Q03.  Opportunity to do Best. (MEAN SCORE)'))
FY16_Jul_Avg_N_Size_Q04 = sum(vaibhav(FY16_Jul,'NUMBER OF RESPONDENTS FOR THE WORKGROUP (N SIZE)','Q04.  Recognition. (MEAN SCORE)'))
FY16_Jul_Avg_N_Size_Q05 = sum(vaibhav(FY16_Jul,'NUMBER OF RESPONDENTS FOR THE WORKGROUP (N SIZE)','Q05.  Cares About Me. (MEAN SCORE)'))
FY16_Jul_Avg_N_Size_Q06 = sum(vaibhav(FY16_Jul,'NUMBER OF RESPONDENTS FOR THE WORKGROUP (N SIZE)','Q06.  Development. (MEAN SCORE)'))
FY16_Jul_Avg_N_Size_Q07 = sum(vaibhav(FY16_Jul,'NUMBER OF RESPONDENTS FOR THE WORKGROUP (N SIZE)','Q07.  Opinions Count. (MEAN SCORE)'))
FY16_Jul_Avg_N_Size_Q08 = sum(vaibhav(FY16_Jul,'NUMBER OF RESPONDENTS FOR THE WORKGROUP (N SIZE)','Q08.  Mission/Purpose. (MEAN SCORE)'))
FY16_Jul_Avg_N_Size_Q09 = sum(vaibhav(FY16_Jul,'NUMBER OF RESPONDENTS FOR THE WORKGROUP (N SIZE)','Q09.  Committed to Quality. (MEAN SCORE)'))
FY16_Jul_Avg_N_Size_Q10 = sum(vaibhav(FY16_Jul,'NUMBER OF RESPONDENTS FOR THE WORKGROUP (N SIZE)','Q10.  Best Friend. (MEAN SCORE)'))
FY16_Jul_Avg_N_Size_Q11 = sum(vaibhav(FY16_Jul,'NUMBER OF RESPONDENTS FOR THE WORKGROUP (N SIZE)','Q11.  Progress. (MEAN SCORE)'))
FY16_Jul_Avg_N_Size_Q12 = sum(vaibhav(FY16_Jul,'NUMBER OF RESPONDENTS FOR THE WORKGROUP (N SIZE)','Q12.  Learn and Grow. (MEAN SCORE)'))

FY16_Jul_Q00_Avg_Rating = sum(FY16_Jul['Q00. Weighted Score'])/FY16_Jul_Avg_N_Size_Q00
FY16_Jul_Q01_Avg_Rating = sum(FY16_Jul['Q01. Weighted Score'])/FY16_Jul_Avg_N_Size_Q01
FY16_Jul_Q02_Avg_Rating = sum(FY16_Jul['Q02. Weighted Score'])/FY16_Jul_Avg_N_Size_Q02
FY16_Jul_Q03_Avg_Rating = sum(FY16_Jul['Q03. Weighted Score'])/FY16_Jul_Avg_N_Size_Q03
FY16_Jul_Q04_Avg_Rating = sum(FY16_Jul['Q04. Weighted Score'])/FY16_Jul_Avg_N_Size_Q04
FY16_Jul_Q05_Avg_Rating = sum(FY16_Jul['Q05. Weighted Score'])/FY16_Jul_Avg_N_Size_Q05
FY16_Jul_Q06_Avg_Rating = sum(FY16_Jul['Q06. Weighted Score'])/FY16_Jul_Avg_N_Size_Q06
FY16_Jul_Q07_Avg_Rating = sum(FY16_Jul['Q07. Weighted Score'])/FY16_Jul_Avg_N_Size_Q07
FY16_Jul_Q08_Avg_Rating = sum(FY16_Jul['Q08. Weighted Score'])/FY16_Jul_Avg_N_Size_Q08
FY16_Jul_Q09_Avg_Rating = sum(FY16_Jul['Q09. Weighted Score'])/FY16_Jul_Avg_N_Size_Q09
FY16_Jul_Q10_Avg_Rating = sum(FY16_Jul['Q10. Weighted Score'])/FY16_Jul_Avg_N_Size_Q10
FY16_Jul_Q11_Avg_Rating = sum(FY16_Jul['Q11. Weighted Score'])/FY16_Jul_Avg_N_Size_Q11
FY16_Jul_Q12_Avg_Rating = sum(FY16_Jul['Q12. Weighted Score'])/FY16_Jul_Avg_N_Size_Q12

###########################################################################################################################

FY16_Aug['Q00. Weighted Score'] = saurav(FY16_Aug['NUMBER OF RESPONDENTS FOR THE WORKGROUP (N SIZE)'],FY16_Aug['Q00.  Overall Satisfaction. (MEAN SCORE)'])
FY16_Aug['Q01. Weighted Score'] = saurav(FY16_Aug['NUMBER OF RESPONDENTS FOR THE WORKGROUP (N SIZE)'],FY16_Aug['Q01.  Know What\'s Expected. (MEAN SCORE)'])
FY16_Aug['Q02. Weighted Score'] = saurav(FY16_Aug['NUMBER OF RESPONDENTS FOR THE WORKGROUP (N SIZE)'],FY16_Aug['Q02.  Materials and Equipment. (MEAN SCORE)'])
FY16_Aug['Q03. Weighted Score'] = saurav(FY16_Aug['NUMBER OF RESPONDENTS FOR THE WORKGROUP (N SIZE)'],FY16_Aug['Q03.  Opportunity to do Best. (MEAN SCORE)'])
FY16_Aug['Q04. Weighted Score'] = saurav(FY16_Aug['NUMBER OF RESPONDENTS FOR THE WORKGROUP (N SIZE)'],FY16_Aug['Q04.  Recognition. (MEAN SCORE)'])
FY16_Aug['Q05. Weighted Score'] = saurav(FY16_Aug['NUMBER OF RESPONDENTS FOR THE WORKGROUP (N SIZE)'],FY16_Aug['Q05.  Cares About Me. (MEAN SCORE)'])
FY16_Aug['Q06. Weighted Score'] = saurav(FY16_Aug['NUMBER OF RESPONDENTS FOR THE WORKGROUP (N SIZE)'],FY16_Aug['Q06.  Development. (MEAN SCORE)'])
FY16_Aug['Q07. Weighted Score'] = saurav(FY16_Aug['NUMBER OF RESPONDENTS FOR THE WORKGROUP (N SIZE)'],FY16_Aug['Q07.  Opinions Count. (MEAN SCORE)'])
FY16_Aug['Q08. Weighted Score'] = saurav(FY16_Aug['NUMBER OF RESPONDENTS FOR THE WORKGROUP (N SIZE)'],FY16_Aug['Q08.  Mission/Purpose. (MEAN SCORE)'])
FY16_Aug['Q09. Weighted Score'] = saurav(FY16_Aug['NUMBER OF RESPONDENTS FOR THE WORKGROUP (N SIZE)'],FY16_Aug['Q09.  Committed to Quality. (MEAN SCORE)'])
FY16_Aug['Q10. Weighted Score'] = saurav(FY16_Aug['NUMBER OF RESPONDENTS FOR THE WORKGROUP (N SIZE)'],FY16_Aug['Q10.  Best Friend. (MEAN SCORE)'])
FY16_Aug['Q11. Weighted Score'] = saurav(FY16_Aug['NUMBER OF RESPONDENTS FOR THE WORKGROUP (N SIZE)'],FY16_Aug['Q11.  Progress. (MEAN SCORE)'])
FY16_Aug['Q12. Weighted Score'] = saurav(FY16_Aug['NUMBER OF RESPONDENTS FOR THE WORKGROUP (N SIZE)'],FY16_Aug['Q12.  Learn and Grow. (MEAN SCORE)'])

FY16_Aug_Avg_N_Size_Q00 = sum(vaibhav(FY16_Aug,'NUMBER OF RESPONDENTS FOR THE WORKGROUP (N SIZE)','Q00.  Overall Satisfaction. (MEAN SCORE)'))
FY16_Aug_Avg_N_Size_Q01 = sum(vaibhav(FY16_Aug,'NUMBER OF RESPONDENTS FOR THE WORKGROUP (N SIZE)','Q01.  Know What\'s Expected. (MEAN SCORE)'))
FY16_Aug_Avg_N_Size_Q02 = sum(vaibhav(FY16_Aug,'NUMBER OF RESPONDENTS FOR THE WORKGROUP (N SIZE)','Q02.  Materials and Equipment. (MEAN SCORE)'))
FY16_Aug_Avg_N_Size_Q03 = sum(vaibhav(FY16_Aug,'NUMBER OF RESPONDENTS FOR THE WORKGROUP (N SIZE)','Q03.  Opportunity to do Best. (MEAN SCORE)'))
FY16_Aug_Avg_N_Size_Q04 = sum(vaibhav(FY16_Aug,'NUMBER OF RESPONDENTS FOR THE WORKGROUP (N SIZE)','Q04.  Recognition. (MEAN SCORE)'))
FY16_Aug_Avg_N_Size_Q05 = sum(vaibhav(FY16_Aug,'NUMBER OF RESPONDENTS FOR THE WORKGROUP (N SIZE)','Q05.  Cares About Me. (MEAN SCORE)'))
FY16_Aug_Avg_N_Size_Q06 = sum(vaibhav(FY16_Aug,'NUMBER OF RESPONDENTS FOR THE WORKGROUP (N SIZE)','Q06.  Development. (MEAN SCORE)'))
FY16_Aug_Avg_N_Size_Q07 = sum(vaibhav(FY16_Aug,'NUMBER OF RESPONDENTS FOR THE WORKGROUP (N SIZE)','Q07.  Opinions Count. (MEAN SCORE)'))
FY16_Aug_Avg_N_Size_Q08 = sum(vaibhav(FY16_Aug,'NUMBER OF RESPONDENTS FOR THE WORKGROUP (N SIZE)','Q08.  Mission/Purpose. (MEAN SCORE)'))
FY16_Aug_Avg_N_Size_Q09 = sum(vaibhav(FY16_Aug,'NUMBER OF RESPONDENTS FOR THE WORKGROUP (N SIZE)','Q09.  Committed to Quality. (MEAN SCORE)'))
FY16_Aug_Avg_N_Size_Q10 = sum(vaibhav(FY16_Aug,'NUMBER OF RESPONDENTS FOR THE WORKGROUP (N SIZE)','Q10.  Best Friend. (MEAN SCORE)'))
FY16_Aug_Avg_N_Size_Q11 = sum(vaibhav(FY16_Aug,'NUMBER OF RESPONDENTS FOR THE WORKGROUP (N SIZE)','Q11.  Progress. (MEAN SCORE)'))
FY16_Aug_Avg_N_Size_Q12 = sum(vaibhav(FY16_Aug,'NUMBER OF RESPONDENTS FOR THE WORKGROUP (N SIZE)','Q12.  Learn and Grow. (MEAN SCORE)'))

FY16_Aug_Q00_Avg_Rating = sum(FY16_Aug['Q00. Weighted Score'])/FY16_Aug_Avg_N_Size_Q00
FY16_Aug_Q01_Avg_Rating = sum(FY16_Aug['Q01. Weighted Score'])/FY16_Aug_Avg_N_Size_Q01
FY16_Aug_Q02_Avg_Rating = sum(FY16_Aug['Q02. Weighted Score'])/FY16_Aug_Avg_N_Size_Q02
FY16_Aug_Q03_Avg_Rating = sum(FY16_Aug['Q03. Weighted Score'])/FY16_Aug_Avg_N_Size_Q03
FY16_Aug_Q04_Avg_Rating = sum(FY16_Aug['Q04. Weighted Score'])/FY16_Aug_Avg_N_Size_Q04
FY16_Aug_Q05_Avg_Rating = sum(FY16_Aug['Q05. Weighted Score'])/FY16_Aug_Avg_N_Size_Q05
FY16_Aug_Q06_Avg_Rating = sum(FY16_Aug['Q06. Weighted Score'])/FY16_Aug_Avg_N_Size_Q06
FY16_Aug_Q07_Avg_Rating = sum(FY16_Aug['Q07. Weighted Score'])/FY16_Aug_Avg_N_Size_Q07
FY16_Aug_Q08_Avg_Rating = sum(FY16_Aug['Q08. Weighted Score'])/FY16_Aug_Avg_N_Size_Q08
FY16_Aug_Q09_Avg_Rating = sum(FY16_Aug['Q09. Weighted Score'])/FY16_Aug_Avg_N_Size_Q09
FY16_Aug_Q10_Avg_Rating = sum(FY16_Aug['Q10. Weighted Score'])/FY16_Aug_Avg_N_Size_Q10
FY16_Aug_Q11_Avg_Rating = sum(FY16_Aug['Q11. Weighted Score'])/FY16_Aug_Avg_N_Size_Q11
FY16_Aug_Q12_Avg_Rating = sum(FY16_Aug['Q12. Weighted Score'])/FY16_Aug_Avg_N_Size_Q12


# In[722]:


DTE_List = [df.DTE.unique()]

#a=["BlaBla Digital","BlaBla Operations","BlaBla Security","BlaBla Strategy","BlaBla Technology",
#"Capability Network","Communications, Media & Technology","Corporate Functions","Europe Market","Financial Services",
#"Global Technology","Growth Markets","Health & Public Service","North America Market","Other","Products","Resources"]
#for items in a:
 #   if((items in DTE_List).any):
  #      print(True)
   # else:
    #    print(False)
#print(type([df.DTE.unique()]))
#print(FY16.loc[df['DTE']=="BlaBla Digital"].head())
#df.columns.get_loc(col)

'''def dte_data(df,col,item,dte_list):
    if item in dte_list:
        return df.loc[df[col]==item]'''

def dte_data(df,col,item):
    return df.loc[df[col]==item]


# In[745]:


FY16_BlaBla_Digital = dte_data(FY16,'DTE','BlaBla Digital')
FY16_BlaBla_Operations = dte_data(FY16,'DTE','BlaBla Operations')
FY16_BlaBla_Security = dte_data(FY16,'DTE','BlaBla Security')
FY16_BlaBla_Strategy = dte_data(FY16,'DTE','BlaBla Strategy')
FY16_BlaBla_Technology = dte_data(FY16,'DTE','BlaBla Technology')
FY16_Capability_Network = dte_data(FY16,'DTE','Capability Network')
FY16_Communications_Media_Technology = dte_data(FY16,'DTE','Communications, Media & Technology')
FY16_Corporate_Functions = dte_data(FY16,'DTE','Corporate Functions')
FY16_Europe_Market = dte_data(FY16,'DTE','Europe_Market')
FY16_Financial_Services = dte_data(FY16,'DTE','Financial Services')
FY16_Global_Technology = dte_data(FY16,'DTE','Global Technology')
FY16_Growth_Markets = dte_data(FY16,'DTE','Growth_Markets')
FY16_Health_Public_Service = dte_data(FY16,'DTE','Health & Public Service')
FY16_North_America_Market = dte_data(FY16,'DTE','North_America_Market')
FY16_Other = dte_data(FY16,'DTE','Other')
FY16_Products = dte_data(FY16,'DTE','Products')
FY16_Resources = dte_data(FY16,'DTE','Resources')

FY16_Apr_BlaBla_Digital = dte_data(FY16_Apr,'DTE','BlaBla Digital')
FY16_Apr_BlaBla_Operations = dte_data(FY16_Apr,'DTE','BlaBla Operations')
FY16_Apr_BlaBla_Security = dte_data(FY16_Apr,'DTE','BlaBla Security')
FY16_Apr_BlaBla_Strategy = dte_data(FY16_Apr,'DTE','BlaBla Strategy')
FY16_Apr_BlaBla_Technology = dte_data(FY16_Apr,'DTE','BlaBla Technology')
FY16_Apr_Capability_Network = dte_data(FY16_Apr,'DTE','Capability Network')
FY16_Apr_Communications_Media_Technology = dte_data(FY16_Apr,'DTE','Communications, Media & Technology')
FY16_Apr_Corporate_Functions = dte_data(FY16_Apr,'DTE','Corporate Functions')
FY16_Apr_Europe_Market = dte_data(FY16_Apr,'DTE','Europe_Market')
FY16_Apr_Financial_Services = dte_data(FY16_Apr,'DTE','Financial Services')
FY16_Apr_Global_Technology = dte_data(FY16_Apr,'DTE','Global Technology')
FY16_Apr_Growth_Markets = dte_data(FY16_Apr,'DTE','Growth_Markets')
FY16_Apr_Health_Public_Service = dte_data(FY16_Apr,'DTE','Health & Public Service')
FY16_Apr_North_America_Market = dte_data(FY16_Apr,'DTE','North_America_Market')
FY16_Apr_Other = dte_data(FY16_Apr,'DTE','Other')
FY16_Apr_Products = dte_data(FY16_Apr,'DTE','Products')
FY16_Apr_Resources = dte_data(FY16_Apr,'DTE','Resources')

FY16_May_BlaBla_Digital = dte_data(FY16_May,'DTE','BlaBla Digital')
FY16_May_BlaBla_Operations = dte_data(FY16_May,'DTE','BlaBla Operations')
FY16_May_BlaBla_Security = dte_data(FY16_May,'DTE','BlaBla Security')
FY16_May_BlaBla_Strategy = dte_data(FY16_May,'DTE','BlaBla Strategy')
FY16_May_BlaBla_Technology = dte_data(FY16_May,'DTE','BlaBla Technology')
FY16_May_Capability_Network = dte_data(FY16_May,'DTE','Capability Network')
FY16_May_Communications_Media_Technology = dte_data(FY16_May,'DTE','Communications, Media & Technology')
FY16_May_Corporate_Functions = dte_data(FY16_May,'DTE','Corporate Functions')
FY16_May_Europe_Market = dte_data(FY16_May,'DTE','Europe_Market')
FY16_May_Financial_Services = dte_data(FY16_May,'DTE','Financial Services')
FY16_May_Global_Technology = dte_data(FY16_May,'DTE','Global Technology')
FY16_May_Growth_Markets = dte_data(FY16_May,'DTE','Growth_Markets')
FY16_May_Health_Public_Service = dte_data(FY16_May,'DTE','Health & Public Service')
FY16_May_North_America_Market = dte_data(FY16_May,'DTE','North_America_Market')
FY16_May_Other = dte_data(FY16_May,'DTE','Other')
FY16_May_Products = dte_data(FY16_May,'DTE','Products')
FY16_May_Resources = dte_data(FY16_May,'DTE','Resources')

FY16_Jun_BlaBla_Digital = dte_data(FY16_Jun,'DTE','BlaBla Digital')
FY16_Jun_BlaBla_Operations = dte_data(FY16_Jun,'DTE','BlaBla Operations')
FY16_Jun_BlaBla_Security = dte_data(FY16_Jun,'DTE','BlaBla Security')
FY16_Jun_BlaBla_Strategy = dte_data(FY16_Jun,'DTE','BlaBla Strategy')
FY16_Jun_BlaBla_Technology = dte_data(FY16_Jun,'DTE','BlaBla Technology')
FY16_Jun_Capability_Network = dte_data(FY16_Jun,'DTE','Capability Network')
FY16_Jun_Communications_Media_Technology = dte_data(FY16_Jun,'DTE','Communications, Media & Technology')
FY16_Jun_Corporate_Functions = dte_data(FY16_Jun,'DTE','Corporate Functions')
FY16_Jun_Europe_Market = dte_data(FY16_Jun,'DTE','Europe_Market')
FY16_Jun_Financial_Services = dte_data(FY16_Jun,'DTE','Financial Services')
FY16_Jun_Global_Technology = dte_data(FY16_Jun,'DTE','Global Technology')
FY16_Jun_Growth_Markets = dte_data(FY16_Jun,'DTE','Growth_Markets')
FY16_Jun_Health_Public_Service = dte_data(FY16_Jun,'DTE','Health & Public Service')
FY16_Jun_North_America_Market = dte_data(FY16_Jun,'DTE','North_America_Market')
FY16_Jun_Other = dte_data(FY16_Jun,'DTE','Other')
FY16_Jun_Products = dte_data(FY16_Jun,'DTE','Products')
FY16_Jun_Resources = dte_data(FY16_Jun,'DTE','Resources')

FY16_Jul_BlaBla_Digital = dte_data(FY16_Jul,'DTE','BlaBla Digital')
FY16_Jul_BlaBla_Operations = dte_data(FY16_Jul,'DTE','BlaBla Operations')
FY16_Jul_BlaBla_Security = dte_data(FY16_Jul,'DTE','BlaBla Security')
FY16_Jul_BlaBla_Strategy = dte_data(FY16_Jul,'DTE','BlaBla Strategy')
FY16_Jul_BlaBla_Technology = dte_data(FY16_Jul,'DTE','BlaBla Technology')
FY16_Jul_Capability_Network = dte_data(FY16_Jul,'DTE','Capability Network')
FY16_Jul_Communications_Media_Technology = dte_data(FY16_Jul,'DTE','Communications, Media & Technology')
FY16_Jul_Corporate_Functions = dte_data(FY16_Jul,'DTE','Corporate Functions')
FY16_Jul_Europe_Market = dte_data(FY16_Jul,'DTE','Europe_Market')
FY16_Jul_Financial_Services = dte_data(FY16_Jul,'DTE','Financial Services')
FY16_Jul_Global_Technology = dte_data(FY16_Jul,'DTE','Global Technology')
FY16_Jul_Growth_Markets = dte_data(FY16_Jul,'DTE','Growth_Markets')
FY16_Jul_Health_Public_Service = dte_data(FY16_Jul,'DTE','Health & Public Service')
FY16_Jul_North_America_Market = dte_data(FY16_Jul,'DTE','North_America_Market')
FY16_Jul_Other = dte_data(FY16_Jul,'DTE','Other')
FY16_Jul_Products = dte_data(FY16_Jul,'DTE','Products')
FY16_Jul_Resources = dte_data(FY16_Jul,'DTE','Resources')

FY16_Aug_BlaBla_Digital = dte_data(FY16_Aug,'DTE','BlaBla Digital')
FY16_Aug_BlaBla_Operations = dte_data(FY16_Aug,'DTE','BlaBla Operations')
FY16_Aug_BlaBla_Security = dte_data(FY16_Aug,'DTE','BlaBla Security')
FY16_Aug_BlaBla_Strategy = dte_data(FY16_Aug,'DTE','BlaBla Strategy')
FY16_Aug_BlaBla_Technology = dte_data(FY16_Aug,'DTE','BlaBla Technology')
FY16_Aug_Capability_Network = dte_data(FY16_Aug,'DTE','Capability Network')
FY16_Aug_Communications_Media_Technology = dte_data(FY16_Aug,'DTE','Communications, Media & Technology')
FY16_Aug_Corporate_Functions = dte_data(FY16_Aug,'DTE','Corporate Functions')
FY16_Aug_Europe_Market = dte_data(FY16_Aug,'DTE','Europe_Market')
FY16_Aug_Financial_Services = dte_data(FY16_Aug,'DTE','Financial Services')
FY16_Aug_Global_Technology = dte_data(FY16_Aug,'DTE','Global Technology')
FY16_Aug_Growth_Markets = dte_data(FY16_Aug,'DTE','Growth_Markets')
FY16_Aug_Health_Public_Service = dte_data(FY16_Aug,'DTE','Health & Public Service')
FY16_Aug_North_America_Market = dte_data(FY16_Aug,'DTE','North_America_Market')
FY16_Aug_Other = dte_data(FY16_Aug,'DTE','Other')
FY16_Aug_Products = dte_data(FY16_Aug,'DTE','Products')
FY16_Aug_Resources = dte_data(FY16_Aug,'DTE','Resources')

FY16_BlaBla_Digital_Avg_N_Size_Q00 = sum(vaibhav(FY16_BlaBla_Digital,'NUMBER OF RESPONDENTS FOR THE WORKGROUP (N SIZE)','Q00.  Overall Satisfaction. (MEAN SCORE)'))
FY16_BlaBla_Digital_Avg_N_Size_Q01 = sum(vaibhav(FY16_BlaBla_Digital,'NUMBER OF RESPONDENTS FOR THE WORKGROUP (N SIZE)','Q01.  Know What\'s Expected. (MEAN SCORE)'))
FY16_BlaBla_Digital_Avg_N_Size_Q02 = sum(vaibhav(FY16_BlaBla_Digital,'NUMBER OF RESPONDENTS FOR THE WORKGROUP (N SIZE)','Q02.  Materials and Equipment. (MEAN SCORE)'))
FY16_BlaBla_Digital_Avg_N_Size_Q03 = sum(vaibhav(FY16_BlaBla_Digital,'NUMBER OF RESPONDENTS FOR THE WORKGROUP (N SIZE)','Q03.  Opportunity to do Best. (MEAN SCORE)'))
FY16_BlaBla_Digital_Avg_N_Size_Q04 = sum(vaibhav(FY16_BlaBla_Digital,'NUMBER OF RESPONDENTS FOR THE WORKGROUP (N SIZE)','Q04.  Recognition. (MEAN SCORE)'))
FY16_BlaBla_Digital_Avg_N_Size_Q05 = sum(vaibhav(FY16_BlaBla_Digital,'NUMBER OF RESPONDENTS FOR THE WORKGROUP (N SIZE)','Q05.  Cares About Me. (MEAN SCORE)'))
FY16_BlaBla_Digital_Avg_N_Size_Q06 = sum(vaibhav(FY16_BlaBla_Digital,'NUMBER OF RESPONDENTS FOR THE WORKGROUP (N SIZE)','Q06.  Development. (MEAN SCORE)'))
FY16_BlaBla_Digital_Avg_N_Size_Q07 = sum(vaibhav(FY16_BlaBla_Digital,'NUMBER OF RESPONDENTS FOR THE WORKGROUP (N SIZE)','Q07.  Opinions Count. (MEAN SCORE)'))
FY16_BlaBla_Digital_Avg_N_Size_Q08 = sum(vaibhav(FY16_BlaBla_Digital,'NUMBER OF RESPONDENTS FOR THE WORKGROUP (N SIZE)','Q08.  Mission/Purpose. (MEAN SCORE)'))
FY16_BlaBla_Digital_Avg_N_Size_Q09 = sum(vaibhav(FY16_BlaBla_Digital,'NUMBER OF RESPONDENTS FOR THE WORKGROUP (N SIZE)','Q09.  Committed to Quality. (MEAN SCORE)'))
FY16_BlaBla_Digital_Avg_N_Size_Q10 = sum(vaibhav(FY16_BlaBla_Digital,'NUMBER OF RESPONDENTS FOR THE WORKGROUP (N SIZE)','Q10.  Best Friend. (MEAN SCORE)'))
FY16_BlaBla_Digital_Avg_N_Size_Q11 = sum(vaibhav(FY16_BlaBla_Digital,'NUMBER OF RESPONDENTS FOR THE WORKGROUP (N SIZE)','Q11.  Progress. (MEAN SCORE)'))
FY16_BlaBla_Digital_Avg_N_Size_Q12 = sum(vaibhav(FY16_BlaBla_Digital,'NUMBER OF RESPONDENTS FOR THE WORKGROUP (N SIZE)','Q12.  Learn and Grow. (MEAN SCORE)'))

FY16_BlaBla_Digital_Q00_Avg_Rating = sum(FY16_BlaBla_Digital['Q00. Weighted Score'])/FY16_BlaBla_Digital_Avg_N_Size_Q00
FY16_BlaBla_Digital_Q01_Avg_Rating = sum(FY16_BlaBla_Digital['Q01. Weighted Score'])/FY16_BlaBla_Digital_Avg_N_Size_Q01
FY16_BlaBla_Digital_Q02_Avg_Rating = sum(FY16_BlaBla_Digital['Q02. Weighted Score'])/FY16_BlaBla_Digital_Avg_N_Size_Q02
FY16_BlaBla_Digital_Q03_Avg_Rating = sum(FY16_BlaBla_Digital['Q03. Weighted Score'])/FY16_BlaBla_Digital_Avg_N_Size_Q03
FY16_BlaBla_Digital_Q04_Avg_Rating = sum(FY16_BlaBla_Digital['Q04. Weighted Score'])/FY16_BlaBla_Digital_Avg_N_Size_Q04
FY16_BlaBla_Digital_Q05_Avg_Rating = sum(FY16_BlaBla_Digital['Q05. Weighted Score'])/FY16_BlaBla_Digital_Avg_N_Size_Q05
FY16_BlaBla_Digital_Q06_Avg_Rating = sum(FY16_BlaBla_Digital['Q06. Weighted Score'])/FY16_BlaBla_Digital_Avg_N_Size_Q06
FY16_BlaBla_Digital_Q07_Avg_Rating = sum(FY16_BlaBla_Digital['Q07. Weighted Score'])/FY16_BlaBla_Digital_Avg_N_Size_Q07
FY16_BlaBla_Digital_Q08_Avg_Rating = sum(FY16_BlaBla_Digital['Q08. Weighted Score'])/FY16_BlaBla_Digital_Avg_N_Size_Q08
FY16_BlaBla_Digital_Q09_Avg_Rating = sum(FY16_BlaBla_Digital['Q09. Weighted Score'])/FY16_BlaBla_Digital_Avg_N_Size_Q09
FY16_BlaBla_Digital_Q10_Avg_Rating = sum(FY16_BlaBla_Digital['Q10. Weighted Score'])/FY16_BlaBla_Digital_Avg_N_Size_Q10
FY16_BlaBla_Digital_Q11_Avg_Rating = sum(FY16_BlaBla_Digital['Q11. Weighted Score'])/FY16_BlaBla_Digital_Avg_N_Size_Q11
FY16_BlaBla_Digital_Q12_Avg_Rating = sum(FY16_BlaBla_Digital['Q12. Weighted Score'])/FY16_BlaBla_Digital_Avg_N_Size_Q12

FY16_Apr_BlaBla_Digital_Avg_N_Size_Q00 = sum(vaibhav(FY16_Apr_BlaBla_Digital,'NUMBER OF RESPONDENTS FOR THE WORKGROUP (N SIZE)','Q00.  Overall Satisfaction. (MEAN SCORE)'))
FY16_Apr_BlaBla_Digital_Avg_N_Size_Q01 = sum(vaibhav(FY16_Apr_BlaBla_Digital,'NUMBER OF RESPONDENTS FOR THE WORKGROUP (N SIZE)','Q01.  Know What\'s Expected. (MEAN SCORE)'))
FY16_Apr_BlaBla_Digital_Avg_N_Size_Q02 = sum(vaibhav(FY16_Apr_BlaBla_Digital,'NUMBER OF RESPONDENTS FOR THE WORKGROUP (N SIZE)','Q02.  Materials and Equipment. (MEAN SCORE)'))
FY16_Apr_BlaBla_Digital_Avg_N_Size_Q03 = sum(vaibhav(FY16_Apr_BlaBla_Digital,'NUMBER OF RESPONDENTS FOR THE WORKGROUP (N SIZE)','Q03.  Opportunity to do Best. (MEAN SCORE)'))
FY16_Apr_BlaBla_Digital_Avg_N_Size_Q04 = sum(vaibhav(FY16_Apr_BlaBla_Digital,'NUMBER OF RESPONDENTS FOR THE WORKGROUP (N SIZE)','Q04.  Recognition. (MEAN SCORE)'))
FY16_Apr_BlaBla_Digital_Avg_N_Size_Q05 = sum(vaibhav(FY16_Apr_BlaBla_Digital,'NUMBER OF RESPONDENTS FOR THE WORKGROUP (N SIZE)','Q05.  Cares About Me. (MEAN SCORE)'))
FY16_Apr_BlaBla_Digital_Avg_N_Size_Q06 = sum(vaibhav(FY16_Apr_BlaBla_Digital,'NUMBER OF RESPONDENTS FOR THE WORKGROUP (N SIZE)','Q06.  Development. (MEAN SCORE)'))
FY16_Apr_BlaBla_Digital_Avg_N_Size_Q07 = sum(vaibhav(FY16_Apr_BlaBla_Digital,'NUMBER OF RESPONDENTS FOR THE WORKGROUP (N SIZE)','Q07.  Opinions Count. (MEAN SCORE)'))
FY16_Apr_BlaBla_Digital_Avg_N_Size_Q08 = sum(vaibhav(FY16_Apr_BlaBla_Digital,'NUMBER OF RESPONDENTS FOR THE WORKGROUP (N SIZE)','Q08.  Mission/Purpose. (MEAN SCORE)'))
FY16_Apr_BlaBla_Digital_Avg_N_Size_Q09 = sum(vaibhav(FY16_Apr_BlaBla_Digital,'NUMBER OF RESPONDENTS FOR THE WORKGROUP (N SIZE)','Q09.  Committed to Quality. (MEAN SCORE)'))
FY16_Apr_BlaBla_Digital_Avg_N_Size_Q10 = sum(vaibhav(FY16_Apr_BlaBla_Digital,'NUMBER OF RESPONDENTS FOR THE WORKGROUP (N SIZE)','Q10.  Best Friend. (MEAN SCORE)'))
FY16_Apr_BlaBla_Digital_Avg_N_Size_Q11 = sum(vaibhav(FY16_Apr_BlaBla_Digital,'NUMBER OF RESPONDENTS FOR THE WORKGROUP (N SIZE)','Q11.  Progress. (MEAN SCORE)'))
FY16_Apr_BlaBla_Digital_Avg_N_Size_Q12 = sum(vaibhav(FY16_Apr_BlaBla_Digital,'NUMBER OF RESPONDENTS FOR THE WORKGROUP (N SIZE)','Q12.  Learn and Grow. (MEAN SCORE)'))

FY16_Apr_BlaBla_Digital_Q00_Avg_Rating = sum(FY16_Apr_BlaBla_Digital['Q00. Weighted Score'])/FY16_Apr_BlaBla_Digital_Avg_N_Size_Q00
FY16_Apr_BlaBla_Digital_Q01_Avg_Rating = sum(FY16_Apr_BlaBla_Digital['Q01. Weighted Score'])/FY16_Apr_BlaBla_Digital_Avg_N_Size_Q01
FY16_Apr_BlaBla_Digital_Q02_Avg_Rating = sum(FY16_Apr_BlaBla_Digital['Q02. Weighted Score'])/FY16_Apr_BlaBla_Digital_Avg_N_Size_Q02
FY16_Apr_BlaBla_Digital_Q03_Avg_Rating = sum(FY16_Apr_BlaBla_Digital['Q03. Weighted Score'])/FY16_Apr_BlaBla_Digital_Avg_N_Size_Q03
FY16_Apr_BlaBla_Digital_Q04_Avg_Rating = sum(FY16_Apr_BlaBla_Digital['Q04. Weighted Score'])/FY16_Apr_BlaBla_Digital_Avg_N_Size_Q04
FY16_Apr_BlaBla_Digital_Q05_Avg_Rating = sum(FY16_Apr_BlaBla_Digital['Q05. Weighted Score'])/FY16_Apr_BlaBla_Digital_Avg_N_Size_Q05
FY16_Apr_BlaBla_Digital_Q06_Avg_Rating = sum(FY16_Apr_BlaBla_Digital['Q06. Weighted Score'])/FY16_Apr_BlaBla_Digital_Avg_N_Size_Q06
FY16_Apr_BlaBla_Digital_Q07_Avg_Rating = sum(FY16_Apr_BlaBla_Digital['Q07. Weighted Score'])/FY16_Apr_BlaBla_Digital_Avg_N_Size_Q07
FY16_Apr_BlaBla_Digital_Q08_Avg_Rating = sum(FY16_Apr_BlaBla_Digital['Q08. Weighted Score'])/FY16_Apr_BlaBla_Digital_Avg_N_Size_Q08
FY16_Apr_BlaBla_Digital_Q09_Avg_Rating = sum(FY16_Apr_BlaBla_Digital['Q09. Weighted Score'])/FY16_Apr_BlaBla_Digital_Avg_N_Size_Q09
FY16_Apr_BlaBla_Digital_Q10_Avg_Rating = sum(FY16_Apr_BlaBla_Digital['Q10. Weighted Score'])/FY16_Apr_BlaBla_Digital_Avg_N_Size_Q10
FY16_Apr_BlaBla_Digital_Q11_Avg_Rating = sum(FY16_Apr_BlaBla_Digital['Q11. Weighted Score'])/FY16_Apr_BlaBla_Digital_Avg_N_Size_Q11
FY16_Apr_BlaBla_Digital_Q12_Avg_Rating = sum(FY16_Apr_BlaBla_Digital['Q12. Weighted Score'])/FY16_Apr_BlaBla_Digital_Avg_N_Size_Q12

FY16_May_BlaBla_Digital_Avg_N_Size_Q00 = sum(vaibhav(FY16_May_BlaBla_Digital,'NUMBER OF RESPONDENTS FOR THE WORKGROUP (N SIZE)','Q00.  Overall Satisfaction. (MEAN SCORE)'))
FY16_May_BlaBla_Digital_Avg_N_Size_Q01 = sum(vaibhav(FY16_May_BlaBla_Digital,'NUMBER OF RESPONDENTS FOR THE WORKGROUP (N SIZE)','Q01.  Know What\'s Expected. (MEAN SCORE)'))
FY16_May_BlaBla_Digital_Avg_N_Size_Q02 = sum(vaibhav(FY16_May_BlaBla_Digital,'NUMBER OF RESPONDENTS FOR THE WORKGROUP (N SIZE)','Q02.  Materials and Equipment. (MEAN SCORE)'))
FY16_May_BlaBla_Digital_Avg_N_Size_Q03 = sum(vaibhav(FY16_May_BlaBla_Digital,'NUMBER OF RESPONDENTS FOR THE WORKGROUP (N SIZE)','Q03.  Opportunity to do Best. (MEAN SCORE)'))
FY16_May_BlaBla_Digital_Avg_N_Size_Q04 = sum(vaibhav(FY16_May_BlaBla_Digital,'NUMBER OF RESPONDENTS FOR THE WORKGROUP (N SIZE)','Q04.  Recognition. (MEAN SCORE)'))
FY16_May_BlaBla_Digital_Avg_N_Size_Q05 = sum(vaibhav(FY16_May_BlaBla_Digital,'NUMBER OF RESPONDENTS FOR THE WORKGROUP (N SIZE)','Q05.  Cares About Me. (MEAN SCORE)'))
FY16_May_BlaBla_Digital_Avg_N_Size_Q06 = sum(vaibhav(FY16_May_BlaBla_Digital,'NUMBER OF RESPONDENTS FOR THE WORKGROUP (N SIZE)','Q06.  Development. (MEAN SCORE)'))
FY16_May_BlaBla_Digital_Avg_N_Size_Q07 = sum(vaibhav(FY16_May_BlaBla_Digital,'NUMBER OF RESPONDENTS FOR THE WORKGROUP (N SIZE)','Q07.  Opinions Count. (MEAN SCORE)'))
FY16_May_BlaBla_Digital_Avg_N_Size_Q08 = sum(vaibhav(FY16_May_BlaBla_Digital,'NUMBER OF RESPONDENTS FOR THE WORKGROUP (N SIZE)','Q08.  Mission/Purpose. (MEAN SCORE)'))
FY16_May_BlaBla_Digital_Avg_N_Size_Q09 = sum(vaibhav(FY16_May_BlaBla_Digital,'NUMBER OF RESPONDENTS FOR THE WORKGROUP (N SIZE)','Q09.  Committed to Quality. (MEAN SCORE)'))
FY16_May_BlaBla_Digital_Avg_N_Size_Q10 = sum(vaibhav(FY16_May_BlaBla_Digital,'NUMBER OF RESPONDENTS FOR THE WORKGROUP (N SIZE)','Q10.  Best Friend. (MEAN SCORE)'))
FY16_May_BlaBla_Digital_Avg_N_Size_Q11 = sum(vaibhav(FY16_May_BlaBla_Digital,'NUMBER OF RESPONDENTS FOR THE WORKGROUP (N SIZE)','Q11.  Progress. (MEAN SCORE)'))
FY16_May_BlaBla_Digital_Avg_N_Size_Q12 = sum(vaibhav(FY16_May_BlaBla_Digital,'NUMBER OF RESPONDENTS FOR THE WORKGROUP (N SIZE)','Q12.  Learn and Grow. (MEAN SCORE)'))

FY16_May_BlaBla_Digital_Q00_Avg_Rating = sum(FY16_May_BlaBla_Digital['Q00. Weighted Score'])/FY16_May_BlaBla_Digital_Avg_N_Size_Q00
FY16_May_BlaBla_Digital_Q01_Avg_Rating = sum(FY16_May_BlaBla_Digital['Q01. Weighted Score'])/FY16_May_BlaBla_Digital_Avg_N_Size_Q01
FY16_May_BlaBla_Digital_Q02_Avg_Rating = sum(FY16_May_BlaBla_Digital['Q02. Weighted Score'])/FY16_May_BlaBla_Digital_Avg_N_Size_Q02
FY16_May_BlaBla_Digital_Q03_Avg_Rating = sum(FY16_May_BlaBla_Digital['Q03. Weighted Score'])/FY16_May_BlaBla_Digital_Avg_N_Size_Q03
FY16_May_BlaBla_Digital_Q04_Avg_Rating = sum(FY16_May_BlaBla_Digital['Q04. Weighted Score'])/FY16_May_BlaBla_Digital_Avg_N_Size_Q04
FY16_May_BlaBla_Digital_Q05_Avg_Rating = sum(FY16_May_BlaBla_Digital['Q05. Weighted Score'])/FY16_May_BlaBla_Digital_Avg_N_Size_Q05
FY16_May_BlaBla_Digital_Q06_Avg_Rating = sum(FY16_May_BlaBla_Digital['Q06. Weighted Score'])/FY16_May_BlaBla_Digital_Avg_N_Size_Q06
FY16_May_BlaBla_Digital_Q07_Avg_Rating = sum(FY16_May_BlaBla_Digital['Q07. Weighted Score'])/FY16_May_BlaBla_Digital_Avg_N_Size_Q07
FY16_May_BlaBla_Digital_Q08_Avg_Rating = sum(FY16_May_BlaBla_Digital['Q08. Weighted Score'])/FY16_May_BlaBla_Digital_Avg_N_Size_Q08
FY16_May_BlaBla_Digital_Q09_Avg_Rating = sum(FY16_May_BlaBla_Digital['Q09. Weighted Score'])/FY16_May_BlaBla_Digital_Avg_N_Size_Q09
FY16_May_BlaBla_Digital_Q10_Avg_Rating = sum(FY16_May_BlaBla_Digital['Q10. Weighted Score'])/FY16_May_BlaBla_Digital_Avg_N_Size_Q10
FY16_May_BlaBla_Digital_Q11_Avg_Rating = sum(FY16_May_BlaBla_Digital['Q11. Weighted Score'])/FY16_May_BlaBla_Digital_Avg_N_Size_Q11
FY16_May_BlaBla_Digital_Q12_Avg_Rating = sum(FY16_May_BlaBla_Digital['Q12. Weighted Score'])/FY16_May_BlaBla_Digital_Avg_N_Size_Q12

FY16_Jun_BlaBla_Digital_Avg_N_Size_Q00 = sum(vaibhav(FY16_Jun_BlaBla_Digital,'NUMBER OF RESPONDENTS FOR THE WORKGROUP (N SIZE)','Q00.  Overall Satisfaction. (MEAN SCORE)'))
FY16_Jun_BlaBla_Digital_Avg_N_Size_Q01 = sum(vaibhav(FY16_Jun_BlaBla_Digital,'NUMBER OF RESPONDENTS FOR THE WORKGROUP (N SIZE)','Q01.  Know What\'s Expected. (MEAN SCORE)'))
FY16_Jun_BlaBla_Digital_Avg_N_Size_Q02 = sum(vaibhav(FY16_Jun_BlaBla_Digital,'NUMBER OF RESPONDENTS FOR THE WORKGROUP (N SIZE)','Q02.  Materials and Equipment. (MEAN SCORE)'))
FY16_Jun_BlaBla_Digital_Avg_N_Size_Q03 = sum(vaibhav(FY16_Jun_BlaBla_Digital,'NUMBER OF RESPONDENTS FOR THE WORKGROUP (N SIZE)','Q03.  Opportunity to do Best. (MEAN SCORE)'))
FY16_Jun_BlaBla_Digital_Avg_N_Size_Q04 = sum(vaibhav(FY16_Jun_BlaBla_Digital,'NUMBER OF RESPONDENTS FOR THE WORKGROUP (N SIZE)','Q04.  Recognition. (MEAN SCORE)'))
FY16_Jun_BlaBla_Digital_Avg_N_Size_Q05 = sum(vaibhav(FY16_Jun_BlaBla_Digital,'NUMBER OF RESPONDENTS FOR THE WORKGROUP (N SIZE)','Q05.  Cares About Me. (MEAN SCORE)'))
FY16_Jun_BlaBla_Digital_Avg_N_Size_Q06 = sum(vaibhav(FY16_Jun_BlaBla_Digital,'NUMBER OF RESPONDENTS FOR THE WORKGROUP (N SIZE)','Q06.  Development. (MEAN SCORE)'))
FY16_Jun_BlaBla_Digital_Avg_N_Size_Q07 = sum(vaibhav(FY16_Jun_BlaBla_Digital,'NUMBER OF RESPONDENTS FOR THE WORKGROUP (N SIZE)','Q07.  Opinions Count. (MEAN SCORE)'))
FY16_Jun_BlaBla_Digital_Avg_N_Size_Q08 = sum(vaibhav(FY16_Jun_BlaBla_Digital,'NUMBER OF RESPONDENTS FOR THE WORKGROUP (N SIZE)','Q08.  Mission/Purpose. (MEAN SCORE)'))
FY16_Jun_BlaBla_Digital_Avg_N_Size_Q09 = sum(vaibhav(FY16_Jun_BlaBla_Digital,'NUMBER OF RESPONDENTS FOR THE WORKGROUP (N SIZE)','Q09.  Committed to Quality. (MEAN SCORE)'))
FY16_Jun_BlaBla_Digital_Avg_N_Size_Q10 = sum(vaibhav(FY16_Jun_BlaBla_Digital,'NUMBER OF RESPONDENTS FOR THE WORKGROUP (N SIZE)','Q10.  Best Friend. (MEAN SCORE)'))
FY16_Jun_BlaBla_Digital_Avg_N_Size_Q11 = sum(vaibhav(FY16_Jun_BlaBla_Digital,'NUMBER OF RESPONDENTS FOR THE WORKGROUP (N SIZE)','Q11.  Progress. (MEAN SCORE)'))
FY16_Jun_BlaBla_Digital_Avg_N_Size_Q12 = sum(vaibhav(FY16_Jun_BlaBla_Digital,'NUMBER OF RESPONDENTS FOR THE WORKGROUP (N SIZE)','Q12.  Learn and Grow. (MEAN SCORE)'))

FY16_Jun_BlaBla_Digital_Q00_Avg_Rating = sum(FY16_Jun_BlaBla_Digital['Q00. Weighted Score'])/FY16_Jun_BlaBla_Digital_Avg_N_Size_Q00
FY16_Jun_BlaBla_Digital_Q01_Avg_Rating = sum(FY16_Jun_BlaBla_Digital['Q01. Weighted Score'])/FY16_Jun_BlaBla_Digital_Avg_N_Size_Q01
FY16_Jun_BlaBla_Digital_Q02_Avg_Rating = sum(FY16_Jun_BlaBla_Digital['Q02. Weighted Score'])/FY16_Jun_BlaBla_Digital_Avg_N_Size_Q02
FY16_Jun_BlaBla_Digital_Q03_Avg_Rating = sum(FY16_Jun_BlaBla_Digital['Q03. Weighted Score'])/FY16_Jun_BlaBla_Digital_Avg_N_Size_Q03
FY16_Jun_BlaBla_Digital_Q04_Avg_Rating = sum(FY16_Jun_BlaBla_Digital['Q04. Weighted Score'])/FY16_Jun_BlaBla_Digital_Avg_N_Size_Q04
FY16_Jun_BlaBla_Digital_Q05_Avg_Rating = sum(FY16_Jun_BlaBla_Digital['Q05. Weighted Score'])/FY16_Jun_BlaBla_Digital_Avg_N_Size_Q05
FY16_Jun_BlaBla_Digital_Q06_Avg_Rating = sum(FY16_Jun_BlaBla_Digital['Q06. Weighted Score'])/FY16_Jun_BlaBla_Digital_Avg_N_Size_Q06
FY16_Jun_BlaBla_Digital_Q07_Avg_Rating = sum(FY16_Jun_BlaBla_Digital['Q07. Weighted Score'])/FY16_Jun_BlaBla_Digital_Avg_N_Size_Q07
FY16_Jun_BlaBla_Digital_Q08_Avg_Rating = sum(FY16_Jun_BlaBla_Digital['Q08. Weighted Score'])/FY16_Jun_BlaBla_Digital_Avg_N_Size_Q08
FY16_Jun_BlaBla_Digital_Q09_Avg_Rating = sum(FY16_Jun_BlaBla_Digital['Q09. Weighted Score'])/FY16_Jun_BlaBla_Digital_Avg_N_Size_Q09
FY16_Jun_BlaBla_Digital_Q10_Avg_Rating = sum(FY16_Jun_BlaBla_Digital['Q10. Weighted Score'])/FY16_Jun_BlaBla_Digital_Avg_N_Size_Q10
FY16_Jun_BlaBla_Digital_Q11_Avg_Rating = sum(FY16_Jun_BlaBla_Digital['Q11. Weighted Score'])/FY16_Jun_BlaBla_Digital_Avg_N_Size_Q11
FY16_Jun_BlaBla_Digital_Q12_Avg_Rating = sum(FY16_Jun_BlaBla_Digital['Q12. Weighted Score'])/FY16_Jun_BlaBla_Digital_Avg_N_Size_Q12

FY16_Jul_BlaBla_Digital_Avg_N_Size_Q00 = sum(vaibhav(FY16_Jul_BlaBla_Digital,'NUMBER OF RESPONDENTS FOR THE WORKGROUP (N SIZE)','Q00.  Overall Satisfaction. (MEAN SCORE)'))
FY16_Jul_BlaBla_Digital_Avg_N_Size_Q01 = sum(vaibhav(FY16_Jul_BlaBla_Digital,'NUMBER OF RESPONDENTS FOR THE WORKGROUP (N SIZE)','Q01.  Know What\'s Expected. (MEAN SCORE)'))
FY16_Jul_BlaBla_Digital_Avg_N_Size_Q02 = sum(vaibhav(FY16_Jul_BlaBla_Digital,'NUMBER OF RESPONDENTS FOR THE WORKGROUP (N SIZE)','Q02.  Materials and Equipment. (MEAN SCORE)'))
FY16_Jul_BlaBla_Digital_Avg_N_Size_Q03 = sum(vaibhav(FY16_Jul_BlaBla_Digital,'NUMBER OF RESPONDENTS FOR THE WORKGROUP (N SIZE)','Q03.  Opportunity to do Best. (MEAN SCORE)'))
FY16_Jul_BlaBla_Digital_Avg_N_Size_Q04 = sum(vaibhav(FY16_Jul_BlaBla_Digital,'NUMBER OF RESPONDENTS FOR THE WORKGROUP (N SIZE)','Q04.  Recognition. (MEAN SCORE)'))
FY16_Jul_BlaBla_Digital_Avg_N_Size_Q05 = sum(vaibhav(FY16_Jul_BlaBla_Digital,'NUMBER OF RESPONDENTS FOR THE WORKGROUP (N SIZE)','Q05.  Cares About Me. (MEAN SCORE)'))
FY16_Jul_BlaBla_Digital_Avg_N_Size_Q06 = sum(vaibhav(FY16_Jul_BlaBla_Digital,'NUMBER OF RESPONDENTS FOR THE WORKGROUP (N SIZE)','Q06.  Development. (MEAN SCORE)'))
FY16_Jul_BlaBla_Digital_Avg_N_Size_Q07 = sum(vaibhav(FY16_Jul_BlaBla_Digital,'NUMBER OF RESPONDENTS FOR THE WORKGROUP (N SIZE)','Q07.  Opinions Count. (MEAN SCORE)'))
FY16_Jul_BlaBla_Digital_Avg_N_Size_Q08 = sum(vaibhav(FY16_Jul_BlaBla_Digital,'NUMBER OF RESPONDENTS FOR THE WORKGROUP (N SIZE)','Q08.  Mission/Purpose. (MEAN SCORE)'))
FY16_Jul_BlaBla_Digital_Avg_N_Size_Q09 = sum(vaibhav(FY16_Jul_BlaBla_Digital,'NUMBER OF RESPONDENTS FOR THE WORKGROUP (N SIZE)','Q09.  Committed to Quality. (MEAN SCORE)'))
FY16_Jul_BlaBla_Digital_Avg_N_Size_Q10 = sum(vaibhav(FY16_Jul_BlaBla_Digital,'NUMBER OF RESPONDENTS FOR THE WORKGROUP (N SIZE)','Q10.  Best Friend. (MEAN SCORE)'))
FY16_Jul_BlaBla_Digital_Avg_N_Size_Q11 = sum(vaibhav(FY16_Jul_BlaBla_Digital,'NUMBER OF RESPONDENTS FOR THE WORKGROUP (N SIZE)','Q11.  Progress. (MEAN SCORE)'))
FY16_Jul_BlaBla_Digital_Avg_N_Size_Q12 = sum(vaibhav(FY16_Jul_BlaBla_Digital,'NUMBER OF RESPONDENTS FOR THE WORKGROUP (N SIZE)','Q12.  Learn and Grow. (MEAN SCORE)'))

FY16_Jul_BlaBla_Digital_Q00_Avg_Rating = sum(FY16_Jul_BlaBla_Digital['Q00. Weighted Score'])/FY16_Jul_BlaBla_Digital_Avg_N_Size_Q00
FY16_Jul_BlaBla_Digital_Q01_Avg_Rating = sum(FY16_Jul_BlaBla_Digital['Q01. Weighted Score'])/FY16_Jul_BlaBla_Digital_Avg_N_Size_Q01
FY16_Jul_BlaBla_Digital_Q02_Avg_Rating = sum(FY16_Jul_BlaBla_Digital['Q02. Weighted Score'])/FY16_Jul_BlaBla_Digital_Avg_N_Size_Q02
FY16_Jul_BlaBla_Digital_Q03_Avg_Rating = sum(FY16_Jul_BlaBla_Digital['Q03. Weighted Score'])/FY16_Jul_BlaBla_Digital_Avg_N_Size_Q03
FY16_Jul_BlaBla_Digital_Q04_Avg_Rating = sum(FY16_Jul_BlaBla_Digital['Q04. Weighted Score'])/FY16_Jul_BlaBla_Digital_Avg_N_Size_Q04
FY16_Jul_BlaBla_Digital_Q05_Avg_Rating = sum(FY16_Jul_BlaBla_Digital['Q05. Weighted Score'])/FY16_Jul_BlaBla_Digital_Avg_N_Size_Q05
FY16_Jul_BlaBla_Digital_Q06_Avg_Rating = sum(FY16_Jul_BlaBla_Digital['Q06. Weighted Score'])/FY16_Jul_BlaBla_Digital_Avg_N_Size_Q06
FY16_Jul_BlaBla_Digital_Q07_Avg_Rating = sum(FY16_Jul_BlaBla_Digital['Q07. Weighted Score'])/FY16_Jul_BlaBla_Digital_Avg_N_Size_Q07
FY16_Jul_BlaBla_Digital_Q08_Avg_Rating = sum(FY16_Jul_BlaBla_Digital['Q08. Weighted Score'])/FY16_Jul_BlaBla_Digital_Avg_N_Size_Q08
FY16_Jul_BlaBla_Digital_Q09_Avg_Rating = sum(FY16_Jul_BlaBla_Digital['Q09. Weighted Score'])/FY16_Jul_BlaBla_Digital_Avg_N_Size_Q09
FY16_Jul_BlaBla_Digital_Q10_Avg_Rating = sum(FY16_Jul_BlaBla_Digital['Q10. Weighted Score'])/FY16_Jul_BlaBla_Digital_Avg_N_Size_Q10
FY16_Jul_BlaBla_Digital_Q11_Avg_Rating = sum(FY16_Jul_BlaBla_Digital['Q11. Weighted Score'])/FY16_Jul_BlaBla_Digital_Avg_N_Size_Q11
FY16_Jul_BlaBla_Digital_Q12_Avg_Rating = sum(FY16_Jul_BlaBla_Digital['Q12. Weighted Score'])/FY16_Jul_BlaBla_Digital_Avg_N_Size_Q12

FY16_Aug_BlaBla_Digital_Avg_N_Size_Q00 = sum(vaibhav(FY16_Aug_BlaBla_Digital,'NUMBER OF RESPONDENTS FOR THE WORKGROUP (N SIZE)','Q00.  Overall Satisfaction. (MEAN SCORE)'))
FY16_Aug_BlaBla_Digital_Avg_N_Size_Q01 = sum(vaibhav(FY16_Aug_BlaBla_Digital,'NUMBER OF RESPONDENTS FOR THE WORKGROUP (N SIZE)','Q01.  Know What\'s Expected. (MEAN SCORE)'))
FY16_Aug_BlaBla_Digital_Avg_N_Size_Q02 = sum(vaibhav(FY16_Aug_BlaBla_Digital,'NUMBER OF RESPONDENTS FOR THE WORKGROUP (N SIZE)','Q02.  Materials and Equipment. (MEAN SCORE)'))
FY16_Aug_BlaBla_Digital_Avg_N_Size_Q03 = sum(vaibhav(FY16_Aug_BlaBla_Digital,'NUMBER OF RESPONDENTS FOR THE WORKGROUP (N SIZE)','Q03.  Opportunity to do Best. (MEAN SCORE)'))
FY16_Aug_BlaBla_Digital_Avg_N_Size_Q04 = sum(vaibhav(FY16_Aug_BlaBla_Digital,'NUMBER OF RESPONDENTS FOR THE WORKGROUP (N SIZE)','Q04.  Recognition. (MEAN SCORE)'))
FY16_Aug_BlaBla_Digital_Avg_N_Size_Q05 = sum(vaibhav(FY16_Aug_BlaBla_Digital,'NUMBER OF RESPONDENTS FOR THE WORKGROUP (N SIZE)','Q05.  Cares About Me. (MEAN SCORE)'))
FY16_Aug_BlaBla_Digital_Avg_N_Size_Q06 = sum(vaibhav(FY16_Aug_BlaBla_Digital,'NUMBER OF RESPONDENTS FOR THE WORKGROUP (N SIZE)','Q06.  Development. (MEAN SCORE)'))
FY16_Aug_BlaBla_Digital_Avg_N_Size_Q07 = sum(vaibhav(FY16_Aug_BlaBla_Digital,'NUMBER OF RESPONDENTS FOR THE WORKGROUP (N SIZE)','Q07.  Opinions Count. (MEAN SCORE)'))
FY16_Aug_BlaBla_Digital_Avg_N_Size_Q08 = sum(vaibhav(FY16_Aug_BlaBla_Digital,'NUMBER OF RESPONDENTS FOR THE WORKGROUP (N SIZE)','Q08.  Mission/Purpose. (MEAN SCORE)'))
FY16_Aug_BlaBla_Digital_Avg_N_Size_Q09 = sum(vaibhav(FY16_Aug_BlaBla_Digital,'NUMBER OF RESPONDENTS FOR THE WORKGROUP (N SIZE)','Q09.  Committed to Quality. (MEAN SCORE)'))
FY16_Aug_BlaBla_Digital_Avg_N_Size_Q10 = sum(vaibhav(FY16_Aug_BlaBla_Digital,'NUMBER OF RESPONDENTS FOR THE WORKGROUP (N SIZE)','Q10.  Best Friend. (MEAN SCORE)'))
FY16_Aug_BlaBla_Digital_Avg_N_Size_Q11 = sum(vaibhav(FY16_Aug_BlaBla_Digital,'NUMBER OF RESPONDENTS FOR THE WORKGROUP (N SIZE)','Q11.  Progress. (MEAN SCORE)'))
FY16_Aug_BlaBla_Digital_Avg_N_Size_Q12 = sum(vaibhav(FY16_Aug_BlaBla_Digital,'NUMBER OF RESPONDENTS FOR THE WORKGROUP (N SIZE)','Q12.  Learn and Grow. (MEAN SCORE)'))

FY16_Aug_BlaBla_Digital_Q00_Avg_Rating = sum(FY16_Aug_BlaBla_Digital['Q00. Weighted Score'])/FY16_Aug_BlaBla_Digital_Avg_N_Size_Q00
FY16_Aug_BlaBla_Digital_Q01_Avg_Rating = sum(FY16_Aug_BlaBla_Digital['Q01. Weighted Score'])/FY16_Aug_BlaBla_Digital_Avg_N_Size_Q01
FY16_Aug_BlaBla_Digital_Q02_Avg_Rating = sum(FY16_Aug_BlaBla_Digital['Q02. Weighted Score'])/FY16_Aug_BlaBla_Digital_Avg_N_Size_Q02
FY16_Aug_BlaBla_Digital_Q03_Avg_Rating = sum(FY16_Aug_BlaBla_Digital['Q03. Weighted Score'])/FY16_Aug_BlaBla_Digital_Avg_N_Size_Q03
FY16_Aug_BlaBla_Digital_Q04_Avg_Rating = sum(FY16_Aug_BlaBla_Digital['Q04. Weighted Score'])/FY16_Aug_BlaBla_Digital_Avg_N_Size_Q04
FY16_Aug_BlaBla_Digital_Q05_Avg_Rating = sum(FY16_Aug_BlaBla_Digital['Q05. Weighted Score'])/FY16_Aug_BlaBla_Digital_Avg_N_Size_Q05
FY16_Aug_BlaBla_Digital_Q06_Avg_Rating = sum(FY16_Aug_BlaBla_Digital['Q06. Weighted Score'])/FY16_Aug_BlaBla_Digital_Avg_N_Size_Q06
FY16_Aug_BlaBla_Digital_Q07_Avg_Rating = sum(FY16_Aug_BlaBla_Digital['Q07. Weighted Score'])/FY16_Aug_BlaBla_Digital_Avg_N_Size_Q07
FY16_Aug_BlaBla_Digital_Q08_Avg_Rating = sum(FY16_Aug_BlaBla_Digital['Q08. Weighted Score'])/FY16_Aug_BlaBla_Digital_Avg_N_Size_Q08
FY16_Aug_BlaBla_Digital_Q09_Avg_Rating = sum(FY16_Aug_BlaBla_Digital['Q09. Weighted Score'])/FY16_Aug_BlaBla_Digital_Avg_N_Size_Q09
FY16_Aug_BlaBla_Digital_Q10_Avg_Rating = sum(FY16_Aug_BlaBla_Digital['Q10. Weighted Score'])/FY16_Aug_BlaBla_Digital_Avg_N_Size_Q10
FY16_Aug_BlaBla_Digital_Q11_Avg_Rating = sum(FY16_Aug_BlaBla_Digital['Q11. Weighted Score'])/FY16_Aug_BlaBla_Digital_Avg_N_Size_Q11
FY16_Aug_BlaBla_Digital_Q12_Avg_Rating = sum(FY16_Aug_BlaBla_Digital['Q12. Weighted Score'])/FY16_Aug_BlaBla_Digital_Avg_N_Size_Q12

FY16_BlaBla_Operations_Avg_N_Size_Q00 = sum(vaibhav(FY16_BlaBla_Operations,'NUMBER OF RESPONDENTS FOR THE WORKGROUP (N SIZE)','Q00.  Overall Satisfaction. (MEAN SCORE)'))
FY16_BlaBla_Operations_Avg_N_Size_Q01 = sum(vaibhav(FY16_BlaBla_Operations,'NUMBER OF RESPONDENTS FOR THE WORKGROUP (N SIZE)','Q01.  Know What\'s Expected. (MEAN SCORE)'))
FY16_BlaBla_Operations_Avg_N_Size_Q02 = sum(vaibhav(FY16_BlaBla_Operations,'NUMBER OF RESPONDENTS FOR THE WORKGROUP (N SIZE)','Q02.  Materials and Equipment. (MEAN SCORE)'))
FY16_BlaBla_Operations_Avg_N_Size_Q03 = sum(vaibhav(FY16_BlaBla_Operations,'NUMBER OF RESPONDENTS FOR THE WORKGROUP (N SIZE)','Q03.  Opportunity to do Best. (MEAN SCORE)'))
FY16_BlaBla_Operations_Avg_N_Size_Q04 = sum(vaibhav(FY16_BlaBla_Operations,'NUMBER OF RESPONDENTS FOR THE WORKGROUP (N SIZE)','Q04.  Recognition. (MEAN SCORE)'))
FY16_BlaBla_Operations_Avg_N_Size_Q05 = sum(vaibhav(FY16_BlaBla_Operations,'NUMBER OF RESPONDENTS FOR THE WORKGROUP (N SIZE)','Q05.  Cares About Me. (MEAN SCORE)'))
FY16_BlaBla_Operations_Avg_N_Size_Q06 = sum(vaibhav(FY16_BlaBla_Operations,'NUMBER OF RESPONDENTS FOR THE WORKGROUP (N SIZE)','Q06.  Development. (MEAN SCORE)'))
FY16_BlaBla_Operations_Avg_N_Size_Q07 = sum(vaibhav(FY16_BlaBla_Operations,'NUMBER OF RESPONDENTS FOR THE WORKGROUP (N SIZE)','Q07.  Opinions Count. (MEAN SCORE)'))
FY16_BlaBla_Operations_Avg_N_Size_Q08 = sum(vaibhav(FY16_BlaBla_Operations,'NUMBER OF RESPONDENTS FOR THE WORKGROUP (N SIZE)','Q08.  Mission/Purpose. (MEAN SCORE)'))
FY16_BlaBla_Operations_Avg_N_Size_Q09 = sum(vaibhav(FY16_BlaBla_Operations,'NUMBER OF RESPONDENTS FOR THE WORKGROUP (N SIZE)','Q09.  Committed to Quality. (MEAN SCORE)'))
FY16_BlaBla_Operations_Avg_N_Size_Q10 = sum(vaibhav(FY16_BlaBla_Operations,'NUMBER OF RESPONDENTS FOR THE WORKGROUP (N SIZE)','Q10.  Best Friend. (MEAN SCORE)'))
FY16_BlaBla_Operations_Avg_N_Size_Q11 = sum(vaibhav(FY16_BlaBla_Operations,'NUMBER OF RESPONDENTS FOR THE WORKGROUP (N SIZE)','Q11.  Progress. (MEAN SCORE)'))
FY16_BlaBla_Operations_Avg_N_Size_Q12 = sum(vaibhav(FY16_BlaBla_Operations,'NUMBER OF RESPONDENTS FOR THE WORKGROUP (N SIZE)','Q12.  Learn and Grow. (MEAN SCORE)'))

FY16_BlaBla_Operations_Q00_Avg_Rating = sum(FY16_BlaBla_Operations['Q00. Weighted Score'])/FY16_BlaBla_Operations_Avg_N_Size_Q00
FY16_BlaBla_Operations_Q01_Avg_Rating = sum(FY16_BlaBla_Operations['Q01. Weighted Score'])/FY16_BlaBla_Operations_Avg_N_Size_Q01
FY16_BlaBla_Operations_Q02_Avg_Rating = sum(FY16_BlaBla_Operations['Q02. Weighted Score'])/FY16_BlaBla_Operations_Avg_N_Size_Q02
FY16_BlaBla_Operations_Q03_Avg_Rating = sum(FY16_BlaBla_Operations['Q03. Weighted Score'])/FY16_BlaBla_Operations_Avg_N_Size_Q03
FY16_BlaBla_Operations_Q04_Avg_Rating = sum(FY16_BlaBla_Operations['Q04. Weighted Score'])/FY16_BlaBla_Operations_Avg_N_Size_Q04
FY16_BlaBla_Operations_Q05_Avg_Rating = sum(FY16_BlaBla_Operations['Q05. Weighted Score'])/FY16_BlaBla_Operations_Avg_N_Size_Q05
FY16_BlaBla_Operations_Q06_Avg_Rating = sum(FY16_BlaBla_Operations['Q06. Weighted Score'])/FY16_BlaBla_Operations_Avg_N_Size_Q06
FY16_BlaBla_Operations_Q07_Avg_Rating = sum(FY16_BlaBla_Operations['Q07. Weighted Score'])/FY16_BlaBla_Operations_Avg_N_Size_Q07
FY16_BlaBla_Operations_Q08_Avg_Rating = sum(FY16_BlaBla_Operations['Q08. Weighted Score'])/FY16_BlaBla_Operations_Avg_N_Size_Q08
FY16_BlaBla_Operations_Q09_Avg_Rating = sum(FY16_BlaBla_Operations['Q09. Weighted Score'])/FY16_BlaBla_Operations_Avg_N_Size_Q09
FY16_BlaBla_Operations_Q10_Avg_Rating = sum(FY16_BlaBla_Operations['Q10. Weighted Score'])/FY16_BlaBla_Operations_Avg_N_Size_Q10
FY16_BlaBla_Operations_Q11_Avg_Rating = sum(FY16_BlaBla_Operations['Q11. Weighted Score'])/FY16_BlaBla_Operations_Avg_N_Size_Q11
FY16_BlaBla_Operations_Q12_Avg_Rating = sum(FY16_BlaBla_Operations['Q12. Weighted Score'])/FY16_BlaBla_Operations_Avg_N_Size_Q12

FY16_BlaBla_Security_Avg_N_Size_Q00 = sum(vaibhav(FY16_BlaBla_Security,'NUMBER OF RESPONDENTS FOR THE WORKGROUP (N SIZE)','Q00.  Overall Satisfaction. (MEAN SCORE)'))
FY16_BlaBla_Security_Avg_N_Size_Q01 = sum(vaibhav(FY16_BlaBla_Security,'NUMBER OF RESPONDENTS FOR THE WORKGROUP (N SIZE)','Q01.  Know What\'s Expected. (MEAN SCORE)'))
FY16_BlaBla_Security_Avg_N_Size_Q02 = sum(vaibhav(FY16_BlaBla_Security,'NUMBER OF RESPONDENTS FOR THE WORKGROUP (N SIZE)','Q02.  Materials and Equipment. (MEAN SCORE)'))
FY16_BlaBla_Security_Avg_N_Size_Q03 = sum(vaibhav(FY16_BlaBla_Security,'NUMBER OF RESPONDENTS FOR THE WORKGROUP (N SIZE)','Q03.  Opportunity to do Best. (MEAN SCORE)'))
FY16_BlaBla_Security_Avg_N_Size_Q04 = sum(vaibhav(FY16_BlaBla_Security,'NUMBER OF RESPONDENTS FOR THE WORKGROUP (N SIZE)','Q04.  Recognition. (MEAN SCORE)'))
FY16_BlaBla_Security_Avg_N_Size_Q05 = sum(vaibhav(FY16_BlaBla_Security,'NUMBER OF RESPONDENTS FOR THE WORKGROUP (N SIZE)','Q05.  Cares About Me. (MEAN SCORE)'))
FY16_BlaBla_Security_Avg_N_Size_Q06 = sum(vaibhav(FY16_BlaBla_Security,'NUMBER OF RESPONDENTS FOR THE WORKGROUP (N SIZE)','Q06.  Development. (MEAN SCORE)'))
FY16_BlaBla_Security_Avg_N_Size_Q07 = sum(vaibhav(FY16_BlaBla_Security,'NUMBER OF RESPONDENTS FOR THE WORKGROUP (N SIZE)','Q07.  Opinions Count. (MEAN SCORE)'))
FY16_BlaBla_Security_Avg_N_Size_Q08 = sum(vaibhav(FY16_BlaBla_Security,'NUMBER OF RESPONDENTS FOR THE WORKGROUP (N SIZE)','Q08.  Mission/Purpose. (MEAN SCORE)'))
FY16_BlaBla_Security_Avg_N_Size_Q09 = sum(vaibhav(FY16_BlaBla_Security,'NUMBER OF RESPONDENTS FOR THE WORKGROUP (N SIZE)','Q09.  Committed to Quality. (MEAN SCORE)'))
FY16_BlaBla_Security_Avg_N_Size_Q10 = sum(vaibhav(FY16_BlaBla_Security,'NUMBER OF RESPONDENTS FOR THE WORKGROUP (N SIZE)','Q10.  Best Friend. (MEAN SCORE)'))
FY16_BlaBla_Security_Avg_N_Size_Q11 = sum(vaibhav(FY16_BlaBla_Security,'NUMBER OF RESPONDENTS FOR THE WORKGROUP (N SIZE)','Q11.  Progress. (MEAN SCORE)'))
FY16_BlaBla_Security_Avg_N_Size_Q12 = sum(vaibhav(FY16_BlaBla_Security,'NUMBER OF RESPONDENTS FOR THE WORKGROUP (N SIZE)','Q12.  Learn and Grow. (MEAN SCORE)'))

FY16_BlaBla_Security_Q00_Avg_Rating = sum(FY16_BlaBla_Security['Q00. Weighted Score'])/FY16_BlaBla_Security_Avg_N_Size_Q00
FY16_BlaBla_Security_Q01_Avg_Rating = sum(FY16_BlaBla_Security['Q01. Weighted Score'])/FY16_BlaBla_Security_Avg_N_Size_Q01
FY16_BlaBla_Security_Q02_Avg_Rating = sum(FY16_BlaBla_Security['Q02. Weighted Score'])/FY16_BlaBla_Security_Avg_N_Size_Q02
FY16_BlaBla_Security_Q03_Avg_Rating = sum(FY16_BlaBla_Security['Q03. Weighted Score'])/FY16_BlaBla_Security_Avg_N_Size_Q03
FY16_BlaBla_Security_Q04_Avg_Rating = sum(FY16_BlaBla_Security['Q04. Weighted Score'])/FY16_BlaBla_Security_Avg_N_Size_Q04
FY16_BlaBla_Security_Q05_Avg_Rating = sum(FY16_BlaBla_Security['Q05. Weighted Score'])/FY16_BlaBla_Security_Avg_N_Size_Q05
FY16_BlaBla_Security_Q06_Avg_Rating = sum(FY16_BlaBla_Security['Q06. Weighted Score'])/FY16_BlaBla_Security_Avg_N_Size_Q06
FY16_BlaBla_Security_Q07_Avg_Rating = sum(FY16_BlaBla_Security['Q07. Weighted Score'])/FY16_BlaBla_Security_Avg_N_Size_Q07
FY16_BlaBla_Security_Q08_Avg_Rating = sum(FY16_BlaBla_Security['Q08. Weighted Score'])/FY16_BlaBla_Security_Avg_N_Size_Q08
FY16_BlaBla_Security_Q09_Avg_Rating = sum(FY16_BlaBla_Security['Q09. Weighted Score'])/FY16_BlaBla_Security_Avg_N_Size_Q09
FY16_BlaBla_Security_Q10_Avg_Rating = sum(FY16_BlaBla_Security['Q10. Weighted Score'])/FY16_BlaBla_Security_Avg_N_Size_Q10
FY16_BlaBla_Security_Q11_Avg_Rating = sum(FY16_BlaBla_Security['Q11. Weighted Score'])/FY16_BlaBla_Security_Avg_N_Size_Q11
FY16_BlaBla_Security_Q12_Avg_Rating = sum(FY16_BlaBla_Security['Q12. Weighted Score'])/FY16_BlaBla_Security_Avg_N_Size_Q12

FY16_BlaBla_Strategy_Avg_N_Size_Q00 = sum(vaibhav(FY16_BlaBla_Strategy,'NUMBER OF RESPONDENTS FOR THE WORKGROUP (N SIZE)','Q00.  Overall Satisfaction. (MEAN SCORE)'))
FY16_BlaBla_Strategy_Avg_N_Size_Q01 = sum(vaibhav(FY16_BlaBla_Strategy,'NUMBER OF RESPONDENTS FOR THE WORKGROUP (N SIZE)','Q01.  Know What\'s Expected. (MEAN SCORE)'))
FY16_BlaBla_Strategy_Avg_N_Size_Q02 = sum(vaibhav(FY16_BlaBla_Strategy,'NUMBER OF RESPONDENTS FOR THE WORKGROUP (N SIZE)','Q02.  Materials and Equipment. (MEAN SCORE)'))
FY16_BlaBla_Strategy_Avg_N_Size_Q03 = sum(vaibhav(FY16_BlaBla_Strategy,'NUMBER OF RESPONDENTS FOR THE WORKGROUP (N SIZE)','Q03.  Opportunity to do Best. (MEAN SCORE)'))
FY16_BlaBla_Strategy_Avg_N_Size_Q04 = sum(vaibhav(FY16_BlaBla_Strategy,'NUMBER OF RESPONDENTS FOR THE WORKGROUP (N SIZE)','Q04.  Recognition. (MEAN SCORE)'))
FY16_BlaBla_Strategy_Avg_N_Size_Q05 = sum(vaibhav(FY16_BlaBla_Strategy,'NUMBER OF RESPONDENTS FOR THE WORKGROUP (N SIZE)','Q05.  Cares About Me. (MEAN SCORE)'))
FY16_BlaBla_Strategy_Avg_N_Size_Q06 = sum(vaibhav(FY16_BlaBla_Strategy,'NUMBER OF RESPONDENTS FOR THE WORKGROUP (N SIZE)','Q06.  Development. (MEAN SCORE)'))
FY16_BlaBla_Strategy_Avg_N_Size_Q07 = sum(vaibhav(FY16_BlaBla_Strategy,'NUMBER OF RESPONDENTS FOR THE WORKGROUP (N SIZE)','Q07.  Opinions Count. (MEAN SCORE)'))
FY16_BlaBla_Strategy_Avg_N_Size_Q08 = sum(vaibhav(FY16_BlaBla_Strategy,'NUMBER OF RESPONDENTS FOR THE WORKGROUP (N SIZE)','Q08.  Mission/Purpose. (MEAN SCORE)'))
FY16_BlaBla_Strategy_Avg_N_Size_Q09 = sum(vaibhav(FY16_BlaBla_Strategy,'NUMBER OF RESPONDENTS FOR THE WORKGROUP (N SIZE)','Q09.  Committed to Quality. (MEAN SCORE)'))
FY16_BlaBla_Strategy_Avg_N_Size_Q10 = sum(vaibhav(FY16_BlaBla_Strategy,'NUMBER OF RESPONDENTS FOR THE WORKGROUP (N SIZE)','Q10.  Best Friend. (MEAN SCORE)'))
FY16_BlaBla_Strategy_Avg_N_Size_Q11 = sum(vaibhav(FY16_BlaBla_Strategy,'NUMBER OF RESPONDENTS FOR THE WORKGROUP (N SIZE)','Q11.  Progress. (MEAN SCORE)'))
FY16_BlaBla_Strategy_Avg_N_Size_Q12 = sum(vaibhav(FY16_BlaBla_Strategy,'NUMBER OF RESPONDENTS FOR THE WORKGROUP (N SIZE)','Q12.  Learn and Grow. (MEAN SCORE)'))

FY16_BlaBla_Strategy_Q00_Avg_Rating = sum(FY16_BlaBla_Strategy['Q00. Weighted Score'])/FY16_BlaBla_Strategy_Avg_N_Size_Q00
FY16_BlaBla_Strategy_Q01_Avg_Rating = sum(FY16_BlaBla_Strategy['Q01. Weighted Score'])/FY16_BlaBla_Strategy_Avg_N_Size_Q01
FY16_BlaBla_Strategy_Q02_Avg_Rating = sum(FY16_BlaBla_Strategy['Q02. Weighted Score'])/FY16_BlaBla_Strategy_Avg_N_Size_Q02
FY16_BlaBla_Strategy_Q03_Avg_Rating = sum(FY16_BlaBla_Strategy['Q03. Weighted Score'])/FY16_BlaBla_Strategy_Avg_N_Size_Q03
FY16_BlaBla_Strategy_Q04_Avg_Rating = sum(FY16_BlaBla_Strategy['Q04. Weighted Score'])/FY16_BlaBla_Strategy_Avg_N_Size_Q04
FY16_BlaBla_Strategy_Q05_Avg_Rating = sum(FY16_BlaBla_Strategy['Q05. Weighted Score'])/FY16_BlaBla_Strategy_Avg_N_Size_Q05
FY16_BlaBla_Strategy_Q06_Avg_Rating = sum(FY16_BlaBla_Strategy['Q06. Weighted Score'])/FY16_BlaBla_Strategy_Avg_N_Size_Q06
FY16_BlaBla_Strategy_Q07_Avg_Rating = sum(FY16_BlaBla_Strategy['Q07. Weighted Score'])/FY16_BlaBla_Strategy_Avg_N_Size_Q07
FY16_BlaBla_Strategy_Q08_Avg_Rating = sum(FY16_BlaBla_Strategy['Q08. Weighted Score'])/FY16_BlaBla_Strategy_Avg_N_Size_Q08
FY16_BlaBla_Strategy_Q09_Avg_Rating = sum(FY16_BlaBla_Strategy['Q09. Weighted Score'])/FY16_BlaBla_Strategy_Avg_N_Size_Q09
FY16_BlaBla_Strategy_Q10_Avg_Rating = sum(FY16_BlaBla_Strategy['Q10. Weighted Score'])/FY16_BlaBla_Strategy_Avg_N_Size_Q10
FY16_BlaBla_Strategy_Q11_Avg_Rating = sum(FY16_BlaBla_Strategy['Q11. Weighted Score'])/FY16_BlaBla_Strategy_Avg_N_Size_Q11
FY16_BlaBla_Strategy_Q12_Avg_Rating = sum(FY16_BlaBla_Strategy['Q12. Weighted Score'])/FY16_BlaBla_Strategy_Avg_N_Size_Q12

FY16_BlaBla_Technology_Avg_N_Size_Q00 = sum(vaibhav(FY16_BlaBla_Technology,'NUMBER OF RESPONDENTS FOR THE WORKGROUP (N SIZE)','Q00.  Overall Satisfaction. (MEAN SCORE)'))
FY16_BlaBla_Technology_Avg_N_Size_Q01 = sum(vaibhav(FY16_BlaBla_Technology,'NUMBER OF RESPONDENTS FOR THE WORKGROUP (N SIZE)','Q01.  Know What\'s Expected. (MEAN SCORE)'))
FY16_BlaBla_Technology_Avg_N_Size_Q02 = sum(vaibhav(FY16_BlaBla_Technology,'NUMBER OF RESPONDENTS FOR THE WORKGROUP (N SIZE)','Q02.  Materials and Equipment. (MEAN SCORE)'))
FY16_BlaBla_Technology_Avg_N_Size_Q03 = sum(vaibhav(FY16_BlaBla_Technology,'NUMBER OF RESPONDENTS FOR THE WORKGROUP (N SIZE)','Q03.  Opportunity to do Best. (MEAN SCORE)'))
FY16_BlaBla_Technology_Avg_N_Size_Q04 = sum(vaibhav(FY16_BlaBla_Technology,'NUMBER OF RESPONDENTS FOR THE WORKGROUP (N SIZE)','Q04.  Recognition. (MEAN SCORE)'))
FY16_BlaBla_Technology_Avg_N_Size_Q05 = sum(vaibhav(FY16_BlaBla_Technology,'NUMBER OF RESPONDENTS FOR THE WORKGROUP (N SIZE)','Q05.  Cares About Me. (MEAN SCORE)'))
FY16_BlaBla_Technology_Avg_N_Size_Q06 = sum(vaibhav(FY16_BlaBla_Technology,'NUMBER OF RESPONDENTS FOR THE WORKGROUP (N SIZE)','Q06.  Development. (MEAN SCORE)'))
FY16_BlaBla_Technology_Avg_N_Size_Q07 = sum(vaibhav(FY16_BlaBla_Technology,'NUMBER OF RESPONDENTS FOR THE WORKGROUP (N SIZE)','Q07.  Opinions Count. (MEAN SCORE)'))
FY16_BlaBla_Technology_Avg_N_Size_Q08 = sum(vaibhav(FY16_BlaBla_Technology,'NUMBER OF RESPONDENTS FOR THE WORKGROUP (N SIZE)','Q08.  Mission/Purpose. (MEAN SCORE)'))
FY16_BlaBla_Technology_Avg_N_Size_Q09 = sum(vaibhav(FY16_BlaBla_Technology,'NUMBER OF RESPONDENTS FOR THE WORKGROUP (N SIZE)','Q09.  Committed to Quality. (MEAN SCORE)'))
FY16_BlaBla_Technology_Avg_N_Size_Q10 = sum(vaibhav(FY16_BlaBla_Technology,'NUMBER OF RESPONDENTS FOR THE WORKGROUP (N SIZE)','Q10.  Best Friend. (MEAN SCORE)'))
FY16_BlaBla_Technology_Avg_N_Size_Q11 = sum(vaibhav(FY16_BlaBla_Technology,'NUMBER OF RESPONDENTS FOR THE WORKGROUP (N SIZE)','Q11.  Progress. (MEAN SCORE)'))
FY16_BlaBla_Technology_Avg_N_Size_Q12 = sum(vaibhav(FY16_BlaBla_Technology,'NUMBER OF RESPONDENTS FOR THE WORKGROUP (N SIZE)','Q12.  Learn and Grow. (MEAN SCORE)'))

FY16_BlaBla_Technology_Q00_Avg_Rating = sum(FY16_BlaBla_Technology['Q00. Weighted Score'])/FY16_BlaBla_Technology_Avg_N_Size_Q00
FY16_BlaBla_Technology_Q01_Avg_Rating = sum(FY16_BlaBla_Technology['Q01. Weighted Score'])/FY16_BlaBla_Technology_Avg_N_Size_Q01
FY16_BlaBla_Technology_Q02_Avg_Rating = sum(FY16_BlaBla_Technology['Q02. Weighted Score'])/FY16_BlaBla_Technology_Avg_N_Size_Q02
FY16_BlaBla_Technology_Q03_Avg_Rating = sum(FY16_BlaBla_Technology['Q03. Weighted Score'])/FY16_BlaBla_Technology_Avg_N_Size_Q03
FY16_BlaBla_Technology_Q04_Avg_Rating = sum(FY16_BlaBla_Technology['Q04. Weighted Score'])/FY16_BlaBla_Technology_Avg_N_Size_Q04
FY16_BlaBla_Technology_Q05_Avg_Rating = sum(FY16_BlaBla_Technology['Q05. Weighted Score'])/FY16_BlaBla_Technology_Avg_N_Size_Q05
FY16_BlaBla_Technology_Q06_Avg_Rating = sum(FY16_BlaBla_Technology['Q06. Weighted Score'])/FY16_BlaBla_Technology_Avg_N_Size_Q06
FY16_BlaBla_Technology_Q07_Avg_Rating = sum(FY16_BlaBla_Technology['Q07. Weighted Score'])/FY16_BlaBla_Technology_Avg_N_Size_Q07
FY16_BlaBla_Technology_Q08_Avg_Rating = sum(FY16_BlaBla_Technology['Q08. Weighted Score'])/FY16_BlaBla_Technology_Avg_N_Size_Q08
FY16_BlaBla_Technology_Q09_Avg_Rating = sum(FY16_BlaBla_Technology['Q09. Weighted Score'])/FY16_BlaBla_Technology_Avg_N_Size_Q09
FY16_BlaBla_Technology_Q10_Avg_Rating = sum(FY16_BlaBla_Technology['Q10. Weighted Score'])/FY16_BlaBla_Technology_Avg_N_Size_Q10
FY16_BlaBla_Technology_Q11_Avg_Rating = sum(FY16_BlaBla_Technology['Q11. Weighted Score'])/FY16_BlaBla_Technology_Avg_N_Size_Q11
FY16_BlaBla_Technology_Q12_Avg_Rating = sum(FY16_BlaBla_Technology['Q12. Weighted Score'])/FY16_BlaBla_Technology_Avg_N_Size_Q12

FY16_Capability_Network_Avg_N_Size_Q00 = sum(vaibhav(FY16_Capability_Network,'NUMBER OF RESPONDENTS FOR THE WORKGROUP (N SIZE)','Q00.  Overall Satisfaction. (MEAN SCORE)'))
FY16_Capability_Network_Avg_N_Size_Q01 = sum(vaibhav(FY16_Capability_Network,'NUMBER OF RESPONDENTS FOR THE WORKGROUP (N SIZE)','Q01.  Know What\'s Expected. (MEAN SCORE)'))
FY16_Capability_Network_Avg_N_Size_Q02 = sum(vaibhav(FY16_Capability_Network,'NUMBER OF RESPONDENTS FOR THE WORKGROUP (N SIZE)','Q02.  Materials and Equipment. (MEAN SCORE)'))
FY16_Capability_Network_Avg_N_Size_Q03 = sum(vaibhav(FY16_Capability_Network,'NUMBER OF RESPONDENTS FOR THE WORKGROUP (N SIZE)','Q03.  Opportunity to do Best. (MEAN SCORE)'))
FY16_Capability_Network_Avg_N_Size_Q04 = sum(vaibhav(FY16_Capability_Network,'NUMBER OF RESPONDENTS FOR THE WORKGROUP (N SIZE)','Q04.  Recognition. (MEAN SCORE)'))
FY16_Capability_Network_Avg_N_Size_Q05 = sum(vaibhav(FY16_Capability_Network,'NUMBER OF RESPONDENTS FOR THE WORKGROUP (N SIZE)','Q05.  Cares About Me. (MEAN SCORE)'))
FY16_Capability_Network_Avg_N_Size_Q06 = sum(vaibhav(FY16_Capability_Network,'NUMBER OF RESPONDENTS FOR THE WORKGROUP (N SIZE)','Q06.  Development. (MEAN SCORE)'))
FY16_Capability_Network_Avg_N_Size_Q07 = sum(vaibhav(FY16_Capability_Network,'NUMBER OF RESPONDENTS FOR THE WORKGROUP (N SIZE)','Q07.  Opinions Count. (MEAN SCORE)'))
FY16_Capability_Network_Avg_N_Size_Q08 = sum(vaibhav(FY16_Capability_Network,'NUMBER OF RESPONDENTS FOR THE WORKGROUP (N SIZE)','Q08.  Mission/Purpose. (MEAN SCORE)'))
FY16_Capability_Network_Avg_N_Size_Q09 = sum(vaibhav(FY16_Capability_Network,'NUMBER OF RESPONDENTS FOR THE WORKGROUP (N SIZE)','Q09.  Committed to Quality. (MEAN SCORE)'))
FY16_Capability_Network_Avg_N_Size_Q10 = sum(vaibhav(FY16_Capability_Network,'NUMBER OF RESPONDENTS FOR THE WORKGROUP (N SIZE)','Q10.  Best Friend. (MEAN SCORE)'))
FY16_Capability_Network_Avg_N_Size_Q11 = sum(vaibhav(FY16_Capability_Network,'NUMBER OF RESPONDENTS FOR THE WORKGROUP (N SIZE)','Q11.  Progress. (MEAN SCORE)'))
FY16_Capability_Network_Avg_N_Size_Q12 = sum(vaibhav(FY16_Capability_Network,'NUMBER OF RESPONDENTS FOR THE WORKGROUP (N SIZE)','Q12.  Learn and Grow. (MEAN SCORE)'))

FY16_Capability_Network_Q00_Avg_Rating = sum(FY16_Capability_Network['Q00. Weighted Score'])/FY16_Capability_Network_Avg_N_Size_Q00
FY16_Capability_Network_Q01_Avg_Rating = sum(FY16_Capability_Network['Q01. Weighted Score'])/FY16_Capability_Network_Avg_N_Size_Q01
FY16_Capability_Network_Q02_Avg_Rating = sum(FY16_Capability_Network['Q02. Weighted Score'])/FY16_Capability_Network_Avg_N_Size_Q02
FY16_Capability_Network_Q03_Avg_Rating = sum(FY16_Capability_Network['Q03. Weighted Score'])/FY16_Capability_Network_Avg_N_Size_Q03
FY16_Capability_Network_Q04_Avg_Rating = sum(FY16_Capability_Network['Q04. Weighted Score'])/FY16_Capability_Network_Avg_N_Size_Q04
FY16_Capability_Network_Q05_Avg_Rating = sum(FY16_Capability_Network['Q05. Weighted Score'])/FY16_Capability_Network_Avg_N_Size_Q05
FY16_Capability_Network_Q06_Avg_Rating = sum(FY16_Capability_Network['Q06. Weighted Score'])/FY16_Capability_Network_Avg_N_Size_Q06
FY16_Capability_Network_Q07_Avg_Rating = sum(FY16_Capability_Network['Q07. Weighted Score'])/FY16_Capability_Network_Avg_N_Size_Q07
FY16_Capability_Network_Q08_Avg_Rating = sum(FY16_Capability_Network['Q08. Weighted Score'])/FY16_Capability_Network_Avg_N_Size_Q08
FY16_Capability_Network_Q09_Avg_Rating = sum(FY16_Capability_Network['Q09. Weighted Score'])/FY16_Capability_Network_Avg_N_Size_Q09
FY16_Capability_Network_Q10_Avg_Rating = sum(FY16_Capability_Network['Q10. Weighted Score'])/FY16_Capability_Network_Avg_N_Size_Q10
FY16_Capability_Network_Q11_Avg_Rating = sum(FY16_Capability_Network['Q11. Weighted Score'])/FY16_Capability_Network_Avg_N_Size_Q11
FY16_Capability_Network_Q12_Avg_Rating = sum(FY16_Capability_Network['Q12. Weighted Score'])/FY16_Capability_Network_Avg_N_Size_Q12