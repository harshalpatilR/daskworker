import os, socket


target_host = "10.10.182.202" 
 
target_port = 8787  # create a socket object 
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  
 
# connect the client 
client.connect((target_host,target_port))


import webbrowser
webbrowser.open("http://localhost:8787")

