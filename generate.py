import pandas as pd
import random
from datetime import datetime, timedelta

# Define constants
date = "01/12/2025"
time_intervals = [datetime.strptime(f"{hour:02}:{minute:02}", "%H:%M") 
                  for hour in range(24) for minute in range(0, 60, 5)]

# Activity labels based on realistic daily routines
time_activity_map = [
    ("Sleeping", (0, 6)),
    ("Walking", (6, 8)),
    ("Sitting", (8, 12)),
    ("Standing", (12, 14)),
    ("Walking", (14, 16)),
    ("Cycling", (16, 18)),
    ("Running", (18, 20)),
    ("Sitting", (20, 22)),
    ("Sleeping", (22, 24)),
]

# Generate realistic BPM ranges for each activity
activity_bpm_ranges = [
    ("Sleeping", (50, 65)),
    ("Standing", (65, 80)),
    ("Sitting", (60, 75)),
    ("Running", (120, 180)),
    ("Walking", (80, 110)),
    ("Cycling", (90, 140)),
]


# Assign labels and BPM values based on time of day
data = []

for time in time_intervals:
    hour = time.hour
    activity = next((label for label, (start, end) in time_activity_map if start <= hour < end), "Unknown")
    bpm_range = next((rng for act, rng in activity_bpm_ranges if act == activity), (60, 100))
    bpm = random.randint(*bpm_range)
    data.append([date, time.strftime("%H:%M"), bpm, activity])

# Create DataFrame and save to CSV
df = pd.DataFrame(data, columns=["Date", "Time", "BPM", "Label"])
file_path = "/Users/air/Desktop/BSC Projects/HealthAPI/heartrate.csv"
df.to_csv(file_path, index=False)
file_path
