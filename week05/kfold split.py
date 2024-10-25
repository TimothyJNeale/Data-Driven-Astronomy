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

def split_galaxies_qsos(data):
    # split the data into galaxies and qsos arrays
    galaxies = data[data['spec_class'] == b'GALAXY']
    qsos = data[data['spec_class'] == b'QSO']

    return galaxies, qsos


def cross_validate_median_diff(data):
    features, targets = get_features_targets(data)
    dtr = DecisionTreeRegressor(max_depth=19)
    return np.mean(cross_validate_model(dtr, features, targets, 10))

if __name__ == "__main__":
    DATA_FILE = 'sdss_galaxy_colors.npy'
    DATA_DIRECTORY = 'week05'

    INPUT_FILE = os.path.join(DATA_DIRECTORY, DATA_FILE)

    data = np.load(INPUT_FILE)

    # Split the data set into galaxies and QSOs
    galaxies, qsos= split_galaxies_qsos(data)

    # Here we cross validate the model and get the cross-validated median difference
    # The cross_validated_med_diff function is in "written_functions"
    galaxy_med_diff = cross_validate_median_diff(galaxies)
    qso_med_diff = cross_validate_median_diff(qsos)

    # Print the results
    print("Median difference for Galaxies: {:.3f}".format(galaxy_med_diff))
    print("Median difference for QSOs: {:.3f}".format(qso_med_diff))
