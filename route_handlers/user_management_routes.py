import os
from flask import request as req, session, jsonify
from dotenv import load_dotenv
from pymongo import MongoClient
from validation.user_management_validations import validate_sign_up
from queries.user_management_queries import create_user as create_user_query

load_dotenv()

client = MongoClient(os.getenv("mongodb_atlas_access_token"))
database = client.ChatbotDatabase
user_collection = database.users


def login(user_collection_reference):
    aleged_username = req.get_data("username")
    aleged_password = req.get_data("password")
    if aleged_username is not None:
        user_collection.findOne(
            {"user_name": aleged_username, "password": aleged_password}
        )
    print("user session details:", session)
    return {"message": "unbuilt route", "status": False, "status_code": 501}


def create_user(request_data):
    request_data = req.json
    is_valid, error_message = validate_sign_up(request_data)
    if not is_valid:
        return jsonify({"message": error_message, "status": False, "status_code": 400})
    else:
        response = create_user_query(request_data)
        return response
