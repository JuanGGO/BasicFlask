from flask import Flask, request, jsonify

app = Flask(__name__)


@app.route('/')
def hello_world():
    return '<h1>Hello World! Heroku<h1>'


@app.route('/from_flutter/', methods=['POST'])
def get_signal_from_flutter():
    param = request.form.get('title')
    print(param)
    if param:
        return jsonify({
            "Message": "yay flutter talked to me :)",
            "flutter": param}
        )

    else:
        return jsonify({
            'ERROR': 'FU asshole',
            'Request': request
        })

if __name__ == '__main__':
    app.run()
