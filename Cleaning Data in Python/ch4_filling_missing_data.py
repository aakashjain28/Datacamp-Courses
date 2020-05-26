# Calculate the mean of the Ozone column of airquality using the .mean() method on airquality.Ozone.
# Use the .fillna() method to replace all the missing values in the Ozone column of airquality with the mean, oz_mean.
# Hit 'Submit Answer' to see the result of filling in the missing values!

# Calculate the mean of the Ozone column: oz_mean
oz_mean = airquality.Ozone.mean()

# Replace all the missing values in the Ozone column with the mean
airquality['Ozone'] = airquality.Ozone.fillna(oz_mean)

# Print the info of airquality
print(airquality.info())
