from flask import Flask, request
from database import countries

app = Flask(__name__)

# return 200 for health check
@app.get('/')
def health_check():
    return '', 200

@app.get('/country-list')
def list_all():
    less_than = request.args.get('lt') or '2000000000'
    greater_than = request.args.get('gt') or '0'
    qualifying_data = list(
        filter(
            lambda pl: int(less_than) >= pl['population'] >= int(greater_than),
            countries.values()
        )
    )
    return {"countries": qualifying_data}

if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0')