#!/usr/bin/env python
# coding: utf-8

# In[1]:
import pandas
import math
import operator
import sys

def findL1(instance1, instance2, length):
    distance = 0
    for i in range(1,length):
        distance += abs(instance1[i] - instance2[i])
    return distance

def findL2(instance1, instance2, length):
    distance = 0
    for i in range(1,length):
        distance += pow(instance1[i] - instance2[i], 2)
    return math.sqrt(distance)

def findLinf(instance1, instance2, length):
    distances = []
    for i in range(1,length):
        distances.append(abs(instance1[i] - instance2[i]))
    return max(distances)

def getNeighborsL1(trainingSet, testInstance, k):
    distances = []
    length = len(testInstance)
    for x in range(len(trainingSet)):
        dist = findL1(testInstance, trainingSet.iloc[x],length)
        distances.append((trainingSet.iloc[x],dist))
    distances.sort(key=operator.itemgetter(1))
    neighbors = []
    for x in range(k):
        neighbors.append(distances[x][0])
    return neighbors

def getNeighborsL2(trainingSet, testInstance, k):
    distances = []
    length = len(testInstance)
    for x in range(len(trainingSet)):
        dist = findL2(testInstance, trainingSet.iloc[x],length)
        distances.append((trainingSet.iloc[x],dist))
    distances.sort(key=operator.itemgetter(1))
    neighbors = []
    for x in range(k):
        neighbors.append(distances[x][0])
    return neighbors

def getNeighborsLinf(trainingSet, testInstance, k):
    distances = []
    length = len(testInstance)
    for x in range(len(trainingSet)):
        dist = findLinf(testInstance, trainingSet.iloc[x],length)
        distances.append((trainingSet.iloc[x],dist))
    distances.sort(key=operator.itemgetter(1))
    neighbors = []
    for x in range(k):
        neighbors.append(distances[x][0])
    return neighbors

def getResponse(neighbors):
    classVotes = {}
    for x in range(len(neighbors)):
        response = neighbors[x][-5]
        if response in classVotes:
            classVotes[response] += 1
        else:
            classVotes[response] = 1
    sortedVotes = sorted(classVotes.items(), key = operator.itemgetter(1), reverse = True)
    return sortedVotes[0][0]

# python YourCodeName.py --K 3 --method L1
def main():
    df_train = pandas.read_csv('knn_train.csv')
    df_test = pandas.read_csv('knn_test.csv')
    for x in range(len(df_test)):
        if(sys.argv[4] == "L1"):
            neighbors = getNeighborsL1(df_train, df_test.iloc[x],int(sys.argv[2]))
        elif(sys.argv[4] == "L2"):
            neighbors = getNeighborsL2(df_train, df_test.iloc[x],int(sys.argv[2]))
        elif(sys.argv[4] == "Linf"):
            neighbors = getNeighborsLinf(df_train, df_test.iloc[x],int(sys.argv[2]))
        response = getResponse(neighbors)
        print(response)

main()





