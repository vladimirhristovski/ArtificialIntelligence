import os

os.environ['OPENBLAS_NUM_THREADS'] = '1'
from submission_script import *
# from dataset_script import dataset
from zad1_dataset import dataset
from sklearn.naive_bayes import CategoricalNB
from sklearn.preprocessing import OrdinalEncoder

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

    train_set = dataset[:int(0.75 * len(dataset))]
    test_set = dataset[int(0.75 * len(dataset)):]

    train_x = [row[:-1] for row in train_set]
    train_y = [row[-1] for row in train_set]

    test_x = [row[:-1] for row in test_set]
    test_y = [row[-1] for row in test_set]

    train_X = encoder.transform(train_x)
    test_X = encoder.transform(test_x)

    train_Y = train_y
    test_Y = test_y

    classifier = CategoricalNB()
    classifier.fit(train_X, train_Y)

    predicted_class = classifier.predict([test_X[0]])[0]
    true_class = test_Y[0]

    accuracy = 0

    for i in range(len(test_set)):
        predicted_class = classifier.predict([test_X[i]])[0]
        true_class = test_Y[i]
        if predicted_class == true_class:
            accuracy += 1

    accuracy_percentage = accuracy / len(test_set)

    print(accuracy_percentage)

    entry = [el for el in input().split()]

    encoded_entry = encoder.transform([entry])

    predicted_class_entry = classifier.predict(encoded_entry)[0]

    print(predicted_class_entry)

    probabilities_entry = classifier.predict_proba(encoded_entry)

    print(probabilities_entry)

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
