# Extracting numerical values from strings
# Extracting numbers from strings is a common task, particularly when working with unstructured data or log files.

# Say you have the following string: 'the recipe calls for 6 strawberries and 2 bananas'.

# It would be useful to extract the 6 and the 2 from this string to be saved for later use when comparing strawberry to banana ratios.

# When using a regular expression to extract multiple numbers (or multiple pattern matches, to be exact), you can use the re.findall() function. Dan did not discuss this in the video, but it is straightforward to use: You pass in a pattern and a string to re.findall(), and it will return a list of the matches.

# Import the regular expression module
import re

# Find the numeric values: matches
matches = re.findall('\d+', 'the recipe calls for 10 strawberries and 1 banana')

# Print the matches
print(matches)
