#!/usr/bin/env python
# coding: utf-8

# ### Focusing on Data Wrangling
# - CREATING GRAPHS (Colors) [DONE]
# - UNDERSTAND THE RELATIONSHIP BETWEEN FEATURES [DONE]
# - CERATING DUMMIES (ONE HOT ENCODING )
# - SCALING DATA
# - SPLITING DATA IN TRAINING AND TEST [***]
# - SPLITTING DATA INTO FEATURES (INPUTS) AND LABLES (OUTPUTS) [***]

# In[75]:


# Importing Libraries 
import pandas as pd 
import numpy as np
import matplotlib as mp
import matplotlib.pyplot as plt


# In[76]:


# Reading Data
data = pd.read_csv('student_data.csv')
data.head(5)


# In[77]:


# To get initution about the data, lets examine the data set
type(data)
data.dtypes


# In[103]:


# data.isna() returns every single row in the data set. This will give ONLY THOSE ROWS that are NA
nulldata = data[data.isna().any(axis=1)]
print(nulldata)


# In[79]:


# To get the intiution about the situation. Lets visualize how the GRE and GPA impacts the admissions. 
plt.scatter(data.gre, data.gpa, c = data.admit)
plt.xlabel('Student GRE Test Score')
plt.ylabel('Student GPA Grade')


# #### Observation: 
# Looking at the above chart, there is no clear division between sepreates admitted vs. non-admitted. So lets take the rank into consideration. 
# ##### Question: 
# How to assign specific colors to admitted vs. non admitted students? 

# In[81]:


# Taking Rank into consideration. This involves filtering specific values of a feature. 
#So, How do you filter a value and create a subsets of dataframe based on the filter?

data_rank1 = data[data["rank"] == 1]
data_rank1.head(5)


# In[83]:


plt.scatter(data_rank1.gre, data_rank1.gpa, c = data_rank1.admit)
plt.xlabel('Student GRE Test Score')
plt.ylabel('Student GPA Grade')


# In[85]:


data_rank3 = data[data["rank"] == 3]
data_rank3.head(5)


# In[87]:


plt.scatter(data_rank3.gre, data_rank3.gpa, c = data_rank3.admit)
plt.xlabel('Student GRE Test Score')
plt.ylabel('Student GPA Grade')


# # ONE HOT ENCODING
# 
# ### Since the rank plays a important role in showing us relationship between admitted vs. non-admitted student. Lets one hot encode the rank variable
# 
# STEP 1: Concatenate pandas objects along a particular axis with optional set logic along the other axes
# 
# pandas.concat(objs, axis=0, join='outer', join_axes=None, ignore_index=False, keys=None, levels=None, names=None, verify_integrity=False, sort=None, copy=True)[source]
# 
# STEP 2: pandas.get_dummies(data, prefix=None, prefix_sep='', dummyna=False, columns=None, sparse=False, drop_first=False, dtype=None)

# In[94]:


type(data_rank1)
type([data_rank1])


# In[110]:


# Learning Concat 
contact_data_sets = pd.concat([data_rank1, data], axis=0)
contact_data_sets.head(3)


# In[ ]:




