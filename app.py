from flask import Flask, render_template
from blueprints.api_blueprint import api_blueprint
import time
import requests
import json

# create a flask app
app = Flask(__name__, template_folder='templates')

# register the blueprint
app.register_blueprint(api_blueprint)

# defind the landing page
@app.route('/')
def index():

    response = requests.get('http://localhost:3000/api/some-word')
    data = response.json()
    print('the data we got from the server is: ', data)
    word = data['word']

    return render_template('index.html', current_time=time.time(), magic_word=word)


if __name__ == '__main__':
    app.run(debug = True, port=3000)