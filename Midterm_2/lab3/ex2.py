import os

os.environ['OPENBLAS_NUM_THREADS'] = '1'
from submission_script import *
# from dataset_script import dataset
from zad2_dataset import dataset
from sklearn.naive_bayes import GaussianNB

# Ova e primerok od podatochnoto mnozestvo, za treniranje/evaluacija koristete ja
# importiranata promenliva dataset
dataset_sample = [['1', '35', '12', '5', '1', '100', '0'],
                  ['1', '29', '7', '5', '1', '96', '1'],
                  ['1', '50', '8', '1', '3', '132', '0'],
                  ['1', '32', '11.75', '7', '3', '750', '0'],
                  ['1', '67', '9.25', '1', '1', '42', '0']]

if __name__ == '__main__':
    dataset_updated = []
    for row in dataset:
        row_updated = [float(el) for el in row]
        dataset_updated.append(row_updated)

    train_set = dataset_updated[:int(0.85 * len(dataset_updated))]
    test_set = dataset_updated[int(0.85 * len(dataset_updated)):]

    train_x = [row[:-1] for row in train_set]
    train_y = [row[-1] for row in train_set]

    test_x = [row[:-1] for row in test_set]
    test_y = [row[-1] for row in test_set]

    train_X = train_x
    test_X = test_x

    train_Y = train_y
    test_Y = test_y

    classifier = GaussianNB()
    classifier.fit(train_X, train_Y)

    accuracy = 0

    for i in range(len(test_set)):
        predicted_class = classifier.predict([test_X[i]])[0]
        true_class = test_Y[i]
        if predicted_class == true_class:
            accuracy += 1

    accuracy_percentage = accuracy / len(test_set)

    print(accuracy_percentage)

    entry = [el for el in map(float, input().split())]

    predicted_class_entry = classifier.predict([entry])[0]

    print(int(predicted_class_entry))

    probabilities_entry = classifier.predict_proba([entry])

    print(probabilities_entry)

# Na kraj potrebno e da napravite submit na podatochnoto mnozestvo,
# klasifikatorot i encoderot so povik na slednite funkcii

# submit na trenirachkoto mnozestvo
submit_train_data(train_X, train_Y)

# submit na testirachkoto mnozestvo
submit_test_data(test_X, test_Y)

# submit na klasifikatorot
submit_classifier(classifier)

# povtoren import na kraj / ne ja otstranuvajte ovaa linija
