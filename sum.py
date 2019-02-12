#!/usr/bin/env python3

import flask

app = flask.Flask(__name__)

@app.route('/sum/<int:a>/<int:b>/')
def sum(a,b):
	return 'sum : %d' % (a+b)

if __name__ == '__main__':
	app.debug = True
	app.run()