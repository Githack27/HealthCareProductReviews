import re
def cleanText(text):
    text.strip()
    text = re.sub(r'[^\w\s,.\-:;?!"\'()&$%#@+=*<>]', '', text)
    text = re.sub(r'\s+', ' ', text)
    return text