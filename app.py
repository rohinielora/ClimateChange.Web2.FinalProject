from flask import Flask, render_template, g
import sqlite3

from climate_manager.profiles.controller import profile_view
from climate_manager.weather_history.controller import weather_history_view

from climate_manager.weather_history.action import rank_countries_by_temperature
from flask import Flask, render_template

app = Flask(__name__)

def get_db():
    if 'db' not in g:
        g.db = sqlite3.connect('climate.db')
    return g.db

@app.teardown_appcontext
def close_db(exception=None):
    db = g.pop('db', None)
    if db is not None:
        db.close()

@app.route('/')
def home():
    return render_template("home.html")

@app.route('/profile')
def profile():
    return profile_view()

@app.route('/weather_history')
def weather_history():
    return weather_history_view()

if __name__ == '__main__':
    app.run(debug=True)

""" recently added """

@app.route('/temperature_rank')
def temperature_rank():
    ranked_countries = rank_countries_by_temperature()
    return render_template("temperature_rank.html", ranked_countries=ranked_countries)

