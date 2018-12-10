# -*- coding: utf-8 -*-
"""
Created on Sun Dec  9 16:36:53 2018

@author: Craig
"""

import pandas as pd

def get_nLargest_byCat(df, cat_field, cats, target_field, n = 5):
    """
    Helper function to return the n largest (default 5) records in df
    based on summation of target_field, for each category of 
    'cats' in the cat_field
    """
    df_out = pd.DataFrame(columns = df.columns)
    
    for cat in cats:  
        subdf = df[df[cat_field] == cat]
        df_out = df_out.append(subdf.nlargest(n, target_field).
                               sort_values(target_field, ascending = True))
        
    return df_out


def plot_top5_barh(df, cat_field, cats, target_field, vert_axis, horz_label):

    df_top5_prod_sales = get_nLargest_byCat(df = df, cat_field = cat_field,
                                            cats = cats, 
                                            target_field = target_field)
    
    colors = ["tab:blue"]*5 + ["tab:orange"]*5 + ["tab:green"]*5 + ["tab:purple"]*5 
    ax = df_top5_prod_sales.plot(kind = "barh", x = vert_axis, 
                            y = target_field, color = colors, legend = None)
    ax.set_xlabel(horz_label)
    ax.set_ylabel(None)