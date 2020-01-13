from flask import Flask, escape

app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello, World!"

@app.route('/user/<name>')
def show_user_profile(name):
    # show the user profile for that user
    return 'Hello Mr. %s' % escape(name)

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5001)