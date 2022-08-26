from flask import Flask
from database import countries

app = Flask(__name__)

# return 200 for health check
@app.get('/')
def health_check():
    return '', 200

@app.route('/pop/<name>')
def get_contribution(name):
    return str(countries[name]['population'])
if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0')