from flask import Flask, render_template

from models.ProductModel import ProductModel

app = Flask(__name__)

# categories = [
#     {"name": "Всі фрукти", "slug": "all", "emoji": "🍏", "count": 24},
#     {"name": "Ягоди", "slug": "Ягоди", "emoji": "🍒", "count": 4},
#     {"name": "Цитрусові", "slug": "Цитрусові", "emoji": "🍊", "count": 5},
#     {"name": "Кісточкові", "slug": "Кісточкові", "emoji": "🍒", "count": 4},
#     {"name": "Тропічні", "slug": "Тропічні", "emoji": "🍍", "count": 5},
#     {"name": "Яблука та груші", "slug": "Яблука та груші", "emoji": "🍎", "count": 4},
# ]

# products = [
#     {
#         "title": "Банани",
#         "image":"https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQ9jbR37e3S7wEp90WRGU5vhgOGVToSzqU7-z_0cmJQNg&s=10",
#         "price": 45,
#         "rating": 4.8
#     },
#     {
#         "title": "Яблука",
#         "image":"https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSF8sjcAiQrFbZ5mOEHr3bF6tunmLuiwpL9SQrfVzFjUA&s=10",
#         "price": 35,
#         "rating": 4.7
#     },
#     {
#         "title": "Апельсини",
#         "image":"https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSXXJJVKcwPsfWQ1RCKCdEo-ifzQZrvK0XieFwcrVsFBA&s=10",
#         "price": 55,
#         "rating": 4.9
#     },
#     {
#         "title": "Полуниця",
#         "image":"https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTiwedGvaxUSnxQuJDt1OUqke-3aQCHLyBMeDZamm-YoA&s=10",
#         "price": 120,
#         "rating": 4.8
#     },
#     {
#         "title": "Чорниця",
#         "image":"https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTd3qE5sFiqsdD1WG18THuXOfC-2EyLm6r7NyZy0VAfow&s=10",
#         "price": 150,
#         "rating": 4.9
#     },
#     {
#         "title": "Виноград",
#         "image":"https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcS0kqEuB_zj1f9F117bxRP75LQeXztrDhqkgVBKgX4ntw&s=10",
#         "price": 95,
#         "rating": 4.6
#     },
#     {
#         "title": "Ківі",
#         "image":"https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcT2vF733YGUlKzNxa7DAErO4GAtRko1w3IbFIFwPSayOg&s=10",
#         "price": 80,
#         "rating": 4.7
#     },
#     {
#         "title": "Манго",
#         "image":"https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRNIg948q-BotJVQedQC6SbSK78OB_MDbo7q6EoXBEqFw&s=10",
#         "price": 140,
#         "rating": 4.8
#     }
# ]

product_model = ProductModel()


@app.route("/")
def index():
    products = product_model.get_all_products()

    return render_template(
        "index.html",
        products=products
    )

@app.route("/product/<int:id>")
def product_detail(id):
    product = product_model.get_product_by_id(id)

    if product is None:
        return render_template("404.html")

    return render_template(
        "product.html",
        product=product
    )


if __name__ == "__main__":
    app.run(debug=True)