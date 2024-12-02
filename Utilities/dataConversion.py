import datetime

def data_conversion(data):
    for document in data:
        if "timestamp" in document:
            document["timestamp"] = datetime.datetime.fromisoformat(document["timestamp"])
        if 'average_rating' in document:
            document['average_rating'] = float(document['average_rating'])
        if 'price' in document:
            document['price'] = float(document['price'])
            
    return data