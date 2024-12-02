import json
import datetime
from Utilities.dataConversion import data_conversion
from DBHelpers.insertTodatabase import insert_data

def transform():
    with open('dataset/Meta_Health_and_Personal_Care.json', 'r') as meta_file, open('dataset/Health_and_Personal_Care.json', 'r') as product_file:
        meta_data = json.load(meta_file)
        product_data = json.load(product_file)

    if not isinstance(meta_data, list):
        meta_data = [meta_data]
    if not isinstance(product_data, list):
        product_data = [product_data]

    product_data_map = {product["parent_asin"]: product for product in product_data}

    merged_data = []

    for meta in meta_data:
        parent_asin = meta.get("parent_asin")
        if parent_asin and parent_asin in product_data_map:
            product = product_data_map[parent_asin]
            
            merged_entry = {**meta, **product}
            merged_data.append(merged_entry)
            
    #To Avoid issue storing to database
    merged_data = data_conversion(merged_data)
    
    class DateTimeEncoder(json.JSONEncoder):
        def default(self, obj):
            if isinstance(obj, datetime.datetime):
                return obj.isoformat() 
            return super().default(obj)

    output_file = 'dataset/train/train.json'
    with open(output_file, 'w') as file:
        json.dump(merged_data, file, indent=4, cls=DateTimeEncoder)
    print("Successfully completed data transformation")
    
    insert_data()

if __name__ == "__main__":
    transform()