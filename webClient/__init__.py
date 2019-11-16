import json

from flask import Flask, render_template, request
import requests

app = Flask(__name__)

my_rest_URL = 'http://localhost:9999/'
my_rest_figures = 'figure/'


@app.route("/")
def hello():
    return render_template('base.html', output="", item=False)


@app.route('/', methods=['POST'])
def my_form_post():
    # text = request.form['inputText']

    if request.form['submit_button'] == 'clear':
        return render_template('base.html', output="", item=False)
    else:
        if 'gender' in request.form:
            gender = request.form['gender']
            req = requests.get(my_rest_URL + my_rest_figures + gender)
        else:
            req = requests.get(my_rest_URL + my_rest_figures)

        res = req.json()['name']
        return render_template('base.html', output=res, item=True)


if __name__ == "__main__":
    app.run()
