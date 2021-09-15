from flask import *
from models.middleware import *

home = Blueprint("homebp", __name__)

@home.route("/", methods=["POST", "GET"])
def main():
	if verify(session):
		manage = canManage(session);
		print(request.headers) 
		return render_template("home.html", name = session["name"], manage = manage);
	else:
		return redirect("/login");

@home.route("/core")
def core():
	return jsonify({"info":"Core, built for keep alive", "status":"online"})