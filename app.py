# import necessary libraries
# from models import create_classes
import os
from flask import (
    Flask,
    render_template
   )

#################################################
# Flask Setup
#################################################
app = Flask(__name__)


# create route that renders index.html template
@app.route("/")
def home():
    return render_template("index.html")

if __name__ == "__main__":
    app.run()
