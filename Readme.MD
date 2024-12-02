# **Data Preprocessing and Retrieval System**

This project processes and integrates datasets with both structured and unstructured data, stores the results in a database, and enables a retrieval system based on embeddings. The system incorporates Retrieval-Augmented Generation (RAG) to summarize results in response to user prompts.

The user will enter the review of the product they brought and store they brought the product is also added along with the review. Here it is a random choice from DB. With the store name and review, the system, will retireve similar comments, if any matches. With this, the Agent company can filter out the stores with the type of review retrieved from the user and helps in improve their in business model.

---

## **Table of Contents**
1. [Project Overview](#project-overview)
2. [Features](#features)
3. [Technologies Used](#technologies-used)
4. [Future Enhancements](#future-enhancements)

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

--

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

download dataset from the following drive link (file is too large)
- https://drive.google.com/file/d/1HPBEztv_COZOw1TB8ili6v6Dvg_rG-Ag/view?usp=sharing

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
