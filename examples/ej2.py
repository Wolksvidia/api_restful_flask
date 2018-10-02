class Store:
    def __init__(self, name):
        self.name = name
        self.items = []

    def add_item(self, name, price):
        self.items.append({
            'name': name,
            'price': price
        })

    def stock_price(self):
        total = 0
        for item in self.items:
            total += item['price']
        return total

    @classmethod
    def franchise(cls, store):
        return cls(store.name + " - franchise") 
        # Return another store, with the same name as the argument's name, plus " - franchise"

    @staticmethod
    def store_details(store): 
        return '{}, total stock price: {}'.format(store.name, int(store.stock_price()))
        # Return a string representing the argument
        # It should be in the format 'NAME, total stock price: TOTAL'

    

store = Store('test')
store.add_item("algo",124)

fra = Store.franchise(store)
print(fra.name)
print(fra)

print(Store.store_details(store))

