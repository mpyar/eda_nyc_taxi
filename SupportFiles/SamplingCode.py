
# Take a small percentage of entries from each hour of every date.
# Iterating through the monthly data:
#   read a month file -> day -> hour: append sampled data -> move to next hour -> move to next day after 24 hours -> move to next month file
# Create a single dataframe for the year combining all the monthly data

# Select the folder having data files
import os

# Select the folder having data files
os.chdir('E:\\GitRepo\\eda_nyc_taxi\\Data\\trip_records')

# Create a list of all the twelve files to read
file_list = os.listdir()

# initialise an empty dataframe
df = pd.DataFrame()


# iterate through the list of files and sample one by one:
for file_name in file_list:
    try:
        # file path for the current file
        file_path = os.path.join(os.getcwd(), file_name)
        print(f"file_path: {file_path}")
        # Reading the current file
        monthly_df = pd.read_parquet(file_path)

        # We will store the sampled data for the current date in this df by appending the sampled data from each hour to this
        # After completing iteration through each date, we will append this data to the final dataframe.
        sampled_data = pd.DataFrame()

        # Loop through dates and then loop through every hour of each date
        for adate in monthly_df['tpep_pickup_datetime'].dt.date.unique():
            date_df = monthly_df[monthly_df['tpep_pickup_datetime'].dt.date == adate]
            #print(f"date: {adate}")
            # Iterate through each hour of the selected date
            for hour in  date_df['tpep_pickup_datetime'].dt.hour.unique():
                hour_data = date_df[date_df['tpep_pickup_datetime'].dt.hour == hour]

                # Sample 5% of the hourly data randomly
                sample = hour_data.sample(frac = 0.05, random_state = 42)

                # add data of this hour to the dataframe
                sampled_data = pd.concat([sampled_data, sample])

        # Concatenate the sampled data of all the dates to a single dataframe
        df =pd.concat([df, sampled_data])

    except Exception as e:
        print(f"Error reading file {file_name}: {e}")