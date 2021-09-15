from replit import db

"""
Returns data about user 

"""
def getUser(name):
    return db["auth"][name];

def createEditUser(name, password, active, edit_perm, create_perm, auth_perm):
    db["auth"][name] = {
        "password" : password,
        "active" : active,
        "edit_perm" : edit_perm,
        "create_perm" : create_perm,
        "auth_perm" : auth_perm
    };


def getUsers():
    return db["auth"].keys();


def deleteUser(name):
	del db["auth"][name];