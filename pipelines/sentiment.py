from textblob import TextBlob

def analyze_sentiment(paragraph):
    blob = TextBlob(paragraph)
    
    sentiment = blob.sentiment
    polarity = sentiment.polarity 
    subjectivity = sentiment.subjectivity

    if polarity > 0:
        overall_sentiment = "Positive"
    elif polarity < 0:
        overall_sentiment = "Negative"
    else:
        overall_sentiment = "Neutral"

    return overall_sentiment
