from climate_manager.models.location import Location

def create_location_weather_record(location, date, temperature, precipitation):
    return WeatherRecord(location, date, temperature, precipitation)
