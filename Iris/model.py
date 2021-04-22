#import libraries
import sklearn
import sklearn.datasets
import sklearn.ensemble
import sklearn.model_selection
import pickle
import os

#load data
data = sklearn.datasets.load_iris()

#Split the data into test and train
train_data, test_data, train_labels, test_labels = sklearn.model_selection.train_test_split(data.data, data.target, train_size=0.80)
print(train_data,train_labels)

#Train a model using random forest
model = sklearn.ensemble.RandomForestClassifier(n_estimators=500)
model.fit(train_data, train_labels)

#test the model
result = model.score(test_data, test_labels)
print(result)

#save the model 
filename = 'iris_model.pkl'
pickle.dump(model, open(filename, 'wb'))