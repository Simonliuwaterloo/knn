#!/usr/bin/env python
import numpy as np
import pandas as pd
from math import sqrt
import matplotlib.pyplot as plt
import tkinter
#matplotlib doesn't work without tkinter

def data_generate():
    #generate a set of data for testing
    location = np.array([[1.0, 0.9], [1.1, 1.3], [0.1, 0.2], [0.0, 0.1]])
    classes = ['A', 'A', 'B', 'B']
    return location, classes


def load_data(file_name):
    #file_name is the name of your dataset, must be in plain text form, data separated by whitespace
    data_init = pd.read_csv(file_name)
    #read data, store them in data_init in dataframe form
    array_init = np.array(data_init)
    #convert data type from data frame to array
    location = np.zeros(shape = (array_init.shape[0],array_init.shape[1]-1))
    #creat empty array
    for n in range(0,array_init.shape[0]):
        for m in range(0,location.shape[1]):
            location[n,m]=array_init[n,m]
    #fill empty array with location
    classes = list()
    #create empty list
    for n in range(0,array_init.shape[0]):
        classes.append(array_init[n,2])
    #fill list with classes
    return location, classes

def plot_data(location, classes):
    #plot the x and y coordinates(location in a cartesian coordinate system) of data
    x=list()
    y=list()
    for n in range(location.shape[0]):
        x.append(location[n,0])
        y.append(location[n,1])
    plt.scatter(x,y)
    plt.show()
    return 0

def classify(input, location, classes, k):
    #get x and y value of input

    x = input[0]
    y = input[1]

    distance_array = {}
    #create a dictionary to store distance between input data and sample
    list_of_k = list()
    #this list stores the distance of nearest three neighbours
    large_three = list()
    #this list stores the classes of nearest three neighbours


    for n in range(0,location.shape[0]):
        distance_array[sqrt((location[n,0]-x)**2 + (location[n,1]-y)**2)] = classes[n]
    sorted_list = sorted(distance_array)
    #calclute the distance from sample data to new input and store them as keys in a dictionary
    #sort the dictionary according to key values(distance)
    for n in range(0,k):
        list_of_k.append(sorted_list[n])
        #store largest three values of keys in this list
        large_three.append(distance_array[sorted_list[n]])
        #store the classes of these keys in this list
    print("The distance to the ", k, "nearest neighbours are ", list_of_k)
    print("The classes of the ", k, "nearest neighbours are ", large_three)
    if large_three.count('A') > large_three.count('B'):
        print('A')
    else:
        print('B')


a,b = load_data("test_data.txt")
classify([1,2],a,b,3)
plot_data(a,b)
