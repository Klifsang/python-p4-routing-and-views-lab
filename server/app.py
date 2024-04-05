#!/usr/bin/env python3

from flask import Flask, request
import sys

app = Flask(__name__)

@app.route('/')
def index():
    return '<h1>Python Operations with Flask Routing and Views</h1>'

@app.route('/print/<parameter>')
def print_param(parameter):
    print(parameter, file=sys.stdout)
    return parameter

@app.route('/count/<int:parameter>')
def count(parameter):
    return '\n'.join(str(i) for i in range(parameter)) + '\n'

@app.route('/math/<int:num1>/<op>/<int:num2>')
def math(num1, op, num2):
    if op == '+':
        return str(num1 + num2)
    elif op == '-':
        return str(num1 - num2)
    elif op == '*':
        return str(num1 * num2)
    elif op == 'div':
        return str(num1 / num2)
    elif op == '%':
        return str(num1 % num2)

if __name__ == '__main__':
    app.run(port=5555, debug=True)
