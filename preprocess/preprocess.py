#!/usr/bin/env python
#coding: utf8 

from nltk.tokenize import RegexpTokenizer
from nltk.stem import WordNetLemmatizer
import cld2full
from bs4 import BeautifulSoup
import re

en_stop = [
"!!", "?!", "??", "!?", "`", "``", "''", "-lrb-", "-rrb-", "-lsb-", "-rsb-", ",", ".", ":", ";", "\"", "'",
"?", "<", ">", "{", "}", "[", "]", "+", "-", "(", ")", "&", "%", "$", "@", "!", "^", "#", "*", "..", "...", "'ll", "'s",
"'m", "a", "about", "above", "after", "again", "against", "all", "am", "an", "and", "any", "are", "aren't", "as", "at",
"be", "because", "been", "before", "being", "below", "between", "both", "but", "by", "can", "can't", "cannot", "could",
"couldn't", "did", "didn't", "do", "does", "doesn't", "doing", "don't", "down", "during", "each", "few", "for", "from",
"further", "had", "hadn't", "has", "hasn't", "have", "haven't", "having", "he", "he'd", "he'll", "he's", "her", "here",
"here's", "hers", "herself", "him", "himself", "his", "how", "how's", "i", "i'd", "i'll", "i'm", "i've", "if", "in",
"into", "is", "isn't", "it", "it's", "its", "itself", "let's", "me", "more", "most", "mustn't", "my", "myself", "no",
"nor", "not", "of", "off", "on", "once", "only", "or", "other", "ought", "our", "ours ", "ourselves", "out", "over",
"own", "same", "shan't", "she", "she'd", "she'll", "she's", "should", "shouldn't", "so", "some", "such", "than",
"that", "that's", "the", "their", "theirs", "them", "themselves", "then", "there", "there's", "these", "they",
"they'd", "they'll", "they're", "they've", "this", "those", "through", "to", "too", "under", "until", "up", "very",
"was", "wasn't", "we", "we'd", "we'll", "we're", "we've", "were", "weren't", "what", "what's", "when", "when's",
"where", "where's", "which", "while", "who", "who's", "whom", "why", "why's", "with", "won't", "would", "wouldn't",
"you", "you'd", "you'll", "you're", "you've", "your", "yours", "yourself", "yourselves", "###", "return", "arent",
"cant", "couldnt", "didnt", "doesnt", "dont", "hadnt", "hasnt", "havent", "hes", "heres", "hows", "im", "isnt",
"its", "lets", "mustnt", "shant", "shes", "shouldnt", "thats", "theres", "theyll", "theyre", "theyve", "wasnt",
"were", "werent", "whats", "whens", "wheres", "whos", "whys", "wont", "wouldnt", "youd", "youll", "youre", "youve", 
"&amp", "amp;", "&amp;", "&gt", "gt;", "&gt;"
]

def open_without_final_line(path_to_file, method = "plaintext"):
    content = []
    if (method == "plaintext"):
        with open(path_to_file, "r") as f:
            for item in f:
                content.append(item[:-1])
    elif (method == "pickle"):
        import pickle
        with open(path_to_file, "rb") as f:
            content = pickle.load(f)    
    return content

def to_lower(text):
    # just to remind
    return text.lower()

def remove_stop_words(text):
    tokenizer = RegexpTokenizer(r"\w+")
    tokens = tokenizer.tokenize(text)
    stopped_tokens = tokens
      # you can add any further code here
    stopped_tokens = [i for i in stopped_tokens if not i in en_stop]
    t = ' '.join(stopped_tokens)
    return t

def lemmatize(text):
    tokenizer = RegexpTokenizer(r"\w+")
    lemmatizer = WordNetLemmatizer()
    tokens = tokenizer.tokenize(text)
    tokens = [lemmatizer.lemmatize(i, "v") for i in tokens]
    t = ' '.join(tokens)
    return t

def judge_language(text, lang):
    detector = cld2full.detect
    isReliable, textBytesFound, details = detector(line, isPlainText=True)
    detectedLangName = ""
    detectedLangeCode = ""
    if(len(details) > 0):
           detectedLangName, detectedLangeCode = details[0][:2]
    if (detectedLangName == lang):
        return True
    else:
        return False

def remove_html_tag(text):
    soup = BeautifulSoup(text)
    t = soup.get_text()
    return t

def remove_url(text):
    t = text
    t = re.sub(r'https?:\/\/[\S]*', ' ', t)
    return t

def remove_unicode(text):
    t = text
    t = unidecode(unicode(t, encoding = "utf-8"))
    t = "".join([i if ord(i) < 128 else ' ' for i in t])
    return t

def remove_redundant_whitespace(text):
    t = test.split()
    t = ' '.join(t)
    return t