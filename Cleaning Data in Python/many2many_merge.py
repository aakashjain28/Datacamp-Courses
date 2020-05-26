# The final merging scenario occurs when both DataFrames do not have unique keys for a merge. What happens here is that for each duplicated key, every pairwise combination will be created.

# Two example DataFrames that share common key values have been pre-loaded: df1 and df2. Another DataFrame df3, which is the result of df1 merged with df2, has been pre-loaded. All three DataFrames have been printed - look at the output and notice how pairwise combinations have been created. This example is to help you develop your intuition for many-to-many merges.

# Here, you'll work with the site and visited DataFrames from before, and a new survey DataFrame. Your task is to merge site and visited as you did in the earlier exercises. You will then merge this merged DataFrame with survey.

# Begin by exploring the site, visited, and survey DataFrames in the IPython Shell.

# import pandas
import pandas as pd

# Merge site and visited: m2m
m2m = pd.merge(left=site, right=visited, left_on=site['name'], right_on=visited['site'])

# Merge m2m and survey: m2m
m2m = pd.merge(left=m2m, right=survey, left_on=m2m['ident'], right_on=survey['taken'])

# Print the first 20 lines of m2m
print(m2m.head(20))
