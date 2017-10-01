from flask import Flask

app = Flask(__name__)


@app.route('/')
def main_controller():
    return 'Hello World!'


@app.route('/quad')
def quad_controller():
    return 'Quad page'


if __name__ == '__main__':
    app.run()
