import time
import pandas as pd
import numpy as np

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }

def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print('Hello! Let\'s explore some US bikeshare data!')
    # get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs

    city = input("Choose one of these cities to explore Chicago, Washington, New York City: ").strip().lower()
    while city not in ['chicago', 'washington', 'new york city']:
        city = input("Please make sure you Choose one of these cities to explore Chicago, Washington, New York City: ").strip().lower()

    # get user input for month (all, january, february, ... , june)

    month = input("Choose one of these months: January, February, March, April, May, June OR All to explore All months: ").strip().title()
    while month not in ['January', 'february', 'March', 'April', 'May', 'June', 'All']:
        month = input("Please make sure you Choose one of these months: January, February, March, April, May, June OR All to explore All months: ").strip().title()
    # get user input for day of week (all, monday, tuesday, ... sunday)

    day = input("Choose One Of these days: Monday, Tuesday, Wednesday, Thursday,....  Or All to explore All days: ").strip().title()
    while day not in ['Saturday', 'Sunday', 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'All']:
        day = input("Choose One Of these days: Monday, Tuesday, Wednesday, Thursday,....  Or All to explore All days: ").strip().title()

    print('-'*40)
    return city, month, day


def load_data(city, month, day):
    """
    Loads data for the specified city and filters by month and day if applicable.

    Args:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    Returns:
        df - Pandas DataFrame containing city data filtered by month and day
    """

    # Load City Data file to analyze into Data Frame
    df = pd.read_csv(CITY_DATA[city])
    # Convert start time column to datetime datatype
    df['Start Time'] = pd.to_datetime(df['Start Time'])
    # Extract month and day of week from start time column to create new columns for month and day of week
    df['month'] = df['Start Time'].dt.month_name()
    df['Day_of_week'] = df['Start Time'].dt.day_name()
    # print(df['month'])
    print("Modified DataFrame: ", df)
    # Create the filtered DataFrame based on User input
    if month != 'All':
        df = df[df['month'] == month]
    if day != 'All':
        df = df[df['Day_of_week'] == day]
    print("Filtered DataFrame: ", df)
    # Check if there is any NAN values in our DataFrame
    # print(df.isnull().sum())
    # remove any NAN values in the DataFrame
    df.dropna(axis=0, inplace=True)
    # Check if this works well
    print(df.isnull().sum())
    # print(df)
    return df


def time_stats(df, month, day):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    print('please wait!')
    start_time = time.time()

    # display the most common month
    if month == 'All':
        if day == 'All':
            common_month(df)
            common_day(df)
            common_hour(df)

        else:
            common_month(df)
            common_hour(df)
    else:
        if day == 'All':
            common_day(df)
            common_hour(df)
        else:
            common_hour(df)
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def common_month(df):
    """ Get most common month! """
    common_month = df['month'].mode()[0]
    print("Most Common month of travel: ", common_month)


def common_day(df):
    """ Get most common day of day_of_week! """
    common_day = df['Day_of_week'].mode()
    print("Most Common day of week: ", common_day)


def common_hour(df):
    """ Get most common hour of day! """
    df['hour'] = df['Start Time'].dt.hour
    common_hour = df['hour'].mode()[0]
    print("Most Common hour of day: ", common_hour)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()
    # Get the most common start station
    most_common_start_station = df['Start Station'].mode()
    # Get the most common end station
    most_common_end_station = df['End Station'].mode()
    # insert Trip column into DataFrame by combining Start Station and End Station columns
    df['Trip'] = df['Start Station'] + " to " + df['End Station']
    # Get the most common trip
    most_common_trip = df['Trip'].mode()
    # display most commonly used start station
    print("Most Popular Start Station:\n", most_common_start_station)
    # display most commonly used end station
    print("Most Popular End Station:\n", most_common_end_station)
    # display most frequent combination of start station and end station trip
    print("Most Popular Trip:\n", most_common_trip)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()
    # display total travel time
    total_trip_duration = df['Trip Duration'].sum()
    # display mean travel time
    average_travel_time = df['Trip Duration'].mean()
    # Display the results
    print("Total travel time is {} seconds.".format(total_trip_duration))
    print("Average travel time is {} seconds.".format(average_travel_time))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df, city):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()
    # Display counts of user types
    user_type_counts = df['User Type'].value_counts()
    print("Counts Of user types:\n", user_type_counts)

    # this statistics are special for NYC and chicago
    if city != 'washington':
        # Display counts of gender
        gender_counts = df['Gender'].value_counts()
        earliest_year_of_birth = int(df['Birth Year'].min())
        most_recent_year_of_birth =int(df['Birth Year'].max())
        most_common_year_of_birth = int(df['Birth Year'].mode())
        # Display  gender counts, earliest, most recent and most common year of birth
        print("Here are counts of gender:\n", gender_counts)
        print("Wondering about earliest year of birth! Here it is...\n", earliest_year_of_birth)
        print("And what about most recent year?...", most_recent_year_of_birth)
        print("Looks really nice! but let me show you most common year of birth: ", most_common_year_of_birth)


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def display_raw_data(df):
    user_response = input("Would you like to see the raw data? Enter 'yes' or 'y' if ok or 'no' or 'n' if not!")
    while user_response.lower() in ['yes', 'y']:
        print(df.sample(n=5))
        user_response = input("Would you like to see 5 more of raw data?")


def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)
        time_stats(df, month, day)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df, city)
        display_raw_data(df)
        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() not in ['yes', 'y']:
            break


if __name__ == "__main__":
	main()
