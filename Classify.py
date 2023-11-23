# classify.py
from newspaper import Article
import joblib  # For model persistence

def classify_new_article(article_url):
    # Load the saved model and vectorizer
    classifier = joblib.load('classifier_model.joblib')
    vectorizer = joblib.load('tfidf_vectorizer.joblib')

    # Scrape the new article
    article = Article(article_url)
    article.download()
    article.parse()
    text = article.text

    # Vectorize the text using the trained vectorizer
    text_tfidf = vectorizer.transform([text])

    # Make predictions using the trained model
    prediction = classifier.predict(text_tfidf)[0]

    print(f'Predicted Section for the new article: {prediction}')

if __name__ == "__main__":
    new_article_url ='https://www.hindustantimes.com/lifestyle/health/winter-raises-pneumonia-risk-protect-your-lungs-with-these-lifestyle-changes-101700627889457.html'
    classify_new_article(new_article_url)
