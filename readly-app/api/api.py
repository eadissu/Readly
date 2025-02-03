import time
from flask import Flask

app = Flask(__name__)

@app.route('/time') # We call this function from the react side
def get_current_time():
  print(time.time())
  return {'time' : time.time()}

