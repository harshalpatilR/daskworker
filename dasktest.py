import os

print("\n \n ====== Run Dasktest ====== \n")

testloc = "tcp://10.10.167.25:878"
#print("DASK scheduler URL : {} ".format(os.environ["DASKSCHURL"]))
#Connect client to scheduler
from dask.distributed import Client
#client = Client(os.environ["DASKSCHURL"])
client = Client(testloc)

import dask.array as da
x = da.random.random((40000,40000),chunks=(1000,1000))
y = da.exp(x).sum()
print("\n ====== Computation Result: ===== \n")
print(y.compute())
print ("\n ===== end ===== \n")