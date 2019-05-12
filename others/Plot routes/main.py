from flask import Flask, render_template, request, redirect, url_for
import os
import json
from load import resultgeo_Json

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('main.html', data = resultgeo_Json())

if __name__ == '__main__':
    app.run(host='127.0.0.1', port=8075, debug=True)