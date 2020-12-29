from flask import (
    Blueprint, flash, g, redirect, render_template, request, session, url_for
)
import yaml, os

bp = Blueprint('game', __name__, url_prefix='/game')

@bp.route('/play', methods=('GET', 'POST'))
def play():
	file = open(os.path.join (os.getcwd(),"purple\\items.yaml"),'r')
	data = yaml.safe_load(file)
	file.close()
	return (data)

@bp.route('/score', methods=('GET', 'POST'))
def score():
	if request.method == "POST":
		file = open(os.path.join (os.getcwd(),"purple\\items.yaml"),'r')
		data = yaml.safe_load(file)
		file.close()

		temp = data["List"]

		temp.append(request.form["Info"])

		data["List"] = temp
		
		file = open(os.path.join (os.getcwd(),"purple\\items.yaml"),'w')
		yaml.dump(data,file)
		file.close()
		
		return redirect(url_for('game.play'))
	else:
		return render_template('game/score.html')

