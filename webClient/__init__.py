from flask import Flask, render_template, request
import requests

app = Flask(__name__)

REST_FIGURES = 'http://localhost:9999/figure'


@app.route("/")
def hello():
    return render_template('base.html', output="", item=False, error=False, msg="")


@app.route('/', methods=['POST'])
def my_form_post():
    # text = request.form['inputText']
    query = REST_FIGURES
    if request.form['submit_button'] == 'clear':
        return render_template('base.html', output="", item=False, error=False, msg="")
    else:
        if 'gender' in request.form:
            gender = request.form['gender']
            query += gender + '/'

        if request.form['continent'] != "":
            continent = request.form['continent']
            query +=  continent.lower() + '/'

        req = requests.get(query)

        if 'name' in str(req.content) and 'continent' in str(req.content):
            name = req.json()['name']
            continent = req.json()['continent']
        else:
            return render_template('base.html', name="", continent="", item=False,
                                   error=True, msg=req.reason)

        return render_template('base.html', name=name, continent=continent, item=True,
                               error=False, msg="")


if __name__ == "__main__":
    app.run()
