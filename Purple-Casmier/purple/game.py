from flask import (
    Blueprint, flash, g, redirect, render_template, request, session, url_for
)
import yaml, os, random

from purple.PygameFoodGame.Pygame_Food_Game import PlayGame

from time import localtime

def retrieve_time():
    return f"{localtime()[0]}-{localtime()[1]}-{localtime()[2]}"

bp = Blueprint('game', __name__, url_prefix='/')

@bp.route('/play', methods=('GET', 'POST'))
def play():
	if request.method == "POST":
		session['score'] = PlayGame()
		
		return redirect(url_for('game.submit'))
	else:
		return render_template('play.html',mode=0)

@bp.route('/submit', methods=('GET', 'POST'))
def submit():
	if request.method == "POST":
		file = open(os.path.join (os.getcwd(),"purple\\items.yaml"),'r')
		data = yaml.safe_load(file)
		file.close()

		if data["List"] == None:
			temp = []
		else:
			temp = data["List"]

		temp.append([ request.form["USERNAME"], int(request.form["SCORE"]), retrieve_time()])

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
