# **Data Preprocessing and Retrieval System**

This project processes and integrates datasets with both structured and unstructured data, stores the results in a database, and enables a retrieval system based on embeddings. The system incorporates Retrieval-Augmented Generation (RAG) to summarize results in response to user prompts.

The user will enter the review of the product they brought and store they brought the product is also added along with the review. Here it is a random choice from DB. With the store name and review, the system, will retireve similar comments, if any matches. With this, the Agent company can filter out the stores with the type of review retrieved from the user and helps in improve their in business model.

---

## **Table of Contents**
1. [Project Overview](#project-overview)
2. [Features](#features)
3. [Project Structure](#project-structure)
4. [Technologies Used](#technologies-used)
5. [Future Enhancements](#future-enhancements)

---

## **Project Overview**

This project performs the following key tasks:
1. Preprocess datasets by:
   - Cleaning text in unstructured data.
   - Converting epoch timestamps to human-readable formats.
2. Transform the datasets for efficient storage and retrieval.
3. Store the transformed data into a database.
4. Generate embeddings for unstructured data fields for similarity-based retrieval.
5. Use RAG (Retrieval-Augmented Generation) to generate short summaries for user prompts and retrieved data.

---

## **Features**

- **Data Preprocessing:** Automated cleaning, timestamp conversion, and merging of datasets.
- **Embeddings:** Create embeddings for unstructured data to enable similarity-based search.
- **Database Storage:** Save processed data and embeddings in a database for efficient querying.
- **RAG Implementation:** Generate concise summaries for retrieved results based on user prompts.

---

## **Project Structure**
data-retrieval-system/
│
├── data/                    # Raw and processed data files
│   ├── raw/                 # Raw datasets (structured & unstructured)
│   ├── processed/           # Processed and merged dataset files
│
├── embeddings/              # Generated embeddings for unstructured data
│   ├── vectors/             # Stored embeddings in vectorized form
│
├── database/                # Database initialization and schema
│   ├── schema.sql           # SQL scripts for creating tables
│   ├── db_operations.py     # Scripts for database CRUD operations
│
├── scripts/                 # Core processing and retrieval scripts
│   ├── preprocess.py        # Preprocessing pipeline
│   ├── embed_data.py        # Embedding generation for unstructured data
│   ├── retrieval_service.py # Embedding-based search and RAG summarization
│
├── config/                  # Configuration files
│   ├── config.json          # Database and general project configurations
│
├── models/                  # ML models and embedding-related scripts
│   ├── embedding_model.py   # Embedding model integration (e.g., OpenAI or Sentence Transformers)
│   ├── rag_model.py         # RAG summarization model integration
│
├── utils/                   # Utility scripts
│   ├── text_cleaning.py     # Functions for cleaning unstructured data
│   ├── timestamp_utils.py   # Functions for timestamp conversion
│
├── tests/                   # Unit and integration tests
│   ├── test_preprocess.py   # Test cases for preprocessing
│   ├── test_embeddings.py   # Test cases for embeddings and retrieval
│
├── requirements.txt         # Python dependencies
├── README.md                # Project documentation
└── .gitignore               # Ignored files and directories

## **Technologies Used**

- **Programming Language:** Python
- **Database:** MongoDB
- **Libraries:**
  - **Pandas:** For data preprocessing
  - **SentenceTransformers/OpenAI API:** For generating embeddings
  - **RAG (nltk or LangChain integration):** For summarization and retrieval-augmented generation

---

## **Future Enhancements**

- Add support for streaming large datasets
- Implement advanced similarity algorithms (e.g., ANN)
- Extend RAG to include contextual chat capabilities
- Integrate a user-friendly frontend for managing and querying data

Follow these steps to set up and run the project.

### Prerequisites

Make sure you have the following installed:
- Python 3.8 or higher
- `pip` (Python package manager)

### Installation

1. **Clone the Repository**
   ```bash
   git clone https://github.com/your-username/your-repository.git
   cd your-repository

2. **Install Packages**
   ```bash
   pip install requirements.txt

3. **Run API**
   ```bash
   cd Api
   uvicorn api:app --reload

4. **Run the main**
   ```bash
   python -X dev main.py