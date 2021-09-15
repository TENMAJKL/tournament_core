from flask import *
from models.players import *
from models.teams import *
from models.middleware import *
from hashlib import sha256
from replit import db
from datetime import datetime

data = Blueprint("editbp", __name__)

@data.route("/data/", methods=["POST", "GET"])
def view():
	if verify(session):
		return render_template("data.html", users = getPlayers(), getUser = getPlayer)
	else:
		return redirect("/login")


@data.route("/data/add", methods=["POST", "GET"])
def add():
	if verify(session) and canCreate(session):
		error = "";
		if request.method == "POST":
			name = session["name"]
			player = request.form.get("name")
			if request.form.get("name") not in getPlayers():
				team = request.form.get("team")
				if team in getTeams():
					createEditPlayer(
						player,
						request.form.get("kills"),
						request.form.get("deaths"),
						request.form.get("assists"),
						team,
						request.form.get("id"),
						request.form.get("device")
					);
					print(f"{datetime.now()} -> {name} added {player} ", file=open("./log.txt", "w"))
				else:
					error = "This team is not in table!"
			else:
				error = "This name is allready in table!";
		return render_template("add_player.html", error=error)	
	else:
		return redirect("/data")


@data.route("/data/edit/<player>", methods=["POST", "GET"])
def edit(player):
	if verify(session) and canEdit(session):
		error = "";
		if request.method == "POST":
			if player in getPlayers():
				name=session["name"]
				createEditPlayer(
					player,
					request.form.get("kills"),
					request.form.get("deaths"),
					request.form.get("assists"),
					request.form.get("team"),
					request.form.get("id"),
					request.form.get("device")
				);
				print(f"{datetime.now()} -> {name} edited {player} ", file=open("./log.txt", "w"))
			else:
				error = "This name is not in table!";
		return render_template("edit_player.html", error=error, user=getPlayer(player), name=player)	
	else:
		return redirect("/")


@data.route("/data/delete/<player>", methods=["GET"])
def delete(player):
	if verify(session) and canEdit(session):
			if player in getPlayers():
				deletePlayer(player);
			return redirect("/data")
	else:
		return redirect("/")


@data.route("/data/tournament", methods=["GET", "POST"])
def tournament():
	if verify(session) and canEdit(session):
		if request.method == "POST":
			setRounds(request.form.get("rounds"));
		rounds = getRounds();
		return render_template("tournament.html", rounds=rounds)
	else:
		return redirect("/data")

@data.route("/data/tournament/delete", methods=["GET", "POST"])
def tournament_delete():
	if verify(session) and canEdit(session):
		db["players"] = {};
		return redirect("/data/tournament")
	else:
		return redirect("/")

@data.route("/data/tournament/download", methods=["GET", "POST"])
def tournament_download():
	if verify(session) and canEdit(session):
		print(dict(getPlayers()), file=open("./static/data.txt", "w"))

		return send_file("./static/data.txt", as_attachment=True)
	else:
		return redirect("/")

@data.route("/data/api/<token>/<name>", methods=["GET"])
def api(token, name):
	if sha256(token.encode('utf-8')).hexdigest() == "a2d2f98e84e0a28190b1855b1bcdd74ed351fed455497dca89fcbaee4dde1e43":
		if name in getPlayers():
			return jsonify({"responce":"sucess", "name" : name, "data":dict(getPlayer(name))})
		else:
			return jsonify({"responce": "not found"})
	else:
		return jsonify({"responce": "not authorized"})
