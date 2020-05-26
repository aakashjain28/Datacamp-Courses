# Chapter 4 - Visualization in the Data Science Workflow

## Looking at the farmers market data

Loaded is a new dataset, markets. Each row of this DataFrame belongs to an individual farmers market in the continental United States with various information about the market contained in the columns. In this exercise, explore the columns of the data to get familiar with them for future analysis and plotting.

As a first step, print out the first three lines of markets to get an idea of what type of data the columns encode. Then look at the summary descriptions of all of the columns. Since there are so many columns in the DataFrame, you'll want to turn the results 'sideways' by transposing the output to avoid cutting off rows.

### INSTRUCTIONS
- Print the first three rows of the data and transpose by chaining the transpose() method to the DataFrame.
- Print the basic description of every column along with its median and transpose.

## Scatter matrix of numeric columns

You've investigated the new farmer's market data, and it's rather wide – with lots of columns of information for each market's row. Rather than painstakingly going through every combination of numeric columns and making a scatter plot to look at correlations, you decide to make a scatter matrix using the pandas built-in function.

Increasing the figure size with the figsize argument will help give the dense visualization some breathing room. Since there will be a lot of overlap for the points, decreasing the point opacity will help show the density of these overlaps.

### INSTRUCTIONS
- Subset the columns of the markets DataFrame to numeric_columns so the scatter matrix only shows numeric non-binary columns.
- Increase figure size to 15 by 10 to avoid crowding.
- Reduce point opacity to 50% to show regions of overlap.

## Digging in with basic transforms

You are curious to see if the population of a state correlates to the number of items sold at farmer's markets. To check this, take the log of the population and draw a scatter plot against the number of items sold by a market. From your previous explorations of the dataset, you know there will be a lot of overlap, so to get a better handle on the patterns you want to reduce the marker opacity.

### INSTRUCTIONS
- Use numpy (imported as np) to create a new column: log_pop by taking the log of the state population.
- Pass this newly created logged column to the scatter plot function's x-mapping.
- Set the scatter plot's opacity to 25% to show overlap.

## Is longtitude related to months open?

While exploring the farmers market dataset with a scatter matrix, you noticed a potentially interesting relationship between a market's longitude and the number of months it stays open. Digging into this relationship a bit further, you decide to use Seaborn's regression plot to see if there's any weight to this pattern or if the heavy overlap of the points is playing tricks on your eyes.

To make the regression line stand out, you'll want to lower the overlapping background points opacity and color them a muted gray. Since you're not going to be making any formal inference and want to quickly investigate a pattern, you can turn off the default uncertainty band.

### INSTRUCTIONS
- Set the scatter plot's points opacity to 10% and color them 'gray'.
- Disable the default confidence interval band.

## Which state is the most market-friendly?

While exploring the farmer's market data, you wonder what patterns may show up if you aggregated to the state level. Are some states more market-friendly than other states? To investigate this, you group your data by state and get the log-transformed number of markets (log_markets) and state populations (log_pop).

```
markets_and_pop = (markets
    .groupby('state', as_index = False)
    .agg({
       'name': lambda d: log(len(d)),
       'state_pop': lambda d: log(d.iloc[0]) })
    .rename(columns = {
        'name': 'log_markets',
        'state_pop': 'log_pop' }))
```

To visualize, you decide to use a regression plot to get an idea of the 'normal' relationship between market and population numbers and a text-scatter to quickly identify interesting outliers.

## Popularity of goods sold by state

The farmer's market dataset contains columns corresponding to 28 different goods and whether or not they are sold at that market. You're curious to see if there are any interesting stories in this dataset regarding how likely you are to find a given good at a state's markets. To answer this question, you collapse the data into three columns:
- state - the name of the state
- good - the good of interest
- prop_selling - the proportion of markets in that state that sell that good

To quickly determine if patterns emerge, you choose a subset of goods you find interesting and decide to make a simple text-scatter: the good on the x-axis and the proportion of a state's markets that sell that good on the y-axis.

### INSTRUCTIONS
- Filter goods_by_state to the desired goods listed in to_plot.
- Hide the scatter plot points by setting their size to nothing.
- Make the text center aligned, so it sits directly on the good's x-axis location.

## Stacking to find more trends

In the farmers market dataset, you are interested in the number of months that a market stays open in relation to its geography, more specifically its latitude. You're curious to see if there are any regions of the country that behave noticeably different from the others.

To do this, you create a basic map with a scatter plot of the latitude and longitude of each market, coloring each market by the number of months it's open. Further digging into the latitude relationship, you draw a regression plot of the latitude to the number of months open with a flexible fit line to determine if any trends appear. You want to view these simultaneously to get the clearest picture of the trends.

### INSTRUCTIONS
- Set up plt.subplots() to have two vertically stacked plots.
- Assign the first (top) plot to the lat, lon scatter plot.
- Assign the second (bottom) plot to the lat to months_open regression plot.

## Using a plot as a legend

One interesting thread of investigation in the farmer's market data is a state's "market friendliness" and specifically, the outliers. One way to look at this is by using the ratio of farmer's markets to people by state. You could directly look at the ratio; however, a ratio throws away the raw information about a state's population and the number of markets. A large state with a high ratio could be more interesting than a small one.

You can show both the ratio and raw numbers by drawing two plots, one of the ratio and the other of the market number to population scatter plot. To help simplify your now dense visualization, you can use the bar plot as a legend; calling out interesting states by matching the colors of their bars and scatter points.

### INSTRUCTIONS
- Set up two plots side-by-side using plt.subplots().
- Map the column is_selected to the color of both the bar and scatter plot.
- Disable dodge on the bar plot, so the bars are full height.
- Remove the legends in both plots.

## Cleaning up the bakcground

While exploring state-level patterns in goods sold at farmer's markets, a few states stood out to you. North Dakota and New Mexico routinely fell near the bottom of the states regarding their proportion of farmer's markets selling a given good. Whereas Vermont was always near the top. You want to present the general patterns in good sales by state, while also highlighting the states you found interesting.

You make a scatter plot of goods being sold by the proportion of markets that sell that good in a state. To highlight the interesting states, you draw a line between each of the state's points. To make a clean and minimal plot, you reduce the background to a simple set of orienting grids.

### INSTRUCTIONS
- Set the background of the plot to be white with gridlines.
- Encode the x and y-axes of the scatter and line plots with the 'good' being sold and 'prop selling', respectively.
- Remove all the borders from the plot.

## Remixing a plot

You find the relationship between the longitude of a farmer's market and the number of months the market was open fascinating. Intuitively as one gets further South, the growing seasons are longer, and thus the markets can stay open longer. To visualize this story, you summarize the market data at the state level and draw a heatmap with columns corresponding to the duration the markets are open. Each row in the heatmap shows the distribution of the market "season" for a state and rows are sorted in descending order of the state's longitude.

![default heatmap of months open by longitude with a dark to red colorscale](https://assets.datacamp.com/production/repositories/3841/datasets/7a47fd1e8b14fe67b6186437c7f69d44061aa863/Screen%20Shot%202019-02-18%20at%2010.56.43%20AM.png)

The default heatmap leaves a lot to be desired. Decrease the font size to allow each state name to fit without overlap. The dark color palette also clashes with the light background, and the colorbar doesn't help the reader as the point is relative comparisons.

### INSTRUCTIONS
- Decrease the font size to 85% of the default to un-crowd state names.
- Make new color palette that goes from 'white' to 'steelblue'.
- Replace the default palette with the newly created one.
- Remove the continuous color bar legend drawn next to heatmap.

## Enhancing legibility

You and your colleagues have decided that the most important aspect of the data you want to show is the differences between the most "market-friendly" state, Vermont, and the least, Texas. To do this, put two plots side by side – a barplot showing the number of people per farmer's market in the state and a scatter plot showing the population on the x-axis and the number of markets on the y-axis.

Emphasize your findings by calling out Vermont and Texas by assigning them distinct colors. Also, provide a large and easy to read annotation for Texas.

Supplied is a vector state_colors that assigns Vermont and Texas unique colors and all other states gray along with the annotation describing Texas, tx_message.

### INSTRUCTIONS
- Map the supplied color vector state_colors to the bar plot (ax1) with the palette argument in sns.barplot().
- Map the color vector to the scatter plot points with the color argument.
- Make sure annotation text is legible by changing its size to 15.
