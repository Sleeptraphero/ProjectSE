from flask import Flask
from flask import render_template
from flask import request
from os import getenv
from shutil import copyfile
import sqlite3

app = Flask(__name__)
app.config.from_pyfile("config.py")
app.config['DATABASE_FILE'] = "what_is_Monero/data/user_db"

if getenv('GAE_ENV', '').startswith('standard'):
    app_engine_path = "/tmp/user_db"
    copyfile(app.config['DATABASE_FILE'], app_engine_path)
    app.config['DATABASE_FILE'] = app_engine_pathg
else:
    pass

@app.route('/')
def index():
    return render_template('index.html', page_title="What is Monero?")

@app.route('/FAQ')
def first_page():
    return render_template('FAQ.html', page_title="What is Monero?")

@app.route('/newsletter', methods=['POST'])
def create_user():
    try:
        _fname = request.form.get("fname")
        _lname = request.form.get("lname")
        _email = request.form.get("email")
        _mobile = request.form.get("mobile")
        _message = request.form.get("message")
        
        #move to database & adjusted to be injection save
        conn = sqlite3.connect("what_is_Monero/data/user_db")
        c = conn.cursor()
        c.execute("INSERT INTO users VALUES (:fname, :lname, :email, :mobile, :message)", {'fname': _fname, 'lname': _lname, 'email': _email, 'mobile': _mobile, 'message': _message})
        conn.commit()
        conn.close()

        return render_template("newsletter.html", page_title="What is Monero?")

    except Exception:
        error_code = 500
        return render_template("error.html", page_title="What is Monero?")

if __name__ == "__main__":
    app.run(host="localhost", port=8080, debug=True)
