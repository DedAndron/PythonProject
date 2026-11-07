import decimal

class Product():
    def __init__(self, id:int, title:str, image:str, price: decimal, rating:decimal):
        self.id = id
        self.title = title
        self.image = image
        self.price = price
        self.rating = rating