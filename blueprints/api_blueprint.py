from flask import Blueprint, jsonify
import time

# create a flask blueprint for me
api = Blueprint('api', __name__)

api_blueprint = Blueprint('api', __name__, url_prefix='/api')

@api_blueprint.route('/time')
def current_time():
	return jsonify({
		'time': time.time()
	})
	