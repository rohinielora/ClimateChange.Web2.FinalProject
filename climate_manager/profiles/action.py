from climate_manager.models.location import Location

def create_location_profile(name, latitude, longitude):
    return Location(name, latitude, longitude)
