import numpy as np
import pandas as pd

def LoadDataAirfoil(filename, delim = "\t"):
    cols = ['Frequency', 'AngleOfAttack', 'ChordLength', 'FreeStreamVelocity', 'SuctionSideDisplacementThickness', 'ScaledSoundPressureLevel']
    df = pd.read_csv(filename, delimiter=delim, names = cols)
    print(df.head())
    df.columns = ['Frequency', 'AngleOfAttack', 'ChordLength', 'FreeStreamVelocity', 'SuctionSideDisplacementThickness', 'ScaledSoundPressureLevel']
    features = cols[:len(cols)-1] #df.columns [:len(df.columns) - 1]

    y_label = ['ScaledSoundPressureLevel']
    x_df = df[features]
    y_df = df[y_label]
    #print (x_df.head(2))
    x_df = (x_df - x_df.mean()) / x_df.std()
    print (x_df.head(3))
    print(y_df.head(3))

    x_data_set = np.array(pd.DataFrame(x_df, columns=features))
    y_data_set = np.array(pd.DataFrame(y_df, columns=y_label))

    return x_data_set, y_data_set
'''
    x_data_train, x_data_test, y_data_train, y_data_test = train_test_split(
        x_data_set, y_data_set, test_size=0.35, shuffle=False)
    return x_data_train, y_data_train, x_data_test, y_data_test
'''

def run_steep_gradient_descent(data_x, data_y,
                               len_data, alpha, theta):
    """ Run steep gradient descent and updates the Feature vector accordingly_
    :param data_x   : contains the dataset
    :param data_y   : contains the output associated with each data-entry
    :param len_data : length of the data_
    :param alpha    : Learning rate of the model
    :param theta    : Feature vector (weight's for our model)
    ;param return    : Updated Feature's, using
                       curr_features - alpha_ * gradient(w.r.t. feature)
    """
    n = len_data

    prod = np.dot(theta, data_x.transpose())
    prod -= data_y.transpose()
    sum_grad = np.dot(prod, data_x)
    theta = theta - alpha * sum_grad
    print('theta',theta)
    return theta


def sum_of_square_error(data_x, data_y, len_data, theta):
    """ Return sum of square error for error calculation
    :param data_x    : contains our dataset
    :param data_y    : contains the output (result vector)
    :param len_data  : len of the dataset
    :param theta     : contains the feature vector
    :return          : sum of square error computed from given feature's
    """
    prod = np.dot(theta, data_x.transpose())
    prod -= data_y.transpose()
    sum_elem = np.sum(np.square(prod))
    error = sum_elem / (2 * len_data)
    return error

def run_linear_regression(data_x, data_y):
    """ Implement Linear regression over the dataset
    :param data_x  : contains our dataset
    :param data_y  : contains the output (result vector)
    :return        : feature for line of best fit (Feature vector)
    """
    iterations = 100000
    alpha = 0.001
    no_features = data_x.shape[1]
    len_data = data_x.shape[0] - 1

    theta = np.zeros((1, no_features))
    print("shape of Theta:", theta.shape)

    for i in range(0, iterations):
        theta = run_steep_gradient_descent(data_x, data_y,
                                           len_data, alpha, theta)
        error = sum_of_square_error(data_x, data_y, len_data, theta)
        print('At Iteration %d - Error is %.5f ' % (i + 1, error))

    return theta

def main():
    x_data_set,y_data_set =LoadDataAirfoil('airfoil_self_noise.csv',"\t")
    print("Shape of X and Y Transpose data set: ", x_data_set.transpose().shape,y_data_set.transpose().shape)
    theta = run_linear_regression(x_data_set,y_data_set)

main()