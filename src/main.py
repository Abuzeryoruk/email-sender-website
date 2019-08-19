from flask import Flask


app = Flask(__name__)

@app.route('/')
def home():
    return '<h4>Welcome to <h1>emailsender</h1></h4>'

@app.route('/signup')
def signup():
   return 'signup page'


@app.route('/signin')
def signin():
   return 'Signin page'


if __name__ == "__main__":
    app.run(debug=True)
