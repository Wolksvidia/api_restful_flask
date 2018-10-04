from flask import Flask, request
from flask_restful import Resource, Api, reqparse
from flask_jwt import JWT, jwt_required

from security import authenticate, identity
from user import UserRegister

app = Flask(__name__)

app.secret_key = 'secreto'

api = Api(app)

jwt = JWT(app, authenticate, identity) #esto crea un endpoint /auth


items =[]


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
        item = next(filter(lambda i : i['name'] == name, items), None) #retorna el primer mach o None si no hay mach
        return {'item': item}, 200 if item else 404
        #for item in items:
        #   if item['name'] == name:
        #        return item 
        #return {'message': 'Item no found!'}, 404 # {'item': None}
    
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

api.add_resource(Item, '/item/<string:name>')
api.add_resource(ItemList, '/items')
api.add_resource(UserRegister, '/register')

app.run(port=5000, debug=True)
