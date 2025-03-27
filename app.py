import datetime
import os
from dotenv import load_dotenv
from flask import Flask, render_template, request
from pymongo import MongoClient
from urllib.parse import quote_plus


def create_app():
    app = Flask(__name__)

    load_dotenv()

    username = quote_plus(os.getenv("MONGO_USERNAME"))
    password = quote_plus(os.getenv("MONGO_PASSWORD"))
    host = os.getenv("MONGO_HOST")
    dbname = os.getenv("MONGO_DBNAME")

    mongo_uri = (
        f"mongodb+srv://{username}:{password}@python-microblog.1kbff8y.mongodb.net/"
    )

    client = MongoClient(mongo_uri)
    app.db = client.microblog

    @app.route("/", methods=["GET", "POST"])
    def home():
        if request.method == "POST":
            entry_content = request.form.get("content")
            formatted_date = datetime.datetime.today().strftime("%Y-%m-%d")
            app.db.entries.insert_one(
                {"content": entry_content, "date": formatted_date}
            )

        entries_with_date = [
            (
                entry["content"],
                entry["date"],
                datetime.datetime.strptime(entry["date"], "%Y-%m-%d").strftime("%b %d"),
            )
            for entry in app.db.entries.find({})
        ]
        return render_template("home.html", entries=entries_with_date)

    return app
