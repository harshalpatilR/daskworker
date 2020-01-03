import os

schloc = os.environ["DASKSCHURL"]
print("\n ====== Run Dask Xgboost ====== \n")
print(" DASK scheduler URL for Xgboost Client : {} \n".format(schloc))

#Connect client to scheduler
from dask.distributed import Client
client = Client(schloc)

#Use the wine dataset
from sklearn.datasets import load_wine
data = load_wine()

from dask import dataframe as dd
#since the data is numpy series we will not use df = dd.from_pandas(data[‘data’])
#dask has various ways to convert numpy and pandas to dask dataframes      
df = dd.from_array(data['data'])
df.columns = data['feature_names']

#print a few lines
print(" Dataframe : ")
print(df.head())

#Get target variable
dt = dd.from_array(data['target'])
dt.columns = ["target"]
      
#print target classes example
print(dt.head())      

# train and test split
from dask_ml.model_selection import train_test_split
train, test, train_labels, test_labels = train_test_split(df,dt,random_state=123)      
      
#xgboost
from dask_ml.xgboost import XGBClassifier
est = XGBClassifier()      
      
#fit model      
model = est.fit(train, train_labels)

#which features contribute most
model.feature_importances_
import seaborn
seaborn.barplot(data=model.feature_importances_)
      

#predictions
ypred = model.predict(test)

#sample some predictions
print(" Sample initial predictions: ")      
print(ypred[[0,1,2,3]].compute())

#ensure model is predicting all classes - not just 0
print(" Classes other than zero predicted: ")
print(ypred[ypred>0].compute())
      
#check accuracy on test set      
from dask_ml import metrics
print(" Model Accuracy: ")      
print(metrics.accuracy_score(test_labels,model.predict(test)))
      
print("\n === End Dask Xgboost === \n")
