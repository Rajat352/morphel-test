from flask import Flask
import os
import datetime
import subprocess

app = Flask(__name__)

@app.route("/htop")
def htop():
    name = "Rajat"
    username = os.getlogin()
    ist_time = datetime.datetime.now().astimezone().strftime("%Y-%m-%d %H:%M:%S IST")
    top_output = subprocess.getoutput("top -b -n 1")

    return f"""
    <h1>Name: {name}</h1>
    <h2>Username: {username}</h2>
    <h3>Server Time: {ist_time}</h3>
    <pre>{top_output}</pre>
    """

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000)
