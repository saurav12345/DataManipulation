#!/usr/bin/env python
# coding: utf-8

import pandas as pd
import numpy as np

Aug19ToMar20_DF = pd.read_excel(r"C:\Users\saurav.an.kumar\Desktop\PO Skip Analysis\19 20 Data\India PO requestor skip Analysis_08.2019 - 03.2020.xlsx",sheet_name='Data')

Sep18ToJul19_DF = pd.read_excel(r"C:\Users\saurav.an.kumar\Desktop\PO Skip Analysis\PO Biz Case Data-Sep'18 to Jul'19.xlsx",sheet_name='Payment Excl Air Travel')

#print(Aug19ToMar20_DF.head())
#Aug19ToMar20_DF = Aug19ToMar20_DF[((Aug19ToMar20_DF['Invoice Year'] == 2019) & (Aug19ToMar20_DF['Invoice Month'].isin(['Aug','Sep','Oct','Nov','Dec']))) | (Aug19ToMar20_DF['Invoice Year'] == 2020)]
#Aug19ToMar20_DF[['Invoice Year','Invoice Month']].apply(pd.Series.value_counts)
Aug19ToMar20_DF.head()

Aug19ToMar20_DF.describe()

Sep18ToJul19_DF.shape

Sep18ToJul19_DF = Sep18ToJul19_DF[Sep18ToJul19_DF['Month'].isin(['Sep-18','Oct-18','Nov-18','Dec-18','Jan-19','Feb-19','Mar\'19','Apr\'19','May\'19','Jun\'19','Jul\'19'])]
Sep18ToJul19_DF.describe()

#print(Aug19ToMar20_DF.shape)
print(Sep18ToJul19_DF.shape)

Sep18ToJul19_DF.head()

Aug19ToMar20_DF.dtypes

Sep18ToJul19_DF.dtypes

Aug19ToMar20_DF['Payable Amount (USD)'] = abs(Aug19ToMar20_DF['Payable Amount (USD)'])
Aug19ToMar20_DF['Payable Amount (USD)'].head()

LowCostInvoices_Aug19ToMar20 = Aug19ToMar20_DF.loc[Aug19ToMar20_DF['Payable Amount (USD)'] < 500,['Invoice Approval Completion month','Supplier Name','Requestor Name','Spend Category','Payable Amount (USD)']]
#LowCostInvoices_Aug19ToMar20['Invoice Approval Completion month'] = LowCostInvoices_Aug19ToMar20['Invoice Approval Completion month'].map(str)
LowCostInvoices_Aug19ToMar20.head()

LowCostInvoices_Aug19ToMar20_GroupedSingle = LowCostInvoices_Aug19ToMar20.groupby(['Invoice Approval Completion month','Supplier Name','Requestor Name','Spend Category']).agg({'Payable Amount (USD)':'sum','Supplier Name':'count'})
LowCostInvoices_Aug19ToMar20_GroupedSingle.columns = ['Low Cost Invoice Amount','Vendor Count']
LowCostInvoices_Aug19ToMar20_GroupedSingle = LowCostInvoices_Aug19ToMar20_GroupedSingle.reset_index()
LowCostInvoices_Aug19ToMar20_GroupedSingle.head()

Aug19ToMar20_GroupedSingle = Aug19ToMar20_DF.groupby(['Invoice Approval Completion month','Supplier Name','Requestor Name','Spend Category']).agg({'Payable Amount (USD)':'sum','Supplier Name':'count'})
Aug19ToMar20_GroupedSingle.columns = ['Overall Invoice Amount','Overall Vendor Count']
Aug19ToMar20_GroupedSingle = Aug19ToMar20_GroupedSingle.reset_index()
Aug19ToMar20_GroupedSingle.head()

ListOfAnalyticsNo1_Aug19ToMar20 = Aug19ToMar20_GroupedSingle.merge(LowCostInvoices_Aug19ToMar20_GroupedSingle, how='left').fillna(0)
ListOfAnalyticsNo1_Aug19ToMar20.head()

#a = Sep18ToJul19_GroupedSingle_Summary.merge(LowCostInvoices_Sep18ToJul19_GroupedSingle,how='left').fillna(0)
#a['Vendor_Count'] = a['Vendor_Count'].astype(int)
#a.head()

ListOfAnalyticsNo1_Aug19ToMar20['Vendor Count Percentage'] = ListOfAnalyticsNo1_Aug19ToMar20['Vendor Count'] * 100 / ListOfAnalyticsNo1_Aug19ToMar20['Overall Vendor Count']
ListOfAnalyticsNo1_Aug19ToMar20['Vendor Count Percentage'] = ListOfAnalyticsNo1_Aug19ToMar20['Vendor Count Percentage'].map(lambda x: '%2.2f' % x).map(str) + '%'
column_names = ['Invoice Approval Completion month', 'Supplier Name', 'Requestor Name', 'Spend Category','Low Cost Invoice Amount','Overall Invoice Amount','Vendor Count','Overall Vendor Count','Vendor Count Percentage']
ListOfAnalyticsNo1_Aug19ToMar20 = ListOfAnalyticsNo1_Aug19ToMar20.reindex(columns=column_names)
ListOfAnalyticsNo1_Aug19ToMar20.head()

ListOfAnalyticsNo1_Aug19ToMar20.to_excel("C:\\Users\\saurav.an.kumar\\Desktop\\PO Skip Analysis\\Output\\PostPeriodAnalyticsNo1.xlsx".format('xlsxwriter'), sheet_name='PostPeriodAnalyticsNo1', index=False, encoding='utf8')

Sep18ToJul19_DF['Amt LC2'] = Sep18ToJul19_DF[['Amt LC2']] * (-1)
Sep18ToJul19_DF['Amt LC2'].head()

Sep18ToJul19_DF['Year'] = Sep18ToJul19_DF['Year'].map(str)

LowCostInvoices_Sep18ToJul19 = Sep18ToJul19_DF.loc[Sep18ToJul19_DF['Amt LC2'] < 500,['Month','Vendor Name','Requestor Name / Pre Approved','Spend Category','Amt LC2']]
LowCostInvoices_Sep18ToJul19.tail()

LowCostInvoices_Sep18ToJul19.shape

LowCostInvoices_Sep18ToJul19_GroupedSingle = LowCostInvoices_Sep18ToJul19.groupby(['Month','Vendor Name','Requestor Name / Pre Approved','Spend Category']).agg({'Amt LC2':'sum','Vendor Name':'count'})
LowCostInvoices_Sep18ToJul19_GroupedSingle.columns = ['Amt LC2','Vendor_Count']
LowCostInvoices_Sep18ToJul19_GroupedSingle = LowCostInvoices_Sep18ToJul19_GroupedSingle.reset_index()
LowCostInvoices_Sep18ToJul19_GroupedSingle.head()

LowCostInvoices_Sep18ToJul19_GroupedSingle.shape

Sep18ToJul19_GroupedSingle = Sep18ToJul19_DF.groupby(['Month','Vendor Name','Requestor Name / Pre Approved','Spend Category']).agg({'Amt LC2':'sum','Vendor Name':'count'})
Sep18ToJul19_GroupedSingle.columns = ['Overall PO Cost','Overall Vendor Count']
Sep18ToJul19_GroupedSingle = Sep18ToJul19_GroupedSingle.reset_index()
Sep18ToJul19_GroupedSingle.head()

Sep18ToJul19_GroupedSingle.shape

ListOfAnalyticsNo1_Sep18ToJul19 = LowCostInvoices_Sep18ToJul19_GroupedSingle.merge(Sep18ToJul19_GroupedSingle, on=['Month', 'Vendor Name', 'Requestor Name / Pre Approved', 'Spend Category'])
ListOfAnalyticsNo1_Sep18ToJul19.loc[ListOfAnalyticsNo1_Sep18ToJul19['Vendor Name']=='A N S Electricals Pvt. Ltd.',].fillna(0).head()
#ListOfAnalyticsNo1_Sep18ToJul19.head()

ListOfAnalyticsNo1_Sep18ToJul19['Vendor Count Percentage'] = ListOfAnalyticsNo1_Sep18ToJul19['Vendor_Count'] * 100 / ListOfAnalyticsNo1_Sep18ToJul19['Overall Vendor Count']
ListOfAnalyticsNo1_Sep18ToJul19['Vendor Count Percentage'] = ListOfAnalyticsNo1_Sep18ToJul19['Vendor Count Percentage'].map(lambda x: '%2.2f' % x).map(str) + '%'
ListOfAnalyticsNo1_Sep18ToJul19['Amt LC2 Percentage'] = ListOfAnalyticsNo1_Sep18ToJul19['Amt LC2'] * 100 / ListOfAnalyticsNo1_Sep18ToJul19['Overall PO Cost']
ListOfAnalyticsNo1_Sep18ToJul19['Amt LC2 Percentage'] = ListOfAnalyticsNo1_Sep18ToJul19['Amt LC2 Percentage'].map(lambda x: '%2.2f' % x).map(str) + '%'
column_names = ['Month', 'Vendor Name', 'Requestor Name / Pre Approved', 'Spend Category','Amt LC2','Overall PO Cost','Vendor_Count','Overall Vendor Count','Amt LC2 Percentage','Vendor Count Percentage']
ListOfAnalyticsNo1_Sep18ToJul19 = ListOfAnalyticsNo1_Sep18ToJul19.reindex(columns=column_names)
ListOfAnalyticsNo1_Sep18ToJul19.head()

ListOfAnalyticsNo1_Sep18ToJul19 = LowCostInvoices_Sep18ToJul19_GroupedSingle.merge(Sep18ToJul19_GroupedSingle, on=['Month', 'Vendor Name', 'Requestor Name / Pre Approved', 'Spend Category'], how='right')
#ListOfAnalyticsNo1_Sep18ToJul19.loc[ListOfAnalyticsNo1_Sep18ToJul19['Vendor Name']=='A N S Electricals Pvt. Ltd.',].fillna(0).head()
ListOfAnalyticsNo1_Sep18ToJul19.head()

ListOfAnalyticsNo1_Sep18ToJul19.shape

ListOfAnalyticsNo1_Sep18ToJul19.to_excel("C:\\Users\\saurav.an.kumar\\Desktop\\PO Skip Analysis\\Output\\New Folder\\AnalyticsNo1_Sep18ToJul19_1.xlsx".format('xlsxwriter'), sheet_name='AnalyticsNo1_Sep18ToJul19_1', index=False, encoding='utf8')

Sep18ToJul19_GroupedSingle_Summary = Sep18ToJul19_DF.groupby(['Month','Vendor Name','Requestor Name / Pre Approved','Spend Category']).agg({'Amt LC2':'sum','Vendor Name':'count'})
Sep18ToJul19_GroupedSingle_Summary.columns = ['Overall PO Cost','Overall Vendor Count']
Sep18ToJul19_GroupedSingle_Summary = Sep18ToJul19_GroupedSingle_Summary.reset_index()
Sep18ToJul19_GroupedSingle_Summary.tail()

Sep18ToJul19_GroupedSingle_Summary.loc[Sep18ToJul19_GroupedSingle_Summary['Vendor Name']=='A N S Electricals Pvt. Ltd.',].head()

a = Sep18ToJul19_GroupedSingle_Summary.merge(LowCostInvoices_Sep18ToJul19_GroupedSingle,how='left').fillna(0)
a['Vendor_Count'] = a['Vendor_Count'].astype(int)
a.head()

column_names = ['Month', 'Vendor Name', 'Requestor Name / Pre Approved', 'Spend Category','Amt LC2','Overall PO Cost','Vendor_Count','Overall Vendor Count']
a = a.reindex(columns=column_names)
a.head()

a.to_excel("C:\\Users\\saurav.an.kumar\\Desktop\\PO Skip Analysis\\Output\\New Folder\\AnalyticsNo1_Sep18ToJul19_2.xlsx".format('xlsxwriter'), sheet_name='AnalyticsNo1_Sep18ToJul19_2', index=False, encoding='utf8')

LowCostInvoices_Sep18ToJul19_GroupedSingle_Summary.shape

Sep18ToJul19_GroupedSingle_Summary = Sep18ToJul19_DF.groupby(['Year','Month','Vendor Name']).agg({'Amt LC2':'sum','Vendor Name':'count'})
Sep18ToJul19_GroupedSingle_Summary.columns = ['Overall PO Cost','Overall Vendor Count']
Sep18ToJul19_GroupedSingle_Summary = Sep18ToJul19_GroupedSingle_Summary.reset_index()
Sep18ToJul19_GroupedSingle_Summary.tail(20)

Sep18ToJul19_GroupedSingle_Summary.shape

ListOfAnalyticsNo1_Sep18ToJul19_Summary = LowCostInvoices_Sep18ToJul19_GroupedSingle_Summary.merge(Sep18ToJul19_GroupedSingle_Summary, on=['Year', 'Month', 'Vendor Name'], how='left')
ListOfAnalyticsNo1_Sep18ToJul19_Summary.tail(20)

ListOfAnalyticsNo1_Sep18ToJul19_Summary['Vendor Count Percentage'] = ListOfAnalyticsNo1_Sep18ToJul19_Summary['Vendor_Count'] * 100 / ListOfAnalyticsNo1_Sep18ToJul19_Summary['Overall Vendor Count']
ListOfAnalyticsNo1_Sep18ToJul19_Summary['Vendor Count Percentage'] = ListOfAnalyticsNo1_Sep18ToJul19_Summary['Vendor Count Percentage'].map(lambda x: '%2.2f' % x).map(str) + '%'
ListOfAnalyticsNo1_Sep18ToJul19_Summary['Amt LC2 Percentage'] = ListOfAnalyticsNo1_Sep18ToJul19_Summary['Amt LC2'] * 100 / ListOfAnalyticsNo1_Sep18ToJul19_Summary['Overall PO Cost']
ListOfAnalyticsNo1_Sep18ToJul19_Summary['Amt LC2 Percentage'] = ListOfAnalyticsNo1_Sep18ToJul19_Summary['Amt LC2 Percentage'].map(lambda x: '%2.2f' % x).map(str) + '%'
column_names = ['Year', 'Month', 'Vendor Name','Amt LC2','Overall PO Cost','Vendor_Count','Overall Vendor Count','Amt LC2 Percentage','Vendor Count Percentage']
ListOfAnalyticsNo1_Sep18ToJul19_Summary = ListOfAnalyticsNo1_Sep18ToJul19_Summary.reindex(columns=column_names)
ListOfAnalyticsNo1_Sep18ToJul19_Summary.tail(40)

ListOfAnalyticsNo1_Sep18ToJul19_Summary.to_excel("C:\\Users\\saurav.an.kumar\\Desktop\\PO Skip Analysis\\Output\\Sep18ToJul19_Summary_1.xlsx".format('xlsxwriter'), sheet_name='Sep18ToJul19_Summary_1', index=False, encoding='utf8')