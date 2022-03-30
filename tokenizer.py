from nltk.tokenize import word_tokenize
import qalsadi.lemmatizer
# from tashaphyne.stemming import ArabicLightStemmer

# ArListem = ArabicLightStemmer()


def Tokeniz(text):
    return (word_tokenize(text))


def EntityRecognition(text):
    lemmer = qalsadi.lemmatizer.Lemmatizer()
    lemmas = lemmer.lemmatize_text(text, return_pos=True)
    return lemmas
