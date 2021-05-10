from flask import Flask
from flask import render_template
from flask import request
import sqlite3

app = Flask(__name__)

app.config.from_pyfile("config.py")

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
        conn = sqlite3.connect("user_db")
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
