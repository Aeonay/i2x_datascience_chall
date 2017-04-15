#!/usr/bin/env python
'''
Main file that uses the different modules to process some given data, compute
the most important key-words (between 1 and 3 words long), choose the top n
key-words and generate a score for these words compared to some given
files (transcripts 1, 2, 3).
''' 

import sys
import argparse
import configparser
from nltk.util import ngrams

import i2xchall.clean
import i2xchall.analyze


def get_parser():
    '''Get parser for command line arguments.'''
    parser = argparse.ArgumentParser(description="i2x data science challenge.")
    parser.add_argument("-n",
                        "--top-words",
                        dest="top_n",
                        help="Top n words to use for comparaison with the transcript files.")
    return parser


def main():
    '''main function to use the different modules.'''
    parser = get_parser()
    if len(sys.argv) == 1:
        parser.print_help()
        sys.exit(1)
    args = parser.parse_args()

    config = configparser.ConfigParser()
    config.read("config.ini")
    try:
        lang = config["default"]["lang"]
        cinput_file = config["default"]["script"]
        corpus = []
        corpus.append(config["default"]["text1"])
        corpus.append(config["default"]["text2"])
        corpus.append(config["default"]["text3"])
    except ValueError as err:
        print("Error while reading the config file with error message: %s" % err)
        sys.exit(1)

    print("Cleaning data from file %s..." % cinput_file)
    clean_data_tokens = i2xchall.clean.get_clean_document(cinput_file, lang)

    # bigrams and trigrams represent keywords of 2 and 3 words-length
    bigrams = list(ngrams(clean_data_tokens, 2))
    trigrams = list(ngrams(clean_data_tokens, 3))
    # The token list is composed of the 1, 2 and 3-words tokens
    clean_data_tokens += bigrams + trigrams

    print("Analyzing %s to get the most important keywords..." % cinput_file)
    top_keywords = i2xchall.analyze.get_top_keywords(clean_data_tokens)

    # Keep only the keywords ordered and discard their freq values
    top_keywords = [w for w, f in top_keywords]

    # Now, rank these keywords among the transcript texts
    clean_transcripts = []
    for text in corpus:
        clean_transcripts.append(i2xchall.clean.get_clean_document(text, lang))

    args.top_n = int(args.top_n)
    if args.top_n <= 0 or args.top_n > len(top_keywords):
        top_n = len(top_keywords)
    else:
        top_n = args.top_n
    keyword_ranks = []
    for clean_transcript in clean_transcripts:
        keyword_ranks.append(i2xchall.analyze.get_keywords_rank_by_doc(top_keywords[:top_n], clean_transcript))

    for keyword_rank in keyword_ranks:
        print("Keyword ranking for text transcripts (1, 2 and 3):")
        for w, f in keyword_rank[:top_n]:
            print("%s : %.5f" % (w, f))
        print("-----")

if __name__ == "__main__":
    main()
