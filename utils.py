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
    df = pd.read_csv('/Users/air/Desktop/BSC Projects/HealthAPI/UPLOADS/heartrate.csv')
    df['Datetime'] = pd.to_datetime(df['Date'] + ' ' + df['Time'])
    df['Hour'] = df['Datetime'].dt.hour
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
    
    # group minimum and maximum BPM for each hour
    #hourly_min_max = df.groupby('Hour', as_index=False)['BPM'].agg(['min', 'max']).reset_index()
    #3hourly_min_max = hourly_min_max.rename(columns={'min': 'minBPM', 'max': 'maxBPM'})
    
    # Aggregate min and max BPM for each hour, ensuring no unnecessary index column
    hourly_min_max = df.groupby('Hour')['BPM'].agg(minBPM='min', maxBPM='max').reset_index()
    
    
    # Convert the result to a list of dictionaries
    return hourly_min_max.to_dict(orient='records')


