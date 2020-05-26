# Chapter 1 - Highlighting Data

## Hardcoding a highlight

You are working with the city of Houston to look at the relationship between sulfur dioxide (SO2) and nitrogen dioxide (NO2) pollution, specifically, pollution in the most recent year data was collected (2014). You have singled out a particularly bad day, November 26th, where there was a bad spike in the SO2 levels. To draw the viewers attention to this bad day, you will highlight it in a bright orangish-red and color the rest of the points gray.

pandas, matplotlib.pyplot, and seaborn are loaded as pd, plt, and sns, respectively, and will be available in your workspace for the rest of the course.

This course touches on a lot of concepts you may have forgotten, so if you ever need a quick refresher, download the @[Seaborn Cheat Sheet](https://datacamp-community-prod.s3.amazonaws.com/f9f06e72-519a-4722-9912-b5de742dbac4) and keep it handy!

### INSTRUCTIONS
- Modify the list comprehension to color the value corresponding to the 330th day (November 26th) of the year 2014 to orangered and the rest of the points to lightgray.
- Pass the houston_colors array to regplot() using the scatter_kws argument to color the points.

## Programmatically creating a highlight
You are continuing your work for the city of Houston. Now you want to look at the behavior of both NO2 and SO2 when the un-plotted ozone (O3) value was at its highest.

To do this, replace the logic in the current list comprehension with one that compares a row's O3 value with the highest observed O3 in the dataset. Note: use sns.scatterplot() instead of sns.regplot(). This is because sns.scatterplot() can take a non-color vector as its hue argument and colors the points automatically while providing a helpful legend.

### INSTRUCTIONS
- Find the value corresponding to the highest observed O3 value in the houston_pollution DataFrame.
- Append the column 'point type' to the houston_pollution DataFrame to mark if the row contains the highest observed O3.
- Pass this newly created column to the hue argument of sns.scatterplot() to color the points.

## Comparing with 2 KDEs
Imagine that you work for the premier air-filter provider. Your company has asked you to build a report that looks into why 2012 was a particularly good year for sales of your ozone (O3) filter. You downloaded some helpful pollution data from the USGS, and you want to make a concise visualization that compares the general pattern of O3 pollution for 2012 to all other years on record.

To do this, you can build two overlaid kernel density estimation plots (KDEs): one for 2012 O3 data and one for all other years.

### INSTRUCTIONS
- Filter the data in the first sns.kdeplot() call to include only the year 2012.
- Shade under the first KDE with the shade argument.
- Add the label '2012' for the plot legend.
- Repeat the first three steps for second sns.kdeplot() call, but filter the data to not include 2012. Use the label 'other years'.

## Improving your KDEs
One way of enhancing KDEs is with the addition of a rug plot. Rug plots are little dashes drawn beneath the density that show precisely where each data point falls. Adding a rug plot is particularly useful when you don't have a ton of data.

With small amounts of data you often have gaps along your support with no data, and it can be hard to tell whether a non-zero KDE line means data was present or is due to a wide kernel. A rug plot helps address this.

Let's return to the sns.distplot() function to draw two KDEs: one looking at the data for Vandenberg Air Force Base and the other looking at all the other cities in the pollution data. Since there is much less data contributing to the shape of the Vandenberg plot, add a rug plot beneath it.

### INSTRUCTIONS
- Turn off the histogram overlay for the first plot.
- Make the Vandenberg plot 'steelblue'.
- Turn on rug plot functionality in the Vandenberg plot.
- Remove histogram from the non-Vandenberg plot and set its color to 'gray'.

## Beeswarms
Build a beeswarm plot using sns.swarmplot() that looks at the Ozone levels for all the cities in the pollution data for the month of March. To make the beeswarm a bit more legible, decrease the point size to avoid the overcrowding caused by the many points drawn on the screen. Last, since you've done some manipulation of the data to make this plot, provide a title to help the reader orient with what they are viewing.

### INSTRUCTIONS
- Subset the pollution data to include just the observations in March.
- Plot the O3 levels as the continuous value in the swarmplot().
- Decrease the point size to 3 to avoid crowding of the points.
- Title the plot 'March Ozone levels by city'.

## A basic text annotation
On the current scatter plot, you can see a particularly prominent point that contains the largest SO2 value observed for August. This point is Cincinnati on August 11th, 2013; however, you would not be able to learn this information from the plot in its current form. Basic text annotations are great for pointing out interesting outliers and giving a bit more information. Draw the readers attention to this Cincinnati value by adding a basic text annotation that gives a bit of the background about this outlier.

### INSTRUCTIONS
- Filter the data plotted in scatter plot to just August.
- Draw text annotation at x = 0.57 and y = 41 to call out the highest SO2 value.
- Label annotation with 'Cincinnati had highest observed\nSO2 value on Aug 11, 2013' (note the line break).
- Change the font-size to 'large' for the annotation.

## Arrow annotations
Imagine you are a city planner for Long Beach, California. Long Beach is located on the Pacific Ocean and has a large firework show every New Year's Eve. You want to look into if this show negatively impacts the air quality of the city. To do this, you will look at CO and NO2 levels on New Year's Day. However, it turns out that New Year's Day is not one of the outliers in the plot on the right, it's located in one of the more crowded areas.

To help guide the reader to this point, you'll use an annotation along with an arrow that points to the New Year's Day value. This will provide a nice annotation that explains what the viewer is looking while printing the text in a less crowded region of the plot.

### INSTRUCTIONS
- Grab the row from jan_pollution that corresponds to New Years Day 2012 in the city of Long Beach using the pandas' .query() method.
- Use the CO and NO2 column values from the lb_newyears DataFrame to place the endpoint of the arrow.
- Place the annotation arrow's text in the bottom left corner of the display at x = 2, y = 15.
- 'shrink' the arrow to 0.03, so it doesn't occlude the point of interest.

## Combining annotations and color

You believe that Long Beach, California has a smog problem. Using the pollution data, you'll attempt to make a point for increasing smog reduction regulations using your data visualization wizardry. Specifically, you want to focus on the relationship of CO to O3 levels during 2014 at a city council meeting.

To emphasize how Long Beach compares to a set of peer cities, you've decided to highlight Long Beach and draw attention to a particularly bad day where the CO level was 1.6 and O3 was 0.072 using an annotation.

### INSTRUCTIONS
1. Using a list comprehension, make a vector of colors for each point with'orangered' if the point belongs to Long Beach, and 'lightgray' if it doesn't.
2. Second set of instructions
    1. Use the is_lb vector to provide custom colors for each point using the additional keyword argument facecolors in the scatter_kws argument.
    2. In the same scatter_kws dictionary, set the opacity to 0.3.
3. Add an annotation at x = 1.6 and y = 0.072 using the text 'April 30th, Bad Day' to draw attention to a specific point in the data.
