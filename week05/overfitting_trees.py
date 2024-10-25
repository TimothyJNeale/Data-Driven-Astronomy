import numpy as np
from matplotlib import pyplot as plt
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

def accuracy_by_treedepth(features, targets, depths):
    # split the data into training and testing features and predictions
    split = features.shape[0]//2

    train_features = features[:split]
    test_features = features[split:]

    train_targets = targets[:split]
    test_targets = targets[split:]

    # initialise arrays or lists to store the accuracies for the below loop
    train_diffs = []
    test_diffs = []
    
    # loop through depths
    for depth in depths:
        # initialize model with the maximum depth. 
        dtr = DecisionTreeRegressor(max_depth=depth)

        # train the model using the training set
        dtr.fit(train_features, train_targets)

        # get the predictions for the training set and calculate their median_diff
        train_predictions = dtr.predict(train_features)
        train_diffs.append(median_diff(train_predictions, train_targets))

        # get the predictions for the testing set and calculate their median_diff
        test_predictions = dtr.predict(test_features)
        test_diffs.append(median_diff(test_predictions, test_targets))
        
    # return the accuracies for the training and testing sets
    return train_diffs, test_diffs


DATA_FILE = 'sdss_galaxy_colors.npy'
DATA_DIRECTORY = 'week05'

INPUT_FILE = os.path.join(DATA_DIRECTORY, DATA_FILE)

data = np.load(INPUT_FILE)
features, targets = get_features_targets(data)

# Generate several depths to test
tree_depths = [i for i in range(1, 36, 2)]

# Call the function
train_med_diffs, test_med_diffs = accuracy_by_treedepth(features, targets, tree_depths)
print("Depth with lowest median difference : {}".format(tree_depths[test_med_diffs.index(min(test_med_diffs))]))

# Plot the results
train_plot = plt.plot(tree_depths, train_med_diffs, label='Training set')
test_plot = plt.plot(tree_depths, test_med_diffs, label='Validation set')
plt.xlabel("Maximum Tree Depth")
plt.ylabel("Median of Differences")
plt.legend()
plt.show()