import datetime
import os
from dotenv import load_dotenv
from flask import Flask, render_template, request
from pymongo import MongoClient
from urllib.parse import quote_plus

app = Flask(__name__)

load_dotenv()

username = quote_plus(os.getenv("MONGO_USERNAME"))
password = quote_plus(os.getenv("MONGO_PASSWORD"))
host = os.getenv("MONGO_HOST")
dbname = os.getenv("MONGO_DBNAME")

mongo_uri = f"mongodb+srv://{username}:{password}@python-microblog.1kbff8y.mongodb.net/"

client = MongoClient(mongo_uri)
app.db = client.microblog
entries = []


@app.route("/", methods=["GET", "POST"])
def home():
    if request.method == "POST":
        entry_content = request.form.get("content")
        formatted_date = datetime.datetime.today().strftime("%Y-%m-%d")
        entries.insert(0, (entry_content, formatted_date))
        app.db.entries.insert_one({"content": entry_content, "date": formatted_date})

    entries_with_date = [
        (
            entry[0],
            entry[1],
            datetime.datetime.strptime(entry[1], "%Y-%m-%d").strftime("%b %d"),
        )
        for entry in entries
    ]
    return render_template("home.html", entries=entries_with_date)
