# Convert the year column of gapminder using pd.to_numeric().
# Assert that the country column is of type np.object. This has been done for you.
# Assert that the year column is of type np.int64.
# Assert that the life_expectancy column is of type np.float64.

# Convert the year column to numeric
gapminder.year = pd.to_numeric(gapminder.year)

# Test if country is of type object
assert gapminder.country.dtypes == np.object

# Test if year is of type int64
assert gapminder.year.dtypes == np.int64

# Test if life_expectancy is of type float64
assert gapminder.life_expectancy.dtypes == np.float64
