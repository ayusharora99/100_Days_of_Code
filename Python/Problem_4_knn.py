#!/usr/bin/env python
# coding: utf-8

# In[107]:


import pandas
import math
import operator
import sys

df_train = pandas.read_csv('knn_train.csv')
df_test = pandas.read_csv('knn_test.csv')

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

def getNeighbors(trainingSet, testInstance, k):
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
    print(str(sys.argv))


# In[106]:


import pandas
df_train = pandas.read_csv('knn_train.csv')
df_test = pandas.read_csv('knn_test.csv')
df_train.columns

df_train_legit = df_train[['f1', ' f2', ' f3', ' f4']]
df_test_legit = df_test[['f1', ' f2', ' f3', ' f4']]


# In[63]:


import math

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


# In[102]:


import operator 
def getNeighbors(trainingSet, testInstance, k):
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


# In[83]:


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


# In[73]:


# Answer to 2
distance1 = findL1(df_test.iloc[0], df_train.iloc[0], 5)
print('Distance: ' + repr(distance1))


# In[74]:


# Answer to 3
distance2 = findL2(df_test.iloc[0], df_train.iloc[0], 5)
print('Distance: ' + repr(distance2))


# In[75]:


# Answer to 4
distance3 = findLinf(df_test.iloc[0], df_train.iloc[0], 5)
print('Distance: ' + repr(distance3))


# In[98]:


# Answer to 5
neighbors = getNeighbors(df_train, df_test.iloc[0], 5)
print(neighbors)


# In[103]:


# TEST
for x in range(len(df_test)):
    neighbors = getNeighbors(df_train, df_test.iloc[x], 9)
    response = getResponse(neighbors)
    print(response)

