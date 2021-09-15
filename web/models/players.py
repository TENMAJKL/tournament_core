from replit import db

def getPlayer(name):
    return db["players"][name];

def createEditPlayer(name, Kills, Deaths, Assists, team, id, device):

	Kills = float(Kills) if Kills != "" else 1;
	Deaths = float(Deaths) if Deaths != "" else 1;
	Assists = float(Assists) if Assists != "" else 1;

	AKPR = 0.716;
	ASPR = 0.291
	MKPR = 1.3

	rounds = float(getRounds());
	KD = Kills / Deaths;
	KPR = Kills / rounds;
	DPR = Deaths/ rounds;
	SR = (rounds - Deaths)/rounds/ASPR;
	KR = KPR/AKPR; 
	SLR = (KR+0.7 * SR +MKPR + (Assists/10/rounds))/2.7


	db["players"][name] = {
		"Team": team,
		"Kills" : str(Kills), 
		"Deaths" : str(Deaths), 
		"Assists" : str(round(Assists, 3)), 
        "KD" : str(round(KD, 3)), 
        "KPR" : str(round(KPR, 3)), 
        "DPR" : str(round(DPR, 3)), 
        "SVR" : str(round(SR, 3)), 
        "SLR" : str(round(SLR, 3)),
		"id": id,
		"device" : device
        };


def getPlayers():
	return db["players"];

def deletePlayer(name):
	del db["players"][name];

def setRounds(rounds):
	if int(rounds) <= 0:
		db["rounds"] = 1;
	else:
		db["rounds"] = int(rounds);

def getRounds():
	return db["rounds"];


