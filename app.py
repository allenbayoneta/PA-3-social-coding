from flask import Flask, jsonify, render_template
from api import get_location


app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/get_location', methods=['GET'])
def get_location_route():
    location_data = get_location()
    return jsonify(location_data)

if __name__ == '__main__':
    app.run(debug=True)
