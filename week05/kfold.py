import numpy as np
from sklearn.model_selection import KFold
from sklearn.tree import DecisionTreeRegressor
import os


def get_features_targets(data):
    # targets is the last coulmn of the data
    targets = data['redshift']

    # The four features are the colourindexes calculated by u - g, g - r, r - i and i - z.
    features = np.zeros((data.shape[0], 4))
    features[:, 0] = data['u'] - data['g']
    features[:, 1] = data['g'] - data['r']
    features[:, 2] = data['r'] - data['i']
    features[:, 3] = data['i'] - data['z']

    return features, targets

# write a function that calculates the median of the differences
# between our predicted and actual values
def median_diff(predicted, actual):
    return np.median(np.abs(predicted - actual))



def cross_validate_model(model, features, targets, k):
    kf = KFold(n_splits=k, shuffle=True)

    # initialise a list to collect median_diffs for each iteration of the loop below
    median_diffs = []

    for train_indices, test_indices in kf.split(features):
        train_features, test_features = features[train_indices], features[test_indices]
        train_targets, test_targets = targets[train_indices], targets[test_indices]

        # fit the model for the current set
        model.fit(train_features, train_targets)

        # predict using the model
        predictions = model.predict(test_features)

        # calculate the median_diff from predicted values and append to results array
        median_diffs.append(median_diff(predictions, test_targets))

    # return the list with your median difference values
    return median_diffs


DATA_FILE = 'sdss_galaxy_colors.npy'
DATA_DIRECTORY = 'week05'

INPUT_FILE = os.path.join(DATA_DIRECTORY, DATA_FILE)

data = np.load(INPUT_FILE)
features, targets = get_features_targets(data)

# initialize model with a maximum depth of 19
dtr = DecisionTreeRegressor(max_depth=19)

# call your cross validation function
diffs = cross_validate_model(dtr, features, targets, 10)

# Print the values
print('Differences: {}'.format(', '.join(['{:.3f}'.format(val) for val in diffs])))
print('Mean difference: {:.3f}'.format(np.mean(diffs)))