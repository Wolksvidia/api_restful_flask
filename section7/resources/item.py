from flask import request
from flask_restful import Resource, reqparse
from flask_jwt_extended import jwt_required

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
        parser.add_argument('store_id',
            type=int,
            required=True,
            help=message
        )
        return parser.parse_args()

    @jwt_required
    def get(self, name):
        item = ItemModel.find_by_name(name)

        if item:
            return item.json()
        return {'message': 'item not found'}, 404

    def post(self, name):
        if ItemModel.find_by_name(name):
            return {'message': 'El item de nombre {} ya existe'.format(name)}, 400
        
        data = self._parser('Campo requerido!')

        item = ItemModel(name, data['price'], data['store_id'])

        try:
            item.save()
        except:
            return {'message': 'Un ERROR ocurrio'}, 500
        return item.json(), 201

    def put(self, name):
        data = self._parser('Campo requerido!')
        item = ItemModel.find_by_name(name)
        
        if item:
            item.price = data['price']
        else:
            item = ItemModel(name, **data)
        
        try:
            item.save()
        except:
            return {'message': 'Un ERROR ocurrio'}, 500
        
        return item.json(), 201


    def delete(self, name):
        item = ItemModel.find_by_name(name)
        if item:
            item.delete()
            return {'message': 'Item delete'}
        return {'message': 'Item not exist'}, 404

class ItemList(Resource):
    def get(self):
        return {'items': [i.json() for i in ItemModel.find_all()]}