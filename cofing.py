import os

web_server = os.getenv("web_server")

config ={
    "host": "0.0.0.0",
    "port": 80,
    "SERVER_NAME": "lehss.top"
} if web_server else {
    "host": "0.0.0.0"
}