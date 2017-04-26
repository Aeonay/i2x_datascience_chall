'''Test file for analyze.py module'''

import chall.analyze
import unittest

class TestAnalyze(unittest.TestCase):

    def test_get_top_keywords(self):
        '''
        get_top_keywords should accept a list of nltk tokens and return the 
        keywords and their frequency distribution ranked from most frequent to
        least.
        '''
        tokens = ['green', 'paradise', 'city', 'city', 'city', 'grass', 'grass', 'green', 'green', 'city']
        expected_result = [('city', 4), ('green', 3), ('grass', 2), ('paradise', 1)]
        result = chall.analyze.get_top_keywords(tokens)
        self.assertEqual(expected_result, result)

    def test_get_keywords_rank_by_doc(self):
        '''
        get_keywords_rank_by_doc should accept a list of keywords and a list of
        nltk tokens and return a list of keywords and their relative frequency
        among the given list of tokens.
        '''
        keywords = ['green', 'paradise', 'grass', 'cat']
        tokens = ['take', 'green', 'paradise', 'city', 'grass', 'green', 'paradise', 'green']
        len_tokens = len(tokens)
        expected_result = [('green', 3 / len_tokens), ('paradise', 2 / len_tokens), ('grass', 1 / len_tokens)]
        result = chall.analyze.get_keywords_rank_by_doc(keywords, tokens)
        self.assertEqual(expected_result, result)

#if __name__ == "__name__":
#    unittest.main()
