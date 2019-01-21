import sqlite3
from flask import request
from flask_restful import Resource, reqparse
from flask_jwt import jwt_required

class Item(Resource):
    
    @staticmethod
    def _parser(message):
        parser = reqparse.RequestParser() #parsear los datos que vienen en el JSON, solo se admiten los declarados, el resto se borra
        parser.add_argument('price',
            type=float,
            required=True,
            help=message
        )
        return parser.parse_args()

    @classmethod
    def find_by_name(cls, name):   
        connection = sqlite3.connect('data.db')
        cursor = connection.cursor()

        query = 'SELECT * FROM items WHERE name=?'

        result = cursor.execute(query, (name,))
        row = result.fetchone()
        connection.close()

        if row:
            return {'item': {'name': row[0], 'price': row[1]}}
        return None

    @classmethod
    def insert(cld, item):
        connection = sqlite3.connect('data.db')
        cursor = connection.cursor()

        query = 'INSERT INTO items VALUES (?, ?)'

        cursor.execute(query, (item['name'], item['price']))
        connection.commit()
        connection.close()

    @classmethod
    def update(cld, item):
        connection = sqlite3.connect('data.db')
        cursor = connection.cursor()

        query = 'UPDATE items SET price=? WHERE name=?'

        cursor.execute(query, (item['price'],item['name']))
        connection.commit()
        connection.close()

    #@jwt_required()
    def get(self, name):
        item = self.find_by_name(name)

        if item:
            return item
        return {'message': 'item not found'}, 404

    def post(self, name):
        if self.find_by_name(name):
            return {'message': 'El item de nombre {} ya existe'.format(name)}, 400
        
        data = self._parser('Campo requerido!')

        item = {'name': name, 'price': data['price']}

        try:
            self.insert(item)
        except:
            return {'message': 'Un ERROR ocurrio'}, 500
        return item, 201

    def put(self, name):
        data = self._parser('Campo requerido!')
        item = {'name': name, 'price': data['price']}

        if self.find_by_name(name):
            try:
                self.update(item)
            except:
                return {'message': 'Un ERROR ocurrio'}, 500
            return item
        
        try:
            self.insert(item)
        except:
            return {'message': 'Un ERROR ocurrio'}, 500
        return item, 201


    def delete(self, name):
        connection = sqlite3.connect('data.db')
        cursor = connection.cursor()

        query = 'DELETE FROM items WHERE name=?'

        cursor.execute(query, (name,))

        connection.commit()
        connection.close()
        return {'message': 'Item borrado'}


class ItemList(Resource):
    def get(self):
        connection = sqlite3.connect('data.db')
        cursor = connection.cursor()

        query = 'SELECT * FROM items'

        items = []

        result = cursor.execute(query)

        for row in result:
            items.append({'name': row[0], 'price': row[1]})
        
        connection.close()

        return {'items': items}