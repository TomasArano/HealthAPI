import pandas as pd
def calculate_average_bpm_every_hour():
    """
    Calculate the average heart rate (BPM) for each hour of the day.
    
    Reads heartrate data from a CSV file and processes it to compute hourly averages.
    
    Returns:
        list[dict]: A list of dictionaries containing hourly averages, where each dict has:
            - 'Hour': int (0-23) representing the hour
            - 'averageBPM': float representing the average BPM for that hour
            
    Example return value:
        [
            {'Hour': 0, 'averageBPM': 65.5},
            {'Hour': 1, 'averageBPM': 68.2},
            ...
        ]
    """
    # Read the CSV file containing heart rate data
    df = pd.read_csv('/Users/air/Desktop/BSC Projects/HealthAPI/UPLOADS/heartrate.csv')
    
    # Combine Date and Time columns into a datetime object
    df['Datetime'] = pd.to_datetime(df['Date'] + ' ' + df['Time'])
    
    # Extract hour component from datetime
    df['Hour'] = df['Datetime'].dt.hour
    
    # Calculate mean BPM for each hour and format results
    hourly_avg = df.groupby('Hour', as_index=False)['BPM'].mean().rename(columns={'BPM': 'averageBPM'})
    
    return hourly_avg.to_dict(orient='records')

def calculate_hourly_range():
    """
    Calculate the minimum and maximum BPM for each hour of the day.

    Reads the heart rate data from 'heartrate.csv' and processes it to find
    the minimum and maximum BPM within each hour.

    Returns:
        list[dict]: A list of dictionaries, where each dictionary has:
            - 'Hour': int (0-23) representing the hour
            - 'minBPM': float representing the minimum BPM in that hour
            - 'maxBPM': float representing the maximum BPM in that hour
    """
    # Read CSV file
    df = pd.read_csv('/Users/air/Desktop/BSC Projects/HealthAPI/UPLOADS/heartrate.csv')
    
    # Combine Date and Time columns into a datetime object
    df['Datetime'] = pd.to_datetime(df['Date'] + ' ' + df['Time'])
    
    # Extract hour component from datetime
    df['Hour'] = df['Datetime'].dt.hour
    
    # Aggregate min and max BPM for each hour 
    hourly_min_max = df.groupby('Hour')['BPM'].agg(minBPM='min', maxBPM='max').reset_index()
    
    
    # Convert the result to a list of dictionaries
    return hourly_min_max.to_dict(orient='records')

def calculate_time_per_activity():
    """
    Calculate the total time spent on each activity based on the CSV data.
    
    The function reads the CSV file, combines "Date" and "Time" into a datetime,
    computes the duration (in minutes) between consecutive records, and aggregates
    the total time per activity label.
    
    Returns:
        list[dict]: A list where each dictionary has:
            - 'Activity': The label of the activity.
            - 'totalTime': Total time in minutes spent on that activity.
    """
    import pandas as pd
    # Read the CSV file
    df = pd.read_csv('/Users/air/Desktop/BSC Projects/HealthAPI/UPLOADS/heartrate.csv')
    
    # Combine Date and Time into datetime and sort
    df['Datetime'] = pd.to_datetime(df['Date'] + ' ' + df['Time'])
    df = df.sort_values('Datetime')
    
    # Compute duration (in minutes) to next record
    df['NextTime'] = df['Datetime'].shift(-1)
    df['duration'] = (df['NextTime'] - df['Datetime']).dt.total_seconds() / 60
    # Fill the last NaN with the median duration (or 5 if preferred)
    median_duration = df['duration'].median()
    df['duration'] = df['duration'].fillna(median_duration)
    
    # Group by the activity label and sum durations
    activity_duration = df.groupby('Label', as_index=False)['duration'].sum().rename(columns={'Label': 'Activity', 'duration': 'totalTime'})
    
    return activity_duration.to_dict(orient='records')


