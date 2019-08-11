from flask import Flask
from flask_cors import CORS, cross_origin

import os, sys
sys.path.append(os.path.join(os.path.dirname(__file__), "../../"))

from src.regression.simple_linear_regression import simple_linear_regression
from src.regression.multiple_linear_regression import multiple_linear_regression
app = Flask(__name__)
cors = CORS(app)


@app.route('/')
def hello_world():
    return 'Hello World!'


@app.route('/simple_linear_regression')
def simple_linear_regression_test():
    graphs = simple_linear_regression.execute()
    return { 'data': graphs }

@app.route('/multiple_linear_regression')
def multiple_linear_regression_test():
    graphs = multiple_linear_regression.execute()
    return { 'data': graphs }

if __name__ == '__main__':
    app.run()
