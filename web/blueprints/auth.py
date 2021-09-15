from flask import *
from models.middleware import *
from models.auth import *
from hashlib import sha256
import random

auth = Blueprint("loginbp", __name__)

password_string = "qwertyuiopasdfghjklzxcvbnm741085293"

@auth.route("/login/", methods=["POST", "GET"])
def login():
	if not verify(session):
		error = "";
		if request.method == "POST":
			name = request.form.get("name");
			password = sha256(request.form.get("password").encode('utf-8')).hexdigest();
			if name in getUsers():
				user = getUser(name);
				if user["password"] == password:
					session["name"] = name;
					return redirect("/");
				else:
					error = "Wrong username or password!";
			else:
				error = "Wrong username or password!";

		return render_template("login.html", error=error);
	else:
		return redirect("/");

@auth.route("/admin/", methods=["POST", "GET"])
def admin():
    if verify(session) and canManage(session):
        users = getUsers();
        
        return render_template("admin.html", users = users);
    else:
        return redirect("/");

@auth.route("/admin/add", methods=["POST", "GET"])
def add():
	if verify(session) and canManage(session):
		action = "Add user";
		password = "";
		if request.method == "POST":
			print(request.form)
			visible = False;
			edit = False;
			add = False;
			manage = False;

			name = request.form.get("name");

			if request.form.get("visible"):
				visible = True;

			if request.form.get("edit"):
				edit = True;
			
			if  request.form.get("add"):
				add = True;
			
			if request.form.get("manage"):
				manage = True;

			password = "".join(random.sample(password_string, 15));

			if name not in getUsers():
				createEditUser(name, sha256(password.encode('utf-8')).hexdigest(), visible, edit, add, manage);

				password = "Password of " + name + " is " + password;
			else:
				password = "This name is allready taken!"

		return render_template("add_user.html", action = action, password = password );
	else:
		return redirect("/");


@auth.route("/admin/edit/<user>/", methods=["GET", "POST"])
def edit(user):
	if verify(session) and canManage(session) and user != session["name"] and user != "root" and user in getUsers():
		action = "Editing " + user;
		password = "";
		if request.method == "POST":
			visible = False;
			edit = False;
			add = False;
			manage = False;

			if request.form.get("visible"):
				visible = True;

			if request.form.get("edit"):
				edit = True;
			
			if  request.form.get("add"):
				add = True;
			
			if request.form.get("manage"):
				manage = True;

			password = getUser(user)["password"];

			if user in getUsers():
				createEditUser(user, password, visible, edit, add, manage);
		check = {True: "checked", False: ""}
		return render_template("edit_user.html", action = action, user=getUser(user), name=user, check=check);
	else:
		return redirect("/");

@auth.route("/logout")
def logout():
	if verify(session):
		del session["name"]
		return redirect ("/login")
	else:
		return redirect("/login")


@auth.route("/change-password", methods=["POST", "GET"])
def changePassword():
	if verify(session):
		error = "";
		if request.method == "POST":
			old = sha256(request.form.get("old").encode("utf-8")).hexdigest()
			new = request.form.get("new");
			old_db = getUser(session["name"])["password"]
			user = getUser(session["name"])
			if old == old_db:
				password = sha256(new.encode("utf-8")).hexdigest(); 
				createEditUser(session["name"], password, user["active"], user["create_perm"], user["edit_perm"], user["auth_perm"])
				return redirect("/")
			else:
				error = "Old password is wrong!"
		return render_template("change_password.html", error = error)
	else:
		return redirect("/login")

@auth.route("/admin/delete/<user>", methods=["GET"])
def delete(user):
	if verify(session) and canManage(session):
			if user in getUsers() and user != session["name"] and user != "root":
				deleteUser(user);
			return redirect("/admin")
	else:
		return redirect("/")

#root  n1LafkYeEw 