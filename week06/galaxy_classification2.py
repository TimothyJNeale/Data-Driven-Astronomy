import numpy as np
from matplotlib import pyplot as plt
from sklearn.metrics import confusion_matrix
from sklearn.model_selection import cross_val_predict
from sklearn.tree import DecisionTreeClassifier

import itertools
import os

def splitdata_train_test(data, fraction_training):
    # SPlit the data data into two sets, one for training and one for testing
    np.random.seed(0)
    np.random.shuffle(data)
    split = int(len(data) * fraction_training)

    return data[:split], data[split:]
  
def generate_features_targets(data):
    # complete the function by calculating the concentrations

    targets = data['class']

    features = np.empty(shape=(len(data), 13))
    features[:, 0] = data['u-g']
    features[:, 1] = data['g-r']
    features[:, 2] = data['r-i']
    features[:, 3] = data['i-z']
    features[:, 4] = data['ecc']
    features[:, 5] = data['m4_u']
    features[:, 6] = data['m4_g']
    features[:, 7] = data['m4_r']
    features[:, 8] = data['m4_i']
    features[:, 9] = data['m4_z']

    # fill the remaining 3 columns with concentrations in the u, r and z filters
    # concentration in u filter
    features[:, 10] = data['petroR50_u'] / data['petroR90_u']
    # concentration in r filter
    features[:, 11] = data['petroR50_r'] / data['petroR90_r']
    # concentration in z filter
    features[:, 12] = data['petroR50_z'] / data['petroR90_z']

    return features, targets

def plot_confusion_matrix(cm, classes,
                          normalize=False,
                          title='Confusion matrix',
                          cmap=plt.cm.Blues):
    """
    This function prints and plots the confusion matrix.
    Normalization can be applied by setting `normalize=True`.
    """
    plt.imshow(cm, interpolation='nearest', cmap=cmap)
    plt.title(title)
    plt.colorbar()
    tick_marks = np.arange(len(classes))
    plt.xticks(tick_marks, classes, rotation=45)
    plt.yticks(tick_marks, classes)

    if normalize:
        cm = cm.astype('float') / cm.sum(axis=1)[:, np.newaxis]
        print("Normalized confusion matrix")
    else:
        print('Confusion matrix, without normalization')

    print(cm)

    thresh = cm.max() / 2.
    for i, j in itertools.product(range(cm.shape[0]), range(cm.shape[1])):
        plt.text(j, i, "{}".format(cm[i, j]),
                 horizontalalignment="center",
                 color="white" if cm[i, j] > thresh else "black")

    plt.tight_layout()
    plt.ylabel('True Class')
    plt.xlabel('Predicted Class')

    return


def calculate_accuracy(predicted, actual):
    # calculate the number of correctly predicted classes and return the accuracy
    correct = sum(predicted == actual)
    total = len(actual)
    
    return correct / total


if __name__ == "__main__":
    DATA_FILE = 'galaxy_catalogue.npy'
    DATA_DIRECTORY = 'week06'

    INPUT_FILE = os.path.join(DATA_DIRECTORY, DATA_FILE)

    data = np.load(INPUT_FILE)

    # split the data
    features, targets = generate_features_targets(data)

    # train the model to get predicted and actual classes
    dtc = DecisionTreeClassifier()
    predicted = cross_val_predict(dtc, features, targets, cv=10)

    # calculate the model score using your function
    # print(predicted)
    # print(targets)
    model_score = calculate_accuracy(predicted, targets)
    print("Our accuracy score:", model_score)

    # calculate the models confusion matrix using sklearns confusion_matrix function
    class_labels = list(set(targets))
    model_cm = confusion_matrix(y_true=targets, y_pred=predicted, labels=class_labels)

    # Plot the confusion matrix using the provided functions.
    plt.figure()
    plot_confusion_matrix(model_cm, classes=class_labels, normalize=False)
    plt.show()
