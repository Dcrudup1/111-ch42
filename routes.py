from flask import Flask


app = Flask(__name__)

@app.get("/")
def index():
    me = {
        "first_name": "Dedrick",
        "last_name": "Crudup",
        "hobbies": "DIY stuff",
        "is_active": True
    }
    return me