
import os
print(" Client start ")
print(" Client Scheduler url received: "+os.environ["DASKSCHURL"])


os.system("python3 daskxgboost.py")