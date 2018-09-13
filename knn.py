import numpy as np
from math import sqrt

def data():
    location = np.array([[1.0, 0.9], [1.1, 1.3], [0.1, 0.2], [0.0, 0.1]])
    classes = ['A', 'A', 'B', 'B']
    return location, classes

def classify(input, location, classes, k):
    #get x and y value of input

    x = input[0]
    y = input[1]
    #creat a dictionary to store distance
    distance_array = {}
    list_of_k = list()
    large_three = list()
    #calclute the distance from original data to new input

    for n in range(0,location.shape[0]):
        distance_array[sqrt((location[n,0]-x)**2 + (location[n,1]-y)**2)] = classes[n]
    sorted_list = sorted(distance_array)
    for n in range(0,k):
        list_of_k.append(sorted_list[n])
        large_three.append(distance_array[sorted_list[n]])
    print(list_of_k)
    print(distance_array)
    print(large_three)
    if large_three.count('A') > large_three.count('b'):
        print('A')
    else:
        print('B')
