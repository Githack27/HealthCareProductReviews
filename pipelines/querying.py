import requests
import random
import os
import json
from pymongo import MongoClient
from dotenv import load_dotenv

load_dotenv()
API_URL = "http://127.0.0.1:8000/query/"
client = MongoClient(os.getenv("DATABASE_URL"))
db = client[os.getenv("DATABASE_NAME")]
collection = db[os.getenv("COLLECTION_NAME")]

def query_reviews():
    store_cursor = collection.find({}, {"store": 1, "_id": 0})
    store_list = [store['store'] for store in store_cursor if 'store' in store]

    store_name = random.choice(store_list)
    user_review = input("Enter your review: ")
    
    payload = {
        "user_review": user_review,
        "store_name": store_name,
        "similarity_threshold": 0.4
    }

    try:
        response = requests.post(API_URL, json=payload)

        if response.status_code == 200:
            response_data = response.json()
            return json.dumps(response_data, indent=4)
        else:
            print(f"Error: {response.status_code} - {response.text}")
    
    except Exception as e:
        print(f"Error making request: {str(e)}")
    
