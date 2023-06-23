# Set up and import dependencies
import numpy as np

import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func

from flask import Flask, jsonify

import datetime as dt
from dateutil.relativedelta import relativedelta


#################################################
# Database Setup
#################################################
engine = create_engine("sqlite:///./Resources/hawaii.sqlite")

# Reflect an existing database into a new model
Base = automap_base()
# Reflect the tables.
Base.prepare(engine, reflect=True)

# Save reference to the tables
Measurement = Base.classes.measurement
Station = Base.classes.station


#################################################
# Flask Setup
#################################################
app = Flask(__name__)

#################################################
# Flask Routes
#################################################

@app.route("/")
def welcome():
    ## set up welcome page, and links to routes for data
    return (
        f"<h1>Module 10 Challenge</h1>"
        f"<h1>Part 2: Design Your Climate App</h1>"
        f"<h2>Here are the available routes:</h2>"

        f"<ol>Precipitation analysis - retrieve only the last 12 months of data:<br/>" 
        f"<li><a href=http://127.0.0.1:5000/api/v1.0/precipitation>"
        f"/api/v1.0/precipitation</a></li><br/><br/>"

        f"Stations Analysis - list of stations from the dataset:<br/>"
        f"<li><a href=http://127.0.0.1:5000/api/v1.0/stations>"
        f"/api/v1.0/stations</a></li><br/><br/>"
        
        f"Temperature Analysis - list of temperature observations for the previous year:<br/>"
        f"<li><a href=http://127.0.0.1:5000/api/v1.0/tobs>"
        f"/api/v1.0/tobs</a></li><br/><br/>"

        f"List of the minimum, average, and maximum temperature for a specified start date:<br/>"
        f"<li><a href=http://127.0.0.1:5000/api/v1.0/2017-08-23>"
        f"/api/v1.0/start</a></li><br/><br/>"

        f"List of the minimum, average, and maximum temperature for a specified start and end date <br/>"
        f"<li><a href=http://127.0.0.1:5000/api/v1.0/2016-08-23/2017-08-23>"
        f"/api/v1.0/start/end</a></li></ol><br/>"
        f"Brettney Chau-Dang<br/>"

    )

# Precipitation ANalysis:

@app.route("/api/v1.0/precipitation")
def precipitation():
    
    # Create our session (link) from Python to the DB
    session = Session(engine)

    # Date for one year ago from the last data point in the database
    last_years_data = session.query(
        Measurement.date).order_by(Measurement.date.desc()).first()
    (recent_date, ) = last_years_data
    recent_date = dt.datetime.strptime(recent_date, '%Y-%m-%d')
    recent_date = recent_date.date()
    last_years_date = recent_date - relativedelta(years=1)

    # Retrieve precipitation data 
    data_from_last_year = session.query(Measurement.date, Measurement.prcp).filter(
        Measurement.date >= last_years_date).all()

    session.close()

    # Convert results to a dictionary 
    prcp_dictionary = []
    for date, prcp in data_from_last_year:
        if prcp != None:
            prcp_dict = {}
            prcp_dict[date] = prcp
            prcp_dictionary.append(prcp_dict)

    # Return the JSON representation of the dictionary
    return jsonify(prcp_dictionary)

# Stations Analysis:

@app.route("/api/v1.0/stations")
def stations():
    
    # Create our session (link) from Python to the DB
    session = Session(engine)

    # Stations from the dataset
    stations = session.query(Station.station, Station.name,
                             Station.latitude, Station.longitude, Station.elevation).all()

    session.close()

    # Convert the results to a dictionary
    total_stations = []
    for station, name, latitude, longitude, elevation in stations:
        stations_dict = {}
        stations_dict["station"] = station
        stations_dict["name"] = name
        stations_dict["latitude"] = latitude
        stations_dict["longitude"] = longitude
        stations_dict["elevation"] = elevation
        total_stations.append(stations_dict)

    # Return the JSON representation of dictionary
    return jsonify(total_stations)

# Temperature Analysis:

@app.route("/api/v1.0/tobs")
def tobs():
    
    # Create our session (link) from Python to the DB
    session = Session(engine)

    # Date for one year ago from the last data point in the database
    last_years_data = session.query(
        Measurement.date).order_by(Measurement.date.desc()).first()
    (recent_date, ) = last_years_data
    recent_date = dt.datetime.strptime(recent_date, '%Y-%m-%d')
    recent_date = recent_date.date()
    last_years_date = recent_date - relativedelta(years=1)

    # The most active station
    most_active_station = session.query(Measurement.station).\
        group_by(Measurement.station).\
        order_by(func.count().desc()).\
        first()

    # Station ID number
    (most_active_station_id, ) = most_active_station
    print(
        f"The most active station is {most_active_station_id}.")

    # Query the dates and temperature observations of the most-active station for the previous year of data
    last_years_data = session.query(Measurement.date, Measurement.tobs).filter(
        Measurement.station == most_active_station_id).filter(Measurement.date >= last_years_date).all()

    session.close()

    # Convert results to a dictionary
    all_temps_dict = []
    for date, temp in last_years_data:
        if temp != None:
            temps_dict = {}
            temps_dict[date] = temp
            all_temps_dict.append(temps_dict)

    # Return the JSON representation of the dictionary
    return jsonify(all_temps_dict)

# Minimum, Maximum and Average temperature for specific start/end dates:

@app.route('/api/v1.0/<start>', defaults={'end': None})
@app.route("/api/v1.0/<start>/<end>")
def temps_for_date_range(start, end):

    # Create our session (link) from Python to the DB
    session = Session(engine)

    # If there is a start date and an end date
    if end != None:
        temps_data = session.query(func.min(Measurement.tobs), func.avg(Measurement.tobs), func.max(Measurement.tobs)).\
            filter(Measurement.date >= start).filter(
            Measurement.date <= end).all()
    # If we only have a start date
    else:
        temps_data = session.query(func.min(Measurement.tobs), func.avg(Measurement.tobs), func.max(Measurement.tobs)).\
            filter(Measurement.date >= start).all()

    session.close()

    # Convert the results to a list
    temps_list = []
    no_temps_data = False
    for min_temp, avg_temp, max_temp in temps_data:
        if min_temp == None or avg_temp == None or max_temp == None:
            no_temps_data = True
        temps_list.append(min_temp)
        temps_list.append(avg_temp)
        temps_list.append(max_temp)

    # Return the JSON representation of dictionary
    if no_temps_data == True:
        return f"There is no temperature data found for the chosen date range"
    else:
        return jsonify(temps_list)


if __name__ == '__main__':
    app.run(debug=True)