#!/usr/bin/python3

import numpy
from sklearn import tree
from sklearn.datasets import load_iris

iris=load_iris()

x=[0,50,100]
only_data_training=numpy.delete(iris.data,x,axis=0)
only_target_training=numpy.delete(iris.target,x)

test_data=iris.data[x]
#print test_data
test_target=iris.target[x]
#print test_target

clf=tree.DecisionTreeClassifier()
trained_algo=clf.fit(only_data_training,only_target_training)

output=trained_algo.predict(test_data)
print(output)
