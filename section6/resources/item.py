import sqlite3
from flask import request
from flask_restful import Resource, reqparse
from flask_jwt import jwt_required

from models.item import ItemModel

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

    #@jwt_required()
    def get(self, name):
        item = ItemModel.find_by_name(name)

        if item:
            return item
        return {'message': 'item not found'}, 404

    def post(self, name):
        if ItemModel.find_by_name(name):
            return {'message': 'El item de nombre {} ya existe'.format(name)}, 400
        
        data = self._parser('Campo requerido!')

        item = ItemModel(name, data['price'])

        try:
            ItemModel.insert(item)
        except:
            return {'message': 'Un ERROR ocurrio'}, 500
        return item, 201

    def put(self, name):
        data = self._parser('Campo requerido!')
        item = ItemModel(name, data['price'])

        if ItemModel.find_by_name(name):
            try:
                ItemModel.update(item)
            except:
                return {'message': 'Un ERROR ocurrio'}, 500
            return item
        
        try:
            ItemModel.insert(item)
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