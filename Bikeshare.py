import time
import pandas as pd
import numpy as np
#python dictionary
CITY_DATA = { 'chicago': 'chicago.csv',
                        'new york city': 'new_york_city.csv',
                        'washington': 'washington.csv' }
#python lists
cities     = [ "new york city", "chicago", "washington" ]
months     = [ "january", "february", "march", "april", "may", "june", "all" ]
days       = [ "monday", "tuesday", "wednesday", "thursday",
                        "friday", "saturday", "sunday", "all" ]

 

def ask_user_to_select(choice, input_message):
    """
    In this section I've created a function to get the user's input and as per the hint given I've used a while loop to handle invalid inputs. 

    Returns:
        The function returns user's reply if valid.
    """
    reply = ""
#Using while loop to handle invalid inputs
    while len(reply) == 0:
        reply = input(input_message)
        reply = reply.strip().lower()

        if reply in choice:
            return reply
        else:
            reply = ""
            print("Please enter any one of the options given.\n")

def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print('\n ---Hey There! Let\'s explore some US bikeshare data! ----\n')
    # get user input for city (chicago, new york city, washington).
    city = ask_user_to_select(
            cities,
            "Please enter a city: 'new york city', 'chicago' or 'washington' : ")
        
    # get user input for month (all, january, february, ... , june)
    month = ask_user_to_select(
        months, 
        "Please enter month like: 'january', 'february', 'march', 'april' or 'all'(for all months): ")

    # get user input for day of week (all, monday, tuesday, ... sunday)
    day = ask_user_to_select(
        days,
        "Please enter day: 'monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday' or 'all'(for all days): ")

    print('-'*40)
    return city, month, day
    """
    Utilizes ask_user_to_select function to get the input from the users to return the city, month and day required to analyze the data.
    """

def load_data(city, month, day):
    """
    Loads data for the specified city and filters by month and day if applicable.

    Args:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    Returns:
        df - Pandas DataFrame containing city data filtered by month and day
		
	Methods used and their purpose:
		pd.read_csv() - used to read the given csv file.
		pd.to_datetime() - helps to convert string Date time into Python Date time object.
		df[].dt.month -  return a numpy array containing the month of the datetime in the underlying data of the given series object.
		df[].dt.week_day -  return a numpy array containing the week_day of the datetime in the underlying data of the given series object.
		df[].dt.hour -  return a numpy array containing the hour of the datetime in the underlying data of the given series object.
		df[].astype() - used to cast a pandas object to a specific datatype
		day.title() - used to make the first letter of the string upper case.
		
    """
    df = pd.read_csv(CITY_DATA[city], index_col = 0)

    df['Start Time'] = pd.to_datetime(df['Start Time'])     # to cast "Start Time" to datetime.
    df["month"] = df['Start Time'].dt.month                 # extract month from the Start Time column to create an ,month column
    df["week_day"] = df['Start Time'].dt.weekday_name       # extract weekday from the Start Time column to create an weekday column
    df["start_hour"] = df['Start Time'].dt.hour             # extract hour from the Start Time column to create an hour column
    df["start_end"] = df['Start Station'].astype(str) + ' to ' + df['End Station']

    if month != 'all':
        month_index = months.index(month) + 1      # get the list-index of the month.
        df = df[df["month"] == month_index ]                # get a filter for month.

    if day != 'all':
        df = df[df["week_day"] == day.title() ]             # get a filter for week day.
    
    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel.
	Methods used and their purpose:
		time.time() - This method returns the time as a floating point number expressed in seconds since the epoch, in UTC
		.mode() - To calculate the mode of given continuous numeric or nominal data
		.title() - Used to make the first letter of the string upper case.
	"""

    print('\nCalculating The Most Frequent Times of Travel ... \n')
    start_time = time.time()

    # display the most common month
    month_index = df["month"].mode()[0] - 1
    most_common_month = months[month_index].title()

    print("Most common month: ", most_common_month)
    
    # display the most common day of week
    most_common_day = df["week_day"].mode()[0]
    print("Most common day: ", most_common_day)
    
    # display the most common start hour
    most_common_hour = df["start_hour"].mode()[0]
    print("Most common hour: ", most_common_hour)
   
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip.
	Methods used and their purpose:
		time.time() - This method returns the time as a floating point number expressed in seconds since the epoch, in UTC
		.mode() - To calculate the mode of given continuous numeric or nominal data
		.title() - Used to make the first letter of the string upper case.
	"""

    print('\nCalculating The Most Popular Stations and Trip ...\n')
    start_time = time.time()

    # display most commonly used start station
    most_used_start = df['Start Station'].mode()[0]
    print("Most used start station: ", most_used_start)

    # display most commonly used end station
    most_used_end = df['End Station'].mode()[0]
    print("Most used end station: ", most_used_end)

    # display most frequent combination of start station and end station trip
    most_common_combination = df["start_end"].mode()[0]
    print("Most common used combination concerning start- and end-station: ", 
            most_common_combination)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration.
	Methods used and their purpose:
		.sum() - used to calculate the total sum.
		.mean() - used to find average.
	"""

    print("\nCalculating Trip Duration ...\n")
    start_time = time.time()

    # display total travel time
    total_travel_time = df["Trip Duration"].sum()
    print("Total time of travel: ", total_travel_time)

    # display mean travel time
    average_time = df["Trip Duration"].mean()
    print("The average travel-time: ", average_time)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users.
	Methods used and their purpose:
		.value_counts()- returns object containing counts of unique values.
		.count() - returns the count.
		.min() - returns the minimum of the data.
		.max() - returns the maximum of the data.
	"""

    print('\nCalculating User Stats ...\n')
    start_time = time.time()
    
    # Display counts of user types
    print("Count of user types:") 
    user_type = df["User Type"].value_counts()
    print(user_type)

    # Display counts of gender
    if "Gender" in df:
        print("\nCounts concerning client`s gender")
        print("Male persons: ", df.query("Gender == 'Male'").Gender.count())
        print("Female persons: ", df.query("Gender == 'Female'").Gender.count())

    # Display earliest, most recent, and most common year of birth
    if "Birth Year" in df:
        print("\nEarliest year of birth: ", df["Birth Year"].min())
        print("Most recent year of birth: ", df["Birth Year"].max())
        print("Most common year of birth: ", df["Birth Year"].value_counts().idxmax())

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)
	
def display_raw_data(df):
    '''Displays five lines of data if the user specifies that they would like to.
    After displaying five lines, ask the user if they would like to see five more,
    continuing asking until they say stop.

    Args:
        data frame
    Returns:
        none
    '''
    def is_valid(answer):
        if answer.strip().lower() in ['yes', 'no']:
            return True
        else:
            return False
    head = 0
    tail = 5
    valid_input = False
    while valid_input == False:
        answer = input('\nWould you like to view individual trip data? '
                        'Type "yes" or "no":')
        valid_input = is_valid(answer)
        if valid_input == True:
            break
        else:
            print("Wrong input. Please type 'yes' or"
                  " 'no'.")
    if answer.strip().lower() == 'yes':
        # prints every column except the 'journey' column created in statistics()
        print(df[df.columns[0:-1]].iloc[head:tail])
        display_more = ''
        while display_more.lower() != 'no':
            valid_input_2 = False
            while valid_input_2 == False:
                display_more = input('\nWould you like to view more individual'
                                     ' trip data? Type "yes" or "no":\n')
                valid_input_2 = is_valid(display_more)
                if valid_input_2 == True:
                    break
                else:
                    print("Wrong input. Please type "
                          "'yes' or 'no'.")
            if display_more.strip().lower() == 'yes':
                head += 5
                tail += 5
                print(df[df.columns[0:-1]].iloc[head:tail])
            elif display_more.strip().lower() == 'no':
                break




def main():
	print("-----Welcome-----")
    while True:
        city, month, day = get_filters()  
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)
        #raw = input("Do you want to see raw data? Please type 'yes' or 'no':")
		raw = 'yes'
        if raw.strip().lower() == 'yes':
            display_raw_data(df)

        restart = input('\nWould you like to restart? Enter yes or no:\n')
        if restart.lower() != 'yes':
            break
	print("Thank you!")	
	


if __name__ == "__main__":
	main()
