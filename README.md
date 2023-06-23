# Module 10: SQL Alchemy Challenge

## Part 1: Analyze and Explore the Climate Data
Precipitation Analysis:
1. Find the most recent date in the dataset.
2. Using that date, get the previous 12 months of precipitation data by querying the previous 12 months of data.
3. Select only the "date" and "prcp" values.
4. Load the query results into a Pandas DataFrame. Explicitly set the column names.
5. Sort the DataFrame values by "date".
6. Plot the results by using the DataFrame plot method.
7. Use Pandas to print the summary statistics for the precipitation data.
Station Analysis:
1. Design a query to calculate the total number of stations in the dataset.
2. Design a query to find the most-active stations (that is, the stations that have the most rows). To do so, complete the following steps:
- List the stations and observation counts in descending order.
- Answer the following question: which station id has the greatest number of observations?
3. Design a query that calculates the lowest, highest, and average temperatures that filters on the most-active station id found in the previous query.
4. Design a query to get the previous 12 months of temperature observation (TOBS) data. To do so, complete the following steps:
- Filter by the station that has the greatest number of observations.
- Query the previous 12 months of TOBS data for that station.
5. Plot the results as a histogram with bins=12.

## Part 2: Design Your Climate App
1. Start at the homepage, and List all the available routes.
2. "/api/v1.0/precipitation"
- Convert the query results from your precipitation analysis (i.e. retrieve only the last 12 months of data) to a dictionary using date as the key and prcp as the value.
- Return the JSON representation of your dictionary.
3. "/api/v1.0/stations"
- Return a JSON list of stations from the dataset.
4. "/api/v1.0/tobs"
- Query the dates and temperature observations of the most-active station for the previous year of data.
- Return a JSON list of temperature observations for the previous year.
5. "/api/v1.0/<start> and /api/v1.0/<start>/<end>"
- Return a JSON list of the minimum temperature, the average temperature, and the maximum temperature for a specified start or start-end range.
- For a specified start, calculate TMIN, TAVG, and TMAX for all the dates greater than or equal to the start date.
- For a specified start date and end date, calculate TMIN, TAVG, and TMAX for the dates from the start date to the end date, inclusive.
- 
## Reflection
This challenge was broken up into two parts. The first part using Jupyter-Notebook to query the dataset provided into pandas. As I am more comfortable using jupyter-notebook, this section of the assignment was relatively smooth to do in the sense that many of the codes were done in our class activities. I used the hint guide provided by our instructor to reference which activity to which section of the analysis. I had also utilized askBCS, I was unable to meet with my tutor this week, as the person I had scheduled with was ill, so I had gotten alot of help from our TA and my classmates this week.
The API portion of the assignment was quite difficult for me. I ran into a lot of issues with trying to connect through Visual Studio Code, I kept getting warnings and errors when attemping to run my python file. I also ran into quite a few errors that were appearing on the API page itself. "ArgumentError", "Traceback", debugger issues, errors in my code lines and many more. With the help of our class TA, we were able to identify gaps in my codes. First, with simple things like capital and lower case letters such as "measurement.date" vs. "Measurement.date". Another was that I was not properly using my headers for the webpage, and text for <h1>,<h2>,<ol>,<li> which were not aligned with the links I had wanted. Trying to return the data, it was error upon error, and I truly was getting quite frustrated at one point. However, after a lot of hours and aid from the resources available, this part of the challenge was actually very interesting. I had used a lot of the files for the activities we had reviewed in class, and since I was unable to run them during the lectures, seeing it appear once my API was succesful it's pretty fascinating. I was unable to have a tutor session this week, which was very difficult for me, but thank goodness our class has a TA.
