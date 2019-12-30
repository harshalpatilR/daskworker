import cdsw
import os


# Launch two CDSW workers. These are engines that will run in 
# the same project, execute a given code or script, and exit.
workers = cdsw.launch_workers(n=1, cpu=2, memory=4, 
                              kernel="python3",script="daskschedular.py")

cdsw.list_workers()


#Launch dask-scheduler
#os.system("dask-scheduler --host 0.0.0.0 &")


from dask.distributed import Client
daskport = ":8786"
client = Client("127.0.0.1"+daskport)
#client = Client("tcp://10.10.181.214:8786")



# Launch two CDSW workers. These are engines that will run in 
# the same project, execute a given code or script, and exit.
workers = cdsw.launch_workers(n=1, cpu=2, memory=4, 
                              kernel="python3",script="daskworker.py")



from sklearn.datasets import load_wine
data = load_wine()
from dask import dataframe as dd
#df = dd.from_pandas(data[‘data’])
df = dd.from_array(data['data'])
#train, test = df.random_split([0.8, 0.2])

#FIX NEEDED - can not be random - must be same as test
dt = dd.from_array(data['target'])
#train_labels, test_labels = dt.random_split([0.8, 0.2])


import socket    
hostname = socket.gethostname()    
IPAddr = socket.gethostbyname(hostname)    
daskport = ":8786"

from dask.distributed import Client
client = Client("127.0.0.1"+daskport)
#client = Client("tcp://10.10.181.214:8786")

#xgboost
from dask_ml.xgboost import XGBClassifier
est = XGBClassifier()
#train.columns = ["a","b","c","d","e","f","g","h","i","j","k","l","m"]
#est.fit(train, train_labels)

# FIX done
from dask_ml.model_selection import train_test_split
train, test, train_labels, test_labels = train_test_split(df,dt,random_state=123)
train.columns = ["a","b","c","d","e","f","g","h","i","j","k","l","m"]
model = est.fit(train, train_labels)

#which features contribute most
model.feature_importances_

#predictions
model.predict(test)
accuracy = (model.predict(test)==test_labels)
accuracy.sum().compute()
test_labels.describe().compute()
