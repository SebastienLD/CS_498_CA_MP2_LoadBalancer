from flask import Flask
from flask import request

app = Flask(__name__)

SEED_VALUE = 0


@app.post("/")
def set_seed():
    json_body = request.get_json()
    seed_value = json_body["num"]
    global SEED_VALUE
    SEED_VALUE = seed_value
    return "Seed set to " + str(seed_value)


@app.get("/")
def get_seed():
    return str(SEED_VALUE)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
