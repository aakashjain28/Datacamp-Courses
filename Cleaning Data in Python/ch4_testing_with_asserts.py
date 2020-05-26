# Write an assert statement to confirm that there are no missing values in ebola.
    # Use the pd.notnull() function on ebola (or the .notnull() method of ebola) and chain two .all() methods (that is, .all().all()). The first .all() method will return a True or False for each column, while the second .all() method will return a single True or False.
# Write an assert statement to confirm that all values in ebola are greater than or equal to 0.
# Chain two all() methods to the Boolean condition (ebola >= 0).

# Assert that there are no missing values
assert pd.notnull(ebola.all().all())

# Assert that all values are >= 0
assert (ebola >= 0).all().all()
