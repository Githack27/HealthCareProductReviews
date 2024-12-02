import json
import nltk
import networkx as nx
from nltk.tokenize import sent_tokenize, word_tokenize
from nltk.corpus import stopwords
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import numpy as np

def retrieve_feedback_data(response):
    feedback_texts = []
    
    try:
        response = json.loads(response)  
    except json.JSONDecodeError as e:
        return "Invalid JSON input."

    for key, value in response.items():
        if isinstance(value, list): 
            for record in value:
                if isinstance(record, dict):  
                    feedback_text = record.get("text")
                    if feedback_text:  
                        feedback_texts.append(feedback_text)

    joined_feedback = "\n".join(feedback_texts) if feedback_texts else "No feedback available."
    return joined_feedback

def text_summarization(text):
    
    text = retrieve_feedback_data(text)
    sentences = sent_tokenize(text)

    stop_words = set(stopwords.words('english'))
    clean_sentences = [
        ' '.join([word for word in word_tokenize(sentence.lower()) if word.isalnum() and word not in stop_words])
        for sentence in sentences
    ]
    
    vectorizer = TfidfVectorizer()
    tfidf_matrix = vectorizer.fit_transform(clean_sentences)
    
    similarity_matrix = cosine_similarity(tfidf_matrix, tfidf_matrix)
    
    graph = nx.from_numpy_array(similarity_matrix)
    
    scores = nx.pagerank(graph)
    
    ranked_sentences = sorted(((scores[i], sentence) for i, sentence in enumerate(sentences)), reverse=True)
    
    summary = ' '.join([ranked_sentences[i][1] for i in range(len(ranked_sentences))])
    
    return summary

