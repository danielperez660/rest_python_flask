import random

import xmltodict
from flask import Flask, render_template, request
import requests

app = Flask(__name__)

# Sets up the initial URLs for my API and the other 2
REST_FIGURES = 'http://localhost:9999/figure'
REST_BOOKS = 'https://www.goodreads.com/search/index.xml'
REST_TODAY = 'http://history.muffinlabs.com/date'

GOOD_READS_KEY = 'kasyZkeIPzsma2EBH0Lu9w'


# Route setup for default home page
@app.route("/")
def hello():
    return render_template('base.html', output="", item=False, error=False, msg="")


# Form management route where data is requested from my api
@app.route('/', methods=['POST'])
def my_form_post():
    query = REST_FIGURES
    if request.form['submit_button'] == 'clear':
        return render_template('base.html', output="", item=False, error=False, msg="")
    else:
        if 'gender' in request.form:
            gender = request.form['gender']
            query += gender + '/'

        if request.form['continent'] != "":
            continent = request.form['continent']
            query += continent.lower() + '/'

        resp = requests.get(query)

        # Error handling if the response does not have expected content
        if 'name' in str(resp.content) and 'continent' in str(resp.content):
            name = resp.json()['name']
            continent = resp.json()['continent']
        else:
            return render_template('base.html', name="", continent="", item=False,
                                   error=True, msg=resp.reason)

        # Requests data from the other apis
        book_name, book_auth, image_url, year = get_books(name)
        event = today_in_history(year)

        return render_template('base.html', name=name, continent=continent, item=True,
                               error=False, msg="", url=image_url, book_name=book_name, book_auth=book_auth, year=year,
                               event=event)

# Gets xml file from good reads and parses it for relevant data
def get_books(query):
    payload = {'q': query, 'key': GOOD_READS_KEY}
    resp = requests.get(REST_BOOKS, params=payload)

    doc = xmltodict.parse(resp.text)
    works = doc['GoodreadsResponse']['search']['results']['work']

    output = random.choice(works)

    try:
        year = output['original_publication_year']['#text']
    except:
        year = 2000

    return output['best_book']['title'], output['best_book']['author']['name'], \
           output['best_book']['image_url'], year


# Gets data from today in history as a JSON file and finds relevant data
def today_in_history(year):
    resp = requests.get(REST_TODAY)
    resp_data = resp.json()['data']
    temp = []

    year = int(year)

    for i in resp_data['Events']:
        if year - 5 <= int(i['year']) <= year + 5:
            temp.append(i['text'] + " (" + i['year'] + ")")
    output = random.choice(temp)

    # There was no event recorded for this given range of years, returns a default
    if output == "":
        'Probably nothing of value. Who knows...'
    else:
        return output


if __name__ == "__main__":
    app.run()
