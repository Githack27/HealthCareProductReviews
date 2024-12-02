import os
import json
from Utilities.epochToTimeStamp import convert_epoch_to_datetime
from Utilities.cleanSentences import cleanText
from dotenv import load_dotenv

load_dotenv()
folder_path = os.getenv("DATASET_PATH")

def clean_json_data(data):
    if isinstance(data, dict):
        cleaned_dict = {}
        for key, value in data.items():
            if 'timestamp' in key.lower():
                cleaned_dict[key] = convert_epoch_to_datetime(value)
            else:
                cleaned_dict[key] = clean_json_data(value)
        
        return {key: value for key, value in cleaned_dict.items() if value not in [None, "", [], {}]}
    
    elif isinstance(data, list):
        return [clean_json_data(item) for item in data if item not in [None, "", [], {}]]
    
    elif isinstance(data, str):
        data = cleanText(data)
        return data
    
    else:
        return data

def process_json_files():
    for filename in os.listdir(folder_path):
        if filename.endswith(".json"):
            file_path = os.path.join(folder_path, filename)
            
            try:
                with open(file_path, 'r', encoding='utf-8') as file:
                    data = json.load(file)
                
                cleaned_data = clean_json_data(data)
                
                with open(file_path, 'w', encoding='utf-8') as file:
                    json.dump(cleaned_data, file, indent=4)
                
                print(f"Processed: {filename}")
            except Exception as e:
                print(f"Error processing {filename}: {e}")

if __name__ == "__main__":
    process_json_files()
