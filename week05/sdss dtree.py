import numpy as np
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

# write a function that splits the data into training and testing subsets
# trains the model and returns the prediction accuracy with median_diff
def validate_model(model, features, targets):
    # split the data into training and testing features and predictions
    split = features.shape[0]//2

    train_features = features[:split]
    test_features = features[split:]

    train_targets = targets[:split]
    test_targets = targets[split:]

    # train the model
    model.fit(train_features, train_targets)

    # get the predicted_redshifts
    predicted_redshifts = model.predict(test_features)
  
     # use median_diff function to calculate the accuracy
    return median_diff(test_targets, predicted_redshifts)


DATA_FILE = 'sdss_galaxy_colors.npy'
DATA_DIRECTORY = 'week05'

INPUT_FILE = os.path.join(DATA_DIRECTORY, DATA_FILE)

data = np.load(INPUT_FILE)
print(data[0])
print(data['u'])
print(len(data['u']))

features, targets = get_features_targets(data)

print(features[:2])
print(targets[:2])

# initialize model
dtr = DecisionTreeRegressor()

# train the model
dtr.fit(features, targets)

# make predictions using the same features
predictions = dtr.predict(features)

# print out the first 4 predicted redshifts
print(predictions[:4])