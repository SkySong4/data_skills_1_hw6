# PPHA 30537
# Spring 2023
# Homework 6

# YOUR NAME HERE：Tianhua Song

# YOUR CANVAS NAME HERE：tianhuas
# YOUR GITHUB USER NAME HERE：SkySong4

# Due date: Monday May 8th before midnight
# Write your answers in the space between the questions, and commit/push only
# this file to your repo. Note that there can be a difference between giving a
# "minimally" right answer, and a really good answer, so it can pay to put
# thought into your work.

##################

#NOTE: All of the plots the questions ask for should be saved and committed to
# your repo under the name "q1_plot.png", "q2_plot.png", etc. If a question calls
# for more than one plot, name them "q1a_plot", "q1b_plot", etc.

# Question 1: With the x and y values below, create a plot using only Matplotlib.
# You should plot y1 as a scatter plot and y2 as a line, using different colors
# and a legend.  You can name the data simply "y1" and "y2".  Make sure the
# axis labels are legible.  Add a title that reads "HW6 Q1".
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
import os

x = pd.date_range(start='1990/1/1', end='1991/12/1', freq='MS')
y1 = np.random.normal(10, 2, len(x))
y2 = [np.sin(v)+10 for v in range(len(x))]
plt.scatter(x, y1, label='y1', color='blue')
plt.plot(x, y2, label='y2', color='orange')
plt.xlabel('Date')
plt.ylabel('Value')
plt.title('HW6 Q1')
plt.legend()
plt.show()


# Question 2: Using only Matplotlib, reproduce the figure in this repo named
# question_2_figure.png.
x_range = y_range = (10, 20)
midpoint = sum(x_range) / 2
fig, ax = plt.subplots()
ax.plot([x_range[0]+1, x_range[1]-1], [y_range[0]+1, y_range[1]-1], color='blue', label='Blue')
ax.plot([x_range[0]+1, x_range[1]-1], [2*midpoint - y_range[0]-1, 2*midpoint - y_range[1]+1], color='red', label='Red')
ax.set_xlim(*x_range)
ax.set_ylim(*y_range)
ax.set_xticks(range(*x_range, 2))
ax.set_yticks(range(*y_range, 2))
ax.set_yticks([10, 12, 14, 16, 18])
ax.set_title('X marks the spot')
ax.legend(loc='center left')
plt.show()


# Question 3: Load the mpg.csv file that is in this repo, and create a
# plot that tests the following hypothesis: a car with an engine that has
# a higher displacement (i.e. is bigger) will get worse gas mileage than
# one that has a smaller displacement.  Test the same hypothesis for mpg
# against horsepower and weight.
mpg_df = pd.read_csv('mpg.csv')
plt.scatter(mpg_df['displacement'], mpg_df['mpg'])
plt.xlabel('Displacement (cu. in.)')
plt.ylabel('Miles per gallon (mpg)')
plt.title('Displacement vs. mpg')
corr = mpg_df['displacement'].corr(mpg_df['mpg'])
print('Correlation coefficient between displacement and mpg:', corr)
plt.show()

plt.scatter(mpg_df['horsepower'], mpg_df['mpg'])
plt.xlabel('Horsepower (hp)')
plt.ylabel('Miles per gallon (mpg)')
plt.title('Horsepower vs. mpg')
corr = mpg_df['horsepower'].corr(mpg_df['mpg'])
print('Correlation coefficient between horsepower and mpg:', corr)
plt.show()

plt.scatter(mpg_df['weight'], mpg_df['mpg'])
plt.xlabel('Weight (lbs)')
plt.ylabel('Miles per gallon (mpg)')
plt.title('Weight vs. mpg')
corr = mpg_df['weight'].corr(mpg_df['mpg'])
print('Correlation coefficient between weight and mpg:', corr)
plt.show()


# Question 4: Continuing with the data from question 3, create a scatter plot 
# with mpg on the y-axis and cylinders on the x-axis.  Explain what is wrong 
# with this plot with a 1-2 line comment.  Now create a box plot using Seaborn
# that uses cylinders as the groupings on the x-axis, and mpg as the values
# up the y-axis.
plt.scatter(mpg_df['cylinders'], mpg_df['mpg'])
plt.xlabel('Cylinders')
plt.ylabel('Miles per gallon (mpg)')
plt.title('Cylinders vs. mpg')
plt.show()
# As the plot shows, the more or less cylinders a car has, the less energy 
# efficient it is. 4-cylinder cars are the most efficient, 3-cylinder and 
# 8-cylinder car are the least. 
sns.boxplot(x=mpg_df['cylinders'], y=mpg_df['mpg'])
plt.xlabel('Cylinders')
plt.ylabel('Miles per gallon (mpg)')
plt.title('Cylinders vs. mpg')
plt.show()


# Question 5: Continuing with the data from question 3, create a two-by-two 
# grid of subplots, where each one has mpg on the y-axis and one of 
# displacement, horsepower, weight, and acceleration on the x-axis.  To clean 
# up this plot:
#   - Remove the y-axis tick labels (the values) on the right two subplots - 
#     the scale of the ticks will already be aligned because the mpg values 
#     are the same in all axis.  
#   - Add a title to the figure (not the subplots) that reads "Changes in MPG"
#   - Add a y-label to the figure (not the subplots) that says "mpg"
#   - Add an x-label to each subplot for the x values
# Finally, use the savefig method to save this figure to your repo.  If any
# labels or values overlap other chart elements, go back and adjust spacing.
fig, axs = plt.subplots(2, 2, figsize=(10, 8))
axs[0, 0].scatter(mpg_df['displacement'], mpg_df['mpg'])
axs[0, 0].set_title('Displacement')
axs[0, 0].set_xlabel('Displacement (cu. in.)')
axs[0, 0].set_ylabel('Miles per gallon (mpg)')

axs[0, 1].scatter(mpg_df['horsepower'], mpg_df['mpg'])
axs[0, 1].set_title('Horsepower')
axs[0, 1].set_xlabel('Horsepower (hp)')

axs[1, 0].scatter(mpg_df['weight'], mpg_df['mpg'])
axs[1, 0].set_title('Weight')
axs[1, 0].set_xlabel('Weight (lbs)')
axs[1, 0].set_ylabel('Miles per gallon (mpg)')

axs[1, 1].scatter(mpg_df['acceleration'], mpg_df['mpg'])
axs[1, 1].set_title('Acceleration')
axs[1, 1].set_xlabel('Acceleration (sec/0-60mph)')

axs[0, 1].tick_params(labelright=False)
axs[1, 1].tick_params(labelright=False)

fig.suptitle('Changes in MPG')
fig.text(0.04, 0.5, 'mpg', ha='center', va='center', rotation='vertical')
plt.subplots_adjust(left=0.08, bottom=0.08, right=0.94, top=0.90, wspace=0.25, hspace=0.35)
plt.savefig('mpg_changes.png')
plt.show()


# Question 6: Are cars from the USA, Japan, or Europe the least fuel
# efficient, on average?  Answer this with a plot and a one-line comment.
mpg_df.boxplot('mpg', by='origin')
plt.xlabel('Origin')
plt.ylabel('Miles per gallon (mpg)')
plt.title('Distribution of mpg by origin')
plt.show()
# From the plot, cars from USA are the least fuel efficent on average.

# Question 7: Using Seaborn, create a scatter plot of mpg versus displacement,
# while showing dots as different colors depending on the country of origin.
# Explain in a one-line comment what this plot says about the results of 
# question 6.
sns.scatterplot(x='displacement', y='mpg', hue='origin', data=mpg_df)
plt.xlabel('Displacement (cu. in.)')
plt.ylabel('Miles per gallon (mpg)')
plt.title('Miles per gallon vs. displacement, by origin')
plt.show()
# Cars from USA have larger displacement but smaller mpg, so they are the least fuel efficent like Q6 shows above.
