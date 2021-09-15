from models.auth import getUser

def verify(session):
	if "name" in session:
		if getUser(session["name"])["active"]:
			return True;
		else:
			session["name"] = ""

def canEdit(session):
    if getUser(session["name"])["edit_perm"]:
        return True;
    else:
        return False;

def canCreate(session):
    if getUser(session["name"])["create_perm"]:
        return True;
    else:
        return False;


def canManage(session):
    if getUser(session["name"])["auth_perm"]:
        return True;
    else:
        return False;