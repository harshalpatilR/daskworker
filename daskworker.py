import os


print("Worker start")
print("Master IP received"+os.environ["CDSW_MASTER_IP"])

daskmasterport = ":8786"
masterloc = "tcp://" + os.environ["CDSW_MASTER_IP"] + daskmasterport
daskworkercmd = "dask-worker " + masterloc

os.system(daskworkercmd)

print("Dask worker ended " + masterloc )