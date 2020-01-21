import os


print(" Worker start")
print(" Scheduler url received "+os.environ["DASKSCHURL"])

if not os.path.isdir("_daskworker_"):
  os.mkdir("_daskworker_")

#daskmasterport = ":8786"
#masterloc = "tcp://" + os.environ["CDSW_MASTER_IP"] + daskmasterport
daskworkercmd = "dask-worker " + os.environ["DASKSCHURL"] + " --local-directory _daskworker_"

os.system(daskworkercmd)

print("Dask worker ended " + os.environ["DASKSCHURL"] )