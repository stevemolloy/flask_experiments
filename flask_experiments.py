from flask import Flask, render_template, request

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
    return render_template('space_charge.html')


@app.route('/quad_calcs', methods=['POST', 'GET'])
def quad_calcs():
    # result = request.form
    # return render_template("result.html",result = result)
    return request.args.to_dict().__repr__()


if __name__ == '__main__':
    app.run(debug=True)
