

from flask import Flask,request,redirect,Response
import requests
app = Flask(__name__)

@app.route('/', defaults={'path': ''})
@app.route('/<path:path>')
def catch_all(path):
    return 'You want path: %s' % path
  
  
if __name__ == "__main__":
    app.run(debug = False,port=8090)