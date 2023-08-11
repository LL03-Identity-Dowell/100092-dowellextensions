import requests
import json
from datetime import datetime
import uuid
import sys
import os
SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
sys.path.append(os.path.dirname(SCRIPT_DIR))


# DO NOT CHANGE THE CONSTANTS
# COLLECTIONS
NOTIFICATION_COLLECTION = "notification"
ANNOUNCEMENT_COLLECTION = "announcement"

# DOCUMENTS
DOCUMENT_NAMES = {
    NOTIFICATION_COLLECTION: "notification",
    ANNOUNCEMENT_COLLECTION: "announcement"
}

# TEAM ID
TEAM_IDS = {
    NOTIFICATION_COLLECTION: "100092100",
    ANNOUNCEMENT_COLLECTION: "100092200"
}

# FUNCTION ID
DEFAULT_FUNC_ID = "ABCDE"

# SERVER
DATABASE = "extension"
CLUSTER = "extension"

# RECORD LOAD
BASE_URL = "http://uxlivinglab.pythonanywhere.com/"


def format_id(id):
    return f"ObjectId"+"("+"'{id}'"+")"


def get_event_id():
    url = f"{BASE_URL}create_event"

    data = {
        "platformcode": "FB",
        "citycode": "101",
        "daycode": "0",
        "dbcode": "pfm",
        "ip_address": "192.168.0.41",  # get from dowell track my ip function
        "login_id": "lav",  # get from login function
        "session_id": "new",  # get from login function
        "processcode": "1",
        "location": "22446576",  # get from dowell track my ip function
        "objectcode": "1",
        "instancecode": "100051",
        "context": "afdafa ",
        "document_id": "3004",
        "rules": "some rules",
        "status": "work",
        "data_type": "learn",
        "purpose_of_usage": "add",
        "colour": "color value",
        "hashtags": "hash tag alue",
        "mentions": "mentions value",
        "emojis": "emojis",
        "bookmarks": "a book marks"
    }

    r = requests.post(url, json=data)
    if r.status_code == 201:
        return json.loads(r.text)
    else:
        return json.loads(r.text)['error']


def save_document(collection: str, value: dict):
    event_id = get_event_id()

    # Build request data or payload
    payload = json.dumps({
        "cluster": CLUSTER,
        "database": DATABASE,
        "collection": collection,
        "document": DOCUMENT_NAMES[collection],
        "team_member_ID": TEAM_IDS[collection],
        "function_ID": DEFAULT_FUNC_ID,
        "command": "insert",
        "field": {
            "eventId": event_id,
            DOCUMENT_NAMES[collection]: value
        },
        "update_field": {"update_field": "nil"},
        "platform": "bangalore"
    })

    # Setup request headers
    headers = {
        'Content-Type': 'application/json'
    }

    # Send POST request to server
    r = requests.request("POST", BASE_URL, headers=headers, data=payload)
    return json.loads(r.json())


def update_document(
    collection: str,
    new_value: dict,
    document_id: str
):
    # Build request data or payload
    payload = json.dumps({
        "cluster": CLUSTER,
        "database": DATABASE,
        "collection": collection,
        "document": DOCUMENT_NAMES[collection],
        "team_member_ID": TEAM_IDS[collection],
        "function_ID": DEFAULT_FUNC_ID,
        "command": "update",
        "field": {'_id': document_id},
        "update_field": {DOCUMENT_NAMES[collection]: new_value},
        "platform": "bangalore"
    })

    # Setup request headers
    headers = {
        'Content-Type': 'application/json'
    }

    # Send POST request to server
    r = requests.request("POST", BASE_URL, headers=headers, data=payload)
    return json.loads(r.json())


def fetch_document(
    collection: str,
    fields: dict,
):
    # Build request data or payload
    payload = json.dumps({
        "cluster": CLUSTER,
        "database": DATABASE,
        "collection": collection,
        "document": DOCUMENT_NAMES[collection],
        "team_member_ID": TEAM_IDS[collection],
        "function_ID": DEFAULT_FUNC_ID,
        "command": "fetch",
        "field": fields,

        "update_field": {"update_field": "nil"},
        "platform": "bangalore"

    })

    # Setup request headers
    headers = {
        'Content-Type': 'application/json'
    }

    # Send POST request to server
    r = requests.request("POST", BASE_URL, headers=headers, data=payload)
    return json.loads(r.json())


if __name__ == "__main__":
    pass
