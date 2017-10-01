from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def home_controller():
    return render_template('home.html')


@app.route('/quad')
def quad_controller():
    return render_template('quadrupole.html')


if __name__ == '__main__':
    app.run(debug=True)
