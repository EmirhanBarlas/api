import random
from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/random_number', methods=['GET'])
def get_random_number():
    number = random.randint(1, 100)
    return jsonify({'number': number})

if __name__ == '__main__':
    app.run()
