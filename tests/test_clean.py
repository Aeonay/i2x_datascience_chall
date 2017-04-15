'''Test file for clean.py module'''

import i2xchall.clean
import unittest

class TestClean(unittest.TestCase):

    def test_get_clean_tokens(self):
        '''
        get_clean_tokens should take a raw text and tokenize by words,
        lemmatize, lower case every token, remove stop words and remove words
        of length less than 1
        '''
        data = "Take me down 2 to the Paradise City - will you ? - where the grass is green, (etc.)"
        lang = "english"
        expected_result = ['take', 'paradise', 'city', 'grass', 'green', 'etc']
        result = i2xchall.clean.get_clean_tokens(data, lang)
        self.assertEqual(expected_result, result)

#    def test_get_clean_document(self):
#
#        result = get_clean_document(document, lang)

if __name__ == "__name__":
    unittest.main()
