# News Classification 

This repository contains a Python application for scraping news articles, training a text classification model, and evaluating its performance using machine learning techniques.

## Overview

The project consists of three main Python scripts:
- Scrape.py: Scrapes news articles from specified URLs and saves the data to a CSV file.
- Train_model.py: Trains a text classification model using a Naive Bayes classifier based on the scraped news data.
- Classify.py: Uses the trained model to classify new articles provided via URL.

## Installation

### Prerequisites
- Python (3.x recommended)
- pip (Python package installer)

### Steps
1. Clone the repository:
   
   ```git clone https://github.com/your-username/your-repository.git```
2. Navigate to the project directory:
```cd your-repository```
3. Install the required Python packages:
```pip install -r requirements.txt```
### Usage

Scraping News Articles
To scrape news articles from a website and save them to a CSV file:

```python Scrape.py```

### Training the Model
To train the text classification model using the scraped data:

```python Train_model.py```

### Running the Classification
To classify a new article provided via URL:

```python Classify.py```

### Results

The accuracy, classification report, and predictions for the test set are displayed in the console. The classification report is saved to a CSV file named classification_report.csv.

Screenshots

Output of Train_model.py: The accuracy achieved is 75%.
Train Model Output

<img width="515" alt="image" src="https://github.com/priyanka0591/Non-Stop/assets/92290843/3300d11a-861a-4912-9e43-2d06fb17d238">

Output of Classify.py: Predicted section for a sample article is shown.
Classify Output
<img width="683" alt="image" src="https://github.com/priyanka0591/Non-Stop/assets/92290843/8ead1c61-5c91-4975-a3f4-da1b0cc84965">
