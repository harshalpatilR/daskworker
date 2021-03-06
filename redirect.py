import sys
from http.server import HTTPServer, BaseHTTPRequestHandler

if len(sys.argv)-1 != 2:
    print("""
Usage: {} <port_number> <url>
    """.format(sys.argv[0]))
    sys.exit()

class Redirect(BaseHTTPRequestHandler):
   def do_GET(self):
       self.send_response(302)
       self.send_header('Location', sys.argv[2])
       self.end_headers()

HTTPServer(("", int(sys.argv[1])), Redirect).serve_forever()



from flask import Flask, redirect

app = Flask(__name__)

@app.route('/')
def hello():
    return redirect("http://10.10.168.63:8787", code=302)

if __name__ == '__main__':
    app.run(host='0.0.0.0')