from datetime import datetime
import matplotlib.pyplot as plt
from matplotlib.dates import AutoDateLocator
import matplotlib.dates as mdates


def get_date_taken(date_str):
    date_taken = datetime.strptime(date_str, '%Y:%m:%d %H:%M:%S')
    return date_taken.date()


def draw_photo_distribution(config, exif_data_list):
    dates = [get_date_taken(entry['Date Taken']) for entry in exif_data_list]

    # Count the number of photos taken on each date
    date_counts = {}
    for date in dates:
        if date in date_counts:
            date_counts[date] += 1
        else:
            date_counts[date] = 1

    # Sort the dates in ascending order
    sorted_dates = sorted(date_counts.keys())

    # Extract counts for each sorted date
    counts = [date_counts[date] for date in sorted_dates]

    # Create a bar chart
    fig, ax = plt.subplots(figsize=(40, 10))
    ax.bar(sorted_dates, counts, width=0.8, color='blue')
    fig.subplots_adjust(left=0.025, right=0.975)

    # Format x-axis labels to show only the month
    ax.xaxis.set_major_locator(mdates.MonthLocator())
    ax.xaxis.set_major_formatter(mdates.DateFormatter('%b %Y'))

    # Set x-axis labels rotation for better readability
    plt.xticks(rotation=45)

    plt.xlabel('Date')
    plt.ylabel('Count')
    plt.title('Distribution of Photos by Date')

    # Save the plot
    plt.savefig(config.plot_save_path.plot_result_save_path + "daily-aggregation-" + str(
        datetime.now().strftime('%Y%m%d%H%M%S')) + ".jpg")


def draw_photo_distribution_by_month(config, exif_data_list):
    dates = [get_date_taken(entry['Date Taken']) for entry in exif_data_list]

    # Count the number of photos taken in each month
    month_counts = {}
    for date in dates:
        month = date.strftime('%b %Y')
        if month in month_counts:
            month_counts[month] += 1
        else:
            month_counts[month] = 1

    # Extract months and counts for plotting
    months = sorted(list(month_counts.keys()), key=lambda x: datetime.strptime(x, '%b %Y'))
    counts = [month_counts[month] for month in months]

    # Create a bar chart
    fig, ax = plt.subplots(figsize=(40, 12))
    plt.subplots_adjust(left=0.025, right=0.975)
    ax.bar(months, counts, width=0.8, color='blue')  # Changed to months
    ax.set_xlabel('Date')
    ax.set_ylabel('Count')
    ax.set_title('Distribution of Photos by Month')
    plt.xticks(rotation=45)
    ax.xaxis.set_major_locator(AutoDateLocator())

    # Manually set x-axis ticks to display every month
    ax.set_xticks(range(len(months)))
    ax.set_xticklabels(months, rotation=45)

    # Add data values to the bars
    for i, count in enumerate(counts):
        ax.text(i, count, str(count), ha='center', va='bottom')

    # Save the plot using the provided save path from the config
    plt.savefig(config.plot_save_path.plot_result_save_path + "monthly-aggregation-" + datetime.now().strftime(
        '%Y%m%d%H%M%S') + ".jpg")
