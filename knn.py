import numpy as np
import pandas as pd
from math import sqrt

def data_generate():
    location = np.array([[1.0, 0.9], [1.1, 1.3], [0.1, 0.2], [0.0, 0.1]])
    classes = ['A', 'A', 'B', 'B']
    return location, classes

def load_data():
    data_init = pd.read_csv("test_data.txt")
    #read data
    array_init = np.array(data_init)
    #convert data type from data frame to array
    location = np.zeros(shape = (b.shape[0],b.shape[1]-1))
    #creat empty array in which we put coordinates of data
    for n in range(0,b.shape[0]):
        for m in range(0,useful.shape[1]):
            location[n,m]=b[n,m]
    #fill coordinates of data
    classes = list()
    #do the same thing for classes
    for n in range(0,b.shape[0]):
        classes.append(array_init[n,2])
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
