import os
if not os.path.isdir("testdir"):
  os.mkdir("testdir")
  
  
for c in range(2):
  print(c)
  
  
import pandas as pd
import s3fs

df = pd.read_csv('s3://harshalpatil-s3/loans_accepted_2007_to_2018Q4.csv')
df.head()
df.tail()


from IPython.display import IFrame
from IPython.core.display import display
display(IFrame("http://10.10.9.12:8787", '700px', '450px'))