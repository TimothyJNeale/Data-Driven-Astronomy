import numpy as np
from sklearn.tree import DecisionTreeClassifier
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

def dtc_predict_actual(data):
    # split the data into training and testing sets using a training fraction of 0.7
    fraction_training = 0.7
    training, testing = splitdata_train_test(data, fraction_training)

    # generate the feature and targets for the training and test sets
    # i.e. train_features, train_targets, test_features, test_targets
    train_features, train_targets = generate_features_targets(training)
    test_features, test_targets = generate_features_targets(testing)

    # instantiate a decision tree classifier
    dtc = DecisionTreeClassifier()

    # train the classifier with the train_features and train_targets
    dtc.fit(train_features, train_targets)

    # get predictions for the test_features
    predictions = dtc.predict(test_features)

    # return the predictions and the test_targets
    return predictions, test_targets

if __name__ == "__main__":
    DATA_FILE = 'galaxy_catalogue.npy'
    DATA_DIRECTORY = 'week06'

    INPUT_FILE = os.path.join(DATA_DIRECTORY, DATA_FILE)

    data = np.load(INPUT_FILE)

    # # set the fraction of data which should be in the training set
    # fraction_training = 0.7

    # # split the data using your function
    # training, testing = splitdata_train_test(data, fraction_training)

    # # print the key values
    # print('Number data galaxies:', len(data))
    # print('Train fraction:', fraction_training)
    # print('Number of galaxies in training set:', len(training))
    # print('Number of galaxies in testing set:', len(testing))

    # features, targets = generate_features_targets(data)

    # # Print the shape of each array to check the arrays are the correct dimensions. 
    # print("Features shape:", features.shape)
    # print("Targets shape:", targets.shape)

    predicted_class, actual_class = dtc_predict_actual(data)

    # Print some of the initial results
    print("Some initial results...\n   predicted,  actual")
    for i in range(10):
        print("{}. {}, {}".format(i, predicted_class[i], actual_class[i]))