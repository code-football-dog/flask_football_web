# --*-- coding:utf-8 --*--

from flask import Flask
from cofing import config
app = Flask(__name__)
host = config.get("host")
port = config.get("port")
app.config["SERVER_NAME"] = config.get("SERVER_NAME")

@app.route("/")
def index():
    return "hello boy welcome to lehss.top"

if __name__ == '__main__':
    app.run(host, port)