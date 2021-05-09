from flask import Flask
from flask import render_template
from flask import request

app = Flask(__name__)

# configure Flask using environment variables
app.config.from_pyfile("config.py")


@app.route('/')
def index():
    return render_template('index.html', page_title="What is Monero?")

@app.route('/FAQ')
def first_page():
    return render_template('FAQ.html', page_title="What is Monero?")


@app.route('/create', methods=['POST'])
def create_user():
    try:
        fname = request.form.get("fname")
        lname = request.form.get("lname")
        email = request.form.get("email")
        mobile = request.form.get("mobile")
        message = request.form.get("message")
        return render_template("temp.html", page_title="What is Monero?")

    except Exception:
        # something bad happended. Return an error page and a 500 error
        error_code = 500
        return render_template("error.html", page_title="What is Monero?")

if __name__ == "__main__":
    app.run(host="localhost", port=8080, debug=True)
