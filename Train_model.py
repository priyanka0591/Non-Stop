import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn.metrics import accuracy_score, classification_report
import joblib

def train_classification_model(data_file):
    # Read the CSV file into a DataFrame
    df = pd.read_csv(data_file, encoding='latin1')

    # Convert NaN values in 'Text' column to an empty string
    df['Text'] = df['Text'].apply(lambda x: str(x) if not pd.isnull(x) else "")

    # Split the data into training and testing sets
    train_data, test_data = train_test_split(df, test_size=0.2, random_state=42)

    # Extract features (X) and labels (y) from the training data
    X_train = train_data['Text']
    y_train = train_data['Section']

    # Extract features (X) and labels (y) from the testing data
    X_test = test_data['Text']
    y_test = test_data['Section']

    # Use TF-IDF vectorization to convert text data into numerical features
    vectorizer = TfidfVectorizer(max_features=5000)
    X_train_tfidf = vectorizer.fit_transform(X_train)
    X_test_tfidf = vectorizer.transform(X_test)

    # Train a Naive Bayes classifier
    classifier = MultinomialNB()
    classifier.fit(X_train_tfidf, y_train)

    # Save the model and vectorizer for future use
    joblib.dump(classifier, 'classifier_model.joblib')
    joblib.dump(vectorizer, 'tfidf_vectorizer.joblib')

    # Make predictions on the test set
    y_pred = classifier.predict(X_test_tfidf)

    # Print accuracy and classification report
    accuracy = accuracy_score(y_test, y_pred)
    report = classification_report(y_test, y_pred)

    print(f'Accuracy: {accuracy}')
    print('Classification Report:')
    print(report)

    # Save the evaluation report to a CSV file
    report_df = pd.DataFrame({'Actual': y_test, 'Predicted': y_pred})
    report_df.to_csv('classification_report.csv', index=False)

if __name__ == "__main__":
    data_file = 'MergeData1.csv'
    train_classification_model(data_file)