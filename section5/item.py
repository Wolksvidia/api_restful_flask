import sqlite3
from flask import request
from flask_restful import Resource, reqparse
from flask_jwt import jwt_required

items = []

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
        
    @jwt_required()
    def get(self, name):
        connection = sqlite3.connect('data.db')
        cursor = connection.cursor()

        query = 'SELECT * FROM items WHERE name=?'

        result = cursor.execute(query, (name,))
        row = result.fetchone()
        connection.close()

        if row:
            return {'item': {'name': row[0], 'price': row[1]}}
        return {'message': 'item not found'}, 404

    def post(self, name):
        if next(filter(lambda i : i['name'] == name, items), None):
            return {'message': 'El item de nombre {} ya existe'.format(name)}, 400 #BAD REQUEST

        data = Item._parser("El campo no puede estar en blaco!")
        #data = request.get_json(silent=True) #force=True significa que no se nescita del content-type header (NO RECOMENDADO)
        #silent=True si existe algun error fureza un None
        item = {'name': name, 'price': data['price']}
        items.append(item)
        return item, 201 #code 201 is CREATED

    def put(self, name):
        data = Item._parser("El campo no puede estar en blaco!")
        item = next(filter(lambda x: x['name'] == name, items), None)
        if item is None:
            item = {'name': name, 'price': data['price']}
            items.append(item)
        else:
            item.update(data)
        return item

    def delete(self, name):
        global items #si declaro la variable items aca, es solo local, utilizo global para referenciar a la varible global
        items = list(filter(lambda x: x['name'] != name, items))
        return {'message': 'Item borrado'}


class ItemList(Resource):
    def get(self):
        return {'items': items}