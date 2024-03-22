from flask import Flask
import os
from dotenv import load_dotenv
from pymongo import MongoClient
from route_handlers.user_management_routes import (
    login as loginMethod,
    create_user as createUserMethod,
)

app = Flask(__name__)
load_dotenv()
database = MongoClient(os.getenv("mongodb_atlas_access_token"))
session_secret = os.getenv("session_secret")
user_collection = database.user_collection


@app.route("/user-login")
def login():
    return loginMethod(user_collection)


@app.route("/sign-up", methods=["POST"])
def signup():
    createUserMethod()


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)
