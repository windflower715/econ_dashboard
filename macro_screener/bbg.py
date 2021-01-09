#!/usr/bin/env python
# coding: utf-8

# In[25]:


import pdblp
import warnings
warnings.filterwarnings("ignore")
import pandas as pd 


# In[29]:


def bdh(ticker,flds,start, end):
    con = pdblp.BCon(debug=False, port=8194, timeout=5000)
    con.start()
    result = con.bdh([ticker],flds,
                start, end).reset_index()
    result.columns = ['asofdate',ticker]
    result.set_index('asofdate', inplace = True)
    result.index = pd.to_datetime(result.index)
    result[ticker] = result[ticker].astype(float)
    return result


# In[32]:


def bdh_bulk(tkrdict, start_date, end_date): 
    """bdh_bulk ({'spx':'SPX Index','nasdaq':'CCMP Index'},'19900101','20300101')"""
    df = {k:bdh(v,'PX_LAST',start_date,end_date) for k,v in tkrdict.items()}
    df = pd.concat(df, axis =1)
    df.columns = df.columns.droplevel(level=1)
    return df


# In[37]:


def bdh_bulk_flds(tkrdict,flds, start_date, end_date): 
    df = {k:bdh(v,flds,start_date,end_date) for k,v in tkrdict.items()}
    df = pd.concat(df, axis =1)
    df.columns = df.columns.droplevel(level=1)
    return df


# In[ ]:




