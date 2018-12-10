# -*- coding: utf-8 -*-
"""
Created on Sat Dec  8 09:09:08 2018

@author: Craig Snortheim

--Versions--
Python: 3.7.0
pandas: 0.23.4
matplotlib: 3.0.1
"""

#%%
#set directories / filepaths
dir_data = r".\data"
fn_trans = "dh_transactions.csv"
fn_prod = "dh_product_lookup.csv"

#import modules
import os
import pandas as pd
import matplotlib.pyplot as plt
import dh_lib as dh

#%%
"""
Based on review of the dataset user guide and the case study questions, 
the the target dataset will include a join of the transactions
and product data tables. 

Read in the two data tables and join on the UPC field using pandas
Enforce that upc field is read in as string to maintain the 
integrity of the ID and avoid rounding/truncation errors
"""
#%%
fp_trans = os.path.join(dir_data, fn_trans)
fp_prod = os.path.join(dir_data, fn_prod)
df_trans = pd.read_csv(fp_trans, index_col = 0)
df_prod = pd.read_csv(fp_prod, index_col = 0)

df_trans_join_prod = df_trans.join(df_prod) #default left join on index (upc)

#%%
"""
Field name list for easy reference:
    ['upc', 'dollar_sales', 'units', 'time_of_transaction', 'geography', 'week',
       'household', 'store', 'basket', 'day', 'coupon', 'product_description',
       'commodity', 'brand', 'product_size']
    
"""
#%%check unique entries in commodity field
print(set(df_trans_join_prod["commodity"]))
cats = ["syrups", "pancake mixes", "pasta sauce", "pasta"] #set desired order
#%%

"""
a.	What are the top 5 products in each commodity?
b.	What are the top 5 brands in each commodity?

We could look at these questions on a unit or sales basis.
Units provides a more normalized view across the commodities, while
the sales figures provide insight into contribution to revenues.  
Both have value, so we'll do both.
We consider the entire timeframe and all geographies in this analysis.

"""


#%% BY PRODUCT
keep_fields_prod = ["product_description", "commodity", "brand", 
               "dollar_sales", "units"]

df_agg_prod = df_trans_join_prod[keep_fields_prod].groupby(keep_fields_prod[:3], 
                           as_index = False).sum()

#Top 5 products in each commodity by total sales
dh.plot_top5_barh(df= df_agg_prod, cat_field = "commodity", cats = cats, 
             target_field = "dollar_sales", vert_axis = "product_description",
             horz_label = "Total Sales ($)")

#Top 5 products in each commodity by units
dh.plot_top5_barh(df= df_agg_prod, cat_field = "commodity", cats = cats, 
             target_field = "units", vert_axis = "product_description",
             horz_label = "Units Sold")

#%%


#%% BY BRAND
keep_fields_brand = ["commodity", "brand", "dollar_sales", "units"]

df_agg_brand = df_trans_join_prod[keep_fields_brand].groupby(keep_fields_brand[:2], 
                           as_index = False).sum()

#Top 5 brands in each commodity by total sales
dh.plot_top5_barh(df= df_agg_brand, cat_field = "commodity", cats = cats, 
             target_field = "dollar_sales", vert_axis = "brand",
             horz_label = "Total Sales ($)")

#Top 5 brands in each commodity by units
dh.plot_top5_barh(df= df_agg_brand, cat_field = "commodity", cats = cats, 
             target_field = "units", vert_axis = "brand",
             horz_label = "Units Sold")
#%%


