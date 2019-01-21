from flask import Flask, jsonify
from flask_restful import  Api
from flask_jwt_extended import JWTManager

from resources.user import UserRegister, User, UserLogin, TokenRefresh, UserLogout
from resources.item import Item, ItemList
from resources.store import Store, StoreList

from blacklist import BLACKLIST
from datetime import timedelta

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///data.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['PROPAGATE_EXCEPNCIONS'] = True #para que los complementos puedan propagar sus errores
app.secret_key = 'secreto' #se puede usar tambien app.config['JWT_SECRET_KEY']

##BLACKLIST configs
app.config['JWT_BLACKLIST_ENABLED'] = True
app.config['JWT_BLACKLIST_TOKEN_CHECKS'] = ['access', 'refresh']

api = Api(app)

@app.before_first_request
def create_tables():
    db.create_all()

jwt = JWTManager(app)

########### modificacion de respuestas de jwt ################

@jwt.user_claims_loader
#agrega contenido, util para armar jerarquia de permisos
def add_claim_to_jwt(identity):
    if identity == 1: #Esto esta hard-code
        return {'is_admin': True}
    return {'is_admin': False}

@jwt.token_in_blacklist_loader
#la funcion debuelve true si el token esta en la blcklist
def check_if_token_in_blacklist(decrypted_token):
    return decrypted_token['jti'] in BLACKLIST

@jwt.expired_token_loader
#modifica la respuesta cuando el token expiro
def expired_token_callback():
    return jsonify({
        'description': 'El token expiro!',
        'error': 'token_expered'
    }), 401

@jwt.invalid_token_loader
#cuando el token es invalido
def invalid_token_callback(error):
    return jsonify({
        'description': 'Signature verification failed',
        'erro': 'invalid_token'
    }), 401

@jwt.unauthorized_loader
#cuando el no se envia un token
def missing_token_callback():
    return jsonify({
        'description': 'Request does not contain an access token',
        'erro': 'authorization_required'
    }), 401

@jwt.needs_fresh_token_loader
#cuando se envia un non fresh token
def token_nonfresh_callback():
    return jsonify({
        'description': 'The token is not fresh',
        'erro': 'fresh_token_required'
    }), 401

@jwt.revoked_token_loader
#cuando se invalida un token, mediante log out...
def revoked_token_callback():
    return jsonify({
        'description': 'The token has been revoked',
        'erro': 'token_revoked'
    }), 401

###############################################################

api.add_resource(Item, '/item/<string:name>')
api.add_resource(ItemList, '/items')
api.add_resource(UserLogin, '/login')
api.add_resource(UserLogout, '/logout')
api.add_resource(TokenRefresh, '/refresh')
api.add_resource(User, '/user/<int:user_id>')
api.add_resource(UserRegister, '/register')
api.add_resource(Store, '/store/<string:name>')
api.add_resource(StoreList, '/stores')

if __name__ == '__main__':
    from db import db
    #se importa aca para evitar una importacion circular debido a que tambien se importa en los modelos
    db.init_app(app)
    app.run(port=5000, debug=True)
