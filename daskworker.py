import os


print(" Worker start")
print(" Scheduler url received "+os.environ["DASKSCHURL"])

#daskmasterport = ":8786"
#masterloc = "tcp://" + os.environ["CDSW_MASTER_IP"] + daskmasterport
daskworkercmd = "dask-worker " + os.environ["DASKSCHURL"]

os.system(daskworkercmd)

print("Dask worker ended " + os.environ["DASKSCHURL"] )