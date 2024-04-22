from climate_manager.models.location import Location
from climate_manager.models.weather import WeatherRecord

def create_location_weather_record(location, date, temperature, precipitation):
    return WeatherRecord(location, date, temperature, precipitation)
""" recently added """


def rank_countries_by_temperature(conn):
    cursor = conn.cursor()
    cursor.execute("SELECT country, temperature, date FROM country_temperature ORDER BY temperature DESC")
    ranked_countries = cursor.fetchall()
    return ranked_countries
