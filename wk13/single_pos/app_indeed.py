from flask import Flask, render_template, jsonify, redirect
from flask_pymongo import PyMongo
import scrape_indeed

app = Flask(__name__)

mongo = PyMongo(app)


@app.route("/")
def index():
    cursor_position = mongo.db.items.find_one()
    return render_template("index.html", positions_1=cursor_position)


@app.route("/scrape")
def scrape():
    positions = mongo.db.items
    positions_data = scrape_indeed.scrape()
    for item in positions_data:
        positions.update(
            {},
            item,
            upsert=True
        )
    return redirect("http://localhost:5000/", code=302)


if __name__ == "__main__":
    app.run(debug=True)
