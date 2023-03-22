import pandas as pd
import numpy as np

pip install scipy

from scipy import stats

pip install seaborn

import seaborn as sns

# Load the dataset
df = pd.read_csv('heart_cleveland_upload.csv')
df

# Create a contingency table of sex and heart disease status
#condition: 0 = no disease, 1 = disease
#sex (1 = male; 0 = female)
data_chi=pd.crosstab(df["sex"],df["condition"])
data_chi


#Perform the Chi-square test
observedValue=data_chi.values
observedValue


value=stats.chi2_contingency(data_chi)
value


expectedValue=value[3]
expectedValue


chi2=value[0]
p=value[1]
dof=value[2]


# Print the test statistic, p-value, and degrees of freedom
print('Chi-square statistic: ', chi2)
print('p-value: ', p)
print('Degrees of freedom: ', dof)


chiSquare=sum([((o-e)**2)/e for o,e in zip(observedValue,expectedValue)])
chiSquare


chiSquareVal=chiSquare.sum()
chiSquareVal


criticalVal=stats.chi2.ppf(q=0.95,df=1)
criticalVal


if chiSquareVal>=criticalVal:
  print('Null Hypothesis H0 is rejected, Ha is accepted.')
  print('There is a relationship btw the two categorical column("sex and heartdisease")')
else:
  print('Null Hypothesis H0 is accepted, Ha is rejected.')
  print('There is a no relationship btw the two categorical column("sex and heartdisease")')


pval=1-stats.chi2.cdf(x=chiSquareVal,df=1)
pval

if pval<0.05:
  print('Null Hypothesis H0 is rejected, Ha is accepted.')
  print('There is a relationship btw the two categorical column("sex and heartdisease")')
else:
  print('Null Hypothesis H0 is accepted, Ha is rejected.')
  print('There is a no relationship btw the two categorical column("sex and heartdisease")')

