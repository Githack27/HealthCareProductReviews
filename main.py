import os
import importlib.util
import json
from DBHelpers.createdatabase import create_database
from pipelines.querying import query_reviews
from pipelines.RAG import text_summarization
from pipelines.sentiment import analyze_sentiment
from dotenv import load_dotenv

load_dotenv()
config_file = os.getenv("CONFIG_FILE")

def execute_step(file_path, function_name):
    file_name = os.path.basename(file_path)
    spec = importlib.util.spec_from_file_location(file_name, file_path)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)

    func = getattr(module, function_name, None)

    if callable(func):
        print(f"\nExecuting {function_name} from {file_name}...")
        func() 
    else:
        print(f"Error: Function {function_name} not found in {file_name}")

def load_pipeline_config(config_file):
    with open(config_file, "r") as f:
        config = json.load(f)
    return config.get("steps", [])

def run_pipeline():
    pipeline_steps = load_pipeline_config(config_file)
    create_database()
    for step in pipeline_steps:
        file_path = os.path.join("pipelines", step["file"])
        if os.path.exists(file_path):
            execute_step(file_path, step["function"])
        else:
            print(f"Warning: {file_path} does not exist!")
    
    # R-A-G (Retrieval-Augmented-Generation)
    res = query_reviews()
    summary = text_summarization(res)
    sentiment = analyze_sentiment(summary)
    print(f"\nRAG Summarization: {summary}")
    print(f"\nSentimental Analysis of summary: {sentiment}")

if __name__ == "__main__":
    run_pipeline()
