#import os, socket


#target_host = "10.10.182.202" 
 
#target_port = 8787  # create a socket object 
#client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  
 
# connect the client 
#client.connect((target_host,target_port))


#import webbrowser
#webbrowser.open("http://localhost:8787")



# try2

#from flask import Flask, redirect
#import os

#app = Flask(__name__)

#@app.route('/')
#def hello():
#    return redirect("http://127.0.0.1:8787", code=302)

#if __name__ == '__main__':
  
#    cdsw_port = int(os.environ.get('CDSW_APP_PORT'))
#    app.run(host='127.0.0.1', port=cdsw_port)

    
# try3

from flask import Flask,request,redirect,Response
import requests
app = Flask(__name__)
SITE_NAME = "http://10.10.171.178:8787/"
@app.route('/favicon.ico') 
def favicon(): 
    #return send_from_directory(os.path.join(app.root_path, 'static'), 'favicon.ico', mimetype='image/vnd.microsoft.icon')
    return("Flask")
@app.route("/")
def index():
    resp = requests.get("http://10.10.171.178:8787")
    excluded_headers=["content-encoding", "content-length", "transfer-encoding", "connection"]
    headers = [(name, value) for (name, value) in  resp.raw.headers.items() if name.lower() not in excluded_headers]
    response = Response(resp.content, resp.status_code, headers)
    return response
    #return "Flask is running!"
@app.route("/<path:path>",methods=["GET"])
def proxy(path):
    global SITE_NAME
    if request.method=="GET":
        #resp = requests.get("http://10.10.173.17:8787")
        print("URL:")
        print(path)
        print(f"{SITE_NAME}{path}")
        resp = requests.get(f"{SITE_NAME}{path}")
        #excluded_headers = ["content-encoding", "content-length", "transfer-encoding", "connection"]
        excluded_headers = []
        headers = [(name, value) for (name, value) in  resp.raw.headers.items() if name.lower() not in excluded_headers]
        response = Response(resp.content, resp.status_code, headers)
        return response

if __name__ == "__main__":
    app.run(debug = False,port=8090)