# Chapter 3 - Showing uncertainty

## Basic confidence intervals

You are a data scientist for a fireworks manufacturer in Des Moines, Iowa. You need to make a case to the city that your company's large fireworks show has not caused any harm to the city's air. To do this, you look at the average levels for pollutants in the week after the fourth of July and how they compare to readings taken after your last show. By showing confidence intervals around the averages, you can make a case that the recent readings were well within the normal range.

This data is loaded as average_ests with a row for each measured pollutant.

### INSTRUCTIONS

-   Create the lower and upper 95% interval boundaries by subtracting and adding 1.96 standard errors from the mean of estimates.
-   Pass pollutant as the faceting variable to sns.FacetGrid().
-   Unlink the x-axes of the plots, so intervals are all well-sized.
-   Pass the constructed interval boundaries to the mapped plt.hlines() function.

## Annotating confidence intervals

Your data science work with pollution data is legendary, and you are now weighing job offers in both Cincinnati, Ohio and Indianapolis, Indiana. You want to see if the SO2 levels are significantly different in the two cities, and more specifically, which city has lower levels. To test this, you decide to look at the differences in the cities' SO2 values (Indianapolis' - Cincinnati's) over multiple years (provided as diffs_by_year).

Instead of just displaying a p-value for a significant difference between the cities, you decide to look at the 95% confidence intervals (columns lower and upper) of the differences. This allows you to see the magnitude of the differences along with any trends over the years.

### INSTRUCTIONS

-   Provide starting and ending limits (columns lower and upper) for your confidence intervals to plt.hlines().
-   Set interval thickness to 5.
-   Draw a vertical line representing a difference of 0 with plt.axvline().
-   Color the null line 'orangered' to make it stand out.

## Making a confidence band

Vandenberg Air Force Base is often used as a location to launch rockets into space. You have a theory that a recent increase in the pace of rocket launches could be harming the air quality in the surrounding region. To explore this, you plotted a 25-day rolling average line of the measurements of atmospheric NO2. To help decide if any pattern observed is random-noise or not, you decide to add a 99% confidence band around your rolling mean. Adding a confidence band to a trend line can help shed light on the stability of the trend seen. This can either increase or decrease the confidence in the discovered trend.

### INSTRUCTIONS
- Construct upper and lower 99% interval bands by adding and subtracting 2.58 standard errors from the mean.
- Make the point-estimate line white.
- Make the point-estimate line semi-transparent by setting alpha to 0.4.
- Tell plt.fill_between() what values to fill between for each day.

## Separating a lot of bands

It is relatively simple to plot a bunch of trend lines on top of each other for rapid and precise comparisons. Unfortunately, if you need to add uncertainty bands around those lines, the plot becomes very difficult to read. Figuring out whether a line corresponds to the top of one class' band or the bottom of another's can be hard due to band overlap. Luckily in Seaborn, it's not difficult to break up the overlapping bands into separate faceted plots.

To see this, explore trends in SO2 levels for a few cities in the eastern half of the US. If you plot the trends and their confidence bands on a single plot - it's a mess. To fix, use Seaborn's FacetGrid() function to spread out the confidence intervals to multiple panes to ease your inspection.

### INSTRUCTIONS
- Set up a facet grid to separate the plots by the city column in eastern_SO2.
- Send the confidence interval plotting function to map().
- Color the confidence intervals 'coral'.
- Help the overlaid mean line drawn with g.map(plt.plot,...) stand out against the confidence bands by coloring it white.

## Cleaning up bands for overlaps

You are working for the city of Denver, Colorado and want to run an ad campaign about how much cleaner Denver's air is than Long Beach, California's air. To investigate this claim, you will compare the SO2 levels of both cities for the year 2014 (provided as the DataFrame SO2_compare). Since you are solely interested in how the cities compare, you want to keep the bands on the same plot. To make the bands easier to compare, decrease the opacity of the confidence bands and set a clear legend.

### INSTRUCTIONS
- Filter the SO2_compare to the for loops currently selected city.
- Color both the intervals and mean lines with the color accompanying each city.
- Lower the interval and mean line opacities to 0.4 and 0.25, respectively.
- Pass the city name to plt.plot() so the legend is labeled correctly

## 90, 95 & 99% intervals

You are a data scientist for an outdoor adventure company in Fairbanks, Alaska. Recently, customers have been having issues with SO2 pollution, leading to costly cancellations. The company has sensors for CO, NO2, and O3 but not SO2 levels.

You've built a model that predicts SO2 values based on the values of pollutants with sensors (loaded as pollution_model, a statsmodels object). You want to investigate which pollutant's value has the largest effect on your model's SO2 prediction. This will help you know which pollutant's values to pay most attention to when planning outdoor tours. To maximize the amount of information in your report, show multiple levels of uncertainty for the model estimates.

### INSTRUCTIONS
- Fill in the appropriate interval width percents (from 90,95, and 99%) according to the values list in alpha.
- In the for loop, color the interval by its assigned color.
- Pass the loop's width percentage value to plt.hlines() to label the legend.

## 90 & 95% bands

You are looking at a 40-day rolling average of the NO2 pollution levels for the city of Cincinnati in 2013. To provide as detailed a picture of the uncertainty in the trend you want to look at both the 90 and 99% intervals around this rolling estimate.

To do this, set up your two interval sizes and an orange ordinal color palette. Additionally, to enable precise readings of the bands, make them semi-transparent, so the Seaborn background grids show through.

### INSTRUCTIONS
- Set the opacity of the intervals to 40%.
- Calculate the lower and upper confidence bounds.

## Using band thickness instead of coloring

You are a researcher investigating the elevation a rocket reaches before visual is lost and pollutant levels at Vandenberg Air Force Base. You've built a model to predict this relationship (stored in the DataFrame rocket_height_model), and since you are working independently, you don't have the money to pay for color figures in your journal article. You need to make your model results plot work in black and white. To do this, you will plot the 90, 95, and 99% intervals of the effect of each pollutant as successively smaller bars.

### INSTRUCTIONS
- Use a thickness of 15 for 90%, 10 for 95%, and 5 for 99% interval lines.
- Pass the interval thickness value to plt.hlines().
- Set the interval color to 'gray' to lighten contrast.

## The bootstrap histogram

You are considering a vacation to Cincinnati in May, but you have a severe sensitivity to NO2. You pull a few years of pollution data from Cincinnati in May and look at a bootstrap estimate of the average NO2 levels. You only have one estimate to look at the best way to visualize the results of your bootstrap estimates is with a histogram.

While you like the intuition of the bootstrap histogram by itself, your partner who will be going on the vacation with you, likes seeing percent intervals. To accommodate them, you decide to highlight the 95% interval by shading the region.

### INSTRUCTIONS
- Provide the percentile() function with the upper and lower percentiles needed to get a 95% interval.
- Shade the background of the plot in the 95% interval.
- Draw histogram of bootstrap means with 100 bins.

## Bootstrapped regressions

While working for the Long Beach parks and recreation department investigating the relationship between NO2 and SO2 you noticed a cluster of potential outliers that you suspect might be throwing off the correlations.

![SO2 NO2 scatter](https://assets.datacamp.com/production/repositories/3841/datasets/79c91397ef0aa461017354cefaf90bfeb9474ac4/boot_regression_ex_intro.png)

Investigate the uncertainty of your correlations through bootstrap resampling to see how stable your fits are. For convenience, the bootstrap sampling is complete and is provided as no2_so2_boot along with no2_so2 for the non-resampled data.

### INSTRUCTIONS
- Let sns.lmplot() know that it needs to draw a separate regression line for each bootstrap sample.
- Color every regression line 'steelblue' and make them 20% opaque.
- Disable the default Seaborn confidence bands around the regression lines.

## Lots of bootstraps with beeswarms

As a current resident of Cincinnati, you're curious to see how the average NO2 values compare to Des Moines, Indianapolis, and Houston: a few other cities you've lived in.

To look at this, you decide to use bootstrap estimation to look at the mean NO2 values for each city. Because the comparisons are of primary interest, you will use a swarm plot to compare the estimates.

The DataFrame pollution_may is provided along with the bootstrap() function seen in the slides for performing your bootstrap resampling.

### INSTRUCTIONS
- Run bootstrap resampling on each city_NO2 vector.
- Add city name as a column in the bootstrap DataFrame, cur_boot.
- Color all swarm plot points 'coral' to avoid the color-size problem.
