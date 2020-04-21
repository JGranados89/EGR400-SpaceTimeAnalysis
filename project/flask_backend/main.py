from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    # return 'Hello'
    return flask.render_template("index.html", token="Hello World")

if __name__ == '__main__':
    app.run()