from flask import Flask
from datetime import datetime
from pytz import timezone

app = Flask(__name__)


@app.route("/")
def hello_world():
    return "Hello world!"


@app.route("/time")
def time():
    eastern = timezone("US/Eastern")
    fmt = "%Y-%m-%d %H:%M:%S %Z%z"
    loc_dt = datetime.now(eastern)
    return loc_dt.strftime(fmt)


app.run(host="0.0.0.0", port=8080, debug=True)
