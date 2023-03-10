import time
import pandas as pd
import numpy as np

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york': 'new_york_city.csv',
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
    cities = ['chicago','new york','washington']
    while True :
        city = input('Please pick a city (chicago,new york, washington)').lower()
        if city in cities:
            break
        else:
            print('Invalid input')
        
    # get user input for month (all, january, february, ... , june)
    months = ['all','january','february', 'march','april','may','june']
    
    while True:
        month = input('Please enter the month (january,february,march,april,may,june) or all for no filer ').lower()
        if month in months:
            break
        else:
            print('Invalid input')
    # get user input for day of week (all, monday, tuesday, ... sunday)
    days = ['all','monday','tuesday', 'wednesday','thursday','friday','saturday','sunday']
    while True:
        day = input('Please enter the day(monday,tuesday,wednesday,thursday,friday,saturday) or all for no filter ').lower()
        if day in days:
            break
        else:
            print('Invalid input')

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
    df = pd.read_csv(CITY_DATA[city])
     # convert the Start Time column to datetime
    df['Start Time'] = pd.to_datetime(df['Start Time'])
     # extract month and day of week from Start Time to create new columns
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.day_name()

    # filter by month if applicable
    if month != 'all':
        months = ['january', 'february', 'march', 'april', 'may', 'june']
        month = months.index(month) + 1

        # filter by month to create the new dataframe
        df = df[df['month'] == month]

    # filter by day of week if applicable
    if day != 'all':
        # filter by day of week to create the new dataframe
        df = df[df['day_of_week'] == day.title()]

    return df

def display_raw_data(df):
    """ Your docstring here """
    more_data = input("Do you like to view 5 rows of data? reply with yes or no. ").lower()
    i = 0
    while more_data == 'yes':
        print(df[i:i+5])
        i += 5
        more_data = input("Do you like to view 5 rows of data? reply with yes or no. ").lower()
        
    
    
def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # display the most common month
    df['month'] = df['Start Time'].dt.month_name()
    most_common_month = df['month'].mode()[0]
    print("The most common month : ", most_common_month)

    # display the most common day of week
    df['day_of_week'] = df['Start Time'].dt.day_name()
    most_common_day = df['day_of_week'].mode()[0]
    print('The most common month :', most_common_day)

    # display the most common start hour
    df['hour'] = df['Start Time'].dt.hour
    most_common_hour = df['hour'].mode()[0]
    print('The most common month : ', most_common_hour)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # display most commonly used start station
    most_common_start = df['Start Station'].mode()[0]
    print('The most common start station is :', most_common_start) 

    # display most commonly used end station
    most_common_end = df['End Station'].mode()[0]
    print('The most common end station is :', most_common_end)

    # display most frequent combination of start station and end station trip
    common_trip = 'from' + df['Start Station'] +" to "+ df['End Station'].mode()[0]
    print('Most frequent combination of start and end station trips : ', common_trip)

    

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # display total travel time
    total_trip_duration = df['Trip Duration'].sum()
    print('Total travel time is', total_trip_duration)

    # display mean travel time
    average_travel_time = df['Trip Duration'].mean()
    print('Average travel time is', average_travel_time)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # Display counts of user types
    user_types = df['User Type'].value_counts().to_frame()
    print('Types of users:\n', user_types)

    # Display counts of gender
    try:
        print("Gender is\n", df['Gender'].value_counts())


    # Display earliest, most recent, and most common year of birth
        print('Earliest birth year :', df['Birth Year'].min())
        print('Most recent birth year :', df['Birth Year'].max())
        print('Most common birth year :', df['Birth Year'].mode()[0]) 
    except:
        print('No filter with gender allowed in Washington city!')

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)




def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)
        display_raw_data(df)


        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()
