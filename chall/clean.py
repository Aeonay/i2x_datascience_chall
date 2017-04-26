'''
This module cleans a text: tokenize, lemmatize, remove stop words and other
operations in order to keep only relevant keywords.
'''

from nltk.tokenize import RegexpTokenizer
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer


def get_clean_tokens(data, lang):
    '''
    Generate the word list (token array) for a given (raw) text with the
    frequency distribution for each word.
    Input:
        - data: text to analyse
        - lang: string corresponding to the language of the document
    Output:
        - tokens: list, nltk tokens of the "cleaned-up" text document
    '''
    # Recuperate only words (TODO: word_tokenizer defaults to keep the punctuation)
    tokenizer = RegexpTokenizer(r'\W', gaps=True)
    tokens = tokenizer.tokenize(data)

    # Lemmatize data
    lemmatizer = WordNetLemmatizer()
    tokens = [lemmatizer.lemmatize(token) for token in tokens]

    # Stop words are common words (and, he, she, etc.)
    stop_words = set(stopwords.words(lang))  # add other stop words: 'ha', 'wa' ?
    # Lowercase each words and remove stop words
    tokens = [token.lower() for token in tokens]
    tokens = [token for token in tokens if token not in stop_words]

    tokens = [t for t in tokens if len(t) > 1]
    return tokens

def get_clean_document(document, lang):
    '''
    Returns an array of clean tokens by input documents. A wrapper for the
    get_clean_tokes() function.
    Input:
        - document: str path
        - lang: str for the language to use
    Output:
        - clean_output_tokens: list of tokens
    '''
    with open(document, 'r') as f:
        input_data = f.read()
    clean_output_tokens = get_clean_tokens(input_data, lang)
    return clean_output_tokens
