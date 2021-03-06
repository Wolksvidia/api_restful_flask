from flask_restful import Resource, reqparse
from flask_jwt_extended import (
    create_access_token,
    create_refresh_token,
    jwt_refresh_token_required,
    get_jwt_identity,
    jwt_required,
    get_raw_jwt
    )
from werkzeug.security import safe_str_cmp
from models.user import UserModel
from blacklist import BLACKLIST

def _parser():
    parser = reqparse.RequestParser()
    parser.add_argument('username',
        type=str,
        required=True,
        help='Username requerido'
        )
    parser.add_argument('password',
        type=str,
        required=True,
        help='Password requerida'
        )
    return parser.parse_args()


class UserRegister(Resource):

    def post(self):
        data = _parser()
       
        if UserModel.find_by_username(data['username']):
            return {'message': 'El usuario ya existe'}, 400

        user = UserModel(**data)#data es un diccionario como si fuera **kwargs

        user.save()
        
        return {'message': 'Usuario creado con exito'}, 201


class User(Resource):
    @classmethod
    def get(cls, user_id):
        user = UserModel.find_by_id(user_id)
        if not user:
            return {'message': 'User not found'}, 404
        return user.json()

    @classmethod
    def delete(cls, user_id):
        user = UserModel.find_by_id(user_id)
        if user:
            user.delete()
            return {'message': 'User delete'}
        return {'message': 'User not found'}, 404


class UserLogin(Resource):

    @classmethod
    def post(self):
        #get data from de parser
        data = _parser()
        #find user in db
        user = UserModel.find_by_username(data['username'])
        #check password
        if user and safe_str_cmp(user.password, data['password']):
            access_token = create_access_token(identity=user.id, fresh=True)#create access token
            refresh_token = create_refresh_token(user.id)#create a refresh token 
            return {
                'user_id': user.id,
                'access_token': access_token,
                'refresh_token': refresh_token
            }, 200
        return {'message': 'Invalid credentials'}, 401


class UserLogout(Resource):
    @jwt_required
    def post(self):
        jti = get_raw_jwt()['jti'] #jti es "JWT ID" un identificador para un JWT
        BLACKLIST.add(jti)
        return {'message': 'Successfully logged out'}, 200


class TokenRefresh(Resource):
    """Al momento del login se genera un toke fresh... pasado el tiempo para meantener el login 
    se va generando un nuevo accesss token como "no fresh", para determinadas acciones es necesario un token 
    fresh que valide que es el usuario, por lo cual se le solicita que se loguee nuevamente"""
    @jwt_refresh_token_required
    def post(self):
        current_user = get_jwt_identity()
        new_token = create_access_token(identity=current_user, fresh=False)
        return {
                'access_token': new_token
            }, 200
