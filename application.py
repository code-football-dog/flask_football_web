# --*-- coding:utf-8 --*--

from flask import Flask

app = Flask(__name__)
app.config['SERVER_NAME'] = 'lehss.top'

@app.route("/")
def index():
    return "hello boy welcome to lehss.top"

if __name__ == '__main__':
    app.run("0.0.0.0")