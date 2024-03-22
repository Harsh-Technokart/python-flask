import os
from flask import session, jsonify
from dotenv import load_dotenv
from pymongo import MongoClient

load_dotenv()

client = MongoClient(os.getenv("mongodb_atlas_access_token"))
database = client.ChatbotDatabase
user_collection = database.users


def create_user(user_data):
    try:
        user_collection.insert_one(user_data)
        return jsonify(
            {
                "message": f"{user_data.user_name} user added as {user_data.user_type}",
                "status": True,  # Changed status to True for success
                "status_code": 200,  # Changed status_code to 200 for success
            }
        )
    except Exception as e:
        return jsonify(
            {
                "message": f"Error occurred while generating user. error: {e}",
                "status": False,
                "status_code": 500,
            }
        )
