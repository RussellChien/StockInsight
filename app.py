from flask import Flask, render_template, jsonify
import json, csv
import pandas as pd

app = Flask(__name__)

@app.route('/')
def main():
    title = 'Employee SaaStifaction'
    return render_template('test.html', title=title)

@app.route('/data')
def data():
    with open('data/example.json', 'r') as f:
        data = json.load(f)
    return jsonify(data)

if __name__ == '__main__':
    app.run(host='localhost', port=9874, debug=True)