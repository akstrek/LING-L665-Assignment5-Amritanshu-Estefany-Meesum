# -*- coding: utf-8 -*-
"""sklearn_assnt5

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/16-vbDDXzxcnFHXJg3xB7KGK4DCyVOKtQ
"""

import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.model_selection import train_test_split, GridSearchCV
from sklearn.pipeline import Pipeline
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score
from sklearn.svm import LinearSVC

#data = pd.read_csv('waseemDataSet.csv')

#data.head()

#data[['tweet', 'labels']] = data['Mixed'].str.rsplit(' ', 1, expand=True)

#data.head()

#data = data.drop('Mixed', axis=1)
#data.head()

#train, test_data = train_test_split(data, test_size=0.2, random_state=1, stratify=data["labels"])

#print("Train set:")
#print(train.value_counts(normalize=True))
#print("Test set:")
#print(test_data.value_counts(normalize=True))

#train.to_csv("train.csv", index=False)
#test_data.to_csv("test.csv", index=False)

# Load the dataset
train = pd.read_csv("train.csv")

test = pd.read_csv("test.csv")

# Load the hate speech lexicon
lexicon = pd.read_csv("hate_lexicon_wiegand.csv")

# Load the hate speech lexicon
ngram_range = (1, 3) # use 1-3 word n-grams or character n-grams

# Create a pipeline for feature extraction and classification
pipeline = Pipeline([
    ('vectorizer', CountVectorizer(ngram_range=ngram_range)),
    ('classifier', LinearSVC())
])

# Define the parameter grid to search over
param_grid = {
    'vectorizer__min_df': [1, 2, 3],
    'classifier__C': [0.01, 0.1, 1, 10]
}

# Use GridSearchCV to perform a non-exhaustive parameter search
grid_search = GridSearchCV(pipeline, param_grid=param_grid, cv=5, verbose=1, n_jobs=-1)
grid_search.fit(train['tweet'], train['labels'])

# Print the best parameter settings and score
print("Best parameter settings: ", grid_search.best_params_)
print("Training accuracy: ", grid_search.best_score_)

# Evaluate the classifier on the test set
test_pred = grid_search.predict(test['tweet'])
print('Classification report for test set:')
print(classification_report(test['labels'], test_pred))
