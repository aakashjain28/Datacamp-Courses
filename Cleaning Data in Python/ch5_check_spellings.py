# Create a Series called countries consisting of the 'country' column of gapminder.
# Drop all duplicates from countries using the .drop_duplicates() method.
# Write a regular expression that tests your assumptions of what characters belong in countries:
# Anchor the pattern to match exactly what you want by placing a ^ in the beginning and $ in the end.
# Use A-Za-z to match the set of lower and upper case letters, \. to match periods, and \s to match whitespace between words.
# Use str.contains() to create a Boolean vector representing values that match the pattern.
# Invert the mask by placing a ~ before it.
# Subset the countries series using the .loc[] accessor and mask_inverse. Then hit 'Submit Answer' to see the invalid country names!

# Create the series of countries: countries
countries = pd.Series(gapminder.country)

# Drop all the duplicates from countries
countries = countries.drop_duplicates()

# Write the regular expression: pattern
pattern = '^[A-Za-z\.\s]*$'

# Create the Boolean vector: mask
mask = countries.str.contains(pattern)

# Invert the mask: mask_inverse
mask_inverse = ~mask

# Subset countries using mask_inverse: invalid_countries
invalid_countries = countries.loc[mask_inverse]

# Print invalid_countries
print(invalid_countries)
