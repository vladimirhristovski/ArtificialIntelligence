import os

import numpy
import numpy as np

from sklearn.preprocessing import OrdinalEncoder

os.environ['OPENBLAS_NUM_THREADS'] = '1'
from submission_script import *
# from dataset_script import dataset
from zad1_dataset import dataset
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score

# Ova e primerok od podatochnoto mnozestvo, za treniranje/evaluacija koristete ja
# importiranata promenliva dataset
dataset_sample = [['C', 'S', 'O', '1', '2', '1', '1', '2', '1', '2', '0'],
                  ['D', 'S', 'O', '1', '3', '1', '1', '2', '1', '2', '0'],
                  ['C', 'S', 'O', '1', '3', '1', '1', '2', '1', '1', '0'],
                  ['D', 'S', 'O', '1', '3', '1', '1', '2', '1', '2', '0'],
                  ['D', 'A', 'O', '1', '3', '1', '1', '2', '1', '2', '0']]

if __name__ == '__main__':
    encoder = OrdinalEncoder()
    encoder.fit([row[:-1] for row in dataset])

    test_size = 1 - (int(input()) / 100)
    criterion_input = input()

    X = [row[:-1] for row in dataset]
    Y = [row[-1] for row in dataset]

    test_X, train_X, test_Y, train_Y = train_test_split(X, Y, train_size=test_size, shuffle=False)
    train_X = encoder.transform(train_X)
    test_X = encoder.transform(test_X)

    classifier = DecisionTreeClassifier(criterion=criterion_input, random_state=0)
    classifier.fit(train_X, train_Y)

    depth = classifier.get_depth()
    leaves = classifier.get_n_leaves()
    importances = list(classifier.feature_importances_)
    leastImportant = np.argmin(classifier.feature_importances_)
    mostImportant = importances.index(max(importances))

    print(f"Depth: {depth}")
    print(f"Number of leaves: {leaves}")
    hitrate = accuracy_score(test_Y, classifier.predict(test_X))
    print(f"Accuracy: {hitrate}")
    print(f"Most important feature: {mostImportant}")
    print(f"Least important feature: {leastImportant}")

# Na kraj potrebno e da napravite submit na podatochnoto mnozestvo,
# klasifikatorot i encoderot so povik na slednite funkcii

# submit na trenirachkoto mnozestvo
submit_train_data(train_X, train_Y)

# submit na testirachkoto mnozestvo
submit_test_data(test_X, test_Y)

# submit na klasifikatorot
submit_classifier(classifier)

# submit na encoderot
submit_encoder(encoder)
