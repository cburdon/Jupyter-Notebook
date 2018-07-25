from flask import Flask, jsonify, render_template, redirect
from scrape_mars import scrape
from flask_pymongo import PyMongo

#flask setup
app = Flask(__name__)

#Mongodb connection
app.config["MONGO_URI"] = "mongodb://localhost:27017/mars"

mongo = PyMongo(app)

@app.route("/scrape")
def scrape_page():
    mars_info = scrape()
    mongo.db.mars.drop()
    mongo.db.mars.insert_one(mars_info)
    return redirect("/")


@app.route("/")
def main():
    mars_scraped = mongo.db.mars.find_one()
    return render_template("index.html", mars_scraped=mars_scraped)

if __name__ == '__main__':
    app.run(debug=True)
