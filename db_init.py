import sqlite3
import csv

def create_tables(cursor):
    # Assuming you already have other table creation statements
    cursor.execute('''
        DROP TABLE IF EXISTS country_temperature
    ''')
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS country_temperature (
            country TEXT,
            temperature REAL,
            date TEXT
        )
    ''')

def insert_temperature_data(cursor, temperature_data):
    for entry in temperature_data:
        cursor.execute('''
            INSERT INTO country_temperature (country, temperature, date) 
            VALUES (?, ?, ?)
        ''', (entry['country'], entry['temperature'], entry['date'].strip()))

def load_temperature_from_csv(filename):
    temperature_data = []
    with open(filename, newline='') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            temperature_data.append(row)
    return temperature_data

def main():
    # Establish a database connection and create a cursor object
    conn = sqlite3.connect('climate.db')
    cursor = conn.cursor()

    # Create tables
    create_tables(cursor)

    # Load temperature data from CSV and insert into the database
    temperature_data = load_temperature_from_csv('country_temperature.csv')
    insert_temperature_data(cursor, temperature_data)

    # Commit changes and close the database connection
    conn.commit()
    
    query = cursor.execute("SELECT * FROM country_temperature")
    rows = query.fetchall()
    print(rows)
    print(rows[1][0])
    print(rows[1][1])
    print(rows[1][2])
    conn.close()

if __name__ == "__main__":
    main()



"""
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
*\

"""
