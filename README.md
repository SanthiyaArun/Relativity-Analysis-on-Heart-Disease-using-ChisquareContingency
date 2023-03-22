# Relativity-Analysis-on-Heart-Disease-using-ChisquareContingency
A chi-square test is a statistical test that is used to determine if there is a significant association between two categorical variables.

Import the necessary modules: scipy.stats and pandas for data manipulation and analysis.
import pandas as pd
from scipy.stats import chi2_contingency

Load the heart disease data into a pandas dataframe.
df = pd.read_csv('heart_disease_data.csv')

Create a contingency table of the two categorical variables
contingency_table = pd.crosstab(df['X'], df['Y'])

Use the chi2_contingency function to perform the chi-square test and obtain the test statistic, p-value, degrees of freedom, and expected frequencies.
statistic, p_value, dof, expected_freq = chi2_contingency(contingency_table)

Interpret the results. If the p-value is less than your chosen significance level (e.g., 0.05), you can reject the null hypothesis that there is no association between the two variables. This would suggest that there is a significant association between heart disease and smoking.
