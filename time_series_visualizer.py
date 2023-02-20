import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
from pandas.plotting import register_matplotlib_converters
register_matplotlib_converters()

# Import data (Make sure to parse dates. Consider setting index column to 'date'.)
df = pd.reimport time_series_visualizer
from unittest import main

# Test your function by calling it here
time_series_visualizer.draw_line_plot()
time_series_visualizer.draw_bar_plot()
time_series_visualizer.draw_box_plot()

# Run unit tests automatically
main(module='test_module', exit=False)ad_csv('fcc-forum-pageviews.csv', parse_dates=['date'], index_col='date')

# Clean data
df = df[
    (df['value'] > df['value'].quantile(0.025))
     & (df['value'] < df['value'].quantile(0.975))]


def draw_line_plot():
    # Draw line plot
    fig, ax = plt.subplots(figsize=(32, 10))
    ax.plot(df.index, df['value'], 'r', linewidth=1)
    ax.set_title("Daily freeCodeCamp Forum Page Views 5/2016-12/2019")
    ax.set_xlabel("Date")
    ax.set_ylabel("Page Views")

    # Save image and return fig (don't change this part)
    fig.savefig('line_plot.png')
    return fig

def draw_bar_plot():
    # Copy and modify data for monthly bar plot
    months = ['January', 'Febuary', 'March', 'April', 'May', 'June',
              'July', 'August', 'September', 'October', 'November', 'December']

    df['month'] = df.index.month
    df['year'] = df.index.year
    df_bar = df.groupby(['year', 'month'])['value'].mean()
    df_bar = df_bar.unstack()

    # Draw bar plot
    fig = df_bar.plot.bar(legend=True, figsize=(10,6), ylabel='Average Page Views', xlabel='Years').figure
    plt.legend(months)


    # Save image and return fig (don't change this part)
    fig.savefig('bar_plot.png')
    return fig

def draw_box_plot():
    months = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun',
              'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']
    # Prepare data for box plots (this part is done!)
    df_box = df.copy()
    df_box.reset_index(inplace=True)
    df_box['year'] = [d.year for d in df_box.date]
    df_box['month'] = [d.strftime('%b') for d in df_box.date]
    print(df_box)

    # Draw box plots (using Seaborn)
    fig = plt.figure(figsize=(14,6))
    plt.subplot(1,2,1)
    sns.boxplot(data=df_box, x='year', y='value')
    plt.ylabel('Page Views')
    plt.title('Year-wise Box Plot (Trend)')
    plt.subplot(1,2,2)
    sns.boxplot(data=df_box, x='month', y='value', order=months)
    plt.ylabel('Page Views')
    plt.title('Month-wise Box Plot (Seasonality)')

    # Save image and return fig (don't change this part)
    fig.savefig('box_plot.png')
    return fig

