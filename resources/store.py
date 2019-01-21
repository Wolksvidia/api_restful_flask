
from flask_restful import Resource

from models.store import StoreModel


class Store(Resource):
    
    def get(self, name):
        store = StoreModel.find_by_name(name)

        if store:
            return store.json()
        return {'message': 'store not found'}, 404

    def post(self, name):
        if StoreModel.find_by_name(name):
            return {'message': 'El store de nombre {} ya existe'.format(name)}, 400

        store = StoreModel(name)

        try:
            store.save()
        except:
            return {'message': 'Un ERROR ocurrio'}, 500
        return store.json(), 201

    def delete(self, name):
        store = StoreModel.find_by_name(name)
        if store:
            store.delete()
            return {'message': 'store delete'}
        return {'message': 'store not exist'}


class StoreList(Resource):
    def get(self):
        return {'Stores': [store.json() for store in StoreModel.find_all()]}
