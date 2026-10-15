
import pandas as pd
from scipy import stats
def read_data(awake_path,sedated_path):
  
  awake_df = pd.read_csv(awake_path)
  sedate_df = pd.read_csv(sedated_path)
  awake_df=awake_df.drop(columns=['Unnamed: 0'])
  sedate_df=sedate_df.drop(columns=['Unnamed: 0'])
  return awake_df,sedate_df


def ttest(feature,awake_df,sedate_df):
# 1. Define sample data
  group_a = awake_df[feature]
  group_b = sedate_df[feature]

# 2. Perform the two-sample t-test
  t_stat, p_value = stats.ttest_ind(group_a, group_b, equal_var=False)

# 3. Print the results
  print(f"T-statistic: {t_stat:.4f}")
  print(f"P-value: {p_value:.4f}")
  if p_value<0.05:
    return print('reject null hypothesis: the means have significant difference')
  else:
    return print('cannot reject null hypothesis: the means have no significant difference')
