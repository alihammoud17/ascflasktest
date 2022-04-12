from nltk.tokenize import word_tokenize
import qalsadi.lemmatizer
import re
import string
import nltk
from nltk.corpus import stopwords
import numpy
# from tashaphyne.stemming import ArabicLightStemmer

# ArListem = ArabicLightStemmer()


def Tokeniz(text):
    return (word_tokenize(text))


def EntityRecognition(text):
    lemmer = qalsadi.lemmatizer.Lemmatizer()
    lemmas = lemmer.lemmatize_text(text, return_pos=True)
    return lemmas


def preprocess(text):
    '''
    text is an arabic string input

    the preprocessed text is returned
    '''

    punctuations = '''`÷×؛<>_()*&^%][ـ،/:"؟.,'{}~¦+|!”…“–ـ''' + \
        string.punctuation
    nltk.download('stopwords')
    # Arabic stop words with nltk
    stop_words = stopwords.words()

    arabic_diacritics = re.compile("""
                                ّ    | # Shadda
                                َ    | # Fatha
                                ً    | # Tanwin Fath
                                ُ    | # Damma
                                ٌ    | # Tanwin Damm
                                ِ    | # Kasra
                                ٍ    | # Tanwin Kasr
                                ْ    | # Sukun
                                ـ     # Tatwil/Kashida
                            """, re.VERBOSE)

    # remove punctuations
    translator = str.maketrans('', '', punctuations)
    text = text.translate(translator)

    # remove Tashkeel
    text = re.sub(arabic_diacritics, '', text)

    # remove longation
    text = re.sub("[إأآا]", "ا", text)
    text = re.sub("ى", "ي", text)
    text = re.sub("ؤ", "ء", text)
    text = re.sub("ئ", "ء", text)
    text = re.sub("ة", "ه", text)
    text = re.sub("گ", "ك", text)

    text = ' '.join(word for word in text.split() if word not in stop_words)

    return text
