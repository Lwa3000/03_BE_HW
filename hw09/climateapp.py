import datetime as dt
import numpy as np
import pandas as pd

import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func

from flask import Flask, jsonify

#################################################
# Database Setup
#################################################
engine = create_engine("sqlite:///hawaii.db")

# reflect an existing database into a new model
Base = automap_base()
# reflect the tables
Base.prepare(engine, reflect=True)

# Save reference to the table
meas=Base.classes.measurement
station=Base.classes.station

# Create our session (link) from Python to the DB
session = Session(engine)

#################################################
# Flask Setup
#################################################
app = Flask(__name__)


#################################################
# Flask Routes
#################################################

@app.route("/")
def welcome():
    """List all available api routes."""
    return (
        f"Available Routes:<br/>"
        f"/api/v1.0/precipitation<br/>"
        f"/api/v1.0/stations<br/>"
        f"/api/v1.0/tobs<br/>"
        f"/api/v1.0/<start>/<end><br>"
    )

@app.route("/api/v1.0/tobs")
def tobs():
  # * Query for the dates and temperature observations from the last year.

  # * Convert the query results to a Dictionary using `date` as the key and `tobs` as the value.

  # * Return the json representation of your dictionary.
	d={}
	l_dates=[]
	l_tobs=[]
  	#Solution: will take the temperature observations from last available year of 
  	#		   data. Also, will take only station ending with 9281 because there are
  	#		   more than 1 stations.

	last_12_months = session.query(meas.date, meas.tobs).\
	filter(meas.date>'2016-08-22').filter(meas.station=='USC00519281')

	for date, tobs in last_12_months.all():
		l_dates.append(date)
		l_tobs.append(tobs)

	d["Dates"]=l_dates
	d["tobs"]=l_tobs

	return jsonify(d)

@app.route("/api/v1.0/stations")
def stations():
	# * Return a json list of stations from the dataset.
	d={}
	l_stations=[]
	result=session.query(station.station)
	for each in result.all():
		l_stations.append(each)
	d["Stations"]=l_stations
	return jsonify(d)

@app.route("/api/v1.0/precipitation")
def precipitation():
	# * Return a json list of Temperature Observations (tobs) for the previous year
	d={}
	l_dates=[]
	l_prcp=[]
  	#Solution: will take the temperature observations from last available year of 
  	#		   data. Also, will take only station ending with 9281 because there are
  	#		   more than 1 stations.

	last_12_months = session.query(meas.date, meas.prcp).\
	filter(meas.date>'2016-08-22').filter(meas.station=='USC00519281')

	for date, tobs in last_12_months.all():
		l_dates.append(date)
		l_prcp.append(tobs)

	d["Dates"]=l_dates
	d["prcp"]=l_prcp
	return jsonify(d)

@app.route("/api/v1.0/<start>/<end>")
def start_end(start,end):
    # * Return a json list of the minimum temperature, the average temperature, and the max temperature for a given start or start-end range.

    # * When given the start only, calculate `TMIN`, `TAVG`, and `TMAX` for all dates greater than and equal to the start date.

    # * When given the start and the end date, calculate the `TMIN`, `TAVG`, and `TMAX` for dates between the start and end date inclusive.
	
	#Assume: - input date format: `%Y-%m-%d`
	#		 - the temperature for all the stations are being used.

	d_return={}
	d={}
	l_dates=[]
	l_tobs=[]

	last_12_months = session.query(meas.date, meas.tobs).\
	    filter(meas.date>=start).filter(meas.date<=end)
	for date, tobs in last_12_months:
	    l_dates.append(date)
	    l_tobs.append(tobs)


	d["Dates"]=l_dates
	d["tobs"]=l_tobs
	df3=pd.DataFrame(d)
	d_return["max"]=int(df3["tobs"].max())
	d_return["min"]=int(df3["tobs"].min())
	d_return["avg"]=int(round(df3["tobs"].mean(),2))

	return jsonify(d_return)

@app.route("/api/v1.0/<start_date>")
def start(start_date):
    # * Return a json list of the minimum temperature, the average temperature, and the max temperature for a given start or start-end range.

    # * When given the start only, calculate `TMIN`, `TAVG`, and `TMAX` for all dates greater than and equal to the start date.

    # * When given the start and the end date, calculate the `TMIN`, `TAVG`, and `TMAX` for dates between the start and end date inclusive.

    #Assume: - input date format: `%Y-%m-%d`
	#		 - the temperature for all the stations are being used.
	
	end='2017-08-23'
	d_return={}
	d={}
	l_dates=[]
	l_tobs=[]

	result = session.query(meas.date, meas.tobs).\
	    filter(meas.date>=start_date).filter(meas.date<=end)
	for date, tobs in result:
	    l_dates.append(date)
	    l_tobs.append(tobs)


	d["Dates"]=l_dates
	d["tobs"]=l_tobs
	df3=pd.DataFrame(d)
	d_return["max"]=int(df3["tobs"].max())
	d_return["min"]=int(df3["tobs"].min())
	d_return["avg"]=int(round(df3["tobs"].mean(),2))

	return jsonify(d_return)

if __name__ == '__main__':
    app.run(debug=True)

