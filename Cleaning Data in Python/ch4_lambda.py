# Use the .replace() method inside a lambda function to remove the dollar sign from the 'total_dollar' column of tips.
# You need to specify two arguments to the .replace() method: The string to be replaced ('$'), and the string to replace it by ('').
# Apply the lambda function over the 'total_dollar' column of tips.
# Use a regular expression to remove the dollar sign from the 'total_dollar' column of tips.
# The pattern has been provided for you: It is the first argument of the re.findall() function.
# Complete the rest of the lambda function and apply it over the 'total_dollar' column of tips. Notice that because re.findall() returns a list, you have to slice it in order to access the actual value.

import re

# Write the lambda function using replace
tips['total_dollar_replace'] = tips.total_dollar.apply(lambda x: x.replace('$', ''))

# Write the lambda function using regular expressions
tips['total_dollar_re'] = tips.total_dollar.apply(lambda x: re.findall('\d+\.\d+', x)[0])

# Print the head of tips
print(tips.head())
