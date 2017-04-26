'''
This module computes the most important keywords (a keyword can be between
1-3 words) from a file and can rank these keywords in other files contents.
'''

import nltk


def get_top_keywords(tokens):
    '''
    Takes a list of tokens (keywords) and returns a list of keywords ranked
    from the most important (by occurence) to the least, with their frequency.
    Input:
        - tokens: list of tokens
    Output:
        - ranked list of tokens and their absolute frequency
    '''
    return nltk.FreqDist(tokens).most_common()

def get_keywords_rank_by_doc(keywords, tokens):
    '''
    Takes a list of keywords and a list of tokens, ranks the keywords according
    to the input tokens and outputs the keywords with their rank.
    Input:
        - keywords: list of keywords
        - tokens: list of tokens
    Output:
        - keyword_rank: list of keywords ranked from the highest occurrence to
        the lowest within a text (a list of tokens from that text)
    '''
    tokens_freq = get_top_keywords(tokens)
    keyword_rank = []
    for token, freq in tokens_freq:
        for keyword in keywords:
            if keyword == token:
                keyword_rank.append((keyword, freq / len(tokens)))
    return keyword_rank
