from flask import Flask, render_template

app = Flask(__name__)

categories = [
    {"name": "Всі фрукти", "slug": "all", "emoji": "🍏", "count": 24},
    {"name": "Ягоди", "slug": "Ягоди", "emoji": "🍒", "count": 4},
    {"name": "Цитрусові", "slug": "Цитрусові", "emoji": "🍊", "count": 5},
    {"name": "Кісточкові", "slug": "Кісточкові", "emoji": "🍒", "count": 4},
    {"name": "Тропічні", "slug": "Тропічні", "emoji": "🍍", "count": 5},
    {"name": "Яблука та груші", "slug": "Яблука та груші", "emoji": "🍎", "count": 4},
]

products = [
    {
        "name": "Банани",
        "category": "Тропічні",
        "price": 45,
        "rating": 4.8,
        "reviews": 124,
        "emoji": "🍌"
    },
    {
        "name": "Яблука",
        "category": "Яблука та груші",
        "price": 35,
        "rating": 4.7,
        "reviews": 98,
        "emoji": "🍎"
    },
    {
        "name": "Апельсини",
        "category": "Цитрусові",
        "price": 55,
        "rating": 4.9,
        "reviews": 156,
        "emoji": "🍊"
    },
    {
        "name": "Полуниця",
        "category": "Ягоди",
        "price": 120,
        "rating": 4.8,
        "reviews": 87,
        "emoji": "🍓"
    },
    {
        "name": "Чорниця",
        "category": "Ягоди",
        "price": 150,
        "rating": 4.9,
        "reviews": 72,
        "emoji": "🫐"
    },
    {
        "name": "Виноград",
        "category": "Ягоди",
        "price": 95,
        "rating": 4.6,
        "reviews": 64,
        "emoji": "🍇"
    },
    {
        "name": "Ківі",
        "category": "Тропічні",
        "price": 80,
        "rating": 4.7,
        "reviews": 53,
        "emoji": "🥝"
    },
    {
        "name": "Манго",
        "category": "Тропічні",
        "price": 140,
        "rating": 4.8,
        "reviews": 45,
        "emoji": "🥭"
    }
]


@app.route("/")
def home():
    return render_template(
        "fruitmarket.html",
        categories=categories,
        products=products
    )


if __name__ == "__main__":
    app.run(debug=True)