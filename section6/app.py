from flask import Flask, jsonify
from flask_restful import  Api
from flask_jwt import JWT

from security import authenticate, identity
from resources.user import UserRegister
from resources.item import Item, ItemList

from datetime import timedelta

app = Flask(__name__)

app.secret_key = 'secreto'

api = Api(app)

app.config['JWT_AUTH_URL_RULE'] = '/login' #cambia el endpoint de /auth a /login
app.config['JWT_EXPIRATION_DELTA'] = timedelta(seconds=1800) #tiempo de expiracion del token
#app.config['JWT_AUTH_USERNAME_KEY'] = 'email' #cambia el autentication key name de username a email
jwt = JWT(app, authenticate, identity) #esto crea un endpoint /auth

@jwt.auth_response_handler
def customized_response_handler(access_token, identity):
    """Esto cambia la respuesta, por default solo devuelve el acces token, y ahora incluye el user_id"""
    return jsonify({
                        'access_token': access_token.decode('utf-8'),
                        'user_id': identity.id
                   })


api.add_resource(Item, '/item/<string:name>')
api.add_resource(ItemList, '/items')
api.add_resource(UserRegister, '/register')

if __name__ == '__main__':
    app.run(port=5000, debug=True)
