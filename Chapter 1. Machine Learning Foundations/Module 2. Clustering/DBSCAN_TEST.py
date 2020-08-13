import numpy as np
np.set_printoptions(suppress=True)
import sys
sys.path.append('..') # append path to utils file to python path
from utils import get_classification_data, show_data, visualise_predictions, colors
import matplotlib.pyplot as plt
import sklearn.datasets
from time import sleep

X, Y = sklearn.datasets.make_moons()
Y = np.zeros_like(Y)
show_data(X, Y)

print(X.Shape,Y.Shape)


def compute_distances(input_X, dataset_X):
    """Takes in an array of inputs and finds each of their distances from every example in a dataset"""
    distances = ## matrix of distances between each input x and each x in our dataset
    for ## enumerate over input
        for ## enumerate over dataset
            distance = ## compute euclidian distance
            distances[i][j] = ## put this distance in the distances matrix
    return distances