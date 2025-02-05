# Health Data Visualization API

A Flask-based REST API that processes and visualizes heart rate data, providing endpoints for analyzing BPM (Beats Per Minute) patterns and activity distributions throughout the day.

## Features

- File upload support for CSV data files
- Heart rate analysis endpoints:
  - Average hourly BPM calculations
  - BPM range analysis
  - Activity duration tracking
- Interactive visualization using Chart.js
- Containerized deployment with Docker

## Tech Stack

- Python 3.12
- Flask
- Pandas (Data Processing)
- Chart.js (Frontend Visualization)
- Docker
- Bootstrap 3.4.1
- Gunicorn (WSGI Server)

## API Endpoints

- **POST /upload** - Upload heart rate data files
- **GET /averageBPM** - Retrieve hourly average heart rate
- **GET /rangeBPM** - Get BPM ranges per hour
- **GET /timeActivity** - Get time spent per activity

## Data Format

The application expects CSV files with the following structure:

```
Date,Time,BPM,Label
01/12/2025,00:00,58,Sleeping
```

