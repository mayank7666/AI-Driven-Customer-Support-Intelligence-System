import pickle

model = pickle.load(open("model.pkl", "rb"))
vectorizer = pickle.load(open("vectorizer.pkl", "rb"))

def classify_query(query):
    query = query.lower()
    vec = vectorizer.transform([query])
    return model.predict(vec)[0]