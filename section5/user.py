import sqlite3
from flask_restful import Resource, reqparse

class User:
    def __init__(self, _id, username, password):
        self.id = _id
        self.username = username
        self.password = password
    
    @classmethod
    def find_by_username(cls, username):
        connection = sqlite3.connect('data.db')
        cursor = connection.cursor()

        query = 'SELECT * FROM users WHERE username=?'
        result = cursor.execute(query, (username,))
        row = result.fetchone()
        if row:
            user = cls(*row)
            #user = cls(row[0], row[1], row[2]) 
        else:
            user = None
        connection.close()
        return user

    @classmethod
    def find_by_id(cls, _id):
        connection = sqlite3.connect('data.db')
        cursor = connection.cursor()

        query = 'SELECT * FROM users WHERE id=?'
        result = cursor.execute(query, (_id,))
        row = result.fetchone()
        if row:
            user = cls(*row)
            #user = cls(row[0], row[1], row[2]) 
        else:
            user = None
        connection.close()
        return user


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
        Connection = sqlite3.connect('data.db')
        cursor = Connection.cursor()
        data = UserRegister._parser()
        
        query = 'INSERT INTO users VALUES (NULL, ?, ?)'
        cursor.execute(query, (data['username'], data['password']))

        Connection.commit()
        Connection.close()

        return {'message': 'Usuario creado con exito'}, 201
