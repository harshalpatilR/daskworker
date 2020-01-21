import cdsw
import os
import socket
import time

# Launch CDSW workers. These are engines that will run in 
# the same project, execute a given code or script, and exit.
# Scheduler engine will keep running in background until session is closed
dask_scheduler = cdsw.launch_workers(n=1, cpu=2, memory=4, 
                              kernel="python3",script="daskschedular.py")


# IP of launched container comes up unknown for a while
# Wait for a while so IP is available in data structure
time.sleep(30)

# Get schedular IP
schedulerid = dask_scheduler[0]["id"]
listtemp = cdsw.list_workers()

for x in listtemp:
  if x["id"] == schedulerid:
    schedulerip = x["ip_address"]
    
    
print(" Scheduler IP: " + schedulerip)

#Scheduler protocol and port - defaults from Dask
schproto = "tcp://"
schport = ":8786"

schloc = schproto + schedulerip + schport
print(" Scheduler URL: " + schloc)


# Launch at least one Dask Worker

dask_client = cdsw.launch_workers(n=1, cpu=2, memory=4, 
                              kernel="python3",script="daskworker.py",
                                  env={"DASKSCHURL": schloc})

# wait for a while until the container is launched successfully
time.sleep(30)



os.putenv("DASKSCHURL", schloc)
#Launch DASK Client - XGboost training job
#os.system("python3 daskxgboost.py")

#Launch DASK test 
os.system("python3 dasktest.py")


#Stop ALL worker processes - Dask Scheduler and Dask Workers
#CDSW will close these automatically if running in background and 
#session is stopped. But we stop explicitly as good practice

cdsw.stop_workers()



