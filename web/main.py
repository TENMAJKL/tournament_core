from flask import *
from replit import db
from blueprints import home, auth, data, teams
app = Flask(__name__)
app.config["SECRET_KEY"] = "xzTBvOtV3nkGLAMmQZqsXPECbRgpeldruhjNI24fWD759JFyw0"
app.register_blueprint(home.home)
app.register_blueprint(auth.auth)
app.register_blueprint(data.data)
app.register_blueprint(teams.teams)

app.run(host='0.0.0.0', port=5000)

"""
Basic shell for adding to db
while True:
	command = input("$ ").split(" ")


	if (command[0] == "del"):
		del db[command[1]][command[2]]
	elif (command[0] == "add"):
		db[command[1]][command[2]]
"""

