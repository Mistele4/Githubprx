from flask import Blueprint, jsonify
import time
import random


# create a flask blueprint for me
api = Blueprint('api', __name__)

api_blueprint = Blueprint('api', __name__, url_prefix='/api')

@api_blueprint.route('/time')
def current_time():
	return jsonify({
		'time': time.time()
	})


@api_blueprint.route('/some-word')
def some_word():

	words = ['apple', 'cat', 'dog', 'banana', 'hello', 'world']
	# get a random word from the list
	random_word = random.choice(words)

	return jsonify({
		'word': random_word
	})
	