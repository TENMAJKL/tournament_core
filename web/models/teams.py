from replit import db
from models.players import *

def getTeam(name):
    return db["teams"][name];

def getTeamMembers(name):
	players = [];
	for player in dict(getPlayers()).keys():
		if getPlayer(player)["Team"] == name:
			players.append({"name":player, "data":dict(getPlayer(player))})
	return players

def createEditTeam(name, wins, loses):
	if wins != None:
		wins = int(wins)
	else:
		wins = 1;
	if loses != None:
		loses = int(loses)
	else:
		loses = 1;
	if loses <= 0:
		loses = 1
	
	if wins <=0:
		wins = 1;


	db["teams"][name] = {
		"wins" : wins,
		"loses" : loses,
		"wl" : str(wins/loses)
	}


def getTeams():
	return db["teams"];

def deleteTeam(name):
	del db["teams"][name];