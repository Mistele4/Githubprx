from flask import Flask
from blueprints.api_blueprint import api_blueprint

app = Flask(__name__)
app.register_blueprint(api_blueprint)

@app.route('/')
def index():
    return '<h1>First Flask App</h1>'


if __name__ == '__main__':
    app.run(debug = True, port=3000)