import random
from flask import Flask, jsonify, abort, request

app = Flask(__name__, static_url_path="")

continents = ['europe', 'asia', 'africa', 'north america', 'south america', 'australia']

male_figures = [{'name': 'Albert Einstein', 'gender': 'male', 'continent': 'europe'},
                {'name': 'Winston Churchill', 'gender': 'male', 'continent': 'europe'},
                {'name': 'Mansa Musa', 'gender': 'male', 'continent': 'africa'},
                {'name': 'Haile Selassie', 'gender': 'male', 'continent': 'africa'},
                {'name': 'Mao Zedong', 'gender': 'male', 'continent': 'asia'},
                {'name': 'Saddam Hussein', 'gender': 'male', 'continent': 'asia'},
                {'name': 'Abraham Lincoln', 'gender': 'male', 'continent': 'north america'},
                {'name': 'Mark Twain', 'gender': 'male', 'continent': 'north america'},
                {'name': 'Che Guevara', 'gender': 'male', 'continent': 'south america'},
                {'name': 'Simon Bolivar', 'gender': 'male', 'continent': 'south america'},
                {'name': 'Hugh Jackman', 'gender': 'male', 'continent': 'australia'},
                {'name': 'Steve Irwin', 'gender': 'male', 'continent': 'australia'}]

female_figures = [{'name': 'Alfonsina Storni', 'gender': 'female', 'continent': 'south america'},
                  {'name': 'Isabel Allende', 'gender': 'female', 'continent': 'south america'},
                  {'name': 'Marlyn Monroe', 'gender': 'female', 'continent': 'north america'},
                  {'name': 'Rosa Parks', 'gender': 'female', 'continent': 'north america'},
                  {'name': 'Wu Zetian', 'gender': 'female', 'continent': 'asia'},
                  {'name': 'Malala Yousafzai', 'gender': 'female', 'continent': 'asia'},
                  {'name': 'Yennenga', 'gender': 'female', 'continent': 'africa'},
                  {'name': 'Miriam Makeba', 'gender': 'female', 'continent': 'africa'},
                  {'name': 'Queen Victoria', 'gender': 'female', 'continent': 'europe'},
                  {'name': 'Catherine the Great', 'gender': 'female', 'continent': 'europe'},
                  {'name': 'Evelyn Scott', 'gender': 'female', 'continent': 'australia'},
                  {'name': 'Edith Cowan', 'gender': 'female', 'continent': 'australia'}]


@app.route('/figure/<string:gender>/<continent>/', methods=['GET'])
@app.route('/figure/<string:gender>/', methods=['GET'])
@app.route('/figure/', methods=['GET'])
def get_person(gender=None, continent=None):

    if gender == 'male':
        temp = []
        if continent and continent in continents:
            for i in male_figures:
                if i['continent'] == continent:
                    temp.append(i)
        elif continent and continent not in continents:
            return 'Unrecognised parameter', 404
        else:
            temp = male_figures.copy()
        return jsonify(random.choice(temp))

    elif gender == 'female':
        temp = []
        if continent and continent in continents:
            for i in female_figures:
                if i['continent'] == continent:
                    temp.append(i)
        elif continent and continent not in continents:
            return 'Unrecognised parameter', 404
        else:
            temp = female_figures.copy()
        return jsonify(random.choice(temp))
    elif not gender:
        return jsonify(random.choice(male_figures+female_figures))
    else:
        return 'Unrecognised parameter', 404


@app.route('/all_figures/', methods=['GET'])
def get_list():
    return jsonify(male_figures+female_figures)


if __name__ == '__main__':
    app.run(port='9999')
