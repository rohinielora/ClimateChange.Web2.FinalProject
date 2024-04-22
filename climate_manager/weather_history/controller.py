from flask import render_template
from .action import create_location_weather_record
from climate_manager.models.location import Location
from climate_manager.profiles.controller import get_location_data

def weather_history_view(conn, location):
    location_detail = get_location_data(location)
    cursor = conn.cursor()
    cursor.execute('''
        SELECT country, temperature, date FROM country_temperature WHERE country = ?
        ''', (location,))

    records = []
    rows = cursor.fetchall()
    for row in rows:
        records.append(create_location_weather_record(row[0], row[2], row[1], 0))

    # record = create_location_weather_record(location, "2024-04-15", 68, 0)
    return render_template("weather_history.html", location=location_detail, records=records)
