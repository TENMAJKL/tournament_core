from flask import *
from models.teams import *
from models.middleware import *
from hashlib import sha256
from replit import db

teams = Blueprint("teamsbp", __name__)

@teams.route("/clans", methods=["POST", "GET"])
def view():
	if verify(session):
		return render_template("clans.html", clans = getTeams(), getClan = getTeam)
	else:
		return redirect("/login")


@teams.route("/clans/add", methods=["POST", "GET"])
def add():
	if verify(session) and canCreate(session):
		error = "";
		if request.method == "POST":
			if request.form.get("name") not in getTeams():
				createEditTeam(
					request.form.get("name"),
					request.form.get("wins"),
					request.form.get("loses"),
				);
			else:
				error = "This clan is allready in table!";
		return render_template("add_clan.html", error=error)	
	else:
		return redirect("/")


@teams.route("/clans/edit/<clan>", methods=["POST", "GET"])
def edit(clan):
	if verify(session) and canEdit(session):
		error = "";
		if request.method == "POST":
			if clan in getTeams():
				createEditTeam(
					clan,
					request.form.get("wins"),
					request.form.get("loses"),
				);
			else:
				error = "This clan is not in table!";
		return render_template("edit_clan.html", error=error, clan=getTeam(clan), name=clan)	
	else:
		return redirect("/")


@teams.route("/clans/delete/<clan>")
def delete(clan):
	if verify(session) and canEdit(session):
		if clan in getTeams():
			deleteTeam(clan)
		return redirect("/clans")
	else:
		return redirect("/")


@teams.route("/clans/api/<token>/<name>", methods=["GET"])
def api(token, name):
	if sha256(token.encode('utf-8')).hexdigest() == "a2d2f98e84e0a28190b1855b1bcdd74ed351fed455497dca89fcbaee4dde1e43":
		if name in getTeams():
			return jsonify({"responce":"sucess", "name":name, "data":dict(getTeam(name)), "players":getTeamMembers(name)})
		else:
			return jsonify({"responce": "not found"})
	else:
		return jsonify({"responce": "not authorized"})