from flask import Flask, request

app = Flask(__name__)


@app.route('/')
def hello_world():
    return '<h1>Hello World! Heroku<h1>'


@app.route('/from_flutter', methods=['POST'])
def get_signal_from_flutter(json):
    param = request.form.get('title')
    print(param)


if __name__ == '__main__':
    app.run()
