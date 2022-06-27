from flask import Flask, render_template, redirect
from flask_pymongo import PyMongo
import scrape_mars
import pandas as pd 

# Set up flask
app = Flask(__name__)
# Connect to pymongo
mongo = PyMongo(app, uri = "mongodb://localhost:27017/mars_database")


@app.route("/")
def index():

	mars = mongo.db.mars.find_one()
	return render_template("index.html", mars=mars)


@app.route("/scrape")
def scrape():

	mars_info = mongo.db.mars
	mars_final = scrape_mars.scrape()
	mars_info.update_one({}, {"$set":mars_final}, upsert=True)


	return redirect("/", code=302)

if __name__ == "__main__":
	app.run(debug=True)