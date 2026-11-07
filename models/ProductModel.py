import decimal
from Product import Product

class ProductModel(Product):
    def __init__(self):
        self.products = [
            Product(
                1,
                "iPhone 15",
                "https://placehold.co/300x200?text=iPhone+15",
                899,
                4.8
            ),
            Product(
                2,
                "Samsung Galaxy S24",
                "https://placehold.co/300x200?text=Samsung",
                799,
                4.7
            ),
            Product(
                3,
                "Xiaomi Redmi Note 13",
                "https://placehold.co/300x200?text=Xiaomi",
                249,
                4.5
            ),
            Product(
                4,
                "Google Pixel 8",
                "https://placehold.co/300x200?text=Pixel",
                699,
                4.6
            )
        ]

    def get_all_products(self):
        return self.products

    def get_product_by_id(self, id):
        for product in self.products:
            if product.id == id:
                return product

        return None

    def create_product(self, product):
        product.id = max(
            (p.id for p in self.products),
            default=0
        ) + 1

        self.products.append(product)
        return product