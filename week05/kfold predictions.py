import numpy as np
from matplotlib import pyplot as plt
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



def cross_validate_predictions(model, features, targets, k):
    kf = KFold(n_splits=k, shuffle=True)

    # declare an array for predicted redshifts from each iteration
    all_predictions = np.zeros_like(targets)

    for train_indices, test_indices in kf.split(features):
        # split the data into training and testing
        train_features, test_features = features[train_indices], features[test_indices]
        train_targets, test_targets = targets[train_indices], targets[test_indices]

        # fit the model for the current set
        model.fit(train_features, train_targets)

        # predict using the model
        predictions = model.predict(test_features)

        # put the predicted values in the all_predictions array defined above
        all_predictions[test_indices] = predictions

    # return the list with your median difference values
    return all_predictions

DATA_FILE = 'sdss_galaxy_colors.npy'
DATA_DIRECTORY = 'week05'

INPUT_FILE = os.path.join(DATA_DIRECTORY, DATA_FILE)

data = np.load(INPUT_FILE)
features, targets = get_features_targets(data)

# initialize model with a maximum depth of 19
dtr = DecisionTreeRegressor(max_depth=19)

# call your cross validation function
predictions = cross_validate_predictions(dtr, features, targets, 10)

# calculate and print the rmsd as a sanity check
diffs = median_diff(predictions, targets)
print('Median difference: {:.3f}'.format(diffs))

# plot the results to see how well our model looks
plt.scatter(targets, predictions, s=0.4)
plt.xlim((0, targets.max()))
plt.ylim((0, predictions.max()))
plt.xlabel('Measured Redshift')
plt.ylabel('Predicted Redshift')
plt.show()