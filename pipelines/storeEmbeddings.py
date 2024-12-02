from pymongo import MongoClient
from sentence_transformers import SentenceTransformer
from typing import List
import os
from dotenv import load_dotenv

load_dotenv()

def store_embeddings():
    mongo_client = MongoClient(os.getenv("DATABASE_URL"))
    db = mongo_client[os.getenv("DATABASE_NAME")]
    mongo_collection = db[os.getenv("COLLECTION_NAME")]

    embedding_model = SentenceTransformer('all-MiniLM-L6-v2')

    def generate_embedding(text: str) -> List[float]:
        if not text:
            return [0.0] * embedding_model.get_sentence_embedding_dimension()
        return embedding_model.encode(text).tolist()

    batch_size = 1000
    last_id = None

    while True:
        query = {"_id": {"$gt": last_id}} if last_id else {}
        documents = list(mongo_collection.find(query).sort("_id").limit(batch_size))

        if not documents:
            break

        for document in documents:
            text = document.get("text")
            if not text:
                continue

            try:
                embeddings = generate_embedding(text)

                update_data = {
                    "embedding": embeddings
                }

                mongo_collection.update_one(
                    {"_id": document["_id"]},
                    {"$set": update_data}
                )
            except Exception as e:
                print(f"Error processing document {document.get('_id')}: {e}")

        last_id = documents[-1]["_id"]
        print(f"Batch of {len(documents)} documents processed successfully.")

    print("All documents processed.")
