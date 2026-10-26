class Car:
    def __init__(self, model="", year=0, manufacturer="", engine_volume=0.0, color="", price=0.0):
        self.model = model
        self.year = year
        self.manufacturer = manufacturer
        self.engine_volume = engine_volume
        self.color = color
        self.price = price

    def input_data(self):
        self.model = input("Enter model name: ")
        self.year = int(input("Enter year of manufacture: "))
        self.manufacturer = input("Enter manufacturer: ")
        self.engine_volume = float(input("Enter engine displacement (L): "))
        self.color = input("Enter car color: ")
        self.price = float(input("Enter car price: "))

    def display_info(self):
        print("\n--- Car Information ---")
        print(f"Model: {self.model}")
        print(f"Year: {self.year}")
        print(f"Manufacturer: {self.manufacturer}")
        print(f"Engine Volume: {self.engine_volume} л")
        print(f"Color: {self.color}")
        print(f"Price: {self.price:.2f}")

    def change_price(self, new_price):
        self.price = new_price
        print("The price of the car has been changed.")

    def car_age(self, current_year):
        return current_year - self.year


car = Car()

car.input_data()
car.display_info()

new_price = float(input("\nEnter the new price of the car:"))
car.change_price(new_price)

car.display_info()

current_year = 2026
print(f"Car age: {car.car_age(current_year)} years")