#!/usr/bin/env python
# coding: utf-8

# In[8]:


import pandas as pd 
import numpy as ny 
import matplotlib.pyplot as plt 
import seaborn as sns 


# In[9]:


df = pd.read_csv("/Users/huzaibibnishafi/Documents/Python projects/results.csv")


# In[10]:


df


# In[11]:


df.columns


# In[12]:


df.describe()


# In[17]:


sns.pairplot(df)


# In[ ]:





# In[ ]:




