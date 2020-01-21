import os
from dask.distributed import Client

print("\n \n ====== Run Dasktest ====== \n")

#manual test
#testloc = "tcp://10.10.167.25:878"
#client = Client(testloc)

#automated test
#print("DASK scheduler URL : {} ".format(os.environ["DASKSCHURL"]))
#Connect client to scheduler
#client = Client(os.environ["DASKSCHURL"])

#test daskarray similar to numpy
import dask.array as da
x = da.random.random((40000,40000),chunks=(1000,1000))
y = da.exp(x).sum()
print("\n ====== Computation Result: ===== \n")
print(y.compute())
print ("\n ===== end ===== \n")