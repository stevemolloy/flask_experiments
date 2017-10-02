from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def home_controller():
    return render_template('home.html')


@app.route('/quad')
def quad_controller():
    return render_template('quadrupole.html')


@app.route('/acceleration/numerical')
def acc_num_controller():
    return render_template('acc_num.html')


@app.route('/acceleration/pi_mode')
def acc_model_controller():
    return render_template('pi_mode_model.html')


@app.route('/space_charge')
def space_charge_controller():
    return render_template('space_holder_template.html', element_type='space_charge')


if __name__ == '__main__':
    app.run(debug=True)
