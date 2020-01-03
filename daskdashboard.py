#import os, socket


#target_host = "10.10.182.202" 
 
#target_port = 8787  # create a socket object 
#client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  
 
# connect the client 
#client.connect((target_host,target_port))


#import webbrowser
#webbrowser.open("http://localhost:8787")



# try2

from flask import Flask, redirect
import os

app = Flask(__name__)

@app.route('/')
def hello():
    return redirect("http://10.10.165.195:8787", code=302)

if __name__ == '__main__':
  
    cdsw_port = int(os.environ.get('CDSW_APP_PORT'))
    app.run(host='127.0.0.1', port=cdsw_port)
    