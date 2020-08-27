from flask import Flask,request,send_from_directory
import json
import random
import database
from scraper import final
import sqlite3
from flask_cors import CORS
import datetime

app = Flask(__name__)
CORS(app)

@app.route("/")
def root():
    return index('index.html')

@app.route("/<path>")
def index(path):
    return send_from_directory('frontend', path)

@app.route("/api/fetchRandom")
def fetchRandom():
    #random 1 to 30 return that as json
    scrape_time = datetime.datetime.now().strftime("%Y_%m_%d_%H")#time when web page was run
    rank = random.randint(1,30)
    if not database.tableExists(scrape_time):
        database.createTable(scrape_time)
        database.write(scrape_time,final)
    data = database.read(scrape_time,rank)
    return {"rank": data[0], "title": data[1], "time": data[2]}

if __name__ == "__main__":
    #app.run()
    #app.run(port=8080, debug=True)
    app.run(port=443, debug=False)
