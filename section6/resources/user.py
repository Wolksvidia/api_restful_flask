import sqlite3
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
        
        connection = sqlite3.connect('data.db')
        cursor = connection.cursor()
        query = 'INSERT INTO users VALUES (NULL, ?, ?)'
        cursor.execute(query, (data['username'], data['password']))
        connection.commit()
        connection.close()
        return {'message': 'Usuario creado con exito'}, 201