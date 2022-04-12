import pickle
from tokenizer import preprocess

MODEL_PATH = "model.pkl"

class _Sentiment_Analysis_Service:
    model = None
    _instance = None

    def predict(self, text):
        # preprocess text
        preprocessedText = preprocess(text)

        # Predict Sentiment
        predictedSentiment = self.model.predict([preprocessedText])
        return predictedSentiment

# factory function
def Sentiment_Analysis_Service():
    # One instance ensuring
    if _Sentiment_Analysis_Service._instance is None:
        _Sentiment_Analysis_Service._instance = _Sentiment_Analysis_Service()
        _Sentiment_Analysis_Service.model = pickle.load(open("model.pkl", "rb"))
    return _Sentiment_Analysis_Service._instance