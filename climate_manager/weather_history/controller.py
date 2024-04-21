from flask import render_template
from .action import create_location_weather_record
from climate_manager.models.location import Location

def weather_history_view():
    location = Location("San Francisco", 37.7749, -122.4194)
    record = create_location_weather_record(location, "2024-04-15", 68, 0)
    return render_template("weather_history.html", location=location, record=record)
