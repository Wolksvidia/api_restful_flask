from werkzeug.security import safe_str_cmp
from user import User

users =[
    User(1, 'admin', '1234')
]

#la mapping al username y al uid se realiza para no tener que iterar la lista de usuarios
username_mapping = {u.username: u for u in users}

userid_mapping = {u.id: u for u in users}

def authenticate(username, password):
    user = username_mapping.get(username, None)
    if user and safe_str_cmp(user.password, password): #no es recomentdado comoparar strings con ==, se utiliza safe_str_cmp
        return user

def identity(payload):
    user_id = payload['identity']
    return userid_mapping.get(user_id, None)
