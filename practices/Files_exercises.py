#!/usr/bin/env python
# coding: utf-8

# In[12]:


with open ('Desktop/data.txt','r',encoding='UTF-8') as f:
    data=f.read()
    print('context{}'.format(data))


# In[26]:


import zipfile
with zipfile.ZipFile('Desktop/党史.zip','r') as zipobj:
    files=zipobj.namelist()
    for file in files:
        try:
            file = file.encode('cp437').decode('gbk')
        except:
            file = file.encode('utf-8').decode('utf-8')
        print(file)


# In[ ]:





# In[ ]:




