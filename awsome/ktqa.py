from flask import Flask,render_template,request,redirect,url_for,session
import config
from models import User,Question,Answer
from exts import db
from decorators import login_required

app = Flask(__name__)
app.config.from_object(config)
db.init_app(app)


@app.route('/')
def index():
	context = {
		'questions': Question.query.order_by('-create_time').all()
	}
	return render_template('index.html',**context)

@app.route('/login/',methods=['GET','POST'])
def login():
	if request.method =='GET':
		return render_template('login.html')
	else:
		telephone = request.form.get('telephone')
		password = request.form.get('password')
		user = User.query.filter(User.telephone == telephone, User.password == password).first()
		if user:
			session['user_id'] = user.id
			#如果想在31天内都不需要再登录
			session.permanent = True
			return redirect(url_for('index'))
		else:
			return '手机号码或密码错误，请核对后再登录！'

@app.route('/regist/',methods=['GET','POST'])
def regist():
	if request.method =='GET':
		return render_template('regist.html')
	else:
		telephone = request.form.get('telephone')
		username = request.form.get('username')
		password1 = request.form.get('password1')
		password2 = request.form.get('password2')

		#手机号码验证，如果被注册了，就不能注册了
		user = User.query.filter(User.telephone == telephone).first()
		if user:
			return "该手机号码已被注册，请更换手机号码！"
		else:
			# password1要和password2相等才可以
			if password1 != password2:
				return "两次输入的密码不一致！"
			else:
				user = User(telephone=telephone,username=username,password=password1)
				db.session.add(user)
				db.session.commit()
				# 如果注册成功，则跳转到登录页面
			return redirect(url_for('login'))

@app.route('/logout/')
def logout():
	# session.pop(user.id)
	# del session['user_id']
	session.clear()
	return redirect(url_for('login'))

@app.route('/question/',methods=['GET','POST'])
@login_required
def question():
	if request.method == 'GET':
		return render_template('question.html')
	else:
		title = request.form.get('title')
		content = request.form.get('content')
		question = Question(title=title,content=content)
		user_id = session.get('user_id')
		user = User.query.filter(User.id == user_id).first()
		question.author = user
		db.session.add(question)
		db.session.commit()
		return redirect(url_for('index'))

@app.route('/detail/<question_id>/')
def detail(question_id):
	question_model = Question.query.filter(Question.id == question_id).first()
	return render_template('detail.html',question=question_model)

@app.route('/add_answer/',methods=['POST'])
@login_required
def add_answer():
	content = request.form.get('answer_content')
	question_id = request.form.get('question_id')
	answer = Answer(content=content)
	user_id = session['user_id']
	user = User.query.filter(User.id == user_id).first()
	answer.author = user
	question = Question.query.filter(Question.id == question_id).first()
	answer.question = question
	db.session.add(answer)
	db.session.commit()
	return redirect(url_for('detail',question_id=question_id))

@app.context_processor
def my_context_processor():
	user_id = session.get('user_id')
	if user_id:
		user = User.query.filter(User.id == user_id).first()
		if user:
			return {'user':user}
	else:
		return {}

if __name__ =='__main__':
	app.run()
