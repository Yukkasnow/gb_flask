from flask import Flask, g, Response
import time

app=Flask(__name__)

@app.route('/')
def hello():
  return 'Hello World!'
#
@app.before_request
def proc_before_request():
    g.start_time=time.time()
#
@app.after_request
def proc_after_request(response):
    if hasattr(g, "start_time"):
        response.headers["process-time"] = time.time() - g.start_time
        # print(response.headers["process-time"])
    return response





