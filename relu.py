import numpy as np

z=np.array([[0,2,3],
            [4,-5,6],
            [7,8,-9]])

def relu(x):
    for o in range(x.shape[0]):
        for p in range(x.shape[1]):
            if x[o,p]<0:
                x[o,p]=0
    return x

def derivative_relu(y):
    for o in range(y.shape[0]):
        for p in range(y.shape[1]):
            if y[o,p] < 0:
                y[o,p]=0
            else :
                y[o,p]=1
    return y


# print(relu(z))