
import os
print("Client start")
print("Scheduler url received"+os.environ["DASKSCHURL"])


os.system("python3 dasktest.py")