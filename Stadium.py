class Stadium:
    def __init__(self, name="", date="", country="", city="", capacity=0.0):
        self.name = name
        self.date = date
        self.country = country
        self.city = city
        self.capacity = capacity

    def input_data(self):
        self.name = input("Enter stadium name: ")
        self.date = input("Enter opening date: ")
        self.country = input("Enter country: ")
        self.city = input("Enter city: ")
        self.capacity = float(input("Enter capacity: "))

    def display_info(self):
        print("\n--- Stadium Information ---")
        print(f"Name: {self.name}")
        print(f"Date: {self.date}")
        print(f"Country: {self.country}")
        print(f"City: {self.city}")
        print(f"Capacity: {self.capacity}")

    def change_name(self, new_name):
        self.name = new_name
        print("The name of the stadium has been changed.")

    def stadium_date(self, current_date):
        return current_date - self.data


stadium = Stadium()

stadium.input_data()
stadium.display_info()

new_name = input("\nEnter the new name of the stadium: ")
stadium.change_name(new_name)

stadium.display_info()

current_date = 2026
print(f"Stadium date: {stadium.stadium_date(current_date)}")