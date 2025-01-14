from flask import Flask, send_from_directory

app = Flask(__name__, static_folder="static/build")

@app.route("/")

def server():
  return send_from_directory(app.static_folder, "index.html")