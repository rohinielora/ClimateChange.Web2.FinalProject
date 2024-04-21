from flask import render_template
from .action import get_locations_for_display, create_weather_history
from climate_manager.models.location import Location
from climate_manager.models.history import History

def location_view():
    location = create_location("New York City", 40.7128, -74.0060)
    return render_template("location.html", location=location)

def weather_history_view(location_name):
    location = create_location("New York City", 40.7128, -74.0060)
    history = create_weather_history(location, "2024-04-20", "16°C", "0mm")
    return render_template("weather_history.html", location=location, history=history)
