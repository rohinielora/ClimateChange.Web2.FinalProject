from flask import render_template
from .action import create_location_profile

def profile_view():
    location = create_location_profile("San Francisco", 37.7749, -122.4194)
    return render_template("profile.html", location=location)
