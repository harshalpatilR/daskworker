import os

if not os.path.isdir("_dasksch_"):
  os.mkdir("_dasksch_")

#Launch dask-scheduler
os.system("dask-scheduler --host 0.0.0.0 --dashboard-address :8080 --local-directory _dasksch_")