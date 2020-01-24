import pandas as pd
from sklearn.datasets import load_wine
import numpy as np

data = load_wine()

#since the data is numpy series we will not use df = dd.from_pandas(data[‘data’])
#dask has various ways to convert numpy and pandas to dask dataframes      
df = pd.DataFrame(data['data'])
df.columns = data['feature_names']


#add target as field
df["target"] = data["target"]


# identify small noise that can be added to each feature
# equal to 1/100 of the std deviation
# noise added will be std normal with 1/100 std deviation
descdf = pd.DataFrame(df.describe())
descdf.loc["std_used"] = descdf.loc["std"]/100

#set no change to target
descdf.loc["std_used","target"] = 0.000000

#isolate the std deviation / 100 vector
stdvec = descdf.loc["std_used"]

################
# no of records to generate in new dataframe 
records=8000000
nrows=len(df)

################
# hold generated data as numpy array
generated_fields = df.columns
generated_rows = {}


################
for i in range(records):

  # identify row with uniform probability
  random_row=round(np.random.uniform(0,nrows-1))
  random_row_record = df.iloc[random_row]
  
  # build a vector of random numbers with 1/100 std deviation, 0 mean, normal
  noisevec = np.vectorize(lambda x: np.random.normal(0,x,1))(stdvec)
  
  # add noise vector to record to get new generated record
  # we have setup 0 noise to be added to target
  random_row_record = random_row_record + noisevec
  
  generated_rows[i]=random_row_record
  
  if(i%100000==0):
    print(" == Records Generated: " + str(i))

####  
gendf = pd.DataFrame.from_dict(generated_rows,orient="index",
                               columns=generated_fields)

####
opfile = "winedatagen.csv"
if os.path.exists(opfile):
  print(" === file found - deleted === ")
  os.remove(opfile)

gendf.to_csv(opfile,index=False)

  