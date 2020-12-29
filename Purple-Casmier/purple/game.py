from flask import (
    Blueprint, flash, g, redirect, render_template, request, session, url_for
)
import yaml, os, random

bp = Blueprint('game', __name__, url_prefix='/')

@bp.route('/play', methods=('GET', 'POST'))
def play():
	if request.method == "POST":
		session['score'] = random.randint(1,10)
		
		return redirect(url_for('game.submit'))
	else:
		return render_template('play.html',mode=0)

@bp.route('/submit', methods=('GET', 'POST'))
def submit():
	if request.method == "POST":
		file = open(os.path.join (os.getcwd(),"purple\\items.yaml"),'r')
		data = yaml.safe_load(file)
		file.close()

		temp = data["List"]

		temp.append(int(request.form["Info"]))

		data["List"] = temp
			
		file = open(os.path.join (os.getcwd(),"purple\\items.yaml"),'w')
		yaml.dump(data,file)
		file.close()

		session.clear()

		return redirect(url_for('game.score'))

	else:
		return render_template('play.html',mode=1)

@bp.route('/score', methods=('GET', 'POST'))
def score():
	file = open(os.path.join (os.getcwd(),"purple\\items.yaml"),'r')
	data = yaml.safe_load(file)
	file.close()
	return render_template('score.html',data=data)

@bp.route('/about', methods=('GET', 'POST'))
def about():
	return render_template('aboutus.html')
