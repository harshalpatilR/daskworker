
print("Client start")
print("Scheduler url received"+os.environ["DASKSCHURL"])


#Connect client to scheduler
from dask.distributed import Client
client = Client(os.environ["DASKSCHURL"])

import dask.array as da
x = da.random.random((40000,40000),chunks=(1000,1000))
y = da.exp(x).sum()
print(y.compute())
