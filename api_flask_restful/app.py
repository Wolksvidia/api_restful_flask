from flask import Flask, request
from flask_restful import Resource, Api
from flask_jwt import JWT, jwt_required

from security import authenticate, identity

app = Flask(__name__)

app.secret_key = 'secreto'

api = Api(app)

jwt = JWT(app, authenticate, identity) #esto crea un endpoint /auth


items =[]


class Item(Resource):
    @jwt_required()
    def get(self, name):
        item = next(filter(lambda i : i['name'] == name, items), None) #retorna el primer mach o None si no hay mach
        return {'item': item}, 200 if item else 404
        #for item in items:
        #   if item['name'] == name:
        #        return item 
        #return {'message': 'Item no found!'}, 404 # {'item': None}
    
    def post(self, name):
        if next(filter(lambda i : i['name'] == name, items), None):
            return {'message': 'El item de nombre {} ya existe'.format(name)}, 400 #BAD REQUEST

        data= request.get_json(silent=True) #force=True significa que no se nescita del content-type header (NO RECOMENDADO)
        #silent=True si existe algun error fureza un None
        item = {'name': name, 'price': data['price']}
        items.append(item)
        return item, 201 #code 201 is CREATED

    def put(self, name):
        data = request.get_json(silent=True)
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

api.add_resource(Item, '/item/<string:name>')
api.add_resource(ItemList, '/items')

app.run(port=5000, debug=True)
