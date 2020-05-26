# Chapter 2 - Using color in visualizations

## Getting rid of unnecessary color

You might want to compare the relationship CO to NO2 values across cities using a simple scatter plot with color to differentiate the different cities' data.

![Scatter plot of CO and NO2 with lots of overlapping plots](https://assets.datacamp.com/production/repositories/3841/datasets/3d05d15adfc2f44884a5abd866bc2fa67fc0cb05/messy_colored_scatter.png)

Unfortunately, the resulting plot is very convoluted. It's hard to make out differences between the cities because one has to differentiate between similar colors. It turns out that sometimes the best color palette for your plot is no color at all.

### INSTRUCTIONS
- To set up a chart faceted by the city, pass the plotting function the pollution data, map the city to the columns, and make the facet three columns wide.
- Use the g.map() function to map a scatterplot() over our grid with the same aesthetic as the original scatter but without the hue argument.

## Fixing Seaborn's bar charts

Seaborn's default values for the colors of bars in a bar chart are not ideal for the most accurate perception. By drawing each bar as a different color, there is a risk of the viewer seeing two identical sized bars as different sizes as people tend to see some colors as 'larger' than others.

![Basic rainbow colored bar plot](https://assets.datacamp.com/production/repositories/3841/datasets/623d266d2194ed81a37d15b895cbd3641f6f5d38/bars_no_border.png)

We discussed two easy ways to fix this. First, to put a border around the bars; second, change all bar colors to the same value. Try both of these solutions on our pollution data.

### INSTRUCTIONS
1. Modify the default barplot by adding a black border around each bar.
2. Now, make your plot more perceptually precise by coloring all bars 'cadetblue'.

## Making a custom continuous palette

You are interested in the pollution levels of Cincinnati for the year 2014. Specifically, you're interested in CO and NO2, so you make a simple scatter plot to show the relationship between the two pollutants.

![Scatterplot of CO and NO2 with uncolored points](https://assets.datacamp.com/production/repositories/3841/datasets/38b3a61c19aec974f73ddb0dc06fdc4a2805857a/basic_no_color_scatter.png)

However, there may be some interesting information in how the value of O3 relates to the two plotted pollutants, so you decide to color the points by their O3 levels. To do this, you need to define an appropriate continuous palette and map your O3 column to it in your scatter plot.

### INSTRUCTIONS
- Create a palette that continuously maps from white to 'orangered'.
- Map the column for O3 values to the color of the points.
- Pass your created palette to the plotting function.

## Customizing a diverging palette heatmap

The default color scheme used by Seaborn's heatmap() doesn't give the value of 0 any special treatment. This is fine for instances when 0 isn't special for the variable you're visualizing but means you will need to customize the palette 0 is special, such as when it represents a neutral value.

For this visualization, you want to compare all the cities against the average pollution value for CO in November 2015. (As is provided in the DataFrame nov_2015_CO).

To do this, use a heat map to encode the number of standard deviations away from the average each city's CO pollution was for the day. You'll need to replace the default palette by creating your own custom diverging palette and passing it to the heatmap and informing the function what your neutral value is.

### INSTRUCTIONS
- Pass the diverging palette to sns.heatmap().
- Add your neutral value to the heat map.
- Set the upper and lower boundaries to the color bar to -4 and 4 to make the legend symmetric.

## Adjusting your palette according to context

You've been asked to make a figure for your company's website. The website has a slick black theme, and it would be pretty jarring if your plot were white. To make your plot match the company aesthetic, you can swap the background to a black one with plt.style.use("dark_background").

The figure you've been asked to make plots O3 values during October 2015 for various cities (provided as oct_2015_o3). You will plot this as a heatmap with the color of each cell encoding how many standard deviations from the overall average O3 value the measurement falls. Due to the website's dark background, you will want to adjust your color palette to encode null value (or 0 standard deviations from the mean) as dark rather than the default white.

### INSTRUCTIONS
- Set the theme of the plot to black with plt.style.use().
- Modify the custom palette to be black for the middle value instead of white.

## Using a custom categorical palette

When you have a line chart with lots of categories choosing your palette carefully is essential. Often default palettes have very similar hues, that are hard to differentiate when spread over the small surface of a line. ColorBrewer palettes are built with this in mind and keep the colors as distinct as possible.

In this exercise, you will make a line plot of the O3 values over the year of 2013 for all the cities where the color of each line is encoded by city. You will use the ColorBrewer palette 'Set2' to improve upon the default color scheme.

### INSTRUCTIONS
- Query data to January of 2013.
- Encode the color of the lines as the city.
- Change the palette to the 'Set2' ColorBrewer palette.

## Dealing with too many categories

Sometimes you may be short on figure space and need to show a lot of data at once. Here you want to show the year-long trajectory of every pollutant for every city in the pollution dataset. Each pollutant trajectory will be plotted as a line with the y-value corresponding to standard deviations from year's average. This means you will have a lot of lines on your plot at once -- way more than you could separate clearly with color.

To deal with this, you have decided to highlight on a small subset of city pollutant combinations (wanted_combos). This subset is the most important to you, and the other trajectories will provide valuable context for comparison. To focus attention, you will set all the non-highlighted trajectories lines to of the same 'other' color.

### INSTRUCTIONS
- Modify the list comprehension to isolate the desired combinations of city and pollutant (wanted_combos).
- Tell the line plot to color the lines by the newly created color_cats column in your DataFrame.
- Use the units argument to determine how, i.e., from which column, the data points should be connected to form each line.
- Disable the binning of points with the estimator argument.

## Coloring ordinal categories

You are working for the Des Moines city council to assess the associations of various pollutant levels in the city. The two most important pollutants are SO2 and NO2 but CO is also of interest. You've only been allowed enough space for a single plot for your part of the report.

You start with a scatter plot of the SO2 and NO2 values as they are most important and then decide to show the CO values using a color scale corresponding to CO quartiles. By binning the continuous CO values, you have turned CO into an ordinal variable that can illuminate broad patterns without requiring much effort from the viewer to compare subtly different shades.

### INSTRUCTIONS
- Set the qcut() function to break 'CO' into quartiles.
- Map the color of your scatter plot to the new quartile column.
- Change the palette to the ColorBrewer palette 'GnBu'.

## Choosing the right variable to encode with color

You're tasked with visualizing pollution values for Long Beach and nearby cities over time. The supplied code makes the below (hard-to-read plot), which consists of maximum pollution values (provided as max_pollutant_values) with the bars colored by the city.

![Mutlicolor and busy bar plots with four rows corresponding to the four pollutants in dataset](https://assets.datacamp.com/production/repositories/3841/datasets/bfdc5024f8b0dba94ef0302824d88affed8180b7/exercise_swap_color_encoding.png)

You can quickly improve this with a few tweaks. By modifying the cities shown to only those in the western half of the country you will avoid clutter. Next, swapping the color-encoding from city to year allows you to use an ordinal palette, saving the reader from continually referring to the legend to check which color corresponds to which city.

### INSTRUCTIONS
- Remove 'Indianapolis', 'Des Moines', 'Cincinnati', 'Houston' from the cities vector.
- Swap the encodings of the city and year variables.
- Use the 'BuGn' ColorBrewer palette to map your colors appropriately for the newly ordinal variable.
