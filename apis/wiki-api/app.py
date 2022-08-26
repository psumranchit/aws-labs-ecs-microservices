from flask import Flask
from database import countries

app = Flask(__name__)

# return 200 for health check
@app.get('/')
def health_check():
    return '', 200

@app.route('/wiki/<name>')
def get_year(name):
    return str(countries[name]['wiki'])

if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0')