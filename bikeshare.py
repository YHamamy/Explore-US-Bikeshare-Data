import time
import pandas as pd
import numpy as np

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }
Months=["January","February","March","April","May","June"]
days=["Sunday","Monday","Tuesday","Wednesday","Thursday","Friday","Saturday"]

def get_filters():
    #Using try except to overcome KeyboardInterrupt.
    try:
        """
        Asks user to specify a city, month, and day to analyze.

        Returns:
            (str) city - name of the city to analyze
            (str) month - name of the month to filter by, or "all" to apply no month filter
            (str) day - name of the day of week to filter by, or "all" to apply no day filter
        """
        print('Hello! Let\'s explore some US bikeshare data!')
        # TO DO: get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
        #Getting city name to analyze
        print("Please choose one of the following cities:\n# chicago\n# new york city\n# washington")
        city = input("Enter city name: \n").lower()

        #using loop incase select wrong choice.
        while city not in CITY_DATA.keys():
            print("You didn't enter valid choice!\n")
            city = input("Re-enter valid city: \n").lower()

        while True:
            print("You can choose one of the folloing filtration options:\n# 'Yes':Choose type of filtration.\n# 'No': No filtration.\n")
            choice=input("Choose one option:\n").lower()
            while choice not in ["yes","no"]:
                print("You didn't enter valid choice!\n")
                choice=input("Re-enter your choice:\n").lower()
            if choice=="yes": #filtration in case of yes
                print("You can choose one of the following option to proceed your filtration:\n# Month\n# Day\n# Both\n")
                filtering=input("Choose your filtration option\n").lower()
                while filtering not in ["month","day","both"]:
                    print("You didn't enter valid choice\n")
                    filtering=input("Re-enter your choice\n").lower()
                    continue
                    # TO DO: get user input for month (all, january, february, ... , june)

                if filtering=="month": #Getting month to analyze.
                    print("You can choose one of the below Months:\nJanuary , February , March , April , May , June.\n")
                    month = input("Enter the required Month: \n").lower().title()
                    day="All"

                    while month not in Months:  #incase of wrong choice,the loop will ask to reenter the name again 
                        print("You didn't enter valid choice!\n")
                        month = input("Re-enter reqired month:\n").lower().title()
                        continue
                    break

                 # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)

                elif filtering=="day": #Getting day to  be analyze.
                    print("You can choose one of the below Days:\nSunday , Monday , Tuesday , Wednesday , Thursday , Friday , Saturday.")
                    day = input("Enter the required Day: \n").lower().title()
                    month="All"

                    while day not in days:
                        print("You didn't enter valid choice!\n")
                        day = input("Re-enter reqired day:\n").lower().title()
                        continue
                    break

                elif filtering=="both": #incase of both month & day filtration
                    print("You can choose one of the below Months:\nJanuary , February , March , April , May , June.\n")
                    month = input("Enter the required Month: \n").lower().title()

                    while month not in Months:
                        print("You didn't enter valid choice!\n")
                        month = input("Re-enter reqired month:\n").lower().title()
                        continue


                    print("You can choose one of the below Days:\nSunday , Monday , Tuesday , Wednesday , Thursday , Friday , Saturday.")
                    day = input("Enter the required Day: \n").lower().title()

                    while day not in days:
                        print("You didn't enter valid choice!\n")
                        day = input("Re-enter reqired day:\n").lower().title()
                        continue

            elif choice=="no": #incase no filtration
                day = "All"
                month = "All"
                break

            else:
                print("You didn't enter valid choice!")
                continue
            break    
                    
    except KeyboardInterrupt:
        print("Keyboard Interruption catched")


    


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
    df = pd.read_csv(CITY_DATA[city]) #load city data into df
    df['Start Time'] = pd.to_datetime(df['Start Time']) #converting start time to datetime
    df['month'] = df['Start Time'].dt.month  #extract month from start time.
    df['day_of_week'] = df['Start Time'].dt.day_name()  #extract day_week from month from start time.
    
    if month != "All":        #filtering month
        
        Months = ["January","February","March","April","May","June"]
        month = Months.index(month) + 1  #using index to get corresponding int.
        
        df = df[df['month'] == month]  #filtering month to create df.
        
    
    if day != "All": #filtering day of the week.
        df = df[df['day_of_week'] == day.title()] #filtering day to create df.


    return df


def time_stats(df):
    
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()
    df['hour'] = df['Start Time'].dt.hour
    

    # TO DO: display the most common month
    #using mode index 0 to get the most common
    
    common_day_month = df['month'].mode()[0]
    print("The most common month:",common_day_month)

    # TO DO: display the most common day of week
    common_day_week = df['day_of_week'].mode()[0]
    print("The most common day of the week:",common_day_week)


    # TO DO: display the most common start hour
    common_start_hour = df['hour'].mode()[0]
    print("the most common start hour:",str(common_start_hour))
    

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()
    
    #using mode index 0 to get the most common

    # TO DO: display most commonly used start station
    commonly_start_station = df['Start Station'].mode()[0]
    print("The most used start station:\n",commonly_start_station)


    # TO DO: display most commonly used end station
    commonly_End_Station = df['End Station'].mode()[0]
    print("The most used end station:\n", commonly_End_Station)


    # TO DO: display most frequent combination of start station and end station trip
    Frequent_Combination = (df['Start Station'] + "_" + df['End Station']).mode()[0]
    print("The frequently combination start and end station:\n",Frequent_Combination.split("_"))   


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()
     #convert sec into H:M:S     
    def times(sec):
          sec %= (24*3600)
          hour = sec//3600
          sec %= 3600
          minute = sec//60
          sec %= 60
          return "%d:%02d:%02d" % (hour,minute,sec)

    # TO DO: display total travel time
    Total_Travel_Time = df['Trip Duration'].sum()  #use Sum() to get the total
    print("Total travel time:\n"+times(Total_Travel_Time)+ " H:M:S")      

    # TO DO: display mean travel time
    Average_Travel_Time = df['Trip Duration'].mean() # use mean() to get the average
    print("Average travel time:\n"+times(Average_Travel_Time)+ " H:M:S")      


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    User_Type = df['User Type'].value_counts()   #get the unique count
    print("Count of user type:\n",User_Type)
          

    # TO DO: Display counts of gender
         
    if "Gender" in df.columns:
          Genders = df['Gender'].value_counts() #count unique gender
          print("Gender count:\n",Genders)
          
    else:  #incase gender coloumn not found 
          print("Gender counts:\nThere is no gender data found for this city")


    # TO DO: Display earliest, most recent, and most common year of birth
    if "Birth Year" in df.columns:
          Earliest = df['Birth Year'].min()  # get the smallest year which is the oldest.
          print("Earliest Year of birth: ",str(Earliest))
          Most_Recent = df['Birth Year'].max() # get the biggest year which is the youngest.        
          print("Most recent birth year: ",str(Most_Recent))
          Most_Commom_Year = df['Birth Year'].mode()[0]  
          print("Most common birth day year: ",str(Most_Commom_Year))

        
    else:  # incase no birthday data found
          print("There is no birth day data found for this city")  


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def display_raw_data(df):
    
    View=0
    while True:
        Display_Raw = input("Would you like to view 5 rows from data row? select Yes or No\n")
        if Display_Raw not in ["yes","no"]: #incase selection was out of list
            print("You didn't enter valid choice")

        if Display_Raw =="yes":
            print(df.iloc[View:View+5])
            View+=5
        elif Display_Raw =="no":
             break        

    
    
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
            print("\nExit\n")
            break


if __name__ == "__main__":
	main()
