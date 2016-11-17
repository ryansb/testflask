#!/usr/bin/env python3
from flask import Flask, render_template, jsonify

app = Flask('hello-flask')

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/test')
def test():
    return jsonify({'hello': 'world'})

if __name__ == '__main__':
    app.run('localhost')
