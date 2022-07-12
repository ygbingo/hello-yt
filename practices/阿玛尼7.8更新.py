#!/usr/bin/env python
# coding: utf-8

# In[10]:


import pandas as pd
df=pd.read_excel("./商品属性表1 0707 lite.xlsx",sheet_name="阿玛尼")
df


# In[17]:


for idx, _ in df.iterrows():
    if not isinstance(df.iloc[idx,6], str):
        continue
    df.iloc[idx,6] = df.iloc[idx,6].replace(" ","，")
df.to_excel("./amani_label.xlsx",sheet_name="amani",index=False)


# In[28]:


df2=pd.read_excel("./amani_label.xlsx")
a=list(df2.loc[0:147,'Unnamed: 9'])
a


# In[30]:





# In[ ]:




