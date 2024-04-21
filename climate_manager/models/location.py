class Location:
    def __init__(self, name, latitude, longitude):
        self.name = name
        self.latitude = latitude
        self.longitude = longitude
        self.weather_history = []

    def add_weather_record(self, record):
        self.weather_history.append(record)
