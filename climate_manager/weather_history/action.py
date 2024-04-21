from climate_manager.models.location import Location

def create_location_weather_record(location, date, temperature, precipitation):
    return WeatherRecord(location, date, temperature, precipitation)
""" recently added """


def rank_countries_by_temperature():
    conn = get_db()
    cursor = conn.cursor()
    cursor.execute("SELECT country, temperature FROM weather ORDER BY temperature DESC")
    ranked_countries = cursor.fetchall()
    return ranked_countries
