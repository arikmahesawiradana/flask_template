from flask import *
from sqlite3 import *
import sys

database = connect("data/database.db", check_same_thread=False)
app = Flask(__name__, template_folder="templates", static_folder="static")
app.config['SECRET_KEY'] = 'your-secret-key'

@app.route('/')
def index():
    version = sys.version
    version = version.split(" ")
    return render_template("index.html", version=version[0])


if __name__ == "__main__":
    app.run(debug=True)