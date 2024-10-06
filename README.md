# US BikeShare Data Analysis 🚴‍♂️📊
This repository provides a comprehensive analysis of bike-share usage data from three major U.S. cities: Chicago, New York City, and Washington. The goal of this project is to uncover key insights regarding the most frequent travel times, popular stations, trip durations, and user demographics. By analyzing this data, we can gain a deeper understanding of urban mobility patterns and user behavior within the bike-share systems.

### Table of Contents
- [Project Overview](#project-overview)
- [Key Features](#key-features)
- [Technologies Used](#technologies-used)
- [Data Sources](#data-sources)
- [Setup Instructions](#setup-instructions)
- [Usage Guide](#usage-guide)
- [Example Analysis](#example-analysis)

## Project Overview
Bike-sharing systems are transforming urban mobility, providing convenient alternatives to cars and public transit. This project explores publicly available bike-share data from Chicago, New York City, and Washington, allowing users to filter data by city, month, and day of the week to reveal interesting trends.

By using Python and data analysis libraries, this project provides the following insights:
- What are the most popular times for bike-sharing trips?
- Which stations are most frequently used by riders?
- What are the typical trip durations across different cities?
- How do user demographics, including gender and birth year, vary across cities?
## Key Features
- Dynamic Data Filtering: Choose any city, month, or day to focus on specific timeframes.
- Comprehensive Travel Stats: Discover the most common times of travel, including the busiest months, days, and hours.
- Station Insights: Identify the most frequently used start and end stations and popular travel routes.
- Trip Duration Analysis: Calculate total and average trip durations.
- User Demographics: Get insights into user types (subscribers or customers), gender distribution, and birth year data where available.
## Technologies Used
- Python 3.7+: Core programming language for data analysis.
- Pandas: For data manipulation and analysis.
- NumPy: For efficient numerical operations.
- CSV files: Data storage format for the bike-share datasets.
## Data Sources
The datasets used in this project are publicly available through bike-share systems for each city:
1. Chicago: chicago.csv
2. New York City: new_york_city.csv
3. Washington: washington.csv
   
Each file includes:
- Start and end times of trips.
- Start and end stations.
- Trip duration.
- User types (Subscriber, Customer).
- Additional data (gender, birth year) for Chicago and New York City.
## Setup Instructions
To run this project locally, follow these steps:

Clone this repository to your local machine:
```
git clone https://github.com/yourusername/bikeshare-analysis.git
cd bikeshare-analysis
```
Install the required dependencies using pip:

```
pip install -r requirements.txt
```
Run the Python script:

```
python bikeshare.py
```
Follow the on-screen prompts to select a city, month, and day of the week for data filtering.

## Usage Guide
Once the script is running, you will be prompted to input the following:

1. City: Select from "Chicago", "New York City", or "Washington".
2. Month: Choose a month (January to June) or type 'all' to analyze the entire range.
3. Day: Select a specific day of the week (Monday to Sunday) or type 'all' to analyze all days.
The program will compute and display key statistics based on your inputs.

## Output Statistics:
- Time Stats: Most common month, day of the week, and hour of the day for bike trips.
- Station Stats: Most common start and end stations, and most frequent trip routes.
- Trip Duration Stats: Total and average trip duration.
- User Stats: Counts of user types, gender distribution (if available), and birth year information.
## Example Analysis
```
City: Chicago
Month: March
Day: Friday
```
Output:
```
Most Common Start Hour: 8 AM
Most Frequent Start Station: Streeter Dr & Grand Ave
Total Trip Duration: 1,002 hours
Average Trip Duration: 12.3 minutes
User Breakdown: 70% Subscribers, 30% Customers
Gender Distribution: 60% Male, 40% Female
Earliest Birth Year: 1945
Most Recent Birth Year: 2000
Most Common Birth Year: 1985
```
