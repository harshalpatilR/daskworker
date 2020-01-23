import os
from sklearn.datasets import make_classification
import pandas as pd
X,y= make_classification(n_samples=5000000, n_features=15, \
                            n_informative=12,n_redundant=2, \
                            n_classes=2, random_state=123)

cnames = ["V"+str(i) for i in range(1,16)] 

datadf = pd.DataFrame(X,columns=cnames)
datadf["target"] = y

opfile = "datagenclassf.csv"
if os.path.exists(opfile):
  print(" === file found - deleted === ")
  os.remove(opfile)

datadf.to_csv(opfile,index=False)

