from fastapi import FastAPI, HTTPException
from pymongo import MongoClient
from sentence_transformers import SentenceTransformer
import numpy as np
import os
from pydantic import BaseModel
from dotenv import load_dotenv

load_dotenv()

app = FastAPI()

client = MongoClient(os.getenv("DATABASE_URL"))
db = client[os.getenv("DATABASE_NAME")]
collection = db[os.getenv("COLLECTION_NAME")]


model = SentenceTransformer('all-MiniLM-L6-v2')
    
def cosine_similarity(vec1, vec2):
    dot_product = np.dot(vec1, vec2)
    norm_a = np.linalg.norm(vec1)
    norm_b = np.linalg.norm(vec2)
    return dot_product / (norm_a * norm_b)

class QueryRequest(BaseModel):
    user_review: str
    store_name: str
    similarity_threshold: float = 0.4
    
@app.post("/query/")
async def query_reviews_with_store(request: QueryRequest):
    try:
        user_review = request.user_review
        store_name = request.store_name
        similarity_threshold = request.similarity_threshold

        user_review_embedding = model.encode(user_review).tolist()

        records = list(collection.find({"store": store_name}, {"_id": 0, "text": 1, "embedding": 1, "title": 1, "rating": 1}))
        
        matching_records = []

        for record in records:
            text = record['text']
            embedding = record['embedding']
            title = record["title"]
            rating = record["rating"]
            similarity = cosine_similarity(user_review_embedding, embedding)
            
            if similarity >= similarity_threshold:
                matching_records.append({"title": title, "text": text, "rating":rating, "similarity": similarity})
                
        if not matching_records:
            for record in records:
                record.pop('embedding', None) 
            print(record["title"])
            return {"\n"+"records": records}

        print("\n"+matching_records["title"])
        return {"matching_records": matching_records}

    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error processing request: {str(e)}")
