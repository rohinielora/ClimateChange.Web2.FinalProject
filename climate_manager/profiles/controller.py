from flask import render_template
from .action import create_location_profile
import csv

def get_location_data(location):
    with open('country.csv', newline='') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            if row['country'] == location:
                location = create_location_profile(row['country'], row['lat'], row['lon'])
                return location

def get_all_locations():
    with open('country.csv', newline='') as csvfile:
        reader = csv.DictReader(csvfile)
        locations = []
        for row in reader:
            location = create_location_profile(row['country'], row['lat'], row['lon'])
            locations.append(location)
        return locations

def profile_view():
    locations = get_all_locations()
    # location = create_location_profile("San Francisco", 37.7749, -122.4194)
    return render_template("profile.html", locations=locations)
