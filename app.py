# Author: Michael Hawes
# 2 March 2017

import os
from flask import Flask, render_template, request, redirect, url_for, session


app = Flask(__name__)
app.config['SECRET_KEY'] = 'F34TF$($e34D'


@app.route('/', methods=['GET', 'POST'])
def index():
    return "Hello"




if __name__ == '__main__':
    PORT = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=PORT, debug=True)
