'''

SOme tips
In the cat problem
I am giving images of 64x64 pixels
This is col imag
So there 3 channles _ R, G, B

Need to flatten each image for Logistic and Neural N/w
Original image shape: (64,64,3,250) (assume 250 images)
Flatten: 64x64x3=12288
New shape = 12288,250 whre #rows = 250, #features = 12288
You need to flatten only for image recognition not for textual data
Need h5py library to read the file. Please download and install using pip
The data set is already split to Test and train
'''

import h5py
import numpy as np
import matplotlib.pyplot as plt


# sigmoid function or logistic function is used as a hypothesis function in classification problems
def sigmoid_function(z):
    return 1 / (1 + np.exp(-z))


def cost_function(h, y):
    return (-y * np.log(h) - (1 - y) * np.log(1 - h)).mean()


# here alpha is the learning rate, X is the feature matrix,y is the target matrix
def logistic_reg(alpha, X, y, max_iterations=70000):
    converged = False
    iterations = 0
    theta = np.zeros(50)
    print(theta)

    while not converged:
        z = np.dot(X, theta)
        h = sigmoid_function(z)
        gradient = np.dot(X.T, (h - y)) / y.size
        theta = theta - (alpha) * gradient

        # z=np.dot(X,theta)
        # h=sigmoid_function(z)
        J = cost_function(h, y)
        print("Minimal cost function J=", J)

        iterations += 1  # update iterations

        if iterations == max_iterations:
            print("Maximum iterations exceeded!")
            print("Minimal cost function J=", J)
            converged = True

    return theta


# In[68]:


if __name__ == '__main__':
    f = h5py.File('test_catvnoncat.h5', 'r+')
    print(list(f.items()))
    X = list(f.get('test_set_x'))
    Y = list(f.get('test_set_y'))
    alpha = 0.1
    theta = logistic_reg(alpha, X,Y , max_iterations=70000)
    print(theta)
    f.close()