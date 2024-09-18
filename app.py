from flask import Flask, render_template, jsonify, request
import requests

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/get_quote', methods=['GET'])
def get_quote():
    # response = requests.get('https://api.quotable.io/random')
    response = requests.get('https://api.quotable.io/random', verify=False)
    if response.status_code == 200:
        data = response.json()
        return jsonify({
            'content': data['content'],
            'author': data['author']
        })
    else:
        return jsonify({'error': 'Could not fetch quote'}), 500


if __name__ == '__main__':
    app.run(debug=True)
