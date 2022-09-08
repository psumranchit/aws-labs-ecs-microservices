from flask import Flask
from database import countries
from flask_cors import CORS, cross_origin

app = Flask(__name__)
cors = CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'

# return 200 for health check
@app.get('/')
def health_check():
    return '', 200

@app.route('/country-name/<name>')
def get_name(name):
    return countries[name]

if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0')