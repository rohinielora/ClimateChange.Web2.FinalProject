import sqlite3
import csv

from climate_manager.models.location import Location
from climate_manager.models.weather import WeatherRecord

def create_tables(cursor):
    cursor.execute('''CREATE TABLE locations (name TEXT, latitude REAL, longitude REAL)''')
    cursor.execute('''CREATE TABLE weather (location_name TEXT, date TEXT, temperature REAL, precipitation REAL)''')

def insert_location_data(cursor, locations):
    for location in locations:
        cursor.execute("INSERT INTO locations VALUES (?, ?, ?)", (location.name, location.latitude, location.longitude))

def insert_weather_data(cursor,
