import cdsw
import os
import socket
import time

# Stop garbage collection warnings from distributed_utils_perf
import logging
logger = logging.getLogger("distributed.utils_perf")
logger.setLevel(logging.ERROR)


# Get schedular IP
schedulerip = os.environ["CDSW_IP_ADDRESS"]

print(" Scheduler IP: " + schedulerip)

#Scheduler protocol and port - defaults from Dask
schproto = "tcp://"
schport = ":8786"

schloc = schproto + schedulerip + schport
print(" Scheduler URL: " + schloc)


# Launch at least one Dask Worker

dask_client = cdsw.launch_workers(n=1, cpu=4, memory=8, 
                              kernel="python3",script="daskworker.py",
                                  env={"DASKSCHURL": schloc})

# wait for a while until the container is launched successfully
time.sleep(10)


if not os.path.isdir("_dasksch_"):
  os.mkdir("_dasksch_")

#Launch dask-scheduler
os.system("dask-scheduler --host 0.0.0.0 --dashboard-address :8080 --local-directory _dasksch_")

