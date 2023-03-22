#!/usr/bin/env python
# coding: utf-8

# In[10]:


import pandas as pd
import numpy as np


# In[11]:


pip install scipy


# In[12]:


from scipy import stats


# In[2]:


pip install seaborn


# In[4]:


import seaborn as sns


# In[6]:


# Load the dataset
df = pd.read_csv('heart_cleveland_upload.csv')
df


# In[7]:


# Create a contingency table of sex and heart disease status
#condition: 0 = no disease, 1 = disease
#sex (1 = male; 0 = female)
data_chi=pd.crosstab(df["sex"],df["condition"])
data_chi


# In[8]:


#Perform the Chi-square test
observedValue=data_chi.values
observedValue


# In[14]:


value=stats.chi2_contingency(data_chi)
value


# In[15]:


expectedValue=value[3]
expectedValue


# In[17]:


chi2=value[0]
p=value[1]
dof=value[2]


# In[18]:


# Print the test statistic, p-value, and degrees of freedom
print('Chi-square statistic: ', chi2)
print('p-value: ', p)
print('Degrees of freedom: ', dof)


# In[19]:


chiSquare=sum([((o-e)**2)/e for o,e in zip(observedValue,expectedValue)])
chiSquare


# In[20]:


chiSquareVal=chiSquare.sum()
chiSquareVal


# In[24]:


criticalVal=stats.chi2.ppf(q=0.95,df=1)
criticalVal


# In[26]:


if chiSquareVal>=criticalVal:
  print('Null Hypothesis H0 is rejected, Ha is accepted.')
  print('There is a relationship btw the two categorical column("sex and heartdisease")')
else:
  print('Null Hypothesis H0 is accepted, Ha is rejected.')
  print('There is a no relationship btw the two categorical column("sex and heartdisease")')


# In[27]:


pval=1-stats.chi2.cdf(x=chiSquareVal,df=1)
pval


# In[28]:


if pval<0.05:
  print('Null Hypothesis H0 is rejected, Ha is accepted.')
  print('There is a relationship btw the two categorical column("sex and heartdisease")')
else:
  print('Null Hypothesis H0 is accepted, Ha is rejected.')
  print('There is a no relationship btw the two categorical column("sex and heartdisease")')

