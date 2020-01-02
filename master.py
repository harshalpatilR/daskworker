# master.py

import cdsw, socket

# Launch two CDSW workers. These are engines that will run in 
# the same project, execute a given code or script, and exit.
workers = cdsw.launch_workers(n=1, cpu=2, memory=4, kernel="python3",script="worker.py")

# Listen on TCP port 6000
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind(("0.0.0.0", 6001))
s.listen(1)

# Accept two connections, one from each worker. Workers will
# execute worker.py.
conn, addr = s.accept()
for i in range(1):
    # Receive a message from each worker and return a response.
    data = conn.recv(20)
    if not data: break
    print("Master received:", data)
    conn.send("Hello From Server!".encode())
conn.close()
