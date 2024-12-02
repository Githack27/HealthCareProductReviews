import os
from pipelines.schema import schema
from pymongo import MongoClient, errors
from dotenv import load_dotenv

load_dotenv()

def create_database():
    try:
        client = MongoClient(os.getenv("DATABASE_URL"))
        db = client[os.getenv("DATABASE_NAME")]
        collection_name = os.getenv("COLLECTION_NAME")
        
        if collection_name in db.list_collection_names():
            print(f"The collection '{collection_name}' already exists.")
        else:
            db.create_collection(collection_name, validator=schema)
            print(f"The collection '{collection_name}' created successfully with schema validation!")
    except errors.CollectionInvalid as e:
        print(f"Collection creation error: {e}")
    except errors.PyMongoError as e:
        print(f"Database connection error: {e}")

if __name__ == "__main__":
    create_database()