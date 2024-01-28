from flask import Flask
import subprocess
import socket

app = Flask(__name__)


@app.post("/")
def set_seed():
    subprocess.Popen(["python3", "stress_cpu.py"])
    return "Stress CPU"


@app.get("/")
def get_seed():
    return socket.gethostname()


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
