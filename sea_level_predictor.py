import pandas as pd
import matplotlib.pyplot as plt
import os
from scipy.stats import linregress
import numpy as np

def draw_plot():
    # Read data from file
    csv_file    = os.path.join(os.path.dirname(os.path.abspath(__file__)),'epa-sea-level.csv')
    df = pd.read_csv(csv_file)

    # Create scatter plot
    plt.figure(figsize=(10, 6))
    plt.scatter(
        df['Year'],
        df['CSIRO Adjusted Sea Level']
    )

    # Create first line of best fit
    result = linregress(
        df['Year'],
        df['CSIRO Adjusted Sea Level']
    )

    years = np.arange(df['Year'].min(), 2051)

    plt.plot(
        years,
        result.intercept + result.slope * years,
        'r',
        label='Fit: 1880-2050'
    )

    # Create second line of best fit
    df_recent = df[df['Year'] >= 2000]

    result_recent = linregress(
        df_recent['Year'],
        df_recent['CSIRO Adjusted Sea Level']
    )

    years_recent = np.arange(2000, 2051)

    plt.plot(
        years_recent,
        result_recent.intercept + result_recent.slope * years_recent,
        'g',
        label='Fit: 2000-2050'
    )

    # Add labels and title
    plt.xlabel('Year')
    plt.ylabel('Sea Level (inches)')
    plt.title('Rise in Sea Level')

    # Save plot and return data for testing (DO NOT MODIFY)
    plt.savefig('sea_level_plot.png')
    return plt.gca()
