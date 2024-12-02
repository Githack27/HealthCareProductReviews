schema = {
    "$jsonSchema": {
        "bsonType": "object",
        "required": ["parent_asin", "asin", "user_id", "average_rating", "main_category", "title"],
        "properties": {
            "main_category": {"bsonType": "string"},
            "title": {"bsonType": "string"},
            "average_rating": {"bsonType": "double"},
            "rating_number": {"bsonType": ["int", "null"]},
            "description": {"bsonType": ["array", "null"], "items": {"bsonType": "string"}},
            "price": {"bsonType": ["double", "null"]},
            "images": {
                "bsonType": ["array", "null"],
                "items": {
                    "bsonType": "object",
                    "properties": {
                        "thumb": {"bsonType": "string"},
                        "large": {"bsonType": "string"},
                        "variant": {"bsonType": "string"},
                        "hi_res": {"bsonType": "string"}
                    }
                }
            },
            "store": {"bsonType": ["string", "null"]},
            "details": {
                "bsonType": ["object", "null"],
                "properties": {
                    "Brand": {"bsonType": "string"},
                    "Item Form": {"bsonType": "string"},
                    "Active Ingredients": {"bsonType": "string"},
                    "Age Range (Description)": {"bsonType": "string"},
                    "Unit Count": {"bsonType": "string"},
                    "Is Discontinued By Manufacturer": {"bsonType": "string"},
                    "Date First Available": {"bsonType": "string"},
                    "Manufacturer": {"bsonType": "string"}
                }
            },
            "parent_asin": {"bsonType": "string"},
            "rating": {"bsonType": ["int", "null"]},
            "text": {"bsonType": ["string", "null"]},
            "asin": {"bsonType": "string"},
            "user_id": {"bsonType": "string"},
            "timestamp": {"bsonType": "date"},
            "helpful_vote": {"bsonType": ["int", "null"]},
            "verified_purchase": {"bsonType": ["bool", "null"]}
        }
    }
}
