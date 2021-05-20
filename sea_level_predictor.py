import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress

def draw_plot():
    # Read data from file
    df = pd.read_csv('epa-sea-level.csv', usecols=['Year', 'CSIRO Adjusted Sea Level'])

    # Create scatter plot
    plt.figure(figsize=(7, 6))
    plt.scatter(x='Year', y='CSIRO Adjusted Sea Level', data=df)

    # Create first line of best fit
    res = linregress(df['Year'], df['CSIRO Adjusted Sea Level'])
    extended_year = list(range(1880, 2050))
    regress = [res.intercept + res.slope * x for x in extended_year]
    plt.plot(extended_year, regress, c='c')

    # Create second line of best fit
    recent_df = df[df['Year'] >= 2000]
    recent_res = linregress(recent_df['Year'], recent_df['CSIRO Adjusted Sea Level'])
    recent_year = list(range(2000, 2050))
    recent_regress = [recent_res.intercept + recent_res.slope * x for x in recent_year]
    plt.plot(recent_year, recent_regress, c='y')

    # Add labels and title
    plt.xlabel('Year')
    plt.ylabel('Sea Level (inches)')
    plt.title('Rise in Sea Level')
    
    # Save plot and return data for testing (DO NOT MODIFY)
    plt.savefig('sea_level_plot.png')
    return plt.gca()