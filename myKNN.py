
"""
This module contains code for myKNN class and related functions.
This functionality is provided in scipy and scikit-learn, but was written for educational purposes.
The class myKNN creates an object that stores a set of observations and labels. It normalises the observations 
and stores the means and standard deviations of the observations. 
It has a method distance_sort that takes a new observation and returns the k nearest observations and labels. The caller
is free provide a value for k, otherwise it defaults to the number of observations in the object, that is he gets
all onservations sorted by distance.
"""

import random
from collections import Counter
import numpy as np
from plottingObservations import plotly_plot

OBSERVATIONS = 5000  # how many observations to generate
PARAMETERS = 5  # how many parameters to generate for each observation
LABELS = 5      # how many labels to generate for each observation
TESTS = 1000     # how many tests to run


class myKNN:
    """
    A class representing a k-nearest neighbors classifier.

    Parameters:
    observations (np.ndarray): The array of observations used for training.
    labels (np.ndarray): The array of labels corresponding to the observations.

    Attributes:
    observations (np.ndarray): The array of observations used for training.
    labels (np.ndarray): The array of labels corresponding to the observations.
    std (np.ndarray): The standard deviation of the observations.
    means (np.ndarray): The mean of the observations.
    normalised_observations (np.ndarray): The normalized observations.

    Methods:
    distance_sort(new_observation: np.ndarray, k=None) -> tuple:
        Calculates the distances between a new observation and the training observations,
        and returns the sorted distances, corresponding observations, and labels.

    """

    def __init__(self, observations: np.ndarray, labels: np.ndarray) -> None:
        self.observations = observations
        self.labels = labels
        self.std = np.std(observations, axis=0)
        self.means = np.mean(observations, axis=0)
        self.normalised_observations = (observations - self.means) / self.std

    def distance_sort(self, new_observation: np.ndarray, k=None) -> tuple:
        if k is None:
            k = len(self.observations)
        distances = np.zeros(len(self.observations))

        normalised_observation = (new_observation - self.means) / self.std
        distances = np.sum((self.normalised_observations -
                            normalised_observation)**2, axis=1)
        sorted_indices = np.argsort(distances[:])
        return distances[sorted_indices][0:k], self.observations[sorted_indices][0:k], self.labels[sorted_indices][0:k]


def generate_single_observation(label, parameter):
    mean = label*10 + parameter*10
    std = mean**(1/2.5)
    return random.gauss(mean, std)


def generate_observations(OBSERVATIONS, PARAMETERS, LABELS):
    observations = []
    labels = []
    for o in range(0, OBSERVATIONS):
        label = random.randint(1, LABELS)
        measurements = []
        for p in range(PARAMETERS):
            measurement = generate_single_observation(label, p)
            measurements.append(measurement)
        observations.append(measurements)
        labels.append(label)
    return np.array(observations), np.array(labels)


def main():
    kNN = myKNN(np.array
                ([
                    [1, 2, 3],
                    [4, 5, 6],
                    [7, 8, 9]
                ]),
                np.array([100, 200, 300])
                )

    # The line `distances, observations, labels = kNN.distance_sort(measurement := np.array([3, 4, 5]))`
    # is calling the `distance_sort` method of the `kNN` object and passing in a new observation
    # `measurement` as an argument.
    distances, observations, labels = kNN.distance_sort(
        measurement := np.array([3, 4, 5]), 3)

    print("Sorted Distances:\n", measurement)
    print("Sorted Distances:\n", distances)
    print("Sorted Observations):\n", observations)
    print("Sorted labels:\n", labels)

    observations, labels = generate_observations(
        OBSERVATIONS, PARAMETERS, LABELS)

    plotly_plot(observations, labels)
    kNN = myKNN(observations, labels)
    matches = nomatches = 0
    k = 30
    for i in range(TESTS):
        label = random.randint(1, LABELS)
        measurement = np.array([generate_single_observation(label, p)
                                for p in range(PARAMETERS)])
        distances, observations, labels = kNN.distance_sort(measurement, k)
    #     print("measurement\n", measurement, label)
    #     print("Sorted Distances:\n", distances[:k])
    #  #   print("Sorted Observations):\n", observations[:k, :])
    #     print("Sorted labels:\n", labels[:k])
        prediction = sorted(Counter(labels[:k]).items(
        ), key=lambda x: x[1], reverse=True)[0][0]
        if prediction == label:
            #        print("match")
            matches += 1
        else:
            #        print("no match")
            nomatches += 1
    print("matches", matches)
    print("nomatches", nomatches)


if __name__ == "__main__":
    main()
