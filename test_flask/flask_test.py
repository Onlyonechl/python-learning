#!/usr/bin/env python3

import os, flask
from flask import Flask, request, redirect, url_for, render_template
from werkzeug import secure_filename

UPLOAD_FOLDER = '/path/to/the/uploads'
ALLOWED_EXTENSIONS = set(['txt','pdf','png','jpg','jpeg','gif'])

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1] in ALLOWED_EXTENSIONS

@app.route('/hello/')
@app.route('/hello/<name>/')
def hello(name=None):
	return render_template('hello.html', name = name)


@app.route('/login/', methods = ['POST','GET'])
def login():
	error = None
	if request.method == 'POST':
		if valid_login(request.form['username'],
					   request.form['password']):
			return log_the_usr_in(request.form['username'])
		else:
			error = 'Invalid username/password'
	# 当请求形式为“GET"或者认证失败则执行以下代码
	return render_template('login.html', error = error)

@app.route('/upload/', methods = ['GET','POST'])
def upload_file():
	if request.method == 'POST':
		f = request.files['the_file']
		if f and allowed_file(f.filename):
			filename = secure_filename(f.filename)
			f.save(os.path.join(app.config['UPLOAD_FOLDER'],filename))
			return redirect(url_for('upload',filename = filename))

	return '''
    <!doctype html>
    <title>Upload new File</title>
    <h1>Upload new File</h1>
    <form action="" method=post enctype=multipart/form-data>
      <p><input type=file name=file>
         <input type=submit value=Upload>
    </form>
    '''


if __name__ == '__main__':
	app.run(debug = True)