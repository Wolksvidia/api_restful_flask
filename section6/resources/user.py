from flask_restful import Resource, reqparse
from models.user import UserModel

class UserRegister(Resource):
    @staticmethod
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

    def post(self):
        data = UserRegister._parser()
       
        if UserModel.find_by_username(data['username']):
            return {'message': 'El usuario ya existe'}, 400

        #user = UserModel(None, data['username'], data['password'])
        user = UserModel(**data)#data es un diccionario como si fuera **kwargs

        user.save()
        
        return {'message': 'Usuario creado con exito'}, 201