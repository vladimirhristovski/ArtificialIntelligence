import os

import numpy as np

os.environ['OPENBLAS_NUM_THREADS'] = '1'
from submission_script import *
# from dataset_script import dataset
from zad2_dataset import dataset
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, recall_score, precision_score
from sklearn.tree import DecisionTreeClassifier

# Ova e primerok od podatochnoto mnozestvo, za treniranje/evaluacija koristete ja
# importiranata promenliva dataset
dataset_sample = [[180.0, 23.6, 25.2, 27.9, 25.4, 14.0, 'Roach'],
                  [12.2, 11.5, 12.2, 13.4, 15.6, 10.4, 'Smelt'],
                  [135.0, 20.0, 22.0, 23.5, 25.0, 15.0, 'Perch'],
                  [1600.0, 56.0, 60.0, 64.0, 15.0, 9.6, 'Pike'],
                  [120.0, 20.0, 22.0, 23.5, 26.0, 14.5, 'Perch']]

if __name__ == '__main__':
    col_index = int(input())
    num_of_trees = int(input())
    criteria_input = input()
    new_test = list(map(int, input().split()))
    new_test = new_test[:col_index] + new_test[col_index + 1:]

    X = [row[:col_index] + row[col_index + 1:-1] for row in dataset]
    Y = [row[-1] for row in dataset]

    train_X, test_X, train_Y, test_Y = train_test_split(X, Y, train_size=0.85, shuffle=False)

    # Drop the inputed column
    train_X_trimmed = [row[:col_index] + row[col_index + 1:] for row in train_X]
    test_X_trimmed = [row[:col_index] + row[col_index + 1:] for row in test_X]

    classifier = RandomForestClassifier(
        n_estimators=num_of_trees,
        criterion=criteria_input,
        random_state=0
    )

    classifier.fit(train_X, train_Y)

    pred_Y = classifier.predict([new_test])
    pred_Y_whole = classifier.predict_proba([new_test])
    pred = classifier.predict(test_X)
    base_acc = accuracy_score(test_Y, pred)

    print(f'Accuracy: {base_acc}')
    print(f'{pred_Y[0]}')
    print(f'{pred_Y_whole[0]}')
    #
    # feature_finder = DecisionTreeClassifier(
    #     criterion=criteria_input,
    #     random_state=0
    # )

    # feature_finder.fit(train_X, train_Y)
    # best_feature_index = np.argmax(feature_finder.feature_importances_)

    # x=[row[:col_index] + [row[2] + row[3]] + row[col_index+1:-1] for row in dataset]
    # print(x)

# Na kraj potrebno e da napravite submit na podatochnoto mnozestvo
# i klasifikatorot so povik na slednite funkcii

# submit na trenirachkoto mnozestvo
submit_train_data(train_X, train_Y)

# submit na testirachkoto mnozestvo
submit_test_data(test_X, test_Y)

# submit na klasifikatorot
submit_classifier(classifier)
