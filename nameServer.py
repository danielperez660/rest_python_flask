import random
from flask import Flask, jsonify, abort, request

app = Flask(__name__, static_url_path="")

figure_names_men = ['Albert Einstein', 'Abraham Lincoln', 'Franklin D. Roosevelt', 'Winston Churchill',
                    'George Washington', 'Mansa Musa', 'Mao Zedong']
figure_names_women = ['Queen Victoria', 'Jane Austen', 'Rosa Parks', 'Catherine the Great', 'Malala Yousafzai',
                      'Marie Curie', 'Rosalind Franklin', 'Margaret Thatcher']


@app.route('/figure/<string:gender>', methods=['GET'])
@app.route('/figure/', methods=['GET'])
def get_person(gender=None):
    if gender == 'male':
        return jsonify({'name': random.choice(figure_names_men), 'gender': 'male'})
    elif gender == 'female':
        return jsonify({'name': random.choice(figure_names_women), 'gender': 'female'})
    elif not gender:
        val = random.choice(figure_names_men + figure_names_women)
        return jsonify({'name': val, 'gender': ['male' if figure_names_women.count(val) == 0 else 'female']})
    else:
        abort(404, 'Unrecognised parameter')


@app.route('/figure/', methods=['POST'])
def post_figure():
    if request.json:
        if request.json['gender'] == 'female':

            if figure_names_women.count(request.json['name']) != 0:
                abort(403, 'Already contained')
            figure_names_women.append(request.json['name'])

        elif request.json['gender'] == 'male':

            if figure_names_men.count(request.json['name']) != 0:
                abort(403, 'Already contained')
            figure_names_men.append(request.json['name'])

    return 'Appended', 201


@app.route('/all_figures/', methods=['GET'])
def get_list():
    all_men_json = [{'name': item, 'gender': 'male'} for item in figure_names_men]
    all_women_json = [{'name': item, 'gender': 'female'} for item in figure_names_women]
    all_people = all_men_json + all_women_json
    return jsonify({'all_figures': all_people})


if __name__ == '__main__':
    app.run(port='9999')
