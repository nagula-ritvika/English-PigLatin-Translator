#__author__ = ritvikareddy2
#__date__ = 2019-02-25

import pig_latin_translator

import logging
from flask import Flask, render_template, request, jsonify

app = Flask(__name__)


# check if the given input is empty
def is_input_empty(input_x):
    return input_x == ' ' or input_x == ''


# create json message to handle GET queries
def send_message(result):
    data = {'translated_string': result,
            }
    resp = jsonify(data)
    resp.status_code = 200

    return resp


@app.route('/')
def home():
    return render_template('index.html')


@app.route('/pig-latin-translator', methods=['GET', 'POST'])
def translate():
    logging.info("someone hit the base endpoint")

    if request.method == 'GET':
        if 'string' in request.args:
            input_sentence = request.args.get('string')
            if is_input_empty(input_sentence):
                return render_template('translator.html', empty_input=True)

            # slice the input to get rid of extra quotes used to pass in the value
            input_sentence = input_sentence[1:-1]
            pig_latin_string = pig_latin_translator.get_translated_string(input_sentence)
            resp = send_message(pig_latin_string)

            return resp
        else:
            return render_template('translator.html')

    else:
        input_sentence = request.form['english_string']
        if is_input_empty(input_sentence):
            return render_template('translator.html', empty_input=True)

        pig_latin_string = pig_latin_translator.get_translated_string(input_sentence)

        return render_template('translator.html', pig_latin_string=pig_latin_string)


if __name__ == '__main__':
    app.run(debug=True)
